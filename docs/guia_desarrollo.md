# 📚 Guía de Desarrollo - Sistema Municipal AI

## 🎯 Introducción

Esta guía contiene todos los comandos esenciales y conceptos fundamentales para trabajar con el **Sistema Municipal AI**. El proyecto está diseñado como una arquitectura de microservicios modulares para procesamiento de documentos municipales, cálculo de impuestos e integración con sistemas externos.

---

## 🏗️ Arquitectura del Proyecto

### Estructura Modular
```
municipal-ai-system/
├── apps/                         # 🎯 Microservicios modulares
│   ├── document_processor/       # OCR, limpieza y extracción
│   ├── tax_calculator/           # Cálculo IIVTNU, ISD, bonificaciones
│   ├── integration_layer/        # Simulación y exportación a GTT/Gestiona
│   └── web_interface/            # Frontend e interfaces de usuario
├── data/                         # 📊 Datos y resultados
│   ├── pdf_examples/             # Documentos PDF de prueba
│   ├── mcp_json/                 # Documentos municipales estructurados
│   ├── outputs/                  # JSON/CSV generados
│   └── tests/                    # Datasets de prueba
├── config/                       # 🔧 Configuración centralizada
│   ├── schemas/                  # Validación JSON
│   ├── infrastructure/           # Docker, Kubernetes
│   └── prompts/                  # Prompts de LLM
├── scripts/                      # ⚙️ Operaciones y utilidades
└── tests/                        # 🧪 Framework de testing
```

### Conceptos Clave
- **Esquemas Municipales**: Formato JSON estructurado para documentos notariales
- **OCR**: Optical Character Recognition (extracción de texto)
- **LLM**: Large Language Models (procesamiento de lenguaje natural)
- **GTT/Gestiona**: Sistemas municipales de gestión tributaria

---

## 🐍 Gestión de Entornos Virtuales

### ¿Por qué usar entornos virtuales?
- **Aislamiento**: Evita conflictos entre dependencias de diferentes proyectos
- **Reproducibilidad**: Garantiza que todos usen las mismas versiones
- **Limpieza**: Mantiene el sistema Python base sin contaminar

### Comandos Esenciales

#### Crear y Activar Entorno Virtual
```bash
# Crear entorno virtual (solo primera vez)
make venv-create
# O manualmente:
python3 -m venv --copies venv

# Activar entorno virtual (cada sesión)
source venv/bin/activate

# Verificar que está activo
echo $VIRTUAL_ENV
which python
```

#### Desactivar y Gestionar
```bash
# Desactivar entorno virtual
deactivate

# Ver información del entorno
make venv-info

# Eliminar entorno virtual (si hay problemas)
rm -rf venv && make venv-create
```

---

## 📦 Consulta y Gestión de Dependencias

### Consultar Ubicación de Dependencias

#### Estado del Entorno
```bash
# Ver si hay entorno virtual activo
echo $VIRTUAL_ENV

# Ver qué Python/pip está usando
which python && which pip

# Ver todas las rutas donde Python busca módulos
python -m site
```

#### Información de Paquetes
```bash
# Listar todos los paquetes instalados
pip list
pip list --format=columns

# Información detallada de un paquete
pip show [nombre_paquete]
pip show numpy

# Ver archivos instalados de un paquete
pip show -f [nombre_paquete]

# Solo paquetes instalados por usuario (sin entorno virtual)
pip list --user
```

#### Búsqueda y Verificación
```bash
# Buscar paquetes instalados
pip list | grep [término]

# Verificar versión específica
pip show [paquete] | grep Version

# Ver dependencias de un paquete
pip show [paquete] | grep Requires
```

### Instalación de Dependencias

#### Con Entorno Virtual (RECOMENDADO)
```bash
# 1. Activar entorno virtual
source venv/bin/activate

# 2. Instalar desde requirements.txt
pip install -r requirements.txt

# 3. Instalar paquete individual
pip install [nombre_paquete]

# 4. Instalar versión específica
pip install [paquete]==1.2.3
```

#### Sin Entorno Virtual (NO recomendado)
```bash
# Instalar solo para usuario actual
pip install --user [paquete]

# Instalar globalmente (requiere sudo)
sudo pip install [paquete]
```

---

## 🛠️ Comandos del Proyecto (Makefile)

### Comandos de Configuración
```bash
# Ver todos los comandos disponibles
make help

# Configuración inicial completa
make setup

# Solo instalar dependencias
make install
```

