# Procedimientos Operativos Sistema Municipal IA
## Ayuntamiento de Alfafar - Operativa Diaria y Gestión Integral

---

## 📋 OBJETIVO DEL DOCUMENTO

Este documento establece los **procedimientos operativos detallados** para la gestión diaria del Sistema Municipal de IA del Ayuntamiento de Alfafar, integrando objetivos específicos, tareas automatizadas, flujos de trabajo y protocolos de intervención humana conforme al marco normativo establecido.

---

## 🎯 OBJETIVOS OPERATIVOS ESPECÍFICOS

### **🏛️ OBJETIVOS ESTRATÉGICOS DEL SISTEMA**

#### **📊 Transformación digital municipal:**
```markdown
OBJETIVO PRINCIPAL:
Automatizar integralmente el procesamiento de documentos notariales 
y cálculo de tributos municipales, eliminando trabajo manual repetitivo 
y mejorando significativamente la calidad del servicio público.

ALCANCE:
✅ TODO el régimen tributario municipal (no solo IIVTNU)
✅ Escalabilidad a otros departamentos municipales
✅ Cumplimiento normativo desde implementación inicial
✅ Adaptación al nivel técnico funcionarios existentes

PRINCIPIOS OPERATIVOS:
- Supervisión humana: Obligatoria en decisiones relevantes
- Transparencia: Explicabilidad completa procesos automatizados
- Reversibilidad: Capacidad modificar/anular decisiones IA
- Mejora continua: Optimización basada feedback operativo
```

#### **🎯 Objetivos específicos por módulo:**

```yaml
# document_processor (OCR + extracción)
document_processor_goals:
  precision_target: ">99% exactitud caracteres OCR"
  coverage_target: "100% documentos notariales estándar"
  processing_time: "<30 segundos por documento"
  data_extraction: ">95% campos obligatorios identificados"
  error_handling: "Escalado automático casos complejos"
  
# tax_calculator (cálculos tributarios)
tax_calculator_goals:
  mathematical_accuracy: "100% precisión cálculos"
  regulatory_compliance: "Actualización normativa <24h"
  all_taxes_coverage: "IBI, IAE, IIVTNU, ICIO, IVTM, tasas"
  validation_speed: "<5 segundos por liquidación"
  audit_trail: "Trazabilidad completa decisiones"

# integration_layer (APIs GTT/Gestiona)
integration_goals:
  system_availability: ">99.5% uptime servicios"
  data_synchronization: "Tiempo real GTT/Gestiona"
  error_recovery: "Recuperación automática fallos temporales"
  compatibility: "Versiones actuales sistemas municipales"
  monitoring: "Alertas proactivas anomalías"

# web_interface (portal funcionarios/ciudadanos)
interface_goals:
  user_experience: ">8/10 satisfacción funcionarios"
  accessibility: "WCAG 2.1 AA cumplimiento"
  response_time: "<2 segundos carga páginas"
  mobile_friendly: "Adaptación dispositivos móviles"
  citizen_self_service: ">80% consultas resueltas autoservicio"
```

---

## 📋 PROCEDIMIENTOS OPERATIVOS DETALLADOS

### **📄 PROCESAMIENTO DOCUMENTOS NOTARIALES**

#### **🔄 Flujo operativo estándar:**

