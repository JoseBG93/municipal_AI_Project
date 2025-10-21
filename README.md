# 🏛️ Municipal AI System - Automatización Integral de Documentos Notariales

## 🎯 Propósito
Sistema integral de automatización para el procesamiento de documentos notariales (escrituras, herencias, compraventas) y cálculo automático de impuestos municipales usando IA/ML/DL.

**Cliente**: Ayuntamiento de Alfafar  
**Objetivo**: Eliminar procesamiento manual, reducir errores y acelerar trámites fiscales.

## 📚 Documentación

- **[📖 Guía de Desarrollo](docs/guia_desarrollo.md)**: Comandos esenciales, gestión de entornos virtuales y flujo de trabajo
- **[✅ Verificación del Sistema](docs/verificacion_guia.md)**: Estado actual y funcionalidades probadas
- **[📋 Contexto del Proyecto](docs/context/)**: Documentos completos de definición y especificación
- **[📊 Ejemplos de MCPs](docs/ejemplos_docs_municipales.md)**: Todos los ejemplos de escrituras en JSON
- **[🏗️ Arquitectura](docs/)**: Diseño del sistema y patrones implementados  
- **[🔧 Configuración](config/)**: Variables de entorno y esquemas de validación
- **[🧪 Testing](tests/)**: Tests unitarios y de integración

### 🚀 Inicio Rápido
```bash
# Configuración inicial
make setup

# Activar entorno virtual
source venv/bin/activate

# Ver estado completo del proyecto
make status

# Gestionar contexto del proyecto
make show-context                              # Ver contexto actual
cp /tus/documentos/*.txt docs/context/         # Subir documentos de contexto
make index-context                             # Indexar documentos

# Ver comandos disponibles  
make help

# Consultar guía completa
cat docs/guia_desarrollo.md
```

## 🏗️ Arquitectura del Sistema
```mermaid
graph TB
    A[Documentos PDF] --> B[Document Processor]
    B --> C[OCR + NLP Engine]
    C --> D[Data Extraction]
    D --> E[Tax Calculator]
    E --> F[Municipal Database]
    F --> G[Web Interface]
    G --> H[Integration APIs]
    H --> I[Sistemas Municipales]
```

## 🛠️ Stack Tecnológico

### **Microservicio 1: Document Processor**
- **OCR**: Tesseract + PyMuPDF
- **NLP**: spaCy + Custom NER Models
- **ML**: Fine-tuned BERT para clasificación
- **API**: FastAPI + Celery (async processing)

### **Microservicio 2: Tax Calculator**
- **Engine**: Rules-based + ML predictions
- **Database**: PostgreSQL + Redis cache
- **Regulations**: JSON schemas + Python validators

### **Interface Web**
- **Framework**: Django Admin + Custom Apps
- **Frontend**: Bootstrap + htmx
- **Reports**: WeasyPrint (PDF generation)

### **Infraestructura**
- **Containerization**: Docker + Kubernetes
- **Cloud**: Google Cloud Platform
- **CI/CD**: GitHub Actions
- **Monitoring**: Prometheus + Grafana

## 📄 Tipos de Documentos Procesados

### **Escrituras de Compraventa**
- 🏠 Datos del inmueble (dirección, referencia catastral)
- 💰 Precio de compraventa y valor catastral
- 👥 Comprador y vendedor (DNI, nombres)
- 📅 Fechas de operación y otorgamiento
- 📋 Cálculo: ITP, AJD, Plusvalía Municipal

### **Documentos de Herencia**
- 👨‍👩‍👧‍👦 Causante y herederos
- 🏠 Bienes inmuebles heredados
- 💰 Valoración de herencia
- 📋 Cálculo: Impuesto de Sucesiones

### **Documentos Privados**
- 📜 Contratos de arrendamiento
- 🤝 Acuerdos patrimoniales
- 📋 Cálculo: Transmisiones Patrimoniales

## 🚀 Features Principales

### **🤖 Procesamiento Inteligente**
- ✅ OCR automático de documentos escaneados
- ✅ Extracción de entidades con NLP custom
- ✅ Clasificación automática por tipo de documento
- ✅ Validación de datos extraídos

