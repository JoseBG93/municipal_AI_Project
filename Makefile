# Makefile para Municipal AI System

.PHONY: help install setup dev test lint format clean docker-build docker-up docker-down

# Variables
PYTHON := python3
PIP := pip3
DOCKER_COMPOSE := docker-compose
VENV_DIR := venv
ACTIVATE := source $(VENV_DIR)/bin/activate

# Default target
help:
	@echo "Comandos disponibles:"
	@echo "  install      - Instalar dependencias"
	@echo "  setup        - Configurar entorno completo"
	@echo "  dev          - Ejecutar en modo desarrollo"
	@echo "  test         - Ejecutar tests"
	@echo "  lint         - Ejecutar linting"
	@echo "  format       - Formatear código"
	@echo "  clean        - Limpiar archivos temporales"
	@echo "  docker-build - Construir imágenes Docker"
	@echo "  docker-up    - Levantar servicios"
	@echo "  docker-down  - Bajar servicios"
	@echo "  venv-create  - Crear entorno virtual"
	@echo "  venv-info    - Mostrar info del entorno"
	@echo "  status       - Mostrar estado general del proyecto"
	@echo "  index-context - Indexar documentos de contexto"
	@echo "  show-context  - Mostrar resumen del contexto disponible"
	@echo "  regenerate-mcps - Regenerar 30 documentos municipales (10 de cada tipo)"

# Instalación de dependencias
install:
	$(PIP) install -r requirements.txt

# Configuración inicial del entorno
setup: install
	@echo "Configurando entorno..."
	@if [ ! -f config/env_vars/.env ]; then \
		cp config/env_vars/.env.template config/env_vars/.env; \
		echo "Archivo .env creado. Configurar variables de entorno."; \
	fi
	@echo "Configuración completa."

# Modo desarrollo
dev:
	@echo "Iniciando en modo desarrollo..."
	cd apps/web_interface && $(PYTHON) manage.py runserver

# Ejecutar tests
test:
	$(PYTHON) -m pytest tests/ -v --cov=apps --cov-report=html

# Linting
lint:
	flake8 apps/ tests/ scripts/
	mypy apps/

# Formateo de código
format:
	black apps/ tests/ scripts/
	isort apps/ tests/ scripts/

# Limpiar archivos temporales
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	rm -rf .coverage

# Docker commands
docker-build:
	$(DOCKER_COMPOSE) build

docker-up:
	$(DOCKER_COMPOSE) up -d

docker-down:
	$(DOCKER_COMPOSE) down

docker-logs:
	$(DOCKER_COMPOSE) logs -f

# Base de datos
db-migrate:
	cd scripts/database && $(PYTHON) migrate.py

db-seed:
	cd scripts/database && $(PYTHON) seed.py

# Datos de prueba
generate-test-data:
	$(PYTHON) scripts/generate_synthetic_data.py

# Regenerar ejemplos sintéticos con nomenclatura clara
regenerate-mcps:
	@echo "🔄 Regenerando documentos municipales sintéticos..."
	@rm -f data/mcp_json/compraventa_*.json data/mcp_json/donacion_[0-9]*.json data/mcp_json/herencia_[0-9]*.json
	$(PYTHON) scripts/generate_synthetic_data.py
	@echo "✅ Regenerados 30 documentos municipales con nomenclatura clara"

# Pipeline completo de testing
pipeline-test:
	$(PYTHON) scripts/test_pipeline.py

# Entorno virtual
venv-create:
	$(PYTHON) -m venv --copies $(VENV_DIR)
	@echo "Entorno virtual creado. Activar con: source $(VENV_DIR)/bin/activate"

venv-info:
	@if [ -d "$(VENV_DIR)" ]; then \
		echo "📍 Entorno virtual: $(shell pwd)/$(VENV_DIR)"; \
		echo "🐍 Python: $(shell pwd)/$(VENV_DIR)/bin/python"; \
		echo "📦 Pip: $(shell pwd)/$(VENV_DIR)/bin/pip"; \
		echo ""; \
		echo "Para activar: source $(VENV_DIR)/bin/activate"; \
		echo "Para desactivar: deactivate"; \
	else \
		echo "❌ Entorno virtual no encontrado. Crear con: make venv-create"; \
	fi