```yaml
# Procedimiento completo: Documento → Liquidación
standard_workflow:
  step_1_reception:
    trigger: "Documento recibido (registro, email, presencial)"
    automated_actions:
      - "Clasificación automática tipo documento"
      - "Asignación número expediente único"
      - "Notificación funcionario responsable"
      - "Backup documento original cifrado"
    human_validation:
      - "Verificación completitud documento"
      - "Confirmación ciudadano identificado correctamente"
    time_target: "<5 minutos recepción → inicio procesamiento"

  step_2_ocr_extraction:
    trigger: "Documento validado para procesamiento"
    automated_actions:
      - "OCR Tesseract + ML post-procesado"
      - "Extracción entidades NER personalizado"
      - "Estructuración datos formato MCP"
      - "Validación coherencia lógica extraída"
    quality_checks:
      - "Confianza OCR >95% → procesamiento automático"
      - "Confianza 85-95% → revisión funcionario"
      - "Confianza <85% → escalado manual obligatorio"
    time_target: "<30 segundos por documento estándar"

  step_3_data_validation:
    trigger: "Datos extraídos disponibles"
    automated_actions:
      - "Verificación cruzada bases catastrales"
      - "Validación formato DNI/NIE/CIF"
      - "Comprobación coherencia fechas/importes"
      - "Detección anomalías valores declarados"
    human_oversight:
      - "Revisión obligatoria si anomalías detectadas"
      - "Validación manual casos edge identificados"
      - "Aprobación funcionario antes cálculo"
    time_target: "<10 minutos validación completa"

  step_4_tax_calculation:
    trigger: "Datos validados y aprobados"
    automated_actions:
      - "Cálculo automático tributos aplicables"
      - "Aplicación exenciones/bonificaciones"
      - "Generación propuesta liquidación"
      - "Cálculo intereses/recargos si procede"
    compliance_checks:
      - "Verificación normativa vigente aplicada"
      - "Validación rangos valores legales"
      - "Confirmación plazos tributarios"
    time_target: "<5 segundos cálculo + validación"

  step_5_human_review:
    trigger: "Propuesta liquidación generada"
    mandatory_review_cases:
      - "Importes liquidación >1000€"
      - "Sanciones o recargos aplicados"
      - "Exenciones automáticas detectadas"
      - "Ciudadano solicita revisión humana"
    optional_review:
      - "Casos estándar <300€"
      - "Procedimientos rutinarios IBI/IAE"
    functionalities:
      - "Override completo decisiones IA"
      - "Justificación obligatoria modificaciones"
      - "Trazabilidad decisiones funcionario"
    time_target: "<24 horas casos obligatorios"

  step_6_integration_systems:
    trigger: "Liquidación aprobada (automática o manual)"
    automated_actions:
      - "Actualización GTT con liquidación"
      - "Registro expediente en Gestiona"
      - "Generación documentación oficial"
      - "Programación notificaciones ciudadano"
    error_handling:
      - "Retry automático fallos temporales"
      - "Escalado técnico fallos persistentes"
      - "Rollback seguro si errores críticos"
    time_target: "<5 minutos integración completa"
```

#### **⚡ Procedimientos urgentes/prioritarios:**

```yaml
# Casos especiales tramitación acelerada
priority_procedures:
  herencias_judiciales:
    priority_level: "ALTA"
    max_processing_time: "4 horas laborables"
    mandatory_human_review: true
    special_validations:
      - "Verificación orden judicial"
      - "Validación herederos legitimados"
      - "Cálculo proporcional cuotas"
    notification: "Automática partes interesadas"

  embargos_tributarios:
    priority_level: "CRÍTICA"
    max_processing_time: "1 hora"
    automated_blocks: "Suspensión procedimientos automáticos"
    human_escalation: "Inmediata a inspector jefe"
    legal_validation: "Obligatoria antes ejecución"

  recursos_ciudadanos:
    priority_level: "ALTA"
    max_response_time: "10 días hábiles"
    procedure:
      - "Revisión humana obligatoria completa"
      - "Análisis motivos recurso"
      - "Re-cálculo manual independiente"
      - "Justificación detallada resolución"
    documentation: "Completa + auditable"
```

---

## 👤 PROTOCOLOS INTERVENCIÓN HUMANA

### **🔍 Supervisión obligatoria decisiones relevantes:**

#### **💰 Criterios activación supervisión:**

```yaml
# Umbrales automáticos supervisión humana
supervision_triggers:
  economic_thresholds:
    liquidaciones_altas: ">1000€ cualquier tributo"
    sanciones: ">300€ (AI Act compliance)"
    rectificaciones: "Cualquier importe modificación"
    devoluciones: ">500€ propuesta devolución"
    
  legal_complexity:
    multiple_herederos: "Más de 2 herederos"
    actividades_mixtas: "IAE múltiples epígrafes"
    propiedades_especiales: "Protección patrimonial"
    situaciones_juridicas: "Divorcios, separaciones"
    
  anomaly_detection:
    valores_atipicos: "Desviación >50% valor catastral"
    patron_inusual: "Transacciones repetitivas mismo ciudadano"
    errores_frecuentes: "Más de 3 errores mismo documento"
    
  citizen_requests:
    explicacion_solicitada: "Ciudadano solicita explicación"
    recurso_presentado: "Cualquier tipo recurso"
    queja_formal: "Registro quejas ciudadano"
```

