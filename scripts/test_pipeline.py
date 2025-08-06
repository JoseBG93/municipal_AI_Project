#!/usr/bin/env python3
"""
Script para probar el pipeline completo del sistema municipal AI
"""

import os
import sys
import json
import logging
from pathlib import Path

# Agregar el directorio raíz al path
sys.path.append(str(Path(__file__).parent.parent))

def setup_logging():
    """Configurar logging para el test"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)

def test_document_processor():
    """Probar el procesador de documentos"""
    logger = logging.getLogger(__name__)
    logger.info("Probando procesador de documentos...")
    
    # TODO: Implementar test del OCR y extracción
    # Esto debe probarse con los módulos de apps/document_processor/
    
    return True

def test_tax_calculator():
    """Probar la calculadora de impuestos"""
    logger = logging.getLogger(__name__)
    logger.info("Probando calculadora de impuestos...")
    
    # TODO: Implementar test de cálculos fiscales
    # Esto debe probarse con los módulos de apps/tax_calculator/
    
    return True

def test_integration_layer():
    """Probar la capa de integración"""
    logger = logging.getLogger(__name__)
    logger.info("Probando capa de integración...")
    
    # TODO: Implementar test de integración con sistemas externos
    # Esto debe probarse con los módulos de apps/integration_layer/
    
    return True

def run_full_pipeline():
    """Ejecutar el pipeline completo"""
    logger = setup_logging()
    
    logger.info("=== INICIANDO TEST DEL PIPELINE COMPLETO ===")
    
    tests = [
        ("Document Processor", test_document_processor),
        ("Tax Calculator", test_tax_calculator),
        ("Integration Layer", test_integration_layer)
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        try:
            logger.info(f"Ejecutando test: {test_name}")
            result = test_func()
            results[test_name] = "PASSED" if result else "FAILED"
            logger.info(f"Test {test_name}: {'PASSED' if result else 'FAILED'}")
        except Exception as e:
            results[test_name] = f"ERROR: {str(e)}"
            logger.error(f"Test {test_name} falló con error: {e}")
    
    # Mostrar resumen
    logger.info("=== RESUMEN DE TESTS ===")
    for test_name, result in results.items():
        logger.info(f"{test_name}: {result}")
    
    # Guardar resultados
    results_file = Path("data/outputs/pipeline_test_results.json")
    results_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(results_file, 'w') as f:
        json.dump({
            "timestamp": str(Path(__file__).stat().st_mtime),
            "results": results
        }, f, indent=2)
    
    logger.info(f"Resultados guardados en: {results_file}")

if __name__ == "__main__":
    run_full_pipeline() 