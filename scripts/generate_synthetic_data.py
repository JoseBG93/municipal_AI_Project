#!/usr/bin/env python3
"""
Script para generar datos sintéticos de prueba para el sistema municipal AI
"""

import json
import random
from datetime import datetime, timedelta
from pathlib import Path

def generate_mcp_compraventa():
    """Generar un documento municipal de compraventa sintético (formato español)"""
    
    nombres = ["Juan Pérez García", "María González López", "Carlos Rodríguez Martín", "Ana López Sánchez", "Pedro Martínez Ruiz"]
    calles = ["Calle Mayor", "Avenida Valencia", "Calle Constitución", "Plaza España", "Calle Real"]
    tipos_inmueble = ["vivienda", "local", "terreno", "oficina", "trastero"]
    
    vendedor = random.choice(nombres)
    comprador = random.choice([n for n in nombres if n != vendedor])
    
    fecha_base = datetime.now() - timedelta(days=random.randint(1, 365))
    
    mcp = {
        "tipo_documento": "compraventa",
        "fecha_documento": fecha_base.strftime("%Y-%m-%d"),
        "numero_protocolo": f"P{random.randint(1000, 9999)}/2024",
        "notario": {
            "nombre": "Dr. " + random.choice(nombres),
            "colegiacion": f"COL{random.randint(100, 999)}"
        },
        "partes": {
            "vendedor": {
                "nombre": vendedor,
                "nif": f"{random.randint(10000000, 99999999)}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}",
                "domicilio": f"{random.choice(calles)} {random.randint(1, 200)}, Alfafar, 46910"
            },
            "comprador": {
                "nombre": comprador,
                "nif": f"{random.randint(10000000, 99999999)}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}",
                "domicilio": f"{random.choice(calles)} {random.randint(1, 200)}, Alfafar, 46910"
            }
        },
        "inmueble": {
            "direccion": f"{random.choice(calles)} {random.randint(1, 200)}, Alfafar, 46910",
            "superficie": round(random.uniform(50, 500), 2),
            "tipo": random.choice(tipos_inmueble),
            "referencia_catastral": f"{random.randint(1000000, 9999999)}YJ4513S{random.randint(1000, 9999)}XX",
            "valor_catastral": random.randint(40000, 200000),
            "valor_real": random.randint(60000, 300000),
            "uso": random.choice(["vivienda_habitual", "segunda_vivienda", "local_comercial", "oficina"])
        },
        "calculo_iivtnu": {
            "sujeto": True,
            "base_imponible": random.randint(5000, 50000),
            "cuota": random.randint(500, 5000)
        },
        "observaciones": "Documento sintético de compraventa generado para pruebas"
    }
    
    return mcp

