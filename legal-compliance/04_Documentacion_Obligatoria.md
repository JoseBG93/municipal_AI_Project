# Documentación Obligatoria Sistema Municipal IA
## Ayuntamiento de Alfafar - Cumplimiento Normativo Integral

---

## 📋 OBJETIVO DEL DOCUMENTO

Este documento establece **exhaustivamente** toda la documentación que el Ayuntamiento de Alfafar tiene la **obligación legal** de crear, mantener actualizada y conservar para el Sistema Municipal de IA, garantizando cumplimiento integral con RGPD, AI Act, LOPDGDD, ENS y normativa sectorial aplicable.

**Fecha de referencia**: 31 julio 2025  
**Marco temporal**: Normativa vigente y entrada en vigor progresiva AI Act hasta agosto 2026

---

## 📚 DOCUMENTACIÓN RGPD OBLIGATORIA

### **1. REGISTRO DE ACTIVIDADES DE TRATAMIENTO (RGPD Art. 30)**

#### **🏛️ Obligatorio para el Ayuntamiento de Alfafar como responsable:**

```yaml
# Tratamiento por cada figura tributaria:

IIVTNU_processing:
  finalidad: "Gestión, liquidación e inspección Incremento Valor Terrenos Urbanos"
  base_legal: "RGPD Art. 6.1.c (obligación legal) + Art. 6.1.e (interés público)"
  normativa_especifica: "LRHL Art. 104-110, Ordenanza IIVTNU Alfafar 2025"
  categorias_datos:
    - identificativos: "DNI, nombre, apellidos, domicilio fiscal"
    - patrimoniales: "Valores transmisión, referencias catastrales, superficies"
    - documentales: "Escrituras notariales, declaraciones, contratos"
  cesiones_terceros: 
    - catastro: "Verificación valores catastrales (base legal: LRHL)"
    - registro_propiedad: "Consulta titularidades (base legal: LH)"
    - notarios: "Comunicaciones liquidaciones (base legal: LN)"
  transferencias_internacionales: "Ninguna"
  plazos_supresion: "4 años desde prescripción tributaria (LRHL Art. 66)"
  medidas_seguridad: "Nivel alto ENS, cifrado AES-256, acceso restringido"

IBI_processing:
  finalidad: "Gestión, liquidación e inspección Impuesto Bienes Inmuebles"
  base_legal: "RGPD Art. 6.1.c (obligación legal)"
  normativa_especifica: "LRHL Art. 60-77, Ordenanza IBI Alfafar 2025"
  categorias_datos:
    - identificativos: "DNI, razón social, domicilio titular"
    - patrimoniales: "Ref. catastral, valor catastral, superficie, uso"
    - tributarios: "Cuotas, bonificaciones, exenciones aplicadas"
  cesiones_terceros:
    - catastro: "Actualización valores (base legal: Ley Catastro)"
    - registro_propiedad: "Transmisiones inmobiliarias (base legal: LH)"
  plazos_supresion: "4 años desde prescripción"
  medidas_seguridad: "Nivel alto ENS, segregación accesos por roles"

IAE_processing:
  finalidad: "Gestión, liquidación e inspección Impuesto Actividades Económicas"
  base_legal: "RGPD Art. 6.1.c (obligación legal)"
  normativa_especifica: "LRHL Art. 78-91, Ordenanza IAE Alfafar 2025"
  categorias_datos:
    - identificativos: "NIF/CIF, denominación, domicilio social/fiscal"
    - actividad_economica: "Epígrafe IAE, descripción actividad, empleados"
    - tributarios: "Cuotas municipales, reducciones, fechas alta/baja"
  cesiones_terceros:
    - aeat: "Coordinación censos (base legal: LGT)"
    - ss: "Verificación empleados (base legal: LGSS)"
  plazos_supresion: "4 años desde prescripción"

# Continuar para ICIO, IVTM y TODAS las tasas municipales...
```