#### **⚙️ Interface funcionario supervision:**

```yaml
# Dashboard supervisión funcionarios
supervision_interface:
  alerts_dashboard:
    pending_reviews: "Lista casos requieren revisión"
    priority_queue: "Ordenación por urgencia/importe"
    automated_suggestions: "Recomendaciones IA + justificación"
    historical_context: "Casos similares + decisiones anteriores"
    
  review_tools:
    side_by_side_comparison: "Documento original vs datos extraídos"
    calculation_breakdown: "Desglose paso a paso cálculos"
    regulatory_references: "Normativa aplicada automáticamente"
    override_options: "Modificación valores + justificación"
    
  approval_workflow:
    single_click_approval: "Casos estándar conformes"
    modification_tools: "Edición valores + justificación"
    rejection_process: "Devolución ciudadano + motivos"
    escalation_options: "Derivación supervisor/DPO"
    
  audit_trail:
    decision_logging: "Registro completo decisiones tomadas"
    time_tracking: "Tiempo dedicado por caso"
    performance_metrics: "Estadísticas funcionario + departamento"
```

### **🚨 Protocolos escalado y emergencia:**

#### **📞 Procedimientos escalado técnico:**

```yaml
# Niveles escalado técnico
technical_escalation:
  level_1_funcionario:
    scope: "Decisiones tributarias estándar"
    authority: "Aprobación/modificación liquidaciones <1000€"
    escalation_triggers:
      - "Casos fuera competencia"
      - "Dudas normativa aplicable"
      - "Errores técnicos sistema"
    response_time: "Inmediato"
    
  level_2_inspector_jefe:
    scope: "Decisiones complejas + supervisión"
    authority: "Aprobación liquidaciones >1000€, sanciones"
    escalation_triggers:
      - "Recursos ciudadanos"
      - "Casos jurídicamente complejos"
      - "Conflictos inter-departamentales"
    response_time: "<4 horas laborables"
    
  level_3_secretario_municipal:
    scope: "Decisiones normativas + compliance"
    authority: "Interpretación normativa, procedimientos"
    escalation_triggers:
      - "Dudas legalidad procedimiento"
      - "Conflictos competencias"
      - "Casos precedente"
    response_time: "<24 horas"
    
  level_4_dpo_legal:
    scope: "Compliance RGPD + AI Act"
    authority: "Protección datos, transparencia algoritmos"
    escalation_triggers:
      - "Derechos ciudadanos ejercicio"
      - "Incidentes protección datos"
      - "Auditorías externas"
    response_time: "<48 horas"
```

#### **🔧 Procedimientos emergencia técnica:**

```yaml
# Protocolos emergencia operativa
emergency_procedures:
  system_downtime:
    immediate_actions:
      - "Activación modo manual tramitación"
      - "Notificación ciudadanos afectados"
      - "Escalado equipo técnico externo"
      - "Registro incidencia completo"
    continuity_plan:
      - "Formularios papel backup"
      - "Cálculos manuales temporales"
      - "Registro manual expedientes"
      - "Sincronización posterior sistemas"
    recovery_process:
      - "Testing funcionalidades críticas"
      - "Migración datos temporales"
      - "Validación integridad información"
      - "Comunicación restablecimiento servicio"
      
  data_breach_suspected:
    immediate_response:
      - "Aislamiento sistemas afectados"
      - "Notificación DPO <1 hora"
      - "Preservación evidencias"
      - "Contacto CCN-CERT si necesario"
    investigation:
      - "Análisis logs auditoría"
      - "Determinación alcance brecha"
      - "Evaluación riesgo ciudadanos"
      - "Documentación completa incidente"
    notification_process:
      - "AEPD <72 horas si alto riesgo"
      - "Ciudadanos afectados <comunicación inmediata>"
      - "Autoridades competentes según caso"
      - "Medidas correctivas implementadas"
```

---

## 🔄 GESTIÓN OPERATIVA DIARIA

### **📊 Monitorización y métricas tiempo real:**

#### **🎯 KPIs operativos diarios:**