def generate_mcp_herencia():
    """Generar un MCP de herencia sintético (formato español)"""
    nombres = ["Juan Pérez García", "María González López", "Carlos Rodríguez Martín", "Ana López Sánchez", "Pedro Martínez Ruiz"]
    calles = ["Calle Mayor", "Avenida Valencia", "Calle Constitución", "Plaza España", "Calle Real"]
    parentescos = ["hijo", "hija", "cónyuge", "padre", "madre"]
    
    causante = random.choice(nombres)
    heredero = random.choice([n for n in nombres if n != causante])
    
    fecha_fallecimiento = datetime.now() - timedelta(days=random.randint(30, 365))
    fecha_documento = fecha_fallecimiento + timedelta(days=random.randint(30, 180))
    
    mcp = {
        "tipo_documento": "herencia",
        "subtipo_documento": "aceptacion_herencia_simple",
        "fecha_documento": fecha_documento.strftime("%Y-%m-%d"),
        "numero_protocolo": f"H{random.randint(1000, 9999)}/2024",
        "notario": {
            "nombre": "Dr. " + random.choice(nombres),
            "colegiacion": f"COL{random.randint(100, 999)}"
        },
        "causante": {
            "nombre": causante,
            "nif": f"{random.randint(10000000, 99999999)}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}",
            "fecha_fallecimiento": fecha_fallecimiento.strftime("%Y-%m-%d"),
            "lugar_fallecimiento": "Alfafar"
        },
        "heredero": {
            "nombre": heredero,
            "nif": f"{random.randint(10000000, 99999999)}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}",
            "parentesco": random.choice(parentescos),
            "domicilio": f"{random.choice(calles)} {random.randint(1, 200)}, Alfafar, 46910",
            "acepta_herencia": True
        },
        "inmueble_heredado": {
            "descripcion": "Vivienda familiar",
            "direccion": f"{random.choice(calles)} {random.randint(1, 200)}, Alfafar, 46910",
            "valor_catastral": random.randint(50000, 200000),
            "valor_real": random.randint(80000, 300000),
            "tipo": "vivienda",
            "referencia_catastral": f"{random.randint(1000000, 9999999)}YJ4513S{random.randint(1000, 9999)}XX",
            "uso": "vivienda_habitual"
        },
        "calculo_isd": {
            "comunidad_autonoma": "Valencia",
            "grupo_parentesco": random.choice([1, 2]),
            "base_imponible": random.randint(80000, 300000),
            "reducciones": random.randint(15000, 100000),
            "base_liquidable": random.randint(0, 50000),
            "cuota_final": random.randint(0, 15000)
        },
        "observaciones": "Documento sintético de herencia generado para pruebas"
    }
    
    return mcp

def generate_mcp_donacion():
    """Generar un MCP de donación sintético (formato español)"""
    nombres = ["Juan Pérez García", "María González López", "Carlos Rodríguez Martín", "Ana López Sánchez", "Pedro Martínez Ruiz"]
    calles = ["Calle Mayor", "Avenida Valencia", "Calle Constitución", "Plaza España", "Calle Real"]
    parentescos = ["hijo", "hija", "nieto", "nieta"]
    
    donante = random.choice(nombres)
    donatario = random.choice([n for n in nombres if n != donante])
    
    fecha_base = datetime.now() - timedelta(days=random.randint(1, 180))
    
    mcp = {
        "tipo_documento": "donacion",
        "subtipo_documento": "donacion_inmueble_familiar",
        "fecha_documento": fecha_base.strftime("%Y-%m-%d"),
        "numero_protocolo": f"D{random.randint(1000, 9999)}/2024",
        "notario": {
            "nombre": "Dr. " + random.choice(nombres),
            "colegiacion": f"COL{random.randint(100, 999)}"
        },
        "donante": {
            "nombre": donante,
            "nif": f"{random.randint(10000000, 99999999)}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}",
            "domicilio": f"{random.choice(calles)} {random.randint(1, 200)}, Alfafar, 46910",
            "estado_civil": random.choice(["soltero", "casado", "viudo"])
        },
        "donatario": {
            "nombre": donatario,
            "nif": f"{random.randint(10000000, 99999999)}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}",
            "parentesco": random.choice(parentescos),
            "domicilio": f"{random.choice(calles)} {random.randint(1, 200)}, Alfafar, 46910"
        },
        "inmueble_donado": {
            "descripcion": random.choice(["Apartamento", "Piso", "Casa unifamiliar", "Local comercial"]),
            "direccion": f"{random.choice(calles)} {random.randint(1, 200)}, Alfafar, 46910",
            "valor_catastral": random.randint(40000, 150000),
            "valor_real": random.randint(60000, 250000),
            "tipo": "vivienda",
            "referencia_catastral": f"{random.randint(1000000, 9999999)}YJ4513S{random.randint(1000, 9999)}XX",
            "superficie": round(random.uniform(50, 200), 2),
            "uso": "vivienda"
        },
        "calculo_isd": {
            "comunidad_autonoma": "Valencia",
            "grupo_parentesco": 2,
            "base_imponible": random.randint(60000, 250000),
            "reducciones_aplicables": [
                {
                    "tipo": "reduccion_parentesco_directo",
                    "importe": random.randint(50000, 100000),
                    "descripcion": "Reducción por parentesco directo descendiente"
                }
            ],
            "total_reducciones": random.randint(50000, 120000),
            "base_liquidable": random.randint(0, 50000),
            "exencion_familiar": random.choice([True, False]),
            "cuota_final": random.randint(0, 5000)
        },
        "observaciones": "Documento sintético de donación generado para pruebas"
    }
    
    return mcp