#### **📋 Formato registro obligatorio (Art. 30.1 RGPD):**

```markdown
# REGISTRO ACTIVIDADES TRATAMIENTO - AYUNTAMIENTO ALFAFAR
## Sistema Municipal IA - Datos Tributarios

### IDENTIFICACIÓN RESPONSABLE:
- Organismo: Ayuntamiento de Alfafar
- NIF: P4600200E
- Dirección: Plaza de la Constitución, 1 - 46910 Alfafar (Valencia)
- Representante: Alcalde/Alcaldesa en ejercicio
- DPO: [Nombre] - dpo@alfafar.es - Tel: 96 XXX XX XX

### POR CADA TRATAMIENTO:
1. **Finalidades específicas del tratamiento**
2. **Categorías de interesados y datos personales**
3. **Destinatarios o categorías de destinatarios**
4. **Transferencias internacionales (si aplicable)**
5. **Plazos de supresión previstos**
6. **Descripción general medidas técnicas y organizativas**
```

### **2. EVALUACIÓN DE IMPACTO EN PROTECCIÓN DATOS (EIPD) - RGPD Art. 35**

#### **🔍 Obligatoria para el Sistema IA Municipal:**

**¿Por qué es obligatoria?**
- ✅ **Tratamiento sistemático y exhaustivo** datos tributarios
- ✅ **Evaluación/valoración personas** (decisiones automatizadas impuestos)
- ✅ **Tratamiento gran escala** (todos contribuyentes Alfafar)
- ✅ **Tecnologías innovadoras** (IA/ML para OCR y cálculos)

#### **📝 Contenido mínimo EIPD (Art. 35.7):**

```yaml
# ESTRUCTURA EIPD SISTEMA MUNICIPAL IA ALFAFAR

seccion_1_descripcion:
  finalidades_tratamiento: "Automatización gestión tributaria municipal"
  interes_legitimo_evaluado: "Eficiencia administrativa + servicio público"
  
seccion_2_necesidad_proporcionalidad:
  finalidades_especificas:
    - liquidacion_automatica: "IIVTNU, IBI, IAE, ICIO, IVTM"
    - calculo_tasas: "Vado, ocupación vía pública, cementerio, etc."
    - deteccion_anomalias: "Patrones irregulares tributarios"
    - ocr_documentos: "Escrituras, declaraciones, autoliquidaciones"
  proporcionalidad_medidas: "Mínima intervención manual, máxima automatización"
  
seccion_3_riesgos_identificados:
    - perdida_confidencialidad: "Acceso no autorizado datos tributarios"
    - perdida_integridad: "Modificación indebida liquidaciones"
    - perdida_disponibilidad: "Interrupción servicio época declaraciones"
    - decision_erronea_ia: "Liquidación incorrecta por algoritmo"
    - discriminacion_algoritmica: "Sesgo en cálculos por zona/perfil"
    
seccion_4_medidas_previstas:
  tecnicas:
    - cifrado_extremo_extremo: "AES-256 datos críticos"
    - segregacion_redes: "VLAN tributaria aislada"
    - autenticacion_reforzada: "2FA funcionarios + certificados"
    - backup_cifrado: "Replicación tiempo real servidor secundario"
    - logs_auditoria: "Trazabilidad completa todas operaciones"
  organizativas:
    - formacion_funcionarios: "Curso RGPD + IA responsable"
    - supervision_humana: "Revisión obligatoria sanciones >300€"
    - procedimientos_respuesta: "Ejercicio derechos ciudadanos <30 días"
    - auditoria_regular: "Trimestral algoritmos + anual seguridad"
```

### **3. DESIGNACIÓN DELEGADO PROTECCIÓN DATOS (DPO) - RGPD Art. 37**

#### **🛡️ Obligatorio para Ayuntamiento (autoridad pública):**