```yaml
# Métricas seguimiento diario
daily_metrics:
  processing_performance:
    documents_processed: "Número documentos procesados"
    processing_time_avg: "Tiempo medio por documento"
    ocr_accuracy: "Precisión OCR promedio"
    human_intervention_rate: "% casos requieren revisión humana"
    
  quality_indicators:
    calculation_accuracy: "% cálculos precisos primer intento"
    citizen_complaints: "Número quejas/errores reportados"
    system_availability: "% uptime sistemas críticos"
    data_integrity_checks: "Verificaciones integridad pasadas"
    
  compliance_metrics:
    rgpd_requests: "Solicitudes derechos ciudadanos"
    response_times: "Tiempo respuesta por tipo solicitud"
    audit_trail_completeness: "% trazabilidad completa"
    human_oversight_compliance: "% decisiones supervisadas correctamente"
    
  citizen_satisfaction:
    processing_speed: "Tiempo tramitación percibido"
    transparency_rating: "Valoración explicaciones proporcionadas"
    self_service_usage: "% consultas resueltas portal"
    complaint_resolution: "Tiempo medio resolución incidencias"
```

#### **📈 Dashboard control operacional:**

```yaml
# Interface control tiempo real
operational_dashboard:
  real_time_status:
    active_documents: "Documentos en procesamiento"
    queue_length: "Cola espera por tipo documento"
    system_health: "Estado servicios críticos"
    alerts_active: "Alertas activas requieren atención"
    
  performance_trends:
    hourly_throughput: "Documentos procesados por hora"
    daily_comparisons: "Comparativa días anteriores"
    weekly_patterns: "Patrones trabajo semanal"
    seasonal_adjustments: "Ajustes épocas declaraciones"
    
  resource_utilization:
    cpu_memory_usage: "Utilización recursos sistema"
    storage_capacity: "Capacidad almacenamiento"
    network_bandwidth: "Uso ancho banda"
    human_resources: "Carga trabajo funcionarios"
    
  predictive_analytics:
    workload_forecast: "Previsión carga próximos días"
    capacity_planning: "Planificación recursos necesarios"
    maintenance_windows: "Ventanas mantenimiento óptimas"
    scaling_recommendations: "Recomendaciones escalado"
```

### **🛠️ Mantenimiento y optimización continua:**

#### **🔧 Rutinas mantenimiento automático:**

```yaml
# Tareas mantenimiento automatizadas
automated_maintenance:
  daily_tasks:
    - "Backup incrementales cifrados"
    - "Limpieza logs antiguos"
    - "Verificación integridad base datos"
    - "Actualización definiciones antivirus"
    - "Sincronización relojes sistema"
    
  weekly_tasks:
    - "Backup completo sistema"
    - "Análisis rendimiento servicios"
    - "Actualización certificados SSL"
    - "Revisión logs seguridad"
    - "Optimización índices base datos"
    
  monthly_tasks:
    - "Auditoría accesos usuarios"
    - "Revisión políticas retención"
    - "Actualización documentación sistema"
    - "Testing planes recuperación"
    - "Evaluación métricas cumplimiento"
    
  quarterly_tasks:
    - "Auditoría seguridad completa"
    - "Revisión arquitectura sistema"
    - "Actualización análisis riesgos"
    - "Evaluación satisfacción usuarios"
    - "Planificación mejoras sistema"
```

#### **📊 Optimización basada en datos:**

```yaml
# Mejora continua basada métricas
continuous_improvement:
  performance_optimization:
    bottleneck_identification: "Análisis cuellos botella"
    algorithm_tuning: "Ajuste parámetros IA"
    infrastructure_scaling: "Escalado recursos según demanda"
    workflow_streamlining: "Optimización procesos manuales"
    
  user_experience_enhancement:
    interface_improvements: "Mejoras UX basadas feedback"
    process_simplification: "Simplificación procedimientos"
    training_needs_analysis: "Identificación necesidades formación"
    documentation_updates: "Actualización guías usuario"
    
  compliance_strengthening:
    regulatory_updates: "Incorporación cambios normativos"
    audit_recommendations: "Implementación recomendaciones auditoría"
    security_hardening: "Refuerzo medidas seguridad"
    transparency_enhancements: "Mejora transparencia procesos"
```

---

## 📋 PROCEDIMIENTOS ESPECÍFICOS POR TRIBUTO