### Comandos de Desarrollo
```bash
# Ejecutar en modo desarrollo
make dev

# Ejecutar tests
make test

# Linting (revisión de código)
make lint

# Formatear código
make format

# Limpiar archivos temporales
make clean
```

### Comandos Docker
```bash
# Construir imágenes Docker
make docker-build

# Levantar todos los servicios
make docker-up

# Bajar servicios
make docker-down

# Ver logs de contenedores
make docker-logs
```

### Comandos de Base de Datos
```bash
# Ejecutar migraciones
make db-migrate

# Poblar con datos de prueba
make db-seed
```

### Comandos Específicos del Proyecto
```bash
# Generar datos sintéticos de prueba
make generate-test-data
# O directamente:
python scripts/generate_synthetic_data.py

# Probar pipeline completo
make pipeline-test
# O directamente:
python scripts/test_pipeline.py
```

---

## 🔍 Ubicaciones de Archivos Importantes

### Con Entorno Virtual Activo
```bash
# Dependencias del proyecto
/home/jose/My_Projects/municipal-ai-system/venv/lib/python3.10/site-packages/

# Ejecutables Python/Pip
/home/jose/My_Projects/municipal-ai-system/venv/bin/python
/home/jose/My_Projects/municipal-ai-system/venv/bin/pip
```

### Sin Entorno Virtual
```bash
# Sistema (instalación global)
/usr/lib/python3/dist-packages/

# Usuario (instalación local)
/home/jose/.local/lib/python3.10/site-packages/

# Ejecutables del sistema
/usr/bin/python3
/usr/bin/pip3
```

---

## 📋 Flujo de Trabajo Recomendado

### 1. Inicio de Sesión Diaria
```bash
# Navegar al proyecto
cd ~/My_Projects/municipal-ai-system

# Activar entorno virtual
source venv/bin/activate

# Verificar estado
make venv-info

# Actualizar dependencias si es necesario
pip install -r requirements.txt
```

### 2. Desarrollo
```bash
# Ejecutar tests antes de trabajar
make test

# Trabajar en código...

# Formatear código
make format

# Ejecutar tests después de cambios
make test

# Linting final
make lint
```

### 3. Testing y Datos
```bash
# Generar datos de prueba si es necesario
make generate-test-data

# Probar pipeline completo
make pipeline-test

# Tests específicos
python -m pytest tests/test_ocr.py -v
```

---

## 🚨 Troubleshooting Común

### Problemas con Entorno Virtual
```bash
# Error: No such file or directory (activate)
rm -rf venv
make venv-create

# Error: Permission denied
sudo apt install python3.10-venv
make venv-create

# Verificar que está funcionando
make venv-info
```

### Problemas con Dependencias
```bash
# Error: Package not found
pip install --upgrade pip
pip install -r requirements.txt

# Conflictos de versiones
pip freeze > current_packages.txt
pip uninstall -r current_packages.txt -y
pip install -r requirements.txt

# Limpiar cache de pip
pip cache purge
```

### Problemas con Docker
```bash
# Contenedores no se inician
make docker-down
make docker-build
make docker-up

# Ver logs específicos
docker logs municipal-ai-system_postgres_1

# Limpiar volúmenes
docker-compose down -v
```

---

## 📊 Comparación de Ubicaciones

| Tipo | Con Entorno Virtual | Sin Entorno Virtual |
|------|--------------------|--------------------|
| **Ubicación** | `venv/lib/python3.10/site-packages/` | `/usr/lib/python3/dist-packages/` |
| **Aislamiento** | ✅ Completo | ❌ Global |
| **Conflictos** | ✅ Sin riesgo | ⚠️ Posibles |
| **Mantenimiento** | ✅ Fácil | ❌ Complejo |
| **Reproducibilidad** | ✅ Alta | ❌ Baja |

---

## 🎓 Conceptos Fundamentales

### Variables de Entorno
```bash
# Ver variable de entorno virtual
echo $VIRTUAL_ENV

# Ver todas las variables Python relevantes
env | grep PYTHON

# Cargar variables desde archivo
source config/env_vars/env_template.txt
```

### Estructura de Paquetes Python
```bash
# Ver estructura de un paquete
find venv/lib/python3.10/site-packages/numpy -name "*.py" | head -10

# Ver información de importación
python -c "import numpy; print(numpy.__file__)"
```