# Estado general del proyecto
status:
	@echo "🏛️ === ESTADO DEL SISTEMA MUNICIPAL AI ==="
	@echo ""
	@echo "📁 Proyecto: $(shell pwd)"
	@echo "📅 Fecha: $(shell date '+%Y-%m-%d %H:%M:%S')"
	@echo ""
	@if [ -d "$(VENV_DIR)" ]; then \
		echo "✅ Entorno virtual: CONFIGURADO"; \
		if [ -n "$$VIRTUAL_ENV" ]; then \
			echo "✅ Estado: ACTIVO ($$VIRTUAL_ENV)"; \
		else \
			echo "⚠️  Estado: INACTIVO (ejecutar: source $(VENV_DIR)/bin/activate)"; \
		fi; \
	else \
		echo "❌ Entorno virtual: NO CONFIGURADO"; \
	fi
	@echo ""
	@echo "📊 Estructura del proyecto:"
	@echo "  📁 Apps: $(shell find apps/ -maxdepth 1 -type d | wc -l) módulos"
	@echo "  📄 Datos JSON: $(shell find data/ -name '*.json' 2>/dev/null | wc -l) archivos"
	@echo "  🧪 Tests: $(shell find tests/ -name '*.py' 2>/dev/null | wc -l) archivos"
	@echo "  📚 Docs: $(shell find docs/ -name '*.md' 2>/dev/null | wc -l) archivos"
	@echo ""
	@echo "🔗 Enlaces útiles:"
	@echo "  📖 Guía de desarrollo: docs/guia_desarrollo.md"
	@echo "  ✅ Verificación: docs/verificacion_guia.md"
	@echo "  ⚙️  Comandos: make help"
	@echo ""
	@if [ -f "data/outputs/pipeline_test_results.json" ]; then \
		echo "✅ Último test del pipeline: COMPLETADO"; \
	else \
		echo "⚠️  Pipeline: ejecutar 'python scripts/test_pipeline.py'"; \
	fi

# Gestión de contexto del proyecto
index-context:
	@echo "📋 === INDEXANDO CONTEXTO DEL PROYECTO ==="
	@echo ""
	@echo "📁 Documentos en docs/context/:"
	@if [ -d "docs/context" ]; then \
		find docs/context -name "*.txt" -o -name "*.md" | sort | while read file; do \
			echo "  📄 $$file ($(shell wc -l < "$$file" 2>/dev/null || echo "0") líneas)"; \
		done; \
		echo ""; \
		echo "📊 Total: $(shell find docs/context -name "*.txt" -o -name "*.md" 2>/dev/null | wc -l) documentos"; \
	else \
		echo "  ⚠️  Carpeta docs/context no existe"; \
	fi
	@echo ""
	@echo "📁 Prompts existentes en config/prompts/:"
	@find config/prompts -name "*.txt" | head -5 | while read file; do \
		echo "  📄 $$file"; \
	done
	@echo ""

show-context:
	@echo "📋 === RESUMEN DEL CONTEXTO DISPONIBLE ==="
	@echo ""
	@echo "🎯 Contexto del proyecto:"
	@if [ -f "docs/context/README.md" ]; then \
		echo "  ✅ README de contexto disponible"; \
	else \
		echo "  ⚠️  README de contexto no encontrado"; \
	fi
	@echo ""
	@echo "📊 Estadísticas:"
	@echo "  📄 Documentos .txt en docs/context: $(shell find docs/context -name "*.txt" 2>/dev/null | wc -l)"
	@echo "  📄 Prompts en config/prompts: $(shell find config/prompts -name "*.txt" 2>/dev/null | wc -l)"
	@echo "  📄 Total documentos de contexto: $(shell find docs/context config/prompts -name "*.txt" 2>/dev/null | wc -l)"
	@echo ""
	@echo "🔗 Para subir nuevos documentos:"
	@echo "  1. Copia archivos .txt a docs/context/"
	@echo "  2. Ejecuta: make index-context"
	@echo "  3. Usa: cat docs/context/archivo.txt para verificar" 