### **🏠 IBI (Impuesto Bienes Inmuebles):**

```yaml
# Procedimientos específicos IBI
ibi_procedures:
  annual_review:
    trigger: "Revisión anual valores catastrales"
    automated_checks:
      - "Comparación valores catastro vs declarados"
      - "Detección modificaciones inmuebles"
      - "Actualización coeficientes municipales"
      - "Aplicación bonificaciones/exenciones"
    human_validation:
      - "Verificación cambios uso inmueble"
      - "Confirmación situaciones especiales"
      - "Aprobación ajustes significativos"
    output: "Propuesta liquidaciones anuales"
    
  modificaciones_durante_ejercicio:
    triggers:
      - "Escritura compraventa recibida"
      - "Licencia obra mayor concedida"
      - "Cambio uso inmueble detectado"
    process:
      - "Cálculo prorrateado temporal"
      - "Aplicación normativa proporcionalidad"
      - "Generación liquidaciones complementarias"
      - "Notificación automática partes"
```

### **🏢 IAE (Impuesto Actividades Económicas):**

```yaml
# Procedimientos específicos IAE
iae_procedures:
  alta_actividad:
    trigger: "Declaración inicio actividad"
    automated_process:
      - "Clasificación automática epígrafe CNAE"
      - "Verificación licencias municipales"
      - "Cálculo cuota según tarifas"
      - "Aplicación reducciones nuevas empresas"
    validation_required:
      - "Actividades múltiples misma empresa"
      - "Epígrafes no clasificados automáticamente"
      - "Solicitudes exención/bonificación"
    integration: "Alta automática censos municipales"
    
  modificacion_actividad:
    triggers:
      - "Cambio epígrafe actividad"
      - "Modificación superficie local"
      - "Variación número empleados"
    process:
      - "Re-cálculo cuota proporcional"
      - "Aplicación normativa cambios"
      - "Generación liquidación diferencia"
      - "Actualización registros municipales"
```

### **💰 IIVTNU (Plusvalía Municipal):**

```yaml
# Procedimientos específicos IIVTNU (especialidad José)
iivtnu_procedures:
  escritura_compraventa:
    reception: "Documento notarial recibido"
    data_extraction:
      - "Identificación transmitente/adquirente"
      - "Descripción inmueble + referencia catastral"
      - "Valor transmisión declarado"
      - "Fecha otorgamiento + transmisión"
    automated_calculation:
      - "Consulta valor catastral actual + histórico"
      - "Aplicación coeficientes actualización"
      - "Cálculo incremento valor"
      - "Aplicación tipo gravamen municipal"
    special_cases:
      - "Herencias: exención automática"
      - "Donaciones familiares: bonificaciones"
      - "Transmisiones onerosas: gravamen completo"
    human_review_required:
      - "Valores declarados anómalos"
      - "Situaciones jurídicas complejas"
      - "Solicitudes exención"
      
  liquidacion_final:
    automated_generation:
      - "Documento liquidación oficial"
      - "Cálculo intereses demora si aplica"
      - "Generación código pago telemático"
      - "Programación notificación ciudadano"
    integration_systems:
      - "Registro GTT liquidación generada"
      - "Actualización Gestiona estado expediente"
      - "Notificación telemática Correos"
```

### **🏗️ ICIO (Impuesto Construcciones):**

```yaml
# Procedimientos específicos ICIO
icio_procedures:
  licencia_obra:
    trigger: "Solicitud licencia obras"
    automated_assessment:
      - "Cálculo presupuesto obra declarado"
      - "Verificación categoría construcción"
      - "Aplicación tipo gravamen municipal"
      - "Estimación coste real construcción"
    validation_checks:
      - "Coherencia presupuesto vs superficie"
      - "Comparación precios mercado local"
      - "Verificación documentación técnica"
    human_oversight:
      - "Obras especiales/singulares"
      - "Discrepancias presupuesto significativas"
      - "Solicitudes bonificación"
```

### **🚗 IVTM (Impuesto Vehículos):**

```yaml
# Procedimientos específicos IVTM
ivtm_procedures:
  padron_anual:
    data_source: "Registro DGT + padron municipal"
    automated_process:
      - "Consulta vehículos empadronados"
      - "Actualización altas/bajas año"
      - "Cálculo cuotas según potencia fiscal"
      - "Aplicación exenciones automáticas"
    special_situations:
      - "Vehículos históricos: exención"
      - "Discapacidad: bonificación 50%"
      - "Baja temporal: prorrateado"
    integration: "Sincronización DGT mensual"
```