```yaml
# DOCUMENTACIÓN DPO OBLIGATORIA

designacion_formal:
  fecha_nombramiento: "Antes activación sistema IA"
  cualificacion_acreditada: "Certificación DPO + experiencia sector público"
  ausencia_conflicto_interes: "No funcionario área tributaria"
  contacto_publico: "Publicado web municipal + registro AEPD"

funciones_especificas_ia:
  - supervision_eipd: "Validación evaluación impacto antes despliegue"
  - formacion_funcionarios: "Curso anual RGPD + IA responsable"
  - punto_contacto_ciudadanos: "Canal directo ejercicio derechos"
  - supervision_algoritmos: "Auditoría trimestral sesgo + discriminación"
  - coordinacion_aepd: "Comunicación incidentes + consultas previas"
  
recursos_garantizados:
  - acceso_directo_alcaldia: "Sin intermediarios"
  - presupuesto_autonomo: "Formación + herramientas + auditorías"
  - tiempo_dedicacion: "Mínimo 50% jornada laboral"
  - acceso_sistemas: "Solo lectura - auditoría completa"
```

---

## 🤖 DOCUMENTACIÓN AI ACT OBLIGATORIA

### **4. SISTEMA DE GESTIÓN DE RIESGOS IA (AI Act Art. 9)**

#### **⚠️ Obligatorio para sistemas IA alto riesgo (gestión tributaria):**

```yaml
# CLASIFICACIÓN SISTEMAS IA MUNICIPAL ALFAFAR

sistemas_alto_riesgo:
  document_processor_ocr:
    categoria: "AI Act Anexo III.5 - Gestión y funcionamiento servicios públicos"
    riesgo_identificado: "Extracción errónea datos → liquidación incorrecta"
    medidas_mitigacion:
      - supervision_humana: "Revisión funcionario antes liquidación final"
      - threshold_confianza: "OCR <95% → revisión manual obligatoria"
      - validation_cruzada: "Contraste múltiples fuentes datos"
      
  tax_calculator_automatico:
    categoria: "AI Act Anexo III.5 - Decisiones automatizadas sector público"
    riesgo_identificado: "Cálculo erróneo → perjuicio económico ciudadano"
    medidas_mitigacion:
      - double_check_algorithm: "Validación cruzada 2 algoritmos independientes"
      - human_override: "Funcionario puede revertir cualquier decisión"
      - audit_trail: "Log completo cada cálculo con justificación"
      
  anomaly_detector:
    categoria: "AI Act Anexo III.5 - Detección fraude sector público"
    riesgo_identificado: "Falso positivo → investigación injustificada"
    medidas_mitigacion:
      - threshold_elevado: "Solo alertas confianza >85%"
      - revision_previa: "Inspector valida antes abrir expediente"
      - explicabilidad: "Factores específicos que generaron alerta"

sistemas_riesgo_limitado:
  web_interface_chatbot:
    categoria: "AI Act Art. 50 - Sistemas interacción humanos"
    obligacion: "Información clara uso IA + limitaciones"
    implementacion: "Banner visible: 'Asistente IA - no vinculante'"

sistemas_riesgo_minimo:
  spam_filter_correos:
    categoria: "AI Act Art. 51 - Código conducta voluntario"
    obligacion: "Ninguna específica - buenas prácticas"
```

### **5. DOCUMENTACIÓN TÉCNICA SISTEMAS IA (AI Act Art. 11)**

#### **📋 Obligatoria antes puesta en funcionamiento:**