def generate_multiple_mcps(count=10):
    """Generar múltiples MCPs de diferentes tipos"""
    mcps = []
    for i in range(count):
        tipo = random.choice(["compraventa", "herencia", "donacion"])
        if tipo == "compraventa":
            mcp = generate_mcp_compraventa()
        elif tipo == "herencia":
            mcp = generate_mcp_herencia()
        else:  # donacion
            mcp = generate_mcp_donacion()
        mcps.append(mcp)
    
    return mcps

def save_synthetic_data():
    """Guardar datos sintéticos en archivos con nomenclatura clara"""
    
    # Crear directorio si no existe
    output_dir = Path("data/mcp_json")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Generar exactamente 10 de cada tipo
    tipos = ["compraventa", "donacion", "herencia"]
    todos_mcps = []
    
    for tipo in tipos:
        print(f"Generando 10 ejemplos de {tipo}...")
        
        for i in range(1, 11):  # 001 a 010
            if tipo == "compraventa":
                mcp = generate_mcp_compraventa()
            elif tipo == "donacion":
                mcp = generate_mcp_donacion()
            else:  # herencia
                mcp = generate_mcp_herencia()
            
            # Guardar archivo individual con nomenclatura clara
            filename = f"{tipo}_{i:03d}.json"
            with open(output_dir / filename, 'w', encoding='utf-8') as f:
                json.dump(mcp, f, indent=2, ensure_ascii=False)
            
            todos_mcps.append(mcp)
    
    # Guardar colección completa
    with open(output_dir / "synthetic_mcps_collection.json", 'w', encoding='utf-8') as f:
        json.dump({
            "generated_at": datetime.now().isoformat(),
            "total_count": len(todos_mcps),
            "por_tipo": {
                "compraventa": 10,
                "donacion": 10, 
                "herencia": 10
            },
            "mcps": todos_mcps
        }, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Generados {len(todos_mcps)} MCPs sintéticos en {output_dir}")
    print(f"   📄 10 compraventas: compraventa_001.json a compraventa_010.json")
    print(f"   📄 10 donaciones: donacion_001.json a donacion_010.json") 
    print(f"   📄 10 herencias: herencia_001.json a herencia_010.json")
    
    # Generar datos de prueba para tests
    test_dir = Path("data/tests")
    test_dir.mkdir(parents=True, exist_ok=True)
    
    # Casos edge
    edge_cases = [
        # MCP con valores mínimos
        {
            **generate_mcp_compraventa(),
            "inmueble": {
                **generate_mcp_compraventa()["inmueble"],
                "superficie": 1.0
            },
            "valor_transaccion": {
                "monto": 1,
                "moneda": "UYU"
            }
        },
        # MCP con valores máximos
        {
            **generate_mcp_compraventa(),
            "inmueble": {
                **generate_mcp_compraventa()["inmueble"],
                "superficie": 10000.0
            },
            "valor_transaccion": {
                "monto": 10000000,
                "moneda": "USD"
            }
        }
    ]
    
    with open(test_dir / "edge_cases.json", 'w', encoding='utf-8') as f:
        json.dump(edge_cases, f, indent=2, ensure_ascii=False)
    
    print(f"Generados casos edge en {test_dir}")

if __name__ == "__main__":
    save_synthetic_data() 