---

## 🎯 ROLES Y RESPONSABILIDADES OPERATIVAS

### **👤 Asignación responsabilidades por perfil:**

#### **🔧 José - Inspector Tributario IIVTNU:**

```yaml
# Responsabilidades operativas José
jose_responsibilities:
  daily_operations:
    primary_focus: "IIVTNU - supervisión decisiones IA"
    document_types:
      - "Escrituras compraventa: revisión casos >1000€"
      - "Herencias: validación exenciones aplicadas"
      - "Donaciones: verificación bonificaciones"
    system_interaction:
      - "Dashboard diario casos pendientes revisión"
      - "Aprobación/modificación liquidaciones automáticas"
      - "Escalado casos complejos inspector jefe"
    quality_assurance:
      - "Verificación precisión cálculos IA"
      - "Feedback sistema casos edge"
      - "Propuestas mejora workflow"
      
  training_role:
    system_champion: "Evangelizador interno IA departamento"
    knowledge_transfer: "Formación compañeros uso herramientas"
    feedback_collection: "Recopilación sugerencias mejora"
    documentation: "Actualización procedimientos operativos"
    
  compliance_support:
    rgpd_compliance: "Verificación tratamiento datos conforme"
    audit_support: "Soporte auditorías internas/externas"
    citizen_requests: "Respuesta solicitudes transparencia"
```

#### **👔 Otros roles departamentales:**

```yaml
# Roles operativos adicionales
departmental_roles:
  inspector_jefe:
    responsibilities:
      - "Supervisión casos >1000€ todos tributos"
      - "Resolución recursos ciudadanos"
      - "Coordinación con otros departamentos"
      - "Aprobación cambios procedimientos"
    system_access: "Full admin + override decisions"
    
  auxiliar_administrativo_general:
    responsibilities:
      - "Atención ciudadana consultas básicas"
      - "Gestión expedientes rutinarios"
      - "Soporte entrada documentos sistema"
      - "Seguimiento plazos procedimientos"
    system_access: "Consulta + entrada datos"
    
  tesorero_municipal:
    responsibilities:
      - "Supervisión recaudación automatizada"
      - "Gestión cobros aplazados/fraccionados"
      - "Coordinación ejecutiva embargos"
      - "Reporting financiero alcaldía"
    system_access: "Reports financieros + gestión cobros"
```

---

## 📞 DIRECTORIO CONTACTOS OPERATIVOS

### **🚨 Contactos emergencia operativa:**

```markdown
SOPORTE TÉCNICO INMEDIATO:
📧 Consultor principal: [definir-contacto@proyecto.es]
📱 Teléfono urgencia: [definir-número-24h]
📧 DPO municipal: [dpo@alfafar.es]

ESCALADO TÉCNICO:
👤 Responsable sistemas: [cto@alfafar.es]
👤 Proveedor cloud: [soporte-enterprise@proveedor.com]
👤 Consultor seguridad: [security@consultor.es]

ESCALADO ADMINISTRATIVO:
👤 Inspector Jefe: [inspector.jefe@alfafar.es]
👤 Secretario Municipal: [secretario@alfafar.es]
👤 Tesorero: [tesorero@alfafar.es]
👤 Alcalde: [alcalde@alfafar.es]

SOPORTE EXTERNO:
☎️ CCN-CERT: +34 91 709 42 00
☎️ INCIBE: 017
📧 AEPD consultas: consultas@aepd.es
```

---

**✅ RESULTADO**: El Ayuntamiento de Alfafar dispondrá de procedimientos operativos detallados y específicos que garantizan el funcionamiento eficiente del Sistema Municipal de IA, con protocolos claros de intervención humana, escalado y gestión de todas las figuras tributarias, asegurando cumplimiento normativo y calidad del servicio público.

---

*Documento: 09_Procedimientos_Operativos.md*  
*Proyecto: Sistema Municipal IA - Ayuntamiento Alfafar*  
*Fecha: 1 agosto 2025*  
*Versión: 1.0 - Procedimientos operativos integrales*