### **💰 Cálculo Automático de Impuestos**
- ✅ Motor de reglas basado en normativa municipal
- ✅ Integración con bases de datos catastrales
- ✅ Cálculo automático de bases imponibles
- ✅ Generación de liquidaciones

### **🌐 Integración Sistemas Municipales**
- ✅ API connector con Catastro
- ✅ Sincronización con sistema tributario
- ✅ Integración con Registro de la Propiedad
- ✅ Export a aplicaciones internas existentes

## 📁 Estructura del Proyecto
```
municipal-ai-system/
├── document-processor/    # Microservicio OCR/NLP
├── tax-calculator/        # Microservicio cálculos
├── web-interface/         # Django admin interface
├── database/             # Schemas y migrations
├── integration/          # APIs sistemas municipales
├── deployment/           # Docker + Kubernetes
└── docs/                # Documentación técnica
```

📁 municipal-ai-system/            # PROYECTO 2: Sistema Municipal IA
│   ├── 📁 document-processor/         # Microservicio procesamiento documentos
│   │   ├── 📁 src/
│   │   │   ├── main.py                # FastAPI para OCR/NLP
│   │   │   ├── models/
│   │   │   │   ├── document.py        # Modelo Document
│   │   │   │   ├── extraction.py      # Modelos extracción datos
│   │   │   │   └── validation.py      # Modelos validación
│   │   │   ├── services/
│   │   │   │   ├── ocr_service.py     # Tesseract + PDF processing
│   │   │   │   ├── nlp_service.py     # spaCy + Custom NER
│   │   │   │   ├── extraction_service.py  # Extracción estructurada
│   │   │   │   └── validation_service.py  # Validación datos
│   │   │   ├── ai_models/
│   │   │   │   ├── document_classifier.py
│   │   │   │   ├── entity_extractor.py
│   │   │   │   └── fine_tuned_models/
│   │   │   └── utils/
│   │   │       ├── pdf_handler.py
│   │   │       ├── text_cleaner.py
│   │   │       └── data_validator.py
│   │   ├── 📁 training/               # Entrenamiento modelos IA
│   │   │   ├── 📁 datasets/
│   │   │   │   ├── raw_documents/     # PDFs originales
│   │   │   │   ├── labeled_data/      # Datos etiquetados
│   │   │   │   └── processed/         # Datos procesados
│   │   │   ├── 📁 notebooks/          # Jupyter notebooks
│   │   │   │   ├── data_exploration.ipynb
│   │   │   │   ├── model_training.ipynb
│   │   │   │   └── evaluation.ipynb
│   │   │   ├── 📁 scripts/
│   │   │   │   ├── prepare_dataset.py
│   │   │   │   ├── train_ner.py
│   │   │   │   └── evaluate_model.py
│   │   │   └── 📁 configs/
│   │   │       ├── spacy_config.cfg
│   │   │       └── training_params.json
│   │   ├── 📁 tests/
│   │   └── 📋 requirements.txt
│   │
│   ├── 📁 tax-calculator/             # Microservicio cálculo impuestos
│   │   ├── 📁 src/
│   │   │   ├── main.py
│   │   │   ├── models/
│   │   │   │   ├── property.py        # Modelo Inmueble
│   │   │   │   ├── tax_calculation.py # Modelo Cálculo
│   │   │   │   └── regulations.py     # Modelo Normativas
│   │   │   ├── services/
│   │   │   │   ├── tax_service.py     # Lógica cálculo
│   │   │   │   ├── rules_engine.py    # Motor reglas
│   │   │   │   └── report_service.py  # Generación informes
│   │   │   └── utils/
│   │   │       ├── calculations.py
│   │   │       └── validators.py
│   │   ├── 📁 regulations/            # Base de datos normativa
│   │   │   ├── municipal_rates.json
│   │   │   ├── state_regulations.json
│   │   │   └── tax_formulas.py
│   │   └── 📁 tests/
│   │
│   ├── 📁 web-interface/              # Django admin interface
│   │   ├── 📁 municipal_admin/
│   │   │   ├── settings.py
│   │   │   ├── urls.py
│   │   │   └── wsgi.py
│   │   ├── 📁 apps/
│   │   │   ├── documents/             # App gestión documentos
│   │   │   ├── taxes/                 # App gestión impuestos
│   │   │   ├── reports/               # App informes
│   │   │   └── integration/           # App integración sistemas
│   │   ├── 📁 templates/
│   │   ├── 📁 static/
│   │   └── 📋 requirements.txt
│   │
│   ├── 📁 database/
│   │   ├── 📁 migrations/
│   │   ├── 📁 seeds/
│   │   │   ├── alfafar_regulations.sql
│   │   │   └── sample_documents.sql
│   │   └── schema.sql
│   │
│   ├── 📁 integration/                # Integración sistemas municipales
│   │   ├── 📁 api_connectors/
│   │   │   ├── catastro_connector.py
│   │   │   ├── registro_connector.py
│   │   │   └── hacienda_connector.py
│   │   └── 📁 data_sync/
│   │
│   ├── 📁 deployment/
│   │   ├── 🐳 docker-compose.yml
│   │   ├── ☸️ kubernetes/
│   │   │   ├── document-processor.yaml
│   │   │   ├── tax-calculator.yaml
│   │   │   └── web-interface.yaml
│   │   └── 🔧 terraform/
│   │       ├── gcp_infrastructure.tf
│   │       └── database.tf
│   │
│   └── 📁 docs/
│       ├── ARCHITECTURE.md
│       ├── API_DOCUMENTATION.md
│       ├── DEPLOYMENT_GUIDE.md
│       ├── USER_MANUAL.md
│       └── INTEGRATION_GUIDE.md
│
└── 📁 shared-resources/               # Recursos compartidos
    ├── 📁 templates/
    │   ├── fastapi_template/
    │   ├── django_template/
    │   └── docker_templates/
    ├── 📁 utils/
    │   ├── common_validators.py
    │   ├── logging_config.py
    │   └── environment_manager.py
    └── 📁 docs/
        ├── CODING_STANDARDS.md
        ├── GIT_WORKFLOW.md
        └── LEARNING_RESOURCES.md

