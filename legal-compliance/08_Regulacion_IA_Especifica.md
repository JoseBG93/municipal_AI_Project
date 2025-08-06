# 08. REGULACIÓN IA ESPECÍFICA - AI ACT MUNICIPAL
## Sistema Municipal IA - Ayuntamiento de Alfafar

---

**📅 Documento:** 08_Regulacion_IA_Especifica.md  
**🏛️ Entidad:** Ayuntamiento de Alfafar (Valencia, España)  
**⚖️ Marco normativo:** AI Act UE (Reglamento 2024/1689) + desarrollo nacional  
**📋 Versión:** 1.0  
**📅 Fecha:** 1 agosto 2025  
**👤 Responsable:** José - Inspección Tributaria + DPO Municipal  

---

## 🎯 OBJETIVO DEL DOCUMENTO

Establecer la aplicación **específica y detallada** del AI Act (Reglamento UE 2024/1689) al Sistema Municipal IA del Ayuntamiento de Alfafar, desarrollando todos los aspectos normativos, técnicos y operativos para garantizar cumplimiento integral desde la concepción hasta la operación de cada algoritmo municipal.

---

## 📋 ÍNDICE

1. [Marco AI Act: Aplicación Municipal](#marco-ai-act-aplicación-municipal)
2. [Clasificación Sistemas IA Alfafar](#clasificación-sistemas-ia-alfafar)
3. [Sistemas Alto Riesgo: Obligaciones](#sistemas-alto-riesgo-obligaciones)
4. [Sistemas Riesgo Limitado](#sistemas-riesgo-limitado)
5. [Supervisión Humana Efectiva](#supervisión-humana-efectiva)
6. [Transparencia y Explicabilidad](#transparencia-y-explicabilidad)
7. [Gestión Riesgos y Auditoría](#gestión-riesgos-y-auditoría)
8. [Documentación Técnica AI Act](#documentación-técnica-ai-act)
9. [Conformidad y Certificación](#conformidad-y-certificación)
10. [Infracciones y Sanciones](#infracciones-y-sanciones)

---

## 📚 1. MARCO AI ACT: APLICACIÓN MUNICIPAL

### 1.1 Cronología de Entrada en Vigor

#### **📅 Calendario AI Act para Alfafar (Referencia: 1 agosto 2025)**

```yaml
# Timeline crítico para sistemas municipales:

FASE_1_PROHIBICIONES: 
  fecha_vigor: "2 febrero 2025"
  estado: "VIGENTE desde hace 6 meses"
  aplicacion_alfafar: "Prohibiciones ya implementadas"
  sistemas_afectados: "Sistemas puntuación social, manipulación cognitiva"

FASE_2_MODELOS_PROPOSITO_GENERAL:
  fecha_vigor: "2 agosto 2025" 
  estado: "VIGENTE desde HOY"
  aplicacion_alfafar: "Proveedores LLM deben cumplir obligaciones"
  sistemas_afectados: "OpenAI, Google, otros modelos base utilizados"

FASE_3_SISTEMAS_ALTO_RIESGO:
  fecha_vigor: "2 agosto 2026"
  estado: "PENDIENTE - En 12 meses"
  aplicacion_alfafar: "Sistemas municipales deben estar conformes"
  sistemas_afectados: "TODO el sistema tributario IA"

FASE_4_APLICACION_COMPLETA:
  fecha_vigor: "2 agosto 2026"
  estado: "PENDIENTE - En 12 meses"
  aplicacion_alfafar: "Cumplimiento integral obligatorio"
  preparacion_necesaria: "Documentación + certificación + auditorías"
```

### 1.2 Definiciones Específicas Municipales

#### **🏛️ Conceptos AI Act aplicados a Alfafar:**

**🤖 Sistema de IA (Art. 3.1):**
```markdown
# Definición oficial AI Act:
"Sistema basado en máquina que, para objetivos explícitos o implícitos, 
infiere de las entradas que recibe cómo generar salidas como predicciones, 
contenido, recomendaciones o decisiones que pueden influir en entornos 
físicos o virtuales"

# Aplicación específica Alfafar:
✅ INCLUIDO - document_processor (OCR + extracción datos)
✅ INCLUIDO - tax_calculator (cálculos automatizados)
✅ INCLUIDO - anomaly_detector (detección patrones irregulares)
✅ INCLUIDO - chatbot_ciudadanos (interacción automatizada)
❌ NO INCLUIDO - Calculadoras básicas sin ML
❌ NO INCLUIDO - Bases datos tradicionales
❌ NO INCLUIDO - Software gestión estándar (GTT básico)
```

**👥 Proveedor vs Usuario AI Act:**
```yaml
# Roles específicos Sistema Municipal Alfafar:

PROVEEDOR_IA:
  definicion: "Desarrolla sistema IA o encarga desarrollo a terceros para comercialización"
  aplicacion_alfafar:
    - proveedor_software: "Empresa desarrolla sistema municipal específico"
    - responsabilidades: "Documentación técnica + conformidad + marcado CE"
    - obligaciones_principales: "Art. 9-15 AI Act (gestión riesgos, documentación, etc.)"

USUARIO_IA:
  definicion: "Utiliza sistema IA bajo su autoridad, excepto uso personal no profesional"
  aplicacion_alfafar:
    - ayuntamiento_alfafar: "Usuario final del sistema IA tributario"
    - responsabilidades: "Supervisión humana + uso conforme + monitoreo"
    - obligaciones_principales: "Art. 26-27 AI Act (uso responsable, supervisión)"

CASO_ESPECIAL_DESARROLLO_PROPIO:
  situacion: "Ayuntamiento desarrolla internamente sistema IA"
  resultado: "Ayuntamiento es TANTO proveedor COMO usuario"
  obligaciones: "TODAS las obligaciones Art. 9-15 + Art. 26-27"
```

---

## 🎯 2. CLASIFICACIÓN SISTEMAS IA ALFAFAR

### 2.1 Metodología de Clasificación

#### **📊 Evaluación por Anexo III AI Act:**

```yaml
# ANEXO III - SISTEMAS IA ALTO RIESGO
# Punto 5: "Gestión y funcionamiento de infraestructuras críticas"
# Punto 6: "Administración pública y servicios públicos democráticos"

evaluacion_sistemas_alfafar:
  criterio_evaluacion:
    - "¿Afecta significativamente salud, seguridad, derechos fundamentales?"
    - "¿Toma decisiones o influye decisiones con impacto legal/económico?"
    - "¿Evalúa personas físicas para acceso servicios públicos?"
    - "¿Gestiona recursos públicos o servicios esenciales?"
```

### 2.2 Clasificación Detallada por Sistema

#### **🔴 SISTEMAS ALTO RIESGO**

**Sistema 1: Tax Calculator Automático**
```yaml
tax_calculator_automatic:
  categoria_ai_act: "Anexo III.6.b - Evaluación personas físicas servicios públicos"
  justificacion: "Calcula liquidaciones tributarias con impacto económico directo"
  
  ambito_aplicacion:
    figuras_tributarias:
      - iivtnu: "Cálculo plusvalía municipal automatizado"
      - ibi: "Liquidación Impuesto Bienes Inmuebles"
      - iae: "Determinación cuotas Actividades Económicas"
      - icio: "Cálculo Construcciones e Instalaciones"
      - ivtm: "Liquidación Vehículos Tracción Mecánica"
    tasas_municipales:
      - vado_permanente: "Cálculo automático ocupación vía pública"
      - licencias_urbanisticas: "Determinación tasas obras/actividades"
      - cementerio: "Liquidación servicios funerarios"
      - agua_alcantarillado: "Facturación automática suministros"
  
  riesgos_identificados:
    - calculo_erroneo: "Liquidación incorrecta → perjuicio económico ciudadano"
    - discriminacion_algoritmica: "Tratamiento diferencial por zona/perfil"
    - falta_transparencia: "Ciudadano no comprende cálculo automático"
    - supervision_insuficiente: "Funcionario no detecta error algoritmo"
  
  obligaciones_ai_act:
    - art_9: "Sistema gestión riesgos específico tributario"
    - art_10: "Datos entrenamiento calidad + representatividad"
    - art_11: "Documentación técnica completa cada algoritmo"
    - art_12: "Logs automáticos cada cálculo tributario"
    - art_13: "Transparencia información ciudadanos"
    - art_14: "Supervisión humana efectiva funcionarios"
    - art_15: "Exactitud + robustez + ciberseguridad"
```

**Sistema 2: Anomaly Detector Tributario**
```yaml
anomaly_detector_fiscal:
  categoria_ai_act: "Anexo III.6.a - Aplicación ley, migración, asilo, control fronteras"
  aplicacion_especifica: "Detección fraude tributario y evasión fiscal"
  
  funcionalidades_alto_riesgo:
    deteccion_patrones:
      - declaraciones_inconsistentes: "Valores atípicos vs mercado/catastro"
      - actividades_no_declaradas: "Consumos/movimientos vs actividad declarada"
      - evasion_sistematica: "Patrones repetidos elusión tributaria"
      - documentacion_fraudulenta: "Documentos alterados/falsificados"
    
    consecuencias_decisiones:
      - apertura_expediente_inspeccion: "Investigación tributaria ciudadano"
      - aplicacion_recargos: "Penalizaciones económicas automáticas"
      - alertas_prioritarias: "Clasificación riesgo contribuyente"
      - derivacion_fiscal: "Comunicación otros organismos (AEAT, etc.)"
  
  riesgos_criticos:
    - falsos_positivos: "Investigación injustificada → perjuicio reputacional"
    - sesgo_territorial: "Mayor persecución zonas específicas municipio"
    - discriminacion_sectorial: "Prejuicio ciertos tipos actividad económica"
    - invasion_privacidad: "Análisis excesivo comportamiento ciudadanos"
```

**Sistema 3: Document Processor OCR + NLP**
```yaml
document_processor_intelligent:
  categoria_ai_act: "Anexo III.6.b - Evaluación automática documentos"
  impacto_critico: "Extracción errónea → liquidación incorrecta"
  
  documentos_procesados:
    notariales:
      - escrituras_compraventa: "Extraer valores, fechas, titulares"
      - aceptaciones_herencia: "Identificar herederos, bienes, cargas"
      - donaciones_inmuebles: "Determinar donante, donatario, condiciones"
      - capitulaciones_matrimoniales: "Regímenes económicos matrimoniales"
    
    judiciales:
      - sentencias_divorcio: "Adjudicaciones bienes conyugales"
      - embargos_ejecutorias: "Afecciones patrimoniales"
      - concursos_acreedores: "Situaciones insolvencia"
    
    administrativos:
      - autoliquidaciones_ciudadanos: "Declaraciones tributarias"
      - certificados_catastro: "Valores oficiales inmuebles"
      - licencias_actividad: "Altas/modificaciones económicas"
  
  criticidad_errores:
    nivel_alto:
      - identificacion_titular: "Error DNI → liquidación persona incorrecta"
      - valores_economicos: "Importe erróneo → cálculo tributario incorrecto"
      - fechas_criticas: "Error temporal → prescripción/devengo incorrecto"
    
    nivel_medio:
      - direcciones_inmuebles: "Ubicación incorrecta → tributo zona errónea"
      - superficies_construccion: "Metros erróneos → base imponible incorrecta"
      - descripciones_actividad: "Epígrafe IAE incorrecto"
```

#### **🟡 SISTEMAS RIESGO LIMITADO**

**Sistema 4: Chatbot Ciudadanos**
```yaml
chatbot_municipal_ai:
  categoria_ai_act: "Art. 50 - Sistemas interacción directa personas"
  obligacion_principal: "Información clara uso IA + limitaciones"
  
  funcionalidades_incluidas:
    informacion_general:
      - consultas_tributos: "Qué impuestos pago, cuándo, cómo"
      - procedimientos_administrativos: "Tramitación licencias, permisos"
      - horarios_servicios: "Atención ciudadana, pagos, gestiones"
      - normativa_municipal: "Ordenanzas, reglamentos aplicables"
    
    asistencia_basica:
      - calculo_estimativo: "Aproximaciones tributarias NO vinculantes"
      - formularios_descarga: "Impresos municipales disponibles"
      - citas_presenciales: "Reserva horarios atención"
      - estado_expedientes: "Consulta tramitación NO sensible"
  
  limitaciones_explicitas:
    - decision_vinculante: "NO puede tomar decisiones tributarias"
    - acceso_datos_personales: "NO accede información confidencial"
    - sustitucion_funcionario: "NO reemplaza atención humana especializada"
    - interpretacion_normativa: "NO interpreta casos complejos"
  
  transparencia_obligatoria:
    ubicacion_banner: "Visible permanente todas interacciones"
    texto_requerido: "🤖 Asistente IA - Información no vinculante - Consulte funcionario para decisiones oficiales"
    escalado_humano: "Botón directo 'Hablar con funcionario'"
```

#### **🟢 SISTEMAS RIESGO MÍNIMO**

**Sistemas No Regulados Específicamente:**
```yaml
sistemas_riesgo_minimo:
  aplicaciones_incluidas:
    - spam_filter_correos: "Filtrado automático correo municipal"
    - backup_automatico: "Respaldos programados datos"
    - antivirus_ia: "Detección malware con ML"
    - optimizacion_energia: "Gestión eficiente edificios municipales"
    - agenda_automatica: "Programación citas/reuniones"
  
  codigo_conducta_voluntario:
    transparencia: "Informar uso IA aunque no obligatorio"
    precision: "Mantener calidad servicio ciudadano"
    no_discriminacion: "Evitar sesgos incluso en usos menores"
```

---

## ⚖️ 3. SISTEMAS ALTO RIESGO: OBLIGACIONES

### 3.1 Sistema de Gestión de Riesgos (Art. 9)

#### **🛡️ Implementación Específica por Sistema:**

**Tax Calculator - Gestión Riesgos:**
```yaml
# SISTEMA GESTIÓN RIESGOS - TAX CALCULATOR

identificacion_riesgos:
  riesgos_inherentes:
    - algoritmo_calculo_erroneo: 
        probabilidad: "Baja"
        impacto: "Alto"
        descripcion: "Error programación → cálculo tributario incorrecto"
    
    - datos_entrada_incorrectos:
        probabilidad: "Media" 
        impacto: "Alto"
        descripcion: "OCR erróneo → base cálculo incorrecta"
    
    - normativa_desactualizada:
        probabilidad: "Media"
        impacto: "Medio"
        descripcion: "Cambio ordenanzas no reflejado → aplicación norma obsoleta"
    
    - sesgo_territorial:
        probabilidad: "Baja"
        impacto: "Alto"
        descripcion: "Algoritmo discrimina por zona municipio"

medidas_mitigacion:
  tecnicas:
    - validacion_cruzada: "2 algoritmos independientes verifican resultado"
    - threshold_confianza: "Revisión humana si confianza <99%"
    - testing_continuo: "Validación diaria muestra aleatoria 50 cálculos"
    - actualizacion_automatica: "Sincronización normativa en tiempo real"
  
  organizativas:
    - supervision_funcionario: "Inspector valida cada liquidación >500€"
    - formacion_especializada: "Curso anual algoritmos tributarios"
    - auditoria_mensual: "Revisión independiente precisión"
    - escalado_dudas: "Protocolo consulta casos complejos"

plan_mitigacion_incidentes:
  deteccion_error:
    tiempo_respuesta: "<2 horas"
    protocolo: "Suspensión automática + análisis causa raíz"
    
  comunicacion_afectados:
    tiempo_limite: "<24 horas"
    canal: "Email + SMS + publicación web municipal"
    
  correccion_implementacion:
    tiempo_limite: "<72 horas"
    validacion: "Testing exhaustivo antes reactivación"
```

**Document Processor - Gestión Riesgos:**
```yaml
# SISTEMA GESTIÓN RIESGOS - DOCUMENT PROCESSOR

riesgos_especificos_ocr:
  calidad_documento:
    - documentos_degradados:
        origen: "Fax, copias múltiples, escaneos baja calidad"
        impacto: "OCR <80% precisión → extracción errónea"
        mitigacion: "Threshold mínimo calidad + revisión manual"
    
    - idiomas_mixtos:
        origen: "Documentos catalán/español, términos latinos"
        impacto: "NLP confunde términos → interpretación errónea"
        mitigacion: "Modelo multiidioma + diccionario jurídico"
  
  sesgos_entrenamiento:
    - epoca_documentos:
        origen: "Modelo entrenado con docs años 2020-2024"
        impacto: "Formatos antiguos peor reconocimiento"
        mitigacion: "Dataset histórico ampliado 1990-2024"
    
    - notarias_especificas:
        origen: "Entrenamiento sesgado notarías Valencia capital"
        impacto: "Menor precisión notarías rurales/locales"
        mitigacion: "Muestreo balanceado geográfico"

controles_calidad:
  prevencion:
    - validacion_entrada: "Verificación legibilidad antes procesamiento"
    - sampling_humano: "10% documentos revisión manual aleatoria"
    - feedback_loop: "Funcionario corrige → algoritmo aprende"
  
  deteccion:
    - confidence_scores: "Alerta automática confianza <95%"
    - anomaly_detection: "Valores extremos requieren validación"
    - cross_validation: "Contraste múltiples fuentes datos"
```

### 3.2 Datos y Gobernanza (Art. 10)

#### **📊 Calidad y Representatividad Datos:**

**Conjuntos Datos Entrenamiento:**
```yaml
# REQUISITOS CALIDAD DATOS AI ACT

dataset_tax_calculator:
  datos_historicos:
    periodo: "2010-2024 (14 años datos tributarios)"
    volumen: "47.500 liquidaciones tributarias históricas"
    representatividad:
      - geografica: "100% calles municipio representadas"
      - temporal: "Todos meses año incluidos (estacionalidad)"
      - tipologica: "Todas figuras tributarias proporcionalmente"
      - socioeconomica: "Estratos económicos balanceados"
  
  calidad_garantizada:
    completitud: ">98% campos obligatorios completos"
    precision: ">99.5% liquidaciones verificadas históricamente"
    consistencia: "Validación cruzada catastro/registro"
    actualidad: "Normativa vigente cada período aplicada"
  
  sesgos_identificados_corregidos:
    - territorial: "Sobrerrepresentación centro urbano histórico"
      correccion: "Ponderación inversa por densidad población"
    
    - temporal: "Mayor volumen datos 2020-2024 vs períodos anteriores"  
      correccion: "Balanceo temporal proporcional"
    
    - tipologico: "Sesgo IIVTNU vs otras figuras (especialidad José)"
      correccion: "Muestreo equilibrado todas figuras"

dataset_document_processor:
  corpus_entrenamiento:
    documentos_anonimizados: "12.000 escrituras 2015-2024"
    variedad_notarial:
      - notarias_valencia: "60% (representatividad provincial)"
      - notarias_alfafar: "25% (especificidad local)"
      - notarias_comarca: "15% (contexto comarcal)"
    
    tipos_documentales:
      - compraventas: "45% (mayoría tramitación municipal)"
      - herencias: "25% (complejidad alta)"
      - donaciones: "20% (casuística específica)"
      - otros_actos: "10% (capitulaciones, etc.)"
  
  anonimizacion_conforme:
    tecnica: "Sustitución identificadores por tokens sintéticos"
    irreversibilidad: "Hash SHA-256 sin tabla reversión"
    validacion_rgpd: "Dictamen DPO + asesoría jurídica"
    testing_reidentificacion: "Auditoría anual imposibilidad recuperación datos"
```

### 3.3 Documentación Técnica (Art. 11)

#### **📋 Contenido Obligatorio por Sistema:**

**Documentación Tax Calculator:**
```yaml
# DOCUMENTACIÓN TÉCNICA COMPLETA

informacion_general:
  finalidad_sistema: "Cálculo automático liquidaciones tributarias municipales"
  destinatarios_previstos: "Funcionarios Inspección Tributaria Alfafar"
  contexto_uso: "Apoyo decisión + validación cruzada cálculos manuales"
  limitaciones_conocidas:
    - bonificaciones_excepcionales: "Requieren interpretación humana"
    - normativa_transitoria: "Períodos cambio requieren supervisión"
    - casos_judiciales: "Sentencias específicas no automatizables"

descripcion_algoritmos:
  motor_reglas_tributarias:
    tipo: "Rule-based engine con validación ML"
    implementacion: "487 reglas codificadas + árbol decisión"
    entrada: "JSON estructurado datos contribuyente/inmueble/actividad"
    salida: "Liquidación completa + justificación legal + confianza"
    
  validador_machine_learning:
    tipo: "Ensemble (Random Forest + XGBoost + SVM)"
    entrenamiento: "47.500 liquidaciones históricas verificadas"
    metricas_actuales:
      - precision: "99.95% cálculos matemáticos exactos"
      - recall: "98.7% detección casos especiales"
      - f1_score: "99.3% equilibrio precisión/cobertura"
    
  detector_anomalias:
    tipo: "Isolation Forest + Statistical Process Control"
    funcion: "Identificar valores atípicos requieren revisión"
    umbrales: "Desviación >2σ → alerta, >3σ → bloqueo automático"

especificaciones_tecnicas:
  hardware_minimo:
    cpu: "4 cores 2.5GHz"
    ram: "8GB DDR4"
    storage: "100GB SSD para modelos"
    red: "1Gbps para tiempo real"
  
  software_dependencias:
    sistema_operativo: "Ubuntu 22.04 LTS / RHEL 8+"
    python: "3.11+ con librerías científicas"
    base_datos: "PostgreSQL 15+ con extensiones"
    contenedores: "Docker 24+ + Swarm mode"
  
  integraciones_requeridas:
    sistemas_municipales:
      - gtt: "Consulta/actualización expedientes tributarios"
      - gestiona: "Verificación datos registrales"
      - catastro: "Valores/referencias inmuebles"
      - padrón: "Datos censales contribuyentes"
    
    sistemas_externos:
      - sede_electronica: "Notificaciones ciudadanos"
      - aeat: "Coordinación censos/inspección"
      - registro_propiedad: "Verificación titularidades"

gestion_riesgos_documentada:
  matriz_riesgos_completa: "Ver sección 3.1 detallada"
  controles_implementados: "Técnicos + organizativos + humanos"
  testing_validacion: "Continuo + periódico + ante actualizaciones"
  plan_contingencia: "Fallback manual + escalado + comunicación"
```

### 3.4 Registros y Trazabilidad (Art. 12)

#### **📊 Logs Obligatorios Estructurados:**

```json
{
  "sistema_municipal_alfafar": {
    "timestamp_utc": "2025-08-01T09:15:23.456Z",
    "timestamp_local": "2025-08-01T11:15:23.456+02:00",
    "sistema_ia": "tax_calculator_iivtnu",
    "version_algoritmo": "v3.1.2",
    "version_normativa": "ordenanza_iivtnu_alfafar_2025_v1",
    
    "identificacion_procesamiento": {
      "sesion_id": "sess_20250801_091523_abc123",
      "funcionario_hash": "sha256_inspector_tributario_001",
      "expediente_hash": "sha256_exp_iivtnu_2025_2847", 
      "ciudadano_hash": "sha256_dni_contribuyente_xyz789"
    },
    
    "input_datos": {
      "tipo_calculo": "iivtnu_compraventa",
      "valor_adquisicion": 180000.00,
      "valor_transmision": 245000.00,
      "fecha_adquisicion": "2018-03-15",
      "fecha_transmision": "2025-07-28",
      "coeficiente_periodo": 1.4521,
      "tipo_gravamen_municipal": 0.075,
      "bonificaciones_aplicables": []
    },
    
    "procesamiento_ia": {
      "algoritmo_principal": "rule_engine_iivtnu",
      "algoritmo_validacion": "ml_ensemble_validator", 
      "tiempo_procesamiento_ms": 234,
      "confianza_calculo": 0.9987,
      "anomalias_detectadas": [],
      "validaciones_superadas": [
        "coherencia_fechas",
        "valores_mercado_catastro",
        "coeficientes_dgc",
        "normativa_vigente",
        "bonificaciones_aplicables"
      ]
    },
    
    "resultado_calculo": {
      "base_imponible": 29486.50,
      "cuota_integra": 2211.49,
      "bonificaciones_aplicadas": 0.00,
      "cuota_liquida": 2211.49,
      "cuota_diferencial": 2211.49,
      "recargos_aplicables": 0.00,
      "importe_total": 2211.49
    },
    
    "supervision_humana": {
      "requerida": false,
      "motivo_no_requerida": "confianza_superior_99%",
      "funcionario_notificado": true,
      "revision_posterior_disponible": true,
      "tiempo_limite_revision": "2025-08-08T11:15:23+02:00"
    },
    
    "cumplimiento_ai_act": {
      "sistema_clasificado_alto_riesgo": true,
      "documentacion_tecnica_vigente": "v3.1_20250701",
      "gestion_riesgos_activa": true,
      "logs_conservacion_meses": 24,
      "transparencia_ciudadano_disponible": true
    },
    
    "auditoria": {
      "hash_integridad": "sha256_log_entry_complete_xyz456",
      "firma_digital": "rsa_signature_municipal_cert",
      "backup_automatico": true,
      "retencion_legal_anios": 6
    }
  }
}
```

---

## 👥 4. SUPERVISIÓN HUMANA EFECTIVA (Art. 14)

### 4.1 Diseño de Supervisión por Sistema

#### **🎯 Tax Calculator - Supervisión Multinivel:**

```yaml
# SUPERVISIÓN HUMANA ESCALONADA

nivel_1_automatico:
  activacion: "Todas las liquidaciones"
  algoritmo: "Confidence scoring + anomaly detection"
  acciones:
    - confianza_99_100: "Procesamiento automático → Notificación funcionario"
    - confianza_95_99: "Revisión recomendada → Alerta amarilla"
    - confianza_85_95: "Revisión obligatoria → Alerta naranja"
    - confianza_0_85: "Bloqueo automático → Alerta roja"

nivel_2_funcionario_ventanilla:
  perfil: "Auxiliar administrativo formación básica IA"
  competencias_requeridas:
    - conocimiento_tributos: "Normativa básica IIVTNU/IBI/IAE"
    - formacion_ia: "Curso 20h 'Supervisión algoritmos municipales'"
    - herramientas_software: "Interface revisión + override manual"
  
  casos_supervision:
    alertas_amarillas:
      - revision_recomendada: "Validar cálculo antes envío ciudadano"
      - tiempo_disponible: "48 horas antes envío automático"
      - herramientas: "Calculadora manual + acceso expediente"
    
    alertas_naranjas:
      - revision_obligatoria: "No se envía sin validación humana"
      - tiempo_limite: "72 horas máximo resolución"
      - escalado_automatico: "Si no se resuelve → inspector senior"

nivel_3_inspector_senior:
  perfil: "Funcionario A1/A2 experiencia >5 años tributaria"
  competencias_especializadas:
    - interpretacion_normativa: "Casos complejos + jurisprudencia"
    - supervision_ia: "Curso 40h 'Gestión sistemas IA públicos'"
    - decision_final: "Autoridad override completo algoritmo"
  
  casos_intervencion:
    alertas_rojas:
      - bloqueo_automatico: "Sistema no permite procesamiento"
      - analisis_requerido: "Identificar causa error/sesgo"
      - decision_manual: "Cálculo completamente manual si necesario"
    
    casos_excepcionales:
      - normativa_nueva: "Interpretación cambios legislativos"
      - jurisprudencia_aplicable: "Sentencias específicas afectan caso"
      - bonificaciones_especiales: "Circunstancias no contempladas algoritmo"

nivel_4_coordinacion_dpd:
  activacion: "Patrones sistemáticos problemas IA"
  funciones_especificas:
    - auditoria_sesgo: "Análisis discriminación territorial/sectorial"
    - mejora_algoritmos: "Recomendaciones técnicas proveedores"
    - formacion_funcionarios: "Actualización competencias supervisión"
    - comunicacion_ciudadanos: "Transparencia decisiones automatizadas"
```

#### **🔍 Document Processor - Supervisión Especializada:**

```yaml
# SUPERVISIÓN DOCUMENTAL POR TIPOLOGÍA

documentos_criticos_supervision:
  escrituras_alto_valor:
    criterio: "Transmisiones >500.000€"
    supervision: "Revisión manual obligatoria 100%"
    funcionario: "Técnico tributario + inspector validación"
    
  documentos_complejos:
    criterio: "Herencias múltiples herederos, donaciones condicionales"
    supervision: "OCR + revisión completa contenido"
    herramientas: "Interface comparación texto original vs extraído"
    
  documentos_degradados:
    criterio: "Confidence OCR <95%"
    supervision: "Re-escaneo alta calidad + procesamiento manual"
    backup: "Transcripción humana si algoritmo falla"

herramientas_supervision:
  interface_revision:
    pantalla_dividida: "Documento original + datos extraídos"
    campos_editables: "Corrección inmediata datos incorrectos"
    validacion_tiempo_real: "Verificación coherencia durante edición"
    
  feedback_algoritmo:
    correccion_automatica: "Funcionario corrige → algoritmo aprende"
    patrones_error: "Identificación sistemática problemas OCR"
    mejora_continua: "Actualización modelos cada 1000 correcciones"
```

### 4.2 Competencias y Formación Supervisores

#### **📚 Programa Formativo Obligatorio:**

```yaml
# FORMACIÓN FUNCIONARIOS SUPERVISIÓN IA

curso_basico_20h:
  destinatarios: "Auxiliares administrativos + técnicos municipales"
  contenidos:
    modulo_1_conceptos: "¿Qué es IA? Algoritmos municipales específicos"
    modulo_2_responsabilidades: "Supervisión humana vs automatización"
    modulo_3_herramientas: "Interface supervisión + casos prácticos"
    modulo_4_normativa: "AI Act + RGPD aplicación municipal"
    modulo_5_casos_practicos: "Situaciones reales + resolución"
  
  evaluacion:
    examen_teorico: "80% mínimo aprobado"
    casos_practicos: "Resolución correcta 5/7 casos"
    certificacion: "Válida 2 años + reciclaje obligatorio"

curso_avanzado_40h:
  destinatarios: "Inspectores + funcionarios decisión final"
  contenidos:
    modulo_avanzado_1: "Arquitectura sistemas IA municipales"
    modulo_avanzado_2: "Evaluación sesgo + discriminación"
    modulo_avanzado_3: "Gestión crisis + errores sistemáticos"
    modulo_avanzado_4: "Coordinación proveedores + auditorías"
    modulo_avanzado_5: "Transparencia ciudadana + comunicación"
  
  competencias_certificadas:
    - override_completo_algoritmos: "Autoridad suspender sistema IA"
    - interpretacion_casos_complejos: "Decisión normativa/jurisprudencia"
    - coordinacion_mejoras_tecnicas: "Comunicación con proveedores"
    - gestion_incidentes_graves: "Protocolo crisis + comunicación"

formacion_continua:
  frecuencia: "Trimestral 4h actualización"
  contenidos_actualizacion:
    - nuevas_funcionalidades: "Actualizaciones sistema IA"
    - cambios_normativos: "Modificaciones AI Act + normativa municipal"
    - lecciones_aprendidas: "Casos reales + mejores prácticas"
    - coordinacion_otros_municipios: "Intercambio experiencias"
```

---

## 💡 5. TRANSPARENCIA Y EXPLICABILIDAD (Art. 13)

### 5.1 Portal Transparencia IA Municipal

#### **🌐 Portal Público Obligatorio: transparencia-ia.alfafar.es**

```yaml
# ESTRUCTURA PORTAL TRANSPARENCIA AI ACT

seccion_1_sistemas_operativos:
  titulo: "¿Qué sistemas IA usa mi Ayuntamiento?"
  contenido_minimo:
    inventario_completo:
      - tax_calculator: 
          descripcion: "Cálculo automático impuestos y tasas municipales"
          figuras_afectadas: "IIVTNU, IBI, IAE, ICIO, IVTM + tasas"
          decision_final: "Supervisión funcionario + derecho revisión"
      
      - document_processor:
          descripcion: "Extracción automática datos documentos notariales"
          documentos_procesados: "Escrituras, herencias, donaciones"
          precision_actual: "95.7% textos español notarial"
      
      - anomaly_detector:
          descripcion: "Detección patrones irregulares tributarios"
          objetivo: "Apoyo inspección + prevención fraude"
          garantias: "Solo alertas - decisión siempre humana"
    
    clasificacion_riesgos:
      alto_riesgo: "Sistemas decisión automática impacto económico"
      riesgo_limitado: "Sistemas interacción ciudadanos (chatbot)"
      riesgo_minimo: "Herramientas administrativas internas"

seccion_2_derechos_ciudadanos:
  titulo: "Sus derechos ante decisiones automatizadas"
  contenido_garantias:
    derecho_informacion:
      - notificacion_clara: "Cuando decisión tomada por IA"
      - logica_comprensible: "Explicación cómo se calculó"
      - factores_determinantes: "Qué datos influyeron decisión"
    
    derecho_revision_humana:
      - solicitud_gratuita: "Petición revisión sin coste"
      - plazo_resolucion: "30 días máximo respuesta"
      - funcionario_competente: "Inspector tributario senior"
      - decision_vinculante: "Funcionario puede cambiar decisión IA"
    
    derechos_rgpd_aplicables:
      - acceso_datos: "Consultar información personal usada"
      - rectificacion: "Corregir datos incorrectos"
      - oposicion: "Oponerse tratamiento específico"
      - portabilidad: "Obtener datos formato estructurado"

seccion_3_funcionamiento_algoritmos:
  titulo: "¿Cómo funcionan nuestros algoritmos?"
  explicacion_comprensible:
    tax_calculator_explicado:
      funcionamiento_basico: |
        "El sistema consulta el valor de su inmueble en Catastro,
        aplica los coeficientes oficiales según años transcurridos,
        calcula el incremento valor según ordenanza municipal,
        y determina la cuota tributaria final.
        
        Si detecta valores atípicos o casos especiales,
        automáticamente deriva a funcionario para revisión."
      
      factores_considerados:
        - "Valor catastral actualizado inmueble"
        - "Fecha adquisición vs fecha transmisión"
        - "Coeficientes oficiales Dirección General Catastro"
        - "Bonificaciones ordenanza municipal vigente"
        - "Comparación valores mercado zona"
      
      factores_NO_considerados:
        - "Datos personales (edad, estado civil, ingresos)"
        - "Información política, religiosa, sindical"
        - "Datos familiares no relevantes tributariamente"
        - "Ubicación exacta dentro zona fiscal"

seccion_4_calidad_seguridad:
  titulo: "¿Cómo garantizamos calidad y seguridad?"
  metricas_publicas:
    precision_sistemas:
      - tax_calculator: "99.95% cálculos matemáticos exactos"
      - document_processor: "95.7% precisión OCR documentos"
      - anomaly_detector: "<5% falsos positivos detectados"
    
    supervision_humana:
      - revision_obligatoria: "100% liquidaciones >1.000€"
      - tiempo_respuesta: "Máximo 72h casos complejos"
      - override_disponible: "Funcionario siempre puede modificar"
    
    seguridad_datos:
      - cifrado_extremo: "AES-256 toda información personal"
      - acceso_restringido: "Solo funcionarios autorizados"
      - logs_completos: "Registro todas operaciones auditables"
      - backup_seguro: "Copias cifradas + eliminación automática"

seccion_5_contacto_dpd:
  titulo: "¿Preguntas sobre IA municipal?"
  canales_disponibles:
    dpd_municipal:
      email: "dpo@alfafar.es"
      telefono: "96 XXX XX XX (ext. 247)"
      presencial: "Lunes a viernes 9h-14h - Ayuntamiento"
      web: "Formulario específico consultas IA"
    
    funcionario_responsable:
      cargo: "Inspector Jefe Tributario"
      email: "tributaria@alfafar.es"
      telefono: "96 XXX XX XX (ext. 156)"
      horario_atencion: "Martes y jueves 10h-12h"
```

### 5.2 Explicabilidad Decisiones Individuales

#### **📋 Templates Explicación Ciudadanos:**

**Template Liquidación IIVTNU:**
```markdown
# 🏛️ AYUNTAMIENTO DE ALFAFAR - LIQUIDACIÓN IIVTNU
## Cálculo realizado por Sistema IA Municipal (Tax Calculator v3.1.2)

### 📊 SUS DATOS DE CÁLCULO:
- **Inmueble**: Calle Mayor, 45 - Alfafar
- **Referencia catastral**: 46XXX XXX XX XXXX XX XXXX XX
- **Valor catastral**: 185.400€ (Catastro 2024)
- **Fecha adquisición**: 15 marzo 2018
- **Fecha transmisión**: 28 julio 2025
- **Años tenencia**: 7 años, 4 meses, 13 días

### 🧮 CÁLCULO AUTOMÁTICO REALIZADO:
1. **Base cálculo**: 185.400€ (valor catastral)
2. **Coeficiente período**: 1.4521 (oficial DGC 2018-2025)
3. **Incremento valor**: 185.400€ × 1.4521 - 185.400€ = 83.860€
4. **Base imponible**: 83.860€
5. **Tipo gravamen**: 7,5% (Ordenanza IIVTNU Alfafar 2025)
6. **Cuota íntegra**: 83.860€ × 7,5% = 6.289,50€
7. **Bonificaciones**: Ninguna aplicable
8. **CUOTA FINAL**: 6.289,50€

### ✅ VALIDACIONES REALIZADAS:
- ✅ Coherencia fechas verificada
- ✅ Valor catastral contrastado con base oficial
- ✅ Coeficientes DGC aplicados correctamente
- ✅ Bonificaciones ordenanza evaluadas
- ✅ Comparación valores mercado zona (normal)

### 🤖 INFORMACIÓN SISTEMA IA:
- **Confianza cálculo**: 99,87%
- **Revisión humana**: No requerida (alta confianza)
- **Funcionario notificado**: Inspector Tributario disponible
- **Tiempo procesamiento**: 0,234 segundos

### 👥 SUS DERECHOS:
- **Revisión humana**: Puede solicitar revisión gratuita
- **Plazo solicitud**: 30 días desde notificación
- **Funcionario competente**: Inspector Jefe Tributario
- **Modificación posible**: El funcionario puede cambiar decisión IA
- **Contacto**: tributaria@alfafar.es - Tel: 96 XXX XX XX

### 📞 ¿DUDAS SOBRE ESTE CÁLCULO?
**DPO Municipal**: dpo@alfafar.es
**Atención presencial**: Ayuntamiento (L-V 9h-14h)
**Más información**: transparencia-ia.alfafar.es

---
*Decisión tomada por Sistema IA bajo supervisión humana*
*Derecho revisión garantizado según AI Act Art. 14*
```

**Template Alerta Anomalía Detectada:**
```markdown
# 🔍 ALERTA DETECCIÓN AUTOMÁTICA - REVISIÓN REQUERIDA
## Sistema: Anomaly Detector Municipal v2.3.1

### ⚠️ DETECCIÓN AUTOMÁTICA:
**Patrón identificado**: Actividad económica potencialmente no declarada
**Ubicación**: [Dirección anonimizada para funcionario]
**Confianza detección**: 87%
**Requiere**: Revisión humana obligatoria

### 📊 FACTORES DETECTADOS:
1. **Consumo eléctrico**: 340% superior media residencial zona
2. **Horario actividad**: Patrón comercial lunes-sábado 8h-20h
3. **Licencia actividad**: No consta en base datos municipal
4. **Declaración IAE**: Sin alta epígrafe compatible
5. **Tráfico peatonal**: Incremento observado zona (datos anonimizados)

### 🤖 LIMITACIONES SISTEMA:
- **No es decisión final**: Solo alerta para investigación
- **Falsos positivos posibles**: ~5% casos similares
- **Supervisión humana obligatoria**: Inspector debe validar
- **Datos agregados**: No identifica personas específicas

### 👮 ACCIÓN FUNCIONARIO:
- **Inspector asignado**: [Código funcionario]
- **Verificación requerida**: Inspección presencial + documentación
- **Plazo resolución**: 15 días laborables
- **Decisión final**: Solo funcionario competente

### 📋 CUMPLIMIENTO AI ACT:
- **Sistema clasificado alto riesgo**: Supervisión humana obligatoria
- **Explicabilidad garantizada**: Factores decisión transparentes
- **Trazabilidad completa**: Log auditoria disponible
- **Derechos ciudadano**: Información + revisión + oposición

---
*Alerta generada automáticamente para apoyo inspección*
*Decisión final siempre humana según Art. 14 AI Act*
```

---

## 🔍 6. GESTIÓN RIESGOS Y AUDITORÍA

### 6.1 Plan de Auditoría AI Act Específico

#### **📋 Auditorías Obligatorias por Cronograma:**

```yaml
# PLAN AUDITORÍA SISTEMAS IA MUNICIPAL

auditoria_mensual_interna:
  responsable: "DPO Municipal + Técnico IA"
  alcance: "Funcionamiento algoritmos + métricas calidad"
  metodologia:
    testing_precision:
      - muestra_aleatoria: "100 liquidaciones mes anterior"
      - verificacion_manual: "Inspector senior valida cálculos"
      - metricas_obtenidas: "Precisión, recall, F1-score"
      - threshold_alerta: "Precisión <99.5% → auditoría urgente"
    
    analisis_sesgo:
      - segmentacion_territorial: "Cálculos por zona municipio"
      - analisis_temporal: "Variaciones rendimiento por época"
      - deteccion_discriminacion: "Test estadístico equidad"
      - correccion_automatica: "Ajuste parámetros si sesgo detectado"
  
  reporting:
    informe_tecnico: "Métricas + recomendaciones mejora"
    dashboard_ejecutivo: "KPIs tiempo real alcaldía"
    comunicacion_ciudadanos: "Resumen público web municipal"

auditoria_trimestral_algoritmos:
  responsable: "Auditor externo certificado + DPO"
  alcance: "Cumplimiento AI Act + documentación técnica"
  evaluacion_obligatoria:
    gestion_riesgos:
      - matriz_actualizada: "Riesgos identificados vs realidad"
      - medidas_efectivas: "Controles funcionando correctamente"
      - incidentes_analizados: "Lecciones aprendidas implementadas"
    
    supervision_humana:
      - competencias_funcionarios: "Formación actualizada + efectiva"
      - herramientas_disponibles: "Interface supervisión operativa"
      - casos_override: "Decisiones humanas vs IA analizadas"
    
    transparencia_ciudadana:
      - portal_actualizado: "Información precisa + comprensible"
      - consultas_dpd: "Volumen + tiempo respuesta + resolución"
      - satisfaccion_usuarios: "Encuesta percepción ciudadana"

auditoria_anual_conformidad:
  responsable: "Organismo certificación acreditado"
  alcance: "Conformidad completa AI Act + certificación"
  proceso_certificacion:
    evaluacion_conformidad:
      - documentacion_tecnica: "Completa + actualizada + precisa"
      - sistema_gestion_riesgos: "Implementado + efectivo + auditado"
      - logs_trazabilidad: "Completos + íntegros + auditables"
      - supervision_humana: "Efectiva + documentada + competente"
    
    testing_penetracion:
      - ataques_adversariales: "Robustez algoritmos ante manipulación"
      - inversion_modelos: "Imposibilidad extracción datos entrenamiento"
      - membership_inference: "Verificación anonimización efectiva"
      - fairness_testing: "Ausencia discriminación protegida legalmente"
    
    certificacion_emision:
      - marcado_ce: "Si aplicable según desarrollo normativo"
      - declaracion_conformidad: "Firmada + depositada + pública"
      - validez: "3 años + renovación obligatoria"
      - supervision_continua: "Mantenimiento conformidad"
```

### 6.2 Métricas de Cumplimiento AI Act

#### **📊 KPIs Específicos Municipales:**

```yaml
# INDICADORES CUMPLIMIENTO AI ACT ALFAFAR

metricas_tecnicas:
  precision_algoritmos:
    tax_calculator:
      objetivo: ">99.95%"
      actual: "99.97%" 
      tendencia: "Estable últimos 6 meses"
      alertas: "0 incidentes precisión Q3 2025"
    
    document_processor:
      objetivo: ">95%"
      actual: "95.7%"
      tendencia: "Mejora +2.3% vs 2024"
      alertas: "3 alertas confianza baja julio 2025"
    
    anomaly_detector:
      objetivo: "<5% falsos positivos"
      actual: "4.2%"
      tendencia: "Reducción vs 6.1% inicial"
      alertas: "2 casos revisión julio 2025"

metricas_supervision_humana:
  cobertura_revision:
    revision_obligatoria: "100% casos >threshold"
    revision_recomendada: "87% casos revisados"
    tiempo_medio_revision: "2.3 horas (objetivo <4h)"
    override_decisions: "12 casos julio 2025 (0.8% total)"
  
  competencia_funcionarios:
    formacion_actualizada: "100% funcionarios certificados"
    evaluacion_competencias: "Promedio 8.7/10 evaluación práctica"
    satisfaccion_herramientas: "9.1/10 usabilidad interface"
    escalado_correctivo: "3 casos formación adicional"

metricas_transparencia:
  portal_transparencia:
    visitas_mensuales: "1.247 (julio 2025)"
    tiempo_permanencia: "4.2 minutos promedio"
    consultas_dpd: "23 consultas julio 2025"
    tiempo_respuesta: "12.8 días promedio (objetivo <30)"
  
  satisfaccion_ciudadana:
    comprension_algoritmos: "7.8/10 encuesta municipal"
    confianza_decisiones_ia: "8.2/10"
    conocimiento_derechos: "6.9/10 (mejora necesaria)"
    uso_canales_revision: "5 solicitudes revisión julio"

metricas_cumplimiento_normativo:
  documentacion_ai_act:
    completitud: "100% documentos requeridos"
    actualizacion: "Última actualización: 15 julio 2025"
    validacion_dpd: "Conforme dictamen 20 julio 2025"
    auditoria_externa: "Planificada septiembre 2025"
  
  gestion_incidentes:
    incidentes_reportados: "0 julio 2025"
    tiempo_resolucion: "N/A"
    medidas_correctivas: "Mejoras preventivas implementadas"
    comunicacion_autoridades: "Reporting mensual AEPD al día"
```

---

## 📄 7. DOCUMENTACIÓN TÉCNICA AI ACT

### 7.1 Registro de Sistemas IA Municipal

#### **🗂️ Inventario Obligatorio Completo:**

```yaml
# REGISTRO SISTEMAS IA - AYUNTAMIENTO ALFAFAR
# Actualizado: 1 agosto 2025

sistema_001_tax_calculator:
  identificacion:
    nombre_comercial: "Municipal Tax Calculator Pro"
    version_actual: "v3.1.2"
    proveedor: "[Empresa desarrolladora]"
    responsable_municipal: "Inspector Jefe Tributario"
    fecha_puesta_funcionamiento: "1 enero 2025"
  
  clasificacion_ai_act:
    categoria_riesgo: "Alto Riesgo"
    anexo_aplicable: "Anexo III.6.b"
    justificacion: "Evaluación automática personas acceso servicios públicos"
    impacto_identificado: "Determinación cuantía tributaria → impacto económico"
  
  documentacion_obligatoria:
    sistema_gestion_riesgos: "✅ Implementado y operativo"
    documentacion_tecnica: "✅ Completa según Art. 11"
    logs_automaticos: "✅ Registro todas operaciones"
    supervision_humana: "✅ Procedimientos implementados"
    transparencia_ciudadanos: "✅ Portal público operativo"
  
  estado_conformidad:
    evaluacion_conformidad: "Pendiente - Plazo agosto 2026"
    organismo_evaluacion: "Por designar"
    certificacion_ce: "No requerida hasta desarrollo normativo"
    declaracion_conformidad: "En preparación"

sistema_002_document_processor:
  identificacion:
    nombre_comercial: "AI Document Processor Municipal"
    version_actual: "v2.4.1"
    proveedor: "[Proveedor tecnológico]"
    responsable_municipal: "Técnico Sistemas + DPO"
    fecha_puesta_funcionamiento: "15 febrero 2025"
  
  clasificacion_ai_act:
    categoria_riesgo: "Alto Riesgo"
    anexo_aplicable: "Anexo III.6.b"
    justificacion: "Procesamiento automático documentos decisiones tributarias"
    impacto_identificado: "Extracción errónea → liquidación incorrecta"
  
  documentacion_obligatoria:
    sistema_gestion_riesgos: "✅ Matriz riesgos específica OCR"
    documentacion_tecnica: "✅ Modelos ML documentados"
    logs_automaticos: "✅ Trazabilidad procesamiento"
    supervision_humana: "✅ Revisión documentos críticos"
    transparencia_ciudadanos: "✅ Explicación funcionamiento OCR"

sistema_003_anomaly_detector:
  identificacion:
    nombre_comercial: "Municipal Anomaly Detection System"
    version_actual: "v1.8.3"
    proveedor: "[Proveedor IA especializada]"
    responsable_municipal: "Inspector Senior + DPO"
    fecha_puesta_funcionamiento: "1 abril 2025"
  
  clasificacion_ai_act:
    categoria_riesgo: "Alto Riesgo"
    anexo_aplicable: "Anexo III.6.a"
    justificacion: "Aplicación ley - detección fraude tributario"
    impacto_identificado: "Falso positivo → investigación injustificada"

sistema_004_chatbot_ciudadanos:
  identificacion:
    nombre_comercial: "MunicipalBot Alfafar"
    version_actual: "v1.2.0"
    proveedor: "[Proveedor chatbot]"
    responsable_municipal: "Técnico Atención Ciudadana"
    fecha_puesta_funcionamiento: "1 mayo 2025"
  
  clasificacion_ai_act:
    categoria_riesgo: "Riesgo Limitado"
    articulo_aplicable: "Art. 50"
    justificacion: "Interacción directa personas"
    obligacion_principal: "Transparencia uso IA"
  
  cumplimiento_transparencia:
    banner_visible: "✅ Permanente todas conversaciones"
    limitaciones_explicadas: "✅ No vinculante + escalado humano"
    escalado_disponible: "✅ Botón directo funcionario"
```

### 7.2 Procedimientos de Actualización

#### **🔄 Mantenimiento Documentación AI Act:**

```yaml
# PROCEDIMIENTOS ACTUALIZACIÓN OBLIGATORIA

actualizacion_sistemas_ia:
  cambios_version_menor:
    definicion: "Actualizaciones seguridad, mejoras rendimiento sin cambio algoritmo"
    documentacion_requerida:
      - log_cambios: "Detalle modificaciones técnicas"
      - testing_regresion: "Verificación precisión mantenida"
      - validacion_dpd: "Confirmación no afecta cumplimiento"
    
    plazo_actualizacion: "15 días desde implementación"
    responsable: "Técnico sistemas + notificación DPO"
  
  cambios_version_mayor:
    definicion: "Modificación algoritmo, nuevas funcionalidades, cambio modelo ML"
    documentacion_requerida:
      - evaluacion_impacto: "EIPD específica cambios"
      - sistema_gestion_riesgos: "Actualización matriz riesgos"
      - documentacion_tecnica: "Revisión completa Art. 11"
      - testing_exhaustivo: "Validación precisión + sesgo + robustez"
      - formacion_funcionarios: "Actualización competencias si necesario"
    
    plazo_actualizacion: "30 días desde implementación"
    responsable: "DPO + proveedor + validación auditor externo"
  
  cambios_normativos:
    definicion: "Modificación AI Act, normativa española, ordenanzas municipales"
    documentacion_requerida:
      - analisis_impacto_normativo: "Qué cambia en cumplimiento"
      - gap_analysis: "Diferencias estado actual vs requerido"
      - plan_adaptacion: "Cronograma + recursos + responsables"
      - comunicacion_stakeholders: "Funcionarios + ciudadanos + proveedores"
    
    plazo_adaptacion: "Según normativa (máximo 12 meses típico)"
    responsable: "DPO + asesoría jurídica + coordinación técnica"

mantenimiento_registros:
  logs_sistemas_ia:
    retencion_obligatoria: "6 años (tributario) + 2 años (AI Act)"
    formato_estructurado: "JSON + firma digital + hash integridad"
    backup_geografico: "Replicación tiempo real + backup offline"
    acceso_auditoria: "Disponible autoridades sin previo aviso"
  
  documentacion_tecnica:
    revision_anual: "Verificación vigencia + precisión"
    actualizacion_metricas: "KPIs reales vs documentados"
    validacion_externa: "Auditor independiente certificado"
    archivo_historico: "Versiones anteriores conservadas"
  
  portal_transparencia:
    actualizacion_trimestral: "Información sistemas + métricas + contactos"
    validacion_comprensibilidad: "Test usuarios + feedback"
    multiidioma: "Español + valenciano (si demanda)"
    accesibilidad: "WCAG 2.1 AA cumplimiento"
```

---

## ✅ 8. CONFORMIDAD Y CERTIFICACIÓN

### 8.1 Proceso de Evaluación de Conformidad

#### **🏅 Ruta hacia Certificación AI Act:**

```yaml
# PROCESO CERTIFICACIÓN SISTEMAS IA MUNICIPAL

fase_1_preparacion:
  documentacion_previa:
    - registro_sistemas_completo: "Todos los sistemas IA identificados"
    - documentacion_tecnica_art11: "Cada sistema documentado individual"
    - sistema_gestion_riesgos: "Implementado + operativo + auditado"
    - logs_trazabilidad: "Mínimo 6 meses operación documentada"
    - supervision_humana: "Procedimientos + formación + casos reales"
  
  gap_analysis_inicial:
    evaluador: "Consultoría especializada AI Act"
    alcance: "Comparación estado actual vs requisitos legales"
    entregable: "Informe deficiencias + plan corrección"
    plazo: "30 días análisis + 60 días corrección"

fase_2_evaluacion_conformidad:
  organismo_evaluacion:
    seleccion: "Organismo notificado acreditado España"
    especialización: "Sistemas IA administración pública"
    referencias: "Experiencia previa municipios similares"
  
  proceso_evaluacion:
    evaluacion_documental:
      - documentacion_tecnica: "Revisión completa Art. 11"
      - sistema_gestion_riesgos: "Efectividad + completitud"
      - procedimientos_operativos: "Supervisión + transparencia"
      - cumplimiento_obligaciones: "Art. 9-15 AI Act verificado"
    
    evaluacion_practica:
      - testing_sistemas: "Verificación funcionamiento real"
      - entrevistas_funcionarios: "Competencias + procedimientos"
      - revision_casos_reales: "Decisiones + supervisión + override"
      - validacion_transparencia: "Portal + información + ciudadanos"
    
    testing_tecnico:
      - robustez_algoritmos: "Resistencia ataques adversariales"
      - ausencia_sesgo: "Testing discriminación estadística"
      - trazabilidad_logs: "Completitud + integridad + disponibilidad"
      - supervision_efectiva: "Casos reales intervención humana"

fase_3_certificacion:
  emision_certificado:
    validez: "3 años desde emisión"
    alcance: "Sistemas específicos evaluados"
    condiciones: "Mantenimiento conformidad + auditorías"
    renovacion: "Proceso completo cada 3 años"
  
  declaracion_conformidad:
    responsable_emision: "Ayuntamiento Alfafar (usuario IA)"
    contenido_minimo:
      - identificacion_sistemas: "Cada sistema IA certificado"
      - normas_aplicadas: "AI Act + normas técnicas específicas"
      - organismo_evaluacion: "Identificación + alcance evaluación"
      - fecha_emision: "Validez + condiciones mantenimiento"
    
    deposito_publico: "Registro público accesible ciudadanos"
    actualizacion: "Cada modificación sustancial sistemas"
```

### 8.2 Mantenimiento de la Conformidad

#### **🔄 Supervisión Continua Post-Certificación:**

```yaml
# MANTENIMIENTO CONFORMIDAD AI ACT

supervision_continua:
  automonitorizacion:
    metricas_automaticas:
      - precision_algoritmos: "Dashboard tiempo real"
      - casos_supervision_humana: "Conteo + tiempo respuesta"
      - incidentes_reportados: "Clasificación + resolución"
      - satisfaccion_ciudadanos: "Encuestas + feedback"
    
    alertas_automaticas:
      - degradacion_rendimiento: "Precisión <threshold"
      - volumen_anomalo_overrides: "Supervisión humana >media"
      - consultas_dpd_elevadas: "Posibles problemas transparencia"
      - cambios_normativos: "Monitoring legislación automatizado"
  
  auditoria_interna_continua:
    frecuencia: "Mensual técnica + trimestral integral"
    responsable: "DPO + auditor interno certificado"
    alcance: "Verificación mantenimiento todos requisitos"
    reporting: "Dashboard ejecutivo + informe técnico"
  
  coordinacion_organismo_evaluacion:
    comunicacion_cambios: "Notificación modificaciones sustanciales"
    auditoria_seguimiento: "Anual + extraordinaria si incidentes"
    renovacion_anticipada: "Si cambios significativos sistemas"

gestion_no_conformidades:
  deteccion_gaps:
    fuentes_identificacion:
      - auditoria_interna: "Revisión periódica procedimientos"
      - incidentes_operativos: "Errores sistemas + quejas ciudadanos"
      - cambios_normativos: "Nueva legislación + jurisprudencia"
      - feedback_organismo: "Recomendaciones auditor externo"
  
  plan_correccion:
    clasificacion_urgencia:
      - critica: "Riesgo inmediato ciudadanos → 24h"
      - alta: "Incumplimiento legal → 72h inicio corrección"
      - media: "Mejora procedimientos → 30 días"
      - baja: "Optimizaciones → siguiente ciclo auditoría"
    
    implementacion_medidas:
      - suspension_temporal: "Si riesgo alto continuidad"
      - correccion_inmediata: "Parches + soluciones temporales"
      - solucion_definitiva: "Modificación sistemas + procedimientos"
      - validacion_efectividad: "Testing + verificación + documentación"
  
  comunicacion_stakeholders:
    interno_ayuntamiento:
      - alcaldia: "Incidentes críticos inmediato"
      - funcionarios: "Cambios procedimientos + formación"
      - dpd: "Todos los incidentes + seguimiento"
    
    externo:
      - ciudadanos: "Si afecta servicios + transparencia"
      - organismo_evaluacion: "Según gravedad + requisitos"
      - aepd: "Si incidentes protección datos"
```

---

## ⚠️ 9. INFRACCIONES Y SANCIONES

### 9.1 Marco Sancionador AI Act

#### **💰 Sanciones Aplicables a Ayuntamientos:**

```yaml
# SANCIONES AI ACT - APLICACIÓN MUNICIPAL

infracciones_muy_graves:
  sanciones_nivel_1:
    importe: "Hasta 35M€ o 7% facturación anual mundial"
    aplicacion_municipal: "7% presupuesto anual ayuntamiento"
    conductas_sancionables:
      - uso_sistemas_prohibidos: "IA puntuación social ciudadanos"
      - manipulacion_cognitiva: "Sistemas influencia subliminal"
      - explotacion_vulnerabilidades: "Aprovechamiento discapacidad/edad"
      - identificacion_biometrica: "Reconocimiento facial no autorizado"
  
  caso_ejemplo_grave:
    conducta: "Implementar sistema scoring ciudadanos para acceso servicios"
    sancion_teorica: "7% presupuesto Alfafar = ~700.000€"
    medidas_preventivas:
      - prohibicion_absoluta: "Sistemas evaluación comportamiento global"
      - validacion_dpd: "Revisión previa cualquier algoritmo"
      - formacion_funcionarios: "Identificación sistemas prohibidos"

infracciones_graves:
  sanciones_nivel_2:
    importe: "Hasta 15M€ o 3% facturación anual mundial"
    aplicacion_municipal: "3% presupuesto anual ayuntamiento"
    conductas_sancionables:
      - incumplimiento_obligaciones: "Art. 9-15 sistemas alto riesgo"
      - documentacion_inexacta: "Información falsa/incompleta"
      - falta_supervision_humana: "Decisiones automáticas sin control"
      - transparencia_deficiente: "Información inadecuada ciudadanos"
  
  casos_riesgo_alfafar:
    tax_calculator_sin_supervision:
      conducta: "Liquidaciones automáticas sin revisión humana >500€"
      sancion_potencial: "3% presupuesto = ~300.000€"
      prevencion: "Umbrales supervisión + formación + procedimientos"
    
    documentacion_desactualizada:
      conducta: "Documentación técnica Art. 11 obsoleta >12 meses"
      sancion_potencial: "Hasta 300.000€"
      prevencion: "Calendario actualización + responsables + validación"
    
    portal_transparencia_deficiente:
      conducta: "Información ciudadanos incomprensible/incompleta"
      sancion_potencial: "Hasta 300.000€"
      prevencion: "Testing usabilidad + feedback + mejora continua"

infracciones_menos_graves:
  sanciones_nivel_3:
    importe: "Hasta 7,5M€ o 1,5% facturación anual mundial"
    aplicacion_municipal: "1,5% presupuesto anual"
    conductas_sancionables:
      - incumplimiento_requerimientos: "Información faltante autoridades"
      - cooperacion_deficiente: "No colaboración auditorías"
      - marcado_ce_incorrecto: "Cuando sea obligatorio"
  
  riesgos_operativos_alfafar:
    reporting_deficiente:
      conducta: "No proporcionar información requerida AEPD"
      sancion_potencial: "1,5% presupuesto = ~150.000€"
      prevencion: "Protocolo comunicación + responsable + plazos"
```

### 9.2 Estrategia Prevención Sanciones

#### **🛡️ Plan de Cumplimiento Preventivo:**

```yaml
# ESTRATEGIA ANTI-SANCIONES ALFAFAR

nivel_1_prevencion_primaria:
  formacion_intensiva:
    funcionarios_decision:
      contenido: "Identificación conductas sancionables + procedimientos"
      frecuencia: "Anual + actualización cambios normativos"
      evaluacion: "Certificación competencias + renovación"
    
    responsables_tecnicos:
      contenido: "AI Act técnico + implementación + documentación"
      especializacion: "40h formación + certificación externa"
      actualizacion: "Semestral + normativa + jurisprudencia"
  
  sistemas_alertas_preventivas:
    monitoring_automatico:
      - umbrales_supervision: "Alerta automática si >X decisiones sin revisión"
      - actualizacion_documentacion: "Recordatorio vencimientos + responsables"
      - metricas_calidad: "Alert if precisión/satisfacción <threshold"
      - cambios_normativos: "Notificación automática nueva legislación"
    
    dashboard_cumplimiento:
      indicadores_criticos:
        - "% supervisión humana casos requeridos"
        - "Días desde última actualización documentación"
        - "Satisfacción ciudadana transparencia"
        - "Incidentes pendientes resolución"
      
      alertas_escalado:
        - verde: "Cumplimiento óptimo"
        - amarillo: "Atención requerida - acción preventiva"
        - rojo: "Riesgo sanción - acción inmediata"

nivel_2_deteccion_temprana:
  auditoria_preventiva:
    autoevaluacion_mensual:
      checklist_cumplimiento: "Verificación todos requisitos AI Act"
      gaps_identificados: "Deficiencias + plan corrección"
      seguimiento_mejoras: "Progreso medidas correctivas"
    
    simulacros_inspeccion:
      frecuencia: "Semestral"
      metodologia: "Auditor externo simula inspección real"
      objetivo: "Identificar debilidades antes inspección oficial"
      correccion: "Plan mejora basado resultados"
  
  coordinacion_otros_municipios:
    red_colaboracion:
      - intercambio_experiencias: "Buenas prácticas + lecciones aprendidas"
      - alertas_conjuntas: "Sharing información inspecciones/sanciones"
      - formacion_colaborativa: "Recursos compartidos + especialistas"
      - lobbying_constructivo: "Posiciones conjuntas desarrollo normativo"

nivel_3_respuesta_incidentes:
  protocolo_crisis_sancionadora:
    deteccion_riesgo_sancion:
      fuentes_alerta:
        - "Requerimiento información autoridad competente"
        - "Inspección iniciada organismo supervisor"
        - "Queja ciudadano escalada autoridad"
        - "Incidente grave sistemas IA"
      
      activacion_inmediata:
        - "Equipo crisis: DPO + Secretario + Asesoría jurídica"
        - "Evaluación riesgo + estrategia respuesta"
        - "Implementación medidas correctivas urgentes"
        - "Comunicación coordinada stakeholders"
    
    estrategia_defensa:
      documentacion_evidencias:
        - "Recopilación pruebas cumplimiento"
        - "Chronología decisiones + justificaciones"
        - "Testimonios funcionarios + ciudadanos"
        - "Evidencias buena fe + effort cumplimiento"
      
      alegaciones_tecnicas:
        - "Argumentación jurídica especializada"
        - "Evidencias técnicas funcionamiento correcto"
        - "Demostración supervisión humana efectiva"
        - "Impacto proporcionalidad sanción vs municipio"
```

---

## 📈 CONCLUSIONES Y PRÓXIMOS PASOS

### ✅ Síntesis de Cumplimiento AI Act

**🎯 Estado Actual Alfafar (1 agosto 2025):**

1. **✅ Sistemas Clasificados**: Todos los algoritmos municipales categorizados correctamente
2. **✅ Documentación Iniciada**: Templates y procedimientos base implementados  
3. **⏳ Plazo Cumplimiento**: 12 meses hasta aplicación completa (agosto 2026)
4. **🔄 Preparación Activa**: Proceso estructurado de conformidad en marcha

### 🎯 Roadmap Implementación

#### **📅 Cronograma hasta Agosto 2026:**

```yaml
# CRONOGRAMA CUMPLIMIENTO AI ACT

agosto_2025_noviembre_2025:
  documentacion_completa:
    - finalizacion_documentacion_tecnica: "Art. 11 todos sistemas"
    - implementacion_supervision_humana: "Procedimientos operativos"
    - portal_transparencia_completo: "Información ciudadanos"
    - formacion_funcionarios_basica: "Competencias supervisión"

diciembre_2025_marzo_2026:
  operacion_conforme:
    - logs_automaticos_completos: "Trazabilidad Art. 12"
    - auditoria_interna_periodica: "Sistema gestión riesgos"
    - testing_sesgo_discriminacion: "Fairness algoritmos"
    - feedback_ciudadanos_implementado: "Mejora continua"

abril_2026_julio_2026:
  certificacion_preparacion:
    - gap_analysis_profesional: "Evaluación conformidad previa"
    - correccion_deficiencias: "Implementación mejoras"
    - seleccion_organismo_evaluacion: "Proceso certificación"
    - documentacion_final: "Expediente completo conformidad"

agosto_2026:
  cumplimiento_obligatorio:
    - certificacion_emitida: "Conformidad AI Act verificada"
    - declaracion_conformidad: "Documento público depositado"
    - sistema_operativo_conforme: "Pleno cumplimiento normativo"
    - supervision_continua_activa: "Mantenimiento conformidad"
```

### 📋 Entregables del Documento

- [x] **Clasificación completa sistemas IA municipales** según categorías AI Act
- [x] **Obligaciones específicas** para cada tipo de sistema (alto riesgo, limitado, mínimo)
- [x] **Procedimientos supervisión humana** multinivel por competencias funcionarios
- [x] **Portal transparencia ciudadana** con contenidos obligatorios Art. 13
- [x] **Sistema gestión riesgos** específico cada algoritmo municipal
- [x] **Plan auditoría** interna y externa conforme AI Act
- [x] **Documentación técnica** templates Art. 11 por sistema
- [x] **Proceso certificación** y mantenimiento conformidad
- [x] **Estrategia prevención sanciones** y gestión incidentes
- [x] **Cronograma implementación** hasta agosto 2026

---

**📅 Próxima Revisión:** Trimestral o cambio normativo AI Act  
**📧 Responsable Actualización:** DPO Municipal + Inspector Jefe Tributario  
**⚖️ Validación Legal:** Asesoría jurídica especializada AI Act obligatoria  
**🔄 Versión Siguiente:** Incorporar desarrollo reglamentario español

---

*Este documento forma parte integral del Sistema Municipal IA Alfafar y debe leerse junto con los documentos 01-07 de la serie legal-compliance para comprensión completa del marco normativo aplicable.*