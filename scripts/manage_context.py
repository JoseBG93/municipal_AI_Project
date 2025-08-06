#!/usr/bin/env python3
"""
Script para gestionar documentos de contexto del proyecto Municipal AI
"""

import os
import sys
from pathlib import Path
import argparse
import json
from datetime import datetime

def scan_context_files():
    """Escanear y catalogar archivos de contexto"""
    
    context_dirs = [
        Path("docs/context"),
        Path("config/prompts") 
    ]
    
    files_info = []
    
    for directory in context_dirs:
        if directory.exists():
            for file_path in directory.rglob("*.txt"):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        lines = len(content.splitlines())
                        words = len(content.split())
                        
                    files_info.append({
                        "path": str(file_path),
                        "directory": str(directory),
                        "filename": file_path.name,
                        "lines": lines,
                        "words": words,
                        "size_kb": round(file_path.stat().st_size / 1024, 2),
                        "modified": datetime.fromtimestamp(file_path.stat().st_mtime).isoformat()
                    })
                except Exception as e:
                    print(f"Error procesando {file_path}: {e}")
    
    return files_info

def generate_context_index():
    """Generar índice de contexto"""
    
    files_info = scan_context_files()
    
    # Crear índice
    index = {
        "generated_at": datetime.now().isoformat(),
        "total_files": len(files_info),
        "total_lines": sum(f["lines"] for f in files_info),
        "total_words": sum(f["words"] for f in files_info),
        "total_size_kb": sum(f["size_kb"] for f in files_info),
        "files": files_info
    }
    
    # Guardar índice
    index_path = Path("docs/context/context_index.json")
    index_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    
    return index, index_path

def show_context_summary():
    """Mostrar resumen del contexto disponible"""
    
    index, index_path = generate_context_index()
    
    print("📋 === RESUMEN DEL CONTEXTO DEL PROYECTO ===\n")
    
    print(f"📊 Estadísticas generales:")
    print(f"  📄 Total archivos: {index['total_files']}")
    print(f"  📝 Total líneas: {index['total_lines']:,}")
    print(f"  📖 Total palabras: {index['total_words']:,}")
    print(f"  💾 Tamaño total: {index['total_size_kb']:.1f} KB")
    print(f"  📅 Generado: {index['generated_at']}")
    print()
    
    # Agrupar por directorio
    by_directory = {}
    for file_info in index['files']:
        dir_name = file_info['directory']
        if dir_name not in by_directory:
            by_directory[dir_name] = []
        by_directory[dir_name].append(file_info)
    
    print("📁 Archivos por directorio:")
    for directory, files in by_directory.items():
        print(f"\n  📂 {directory}/ ({len(files)} archivos)")
        for file_info in sorted(files, key=lambda x: x['filename']):
            print(f"    📄 {file_info['filename']} ({file_info['lines']} líneas, {file_info['size_kb']} KB)")
    
    print(f"\n💾 Índice guardado en: {index_path}")
    
    return index

def copy_prompts_to_context():
    """Copiar prompts existentes a la nueva estructura de contexto"""
    
    prompts_dir = Path("config/prompts")
    context_dir = Path("docs/context")
    
    if not prompts_dir.exists():
        print("❌ No se encontró config/prompts/")
        return
    
    context_dir.mkdir(parents=True, exist_ok=True)
    
    copied_files = []
    
    for txt_file in prompts_dir.rglob("*.txt"):
        # Crear nombre de archivo más descriptivo
        relative_path = txt_file.relative_to(prompts_dir)
        new_name = str(relative_path).replace("/", "_").replace(" ", "_").lower()
        
        dest_path = context_dir / new_name
        
        try:
            with open(txt_file, 'r', encoding='utf-8') as source:
                content = source.read()
            
            with open(dest_path, 'w', encoding='utf-8') as dest:
                dest.write(f"# Origen: {txt_file}\n")
                dest.write(f"# Copiado: {datetime.now().isoformat()}\n\n")
                dest.write(content)
            
            copied_files.append((txt_file, dest_path))
            print(f"✅ Copiado: {txt_file} → {dest_path}")
            
        except Exception as e:
            print(f"❌ Error copiando {txt_file}: {e}")
    
    print(f"\n📊 Total archivos copiados: {len(copied_files)}")
    return copied_files

def search_in_context(search_term):
    """Buscar término en archivos de contexto"""
    
    files_info = scan_context_files()
    matches = []
    
    for file_info in files_info:
        file_path = Path(file_info['path'])
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.splitlines()
                
            for line_num, line in enumerate(lines, 1):
                if search_term.lower() in line.lower():
                    matches.append({
                        "file": str(file_path),
                        "line": line_num,
                        "content": line.strip()
                    })
        except Exception as e:
            print(f"Error buscando en {file_path}: {e}")
    
    return matches

def main():
    parser = argparse.ArgumentParser(description="Gestionar contexto del proyecto Municipal AI")
    parser.add_argument('action', choices=['summary', 'index', 'copy-prompts', 'search'], 
                       help='Acción a realizar')
    parser.add_argument('--term', help='Término a buscar (para search)')
    
    args = parser.parse_args()
    
    if args.action == 'summary':
        show_context_summary()
    elif args.action == 'index':
        index, path = generate_context_index()
        print(f"✅ Índice generado en: {path}")
    elif args.action == 'copy-prompts':
        copy_prompts_to_context()
    elif args.action == 'search':
        if not args.term:
            print("❌ Debes especificar --term para buscar")
            return
        
        matches = search_in_context(args.term)
        print(f"🔍 Buscando '{args.term}'...\n")
        
        if matches:
            for match in matches[:20]:  # Limitar a 20 resultados
                print(f"📄 {match['file']}:{match['line']}")
                print(f"   {match['content']}")
                print()
            
            if len(matches) > 20:
                print(f"... y {len(matches) - 20} resultados más")
        else:
            print("❌ No se encontraron coincidencias")

if __name__ == "__main__":
    main() 