## 🏃‍♂️ Cómo Ejecutar (Desarrollo)

### Con Docker Compose
```bash
# Levantar todos los servicios
docker-compose up -d

# Servicios disponibles:
# - Document Processor: http://localhost:8001
# - Tax Calculator: http://localhost:8002  
# - Web Interface: http://localhost:8000
# - PostgreSQL: localhost:5432
```

### Desarrollo Individual
```bash
# Document Processor
cd document-processor
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn src.main:app --port 8001 --reload

# Tax Calculator
cd tax-calculator
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn src.main:app --port 8002 --reload

# Web Interface
cd web-interface
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

## 📊 Métricas de Impacto Esperadas
- ⚡ **Reducción 90%** tiempo procesamiento documentos
- 🎯 **Precisión >95%** en extracción de datos
- 💰 **Ahorro 80%** costes administrativos
- 📈 **Incremento 300%** productividad funcionarios
- ❌ **Reducción 95%** errores humanos

## 📚 Roadmap de Desarrollo

### Fase 1: MVP Core (Meses 1-2)
- [ ] Document processor básico (OCR + NLP)
- [ ] Tax calculator para compraventas
- [ ] Interface web administrativa
- [ ] Base de datos y modelos

### Fase 2: IA Avanzada (Meses 3-4)  
- [ ] Fine-tuning modelos NLP específicos
- [ ] ML para predicción valores catastrales
- [ ] Validación automática documentos
- [ ] Reports automáticos

### Fase 3: Integración (Meses 5-6)
- [ ] APIs integración sistemas municipales
- [ ] Deployment producción
- [ ] Training funcionarios
- [ ] Monitoring y analytics

## 🔒 Consideraciones de Seguridad
- 🔐 Encriptación end-to-end documentos
- 🛡️ GDPR compliance (datos personales)
- 🔑 Autenticación robusta funcionarios
- 📝 Audit logs completos
- 🏛️ Cumplimiento normativa municipal

## 📞 Contacto
**Proyecto**: Sistema Automatización Municipal  
**Desarrollador**: Jose  
**Cliente**: Ayuntamiento de Alfafar  
**Estado**: En desarrollo (MVP) 