```yaml
# DOCUMENTACIÓN TÉCNICA POR SISTEMA IA

document_processor_ocr:
  informacion_general:
    - finalidad_especifica: "Extracción automática datos documentos notariales"
    - nivel_precision_previsto: ">95% textos español notarial"
    - contexto_uso: "Apoyo funcionarios inspección tributaria"
    - hardware_software: "Tesseract + Custom ML modelo español"
    
  algoritmo_logica:
    - tipo_modelo: "CNN + Transformer OCR + NER spaCy custom"
    - datos_entrenamiento: "10.000 escrituras anonimizadas 2020-2024"
    - metricas_rendimiento: "Precisión 95.7%, Recall 94.2%, F1-Score 94.9%"
    - limitaciones_conocidas: "Documentos manuscritos <80% precisión"
    
  gestion_riesgos:
    - riesgos_identificados: "Texto degradado, escritura ilegible, formatos no estándar"
    - medidas_mitigacion: "Threshold confianza + revisión humana"
    - testing_continuo: "Validación mensual muestra aleatoria 100 documentos"
    
  supervision_humana:
    - tipo_supervision: "Human-in-the-loop continuous"
    - competencias_requeridas: "Funcionario conocimiento tributario + formación IA"
    - procedimientos_intervencion: "Corrección inmediata + feedback algoritmo"

tax_calculator_automatico:
  informacion_general:
    - finalidad_especifica: "Cálculo automático todas figuras tributarias municipales"
    - normativa_aplicada: "LRHL + Ordenanzas fiscales Alfafar vigentes"
    - casos_uso: "IIVTNU, IBI, IAE, ICIO, IVTM + tasas municipales"
    
  algoritmo_logica:
    - tipo_modelo: "Rules-based engine + ML validation"
    - reglas_implementadas: "487 reglas tributarias codificadas"
    - validacion_historica: "Contraste 5.000 liquidaciones 2020-2024"
    - precision_actual: "99.95% cálculos matemáticos exactos"
    
  casos_excepcion:
    - bonificaciones_especiales: "Revisión manual obligatoria"
    - valores_atipicos: "Desviación >20% media → alerta automática"
    - normativa_nueva: "Actualización manual reglas + testing"
```

### **6. LOGS Y TRAZABILIDAD ALGORITMOS (AI Act Art. 12)**

#### **📊 Obligatorio registro automático:**

```json
{
  "sistema_ia": {
    "timestamp": "2025-07-31T10:15:23Z",
    "sistema": "tax_calculator_iivtnu",
    "version_algoritmo": "v2.1.3",
    "accion": "calculo_plusvalia_automatico",
    "input_hash": "sha256_documento_entrada_xyz123",
    "resultado": {
      "base_imponible": 15750.50,
      "cuota_tributaria": 1181.29,
      "tipo_gravamen": 7.5,
      "bonificaciones_aplicadas": "ninguna"
    },
    "confianza_calculo": 0.999,
    "revision_humana_requerida": false,
    "funcionario_responsable": "inspector_001_hash",
    "normativa_aplicada": ["LRHL_Art_104", "Ordenanza_IIVTNU_Alfafar_2025"],
    "tiempo_procesamiento_ms": 156,
    "validaciones_superadas": [
      "coherencia_fechas",
      "valores_catastro",
      "coeficientes_actualizacion",
      "aplicacion_bonificaciones"
    ]
  }
}
```

---

## 📋 DOCUMENTACIÓN LOPDGDD ESPECÍFICA

### **7. ANÁLISIS DE RIESGOS TRATAMIENTO (LOPDGDD Art. 28)**

#### **🔍 Obligatorio adicional a EIPD:**

```yaml
# ANÁLISIS RIESGOS ESPECÍFICO ESPAÑA

riesgos_especificos_lopdgdd:
  datos_identificacion:
    - dni_ciudadanos: "Riesgo alto - identificación unívoca"
    - direcciones_fiscales: "Riesgo medio - localización personas"
    - datos_patrimoniales: "Riesgo alto - información sensible económica"
    
  medidas_especificas:
    - seudonimizacion: "Hash irreversible DNI para logs"
    - minimizacion_acceso: "Solo funcionarios autorizados por rol"
    - cifrado_reforzado: "AES-256 + certificados cualificados"
    - auditoria_nacional: "Coordinación con AEPD"

responsabilidades_funcionarios:
  inspector_tributario:
    - acceso_autorizado: "Solo expedientes asignados"
    - formacion_obligatoria: "Curso LOPDGDD + IA anual"
    - deber_secreto: "Art. 5 LOPDGDD - confidencialidad datos"
    
  tecnico_sistemas:
    - acceso_restringido: "Solo mantenimiento sin datos personales"
    - logs_actividad: "Registro completo acciones sistema"
    - segregacion_funciones: "No acceso datos tributarios contenido"
```