### Comandos de Verificación Rápida
```bash
# Estado general del proyecto
pwd && git status --short && make venv-info

# Verificación de dependencias críticas
pip show pandas numpy requests fastapi

# Estado de servicios Docker
docker ps | grep municipal
```

---

## 📝 Archivos de Configuración Clave

### requirements.txt
Contiene todas las dependencias Python del proyecto con versiones específicas.

### docker-compose.yml
Orquesta todos los microservicios: PostgreSQL, Redis, procesador de documentos, calculadora de impuestos, etc.

### Makefile
Automatiza comandos comunes de desarrollo, testing y despliegue.

### config/schemas/mcp_schema.json
Esquema de validación para documentos municipales (compraventa, herencia, donación).

---

## 🚀 Próximos Pasos Sugeridos

1. **Familiarízate con el entorno virtual**: Practica activar/desactivar
2. **Explora la estructura**: Navega por `apps/` y entiende cada módulo
3. **Ejecuta los tests**: `make test` para verificar que todo funciona
4. **Genera datos de prueba**: `make generate-test-data`
5. **Estudia los esquemas**: Revisa `config/schemas/mcp_schema.json` (esquemas de documentos municipales)
6. **Experimenta con Docker**: `make docker-up` para ver los microservicios

---

## 📋 Gestión de Contexto del Proyecto

### ¿Qué es el Contexto del Proyecto?
El contexto son documentos .txt que definen completamente el proyecto: objetivos, arquitectura, normativas, fases de desarrollo, etc. Estos documentos permiten que el asistente AI tenga comprensión total del sistema.

### Ubicaciones de Contexto
```bash
docs/context/           # Documentos principales de contexto
config/prompts/         # Prompts y especificaciones técnicas
```

### Comandos de Gestión de Contexto
```bash
# Ver resumen del contexto actual
make show-context

# Indexar y catalogar documentos
make index-context

# Gestión avanzada con script Python
python3 scripts/manage_context.py summary          # Resumen completo
python3 scripts/manage_context.py index           # Generar índice
python3 scripts/manage_context.py search --term [término]  # Buscar en contexto
```

### Cómo Añadir Nuevos Documentos de Contexto

**Opción 1: Copia directa (RECOMENDADA)**
```bash
# 1. Copiar archivos .txt a docs/context/
cp /ruta/a/tus/documentos/*.txt docs/context/

# 2. Indexar documentos
make index-context

# 3. Verificar contenido
python3 scripts/manage_context.py summary
```

**Opción 2: Subida manual**
- Arrastra archivos .txt a `docs/context/` en el explorador de archivos
- Ejecuta `make index-context` para catalogarlos

### Estructura Recomendada de Nombres
```
docs/context/
├── 01_definicion_proyecto.txt      # Definición general
├── 02_objetivos_alcance.txt        # Objetivos y alcance  
├── 03_arquitectura_sistema.txt     # Diseño arquitectónico
├── 04_modelo_mcp.txt               # Especificación MCP
├── 05_normativa_legal.txt          # RGPD, LOPDGDD
├── 06_tecnologias.txt              # Stack tecnológico
└── 07_fases_desarrollo.txt         # Planificación
```

---

## 📞 Referencia Rápida de Comandos

```bash
# CONFIGURACIÓN INICIAL
make setup                    # Configurar proyecto completo
source venv/bin/activate     # Activar entorno virtual
make venv-info              # Ver información del entorno

# CONTEXTO DEL PROYECTO
make show-context            # Ver resumen del contexto
make index-context           # Indexar documentos de contexto
python3 scripts/manage_context.py summary  # Análisis completo

# DESARROLLO DIARIO
make test                   # Ejecutar tests
make lint                   # Revisar código
make format                 # Formatear código
make dev                    # Ejecutar en desarrollo

# DATOS Y TESTING
make generate-test-data     # Generar datos sintéticos
make pipeline-test          # Probar pipeline completo
python3 scripts/test_pipeline.py  # Test manual

# DOCKER
make docker-up              # Levantar servicios
make docker-down            # Bajar servicios
make docker-logs            # Ver logs

# CONSULTA DE DEPENDENCIAS
pip list                    # Listar paquetes
pip show [paquete]          # Info de paquete
python -m site              # Ver rutas Python
which python && which pip   # Ver ubicaciones
```

---

**💡 Consejo:** Mantén esta guía abierta mientras trabajas y ve agregando tus propios comandos y notas conforme aprendas más sobre el proyecto. 