---

## 🔒 DOCUMENTACIÓN ENS (ESQUEMA NACIONAL SEGURIDAD)

### **8. DECLARACIÓN APLICABILIDAD ENS MEDIO**

#### **⚙️ Obligatoria para datos tributarios municipales:**

```yaml
# CATEGORIZACIÓN SISTEMA INFORMACIÓN

clasificacion_datos:
  confidencialidad: "MEDIO"
  integridad: "ALTO"  
  disponibilidad: "MEDIO"
  trazabilidad: "ALTO"

justificacion_categoria:
  confidencialidad_medio:
    - "Datos tributarios ciudadanos - no clasificados alto secreto"
    - "Impacto limitado revelación - perjuicio notable no grave"
  integridad_alto:
    - "Liquidaciones tributarias - impacto económico directo"
    - "Modificación indebida → perjuicio grave ciudadanos/ayuntamiento"
  disponibilidad_medio:
    - "Servicio público esencial - no crítico supervivencia"
    - "Interrupción tolerable hasta 24 horas"
  trazabilidad_alto:
    - "Obligación legal tributaria - auditoría completa"
    - "Responsabilidad administrativa funcionarios"

medidas_implementar:
  organizativas:
    - politica_seguridad: "Aprobada por Alcaldía"
    - normativa_uso: "Funcionarios + ciudadanos"
    - plan_formacion: "Anual seguridad + protección datos"
    - gestion_incidentes: "Procedimiento respuesta <4 horas"
    
  operacionales:
    - control_acceso: "Autenticación fuerte + roles granulares"
    - proteccion_instalaciones: "Control físico acceso servidores"
    - gestion_comunicaciones: "Cifrado todas comunicaciones"
    - backup_restauracion: "Diario cifrado + testing mensual"
    
  medidas_proteccion:
    - proteccion_informacion: "Clasificación + etiquetado"
    - cifrado: "AES-256 reposo + TLS 1.3 tránsito"
    - prevencion_malware: "Antivirus + EDR centralizado"
    - monitorizacion: "SIEM tiempo real + alertas"
```

---

## 📅 CRONOGRAMA DOCUMENTACIÓN OBLIGATORIA

### **🗓️ Documentos por crear/actualizar (desde 31 julio 2025):**

#### **📋 PRIORIDAD MÁXIMA (antes activación sistema):**
```yaml
documentos_criticos:
  eipd_completa:
    plazo: "Antes procesamiento datos reales"
    responsable: "DPO + Secretario General"
    validacion: "Dictamen jurídico + consulta AEPD si dudas"
    
  registro_actividades:
    plazo: "Simultáneo activación cada módulo"
    responsable: "DPO + Jefe Servicio Tributario"
    actualizacion: "Cada modificación tratamiento"
    
  documentacion_tecnica_ia:
    plazo: "Antes despliegue cada algoritmo"
    responsable: "Proveedor tecnológico + validación DPO"
    revision: "Cada actualización algoritmo"
```

#### **📋 PRIORIDAD ALTA (primeros 30 días funcionamiento):**
```yaml
documentos_operativos:
  procedimientos_ejercicio_derechos:
    contenido: "ARCO + oposición decisiones automatizadas"
    formato: "Formularios web + presencial + registro"
    
  manual_funcionarios:
    contenido: "Uso sistema + supervisión IA + escalado incidencias"
    formacion: "Presencial obligatoria antes acceso"
    
  plan_auditoria:
    alcance: "Trimestral algoritmos + semestral seguridad"
    metodologia: "Interna + externa anual"
```

#### **📋 PRIORIDAD MEDIA (primeros 90 días):**
```yaml
documentos_mejora:
  analisis_sesgo_algoritmos:
    metodologia: "Testing estadístico discriminación por zona/perfil"
    periodicidad: "Semestral con informe público"
    
  metricas_cumplimiento:
    indicadores: "Tiempo respuesta + precisión + satisfacción"
    reporting: "Mensual interno + semestral público"
```

---

## ✅ CHECKLIST DOCUMENTACIÓN OBLIGATORIA

### **📋 Verificación cumplimiento normativo:**

```markdown
## RGPD (Reglamento General Protección Datos)
☐ Registro actividades tratamiento (Art. 30) - TODAS figuras tributarias
☐ Evaluación impacto protección datos (Art. 35) - Sistema IA completo  
☐ Designación DPO (Art. 37) - Cualificado + sin conflictos
☐ Información transparente ciudadanos (Art. 12-14) - Web municipal
☐ Procedimientos ejercicio derechos (Art. 15-22) - ARCO + oposición

## AI ACT (Reglamento Inteligencia Artificial)  
☐ Clasificación sistemas IA por riesgo - Documentada y justificada
☐ Sistema gestión riesgos (Art. 9) - Cada algoritmo identificado
☐ Documentación técnica (Art. 11) - Antes puesta funcionamiento
☐ Logs automáticos (Art. 12) - Trazabilidad completa operaciones
☐ Supervisión humana (Art. 14) - Procedimientos claros intervención

## LOPDGDD (Ley Orgánica Protección Datos España)
☐ Análisis riesgos específico España (Art. 28) - Adicional EIPD
☐ Medidas seguridad reforzadas - Datos especialmente protegidos
☐ Coordinación AEPD - Canal comunicación directo

## ENS (Esquema Nacional Seguridad)
☐ Declaración aplicabilidad - Categorización sistema medio/alto
☐ Plan seguridad - Medidas organizativas + operacionales + protección
☐ Procedimiento gestión incidentes - Respuesta <4 horas
☐ Auditoría seguridad - Externa anual + interna semestral

## NORMATIVA SECTORIAL TRIBUTARIA
☐ Procedimientos LRHL - Liquidación + inspección + recaudación
☐ Ordenanzas fiscales actualizadas - Todas figuras tributarias
☐ Coordinación otros organismos - Catastro + Registro + Notarios
```

---

## 🔄 MANTENIMIENTO Y ACTUALIZACIÓN

### **📅 Periodicidad obligatoria:**

```yaml
revision_continua:
  registro_actividades: 
    frecuencia: "Cada modificación tratamiento"
    responsable: "DPO"
    
  documentacion_tecnica_ia:
    frecuencia: "Cada actualización algoritmo"
    responsable: "Proveedor + DPO validación"
    
  eipd:
    frecuencia: "Anual + cada cambio sustancial"
    responsable: "DPO + asesoría jurídica"
    
  plan_seguridad_ens:
    frecuencia: "Anual + tras incidentes graves"
    responsable: "Responsable seguridad + DPO"

auditorias_obligatorias:
  interna_trimestral:
    alcance: "Funcionamiento algoritmos IA"
    metodologia: "Checklist cumplimiento + métricas"
    
  externa_anual:
    alcance: "Cumplimiento integral RGPD + AI Act + ENS"
    auditor: "Certificado independiente"
    
  aepd_coordinacion:
    frecuencia: "Según requerimientos + consultas complejas"
    procedimiento: "Canal directo DPO"
```

---

**📅 Documento actualizado**: 31 julio 2025  
**🔄 Próxima revisión**: Al iniciar desarrollo archivo 05  
**📧 Responsable**: DPO + Secretario General Ayuntamiento Alfafar  
**🎯 Versión**: 1.0 - Documentación obligatoria completa