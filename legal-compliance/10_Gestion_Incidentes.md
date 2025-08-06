# 10. GESTIÓN DE INCIDENTES DE SEGURIDAD Y VIOLACIONES DE DATOS
## Sistema Municipal IA - Ayuntamiento de Alfafar

### MARCO NORMATIVO APLICABLE

**Normativa Principal:**
- **RGPD Art. 33-34**: Notificación violaciones de seguridad (72h AEPD, sin demora interesados)
- **LOPDGDD Art. 94-95**: Procedimiento nacional violaciones de datos
- **AI Act Art. 62**: Notificación incidentes graves sistemas alto riesgo
- **ENS**: Gestión de incidentes según nivel MEDIO
- **CCN-STIC 817**: Esquema Nacional de Seguridad - Gestión de Incidentes

---

## 1. CLASIFICACIÓN DE INCIDENTES

### 1.1 INCIDENTES DE SEGURIDAD RGPD

**NIVEL CRÍTICO - Notificación 72h Obligatoria:**
- Acceso no autorizado a datos tributarios ciudadanos
- Cifrado comprometido en base datos PostgreSQL
- Exfiltración documentos notariales (escrituras, herencias)
- Modificación no autorizada cálculos IIVTNU/IBI
- Caída servicios con exposición datos > 24h
- Ransomware/malware en infraestructura crítica
- Compromiso credenciales administradores sistema

**NIVEL ALTO - Evaluación Inmediata:**
- Intentos fallidos acceso masivos (>1000/hora)
- Anomalías procesamiento OCR documentos
- Errores algoritmos IA con decisiones erróneas
- Fallos autenticación ciudadanos portal
- Pérdida temporal conectividad servicios críticos
- Actualizaciones seguridad críticas pendientes >7 días

**NIVEL MEDIO - Monitorización Reforzada:**
- Logs de seguridad incompletos <24h
- Rendimiento degradado servicios no críticos
- Alertas certificados SSL próximos vencimiento
- Accesos desde ubicaciones geográficas inusuales
- Intentos phishing dirigidos personal municipal

**NIVEL BAJO - Seguimiento Rutinario:**
- Fallos menores conectividad temporal <1h
- Actualizaciones menores sistema pendientes
- Logs de auditoría rutinarios
- Intentos acceso desde IPs conocidas bloqueadas

### 1.2 INCIDENTES ESPECÍFICOS IA (AI Act)

**INCIDENTES GRAVES - Notificación Obligatoria:**
- Sesgo discriminatorio detectado en algoritmos tributarios
- Decisiones automatizadas erróneas afectando derechos ciudadanos
- Fallo supervisión humana en procesos críticos
- Corrupción modelos ML/entrenamiento
- Exposición involuntaria lógica algoritmos propietarios
- Manipulación externa resultados IA

**INCIDENTES TÉCNICOS IA:**
- Degradación precisión modelos OCR <85%
- Falsos positivos masivos detección anomalías >10%
- Latencia procesamiento >30 segundos documentos
- Errores entrenamiento modelos nuevos
- Incompatibilidad versiones librerías ML
- Recursos computacionales insuficientes

---

## 2. ESTRUCTURA ORGANIZATIVA GESTIÓN INCIDENTES

### 2.1 EQUIPO DE RESPUESTA A INCIDENTES (ERI)

**COORDINADOR INCIDENTES (José - Inspección Tributaria):**
- Clasificación inicial gravedad incidente
- Activación protocolos respuesta
- Comunicación AEPD/autoridades
- Coordinación equipos técnicos
- Supervisión resolución y documentación

**RESPONSABLE TÉCNICO (Informática Municipal):**
- Análisis técnico incidente
- Implementación medidas contención
- Coordinación equipos externos si necesario
- Verificación integridad sistemas
- Documentación técnica incidente

**RESPONSABLE LEGAL (Secretaría General):**
- Evaluación implicaciones legales
- Redacción notificaciones oficiales
- Comunicación ciudadanos afectados
- Coordinación con asesores jurídicos
- Seguimiento procedimientos sancionadores

**DELEGADO PROTECCIÓN DATOS (DPD):**
- Supervisión cumplimiento RGPD
- Evaluación riesgos para derechos ciudadanos
- Validación notificaciones AEPD
- Registro incidentes Registro Actividades
- Propuesta mejoras organizativas

### 2.2 ESCALADO Y COMUNICACIÓN

**ESCALADO NIVEL 1 - Técnico Sistemas:**
- Detección inicial automatizada/manual
- Clasificación preliminar incidente
- Medidas contención inmediatas
- Notificación Coordinador ERI

**ESCALADO NIVEL 2 - Coordinador ERI:**
- Validación clasificación incidente
- Activación equipos respuesta
- Evaluación necesidad notificación externa
- Coordinación medidas técnicas/organizativas

**ESCALADO NIVEL 3 - Dirección Municipal:**
- Incidentes críticos con impacto público
- Decisiones recursos extraordinarios
- Comunicación medios/ciudadanía
- Coordinación autoridades superiores

---

## 3. PROCEDIMIENTOS DE RESPUESTA

### 3.1 DETECCIÓN Y NOTIFICACIÓN INICIAL

**DETECCIÓN AUTOMATIZADA:**
```yaml
Monitorización 24/7:
  - SIEM: Correlación eventos seguridad
  - Logs: Análisis patrones anómalos
  - Métricas: Umbrales rendimiento/disponibilidad
  - Backup: Verificación integridad
  - Red: Tráfico anómalo/intrusiones

Alertas Automáticas:
  - Email: Equipo técnico + Coordinador ERI
  - SMS: Incidentes críticos
  - Dashboard: Estado tiempo real
  - Integración: Sistemas municipal existentes
```

**DETECCIÓN MANUAL:**
- Personal municipal: Formulario web incidentes
- Ciudadanos: Canal específico portal municipal
- Terceros: Email seguridad@alfafar.es
- Auditorías: Hallazgos revisiones periódicas

**TIEMPO RESPUESTA MÁXIMO:**
- **Crítico**: 15 minutos
- **Alto**: 1 hora
- **Medio**: 4 horas
- **Bajo**: 24 horas

### 3.2 EVALUACIÓN Y CLASIFICACIÓN

**CRITERIOS EVALUACIÓN INICIAL (15 min máximo):**

1. **Afectación Datos Personales:**
   - Nº ciudadanos afectados
   - Categorías datos (comunes/especiales)
   - Probabilidad acceso no autorizado
   - Reversibilidad del incidente

2. **Impacto Servicios Críticos:**
   - IIVTNU: Cálculos/notificaciones
   - IBI: Padrones/liquidaciones  
   - Portal Ciudadano: Acceso servicios
   - GTT/Gestiona: Integración sistemas

3. **Riesgo Derechos Ciudadanos:**
   - Discriminación algoritmos
   - Decisiones automatizadas erróneas
   - Exposición información sensible
   - Afectación procedimientos administrativos

**MATRIZ DE CLASIFICACIÓN:**
```
CRÍTICO: Datos>1000 + Acceso Confirmado + Servicios Críticos Afectados
ALTO: Datos>100 + Probable Acceso + Servicios Importantes Afectados  
MEDIO: Datos>10 + Posible Acceso + Servicios Menores Afectados
BAJO: Datos<10 + Sin Acceso + Sin Afectación Servicios
```

### 3.3 CONTENCIÓN Y MITIGACIÓN

**MEDIDAS CONTENCIÓN INMEDIATA:**

**Incidentes Seguridad Datos:**
1. **Aislamiento Afectado** (5 min):
   - Desconexión segmentos red comprometidos
   - Revocación credenciales afectadas
   - Bloqueo IPs/usuarios sospechosos
   - Preservación evidencias forenses

2. **Evaluación Alcance** (30 min):
   - Identificación datos específicos afectados
   - Período temporal compromiso
   - Vectores ataque utilizados
   - Sistemas adicionales en riesgo

3. **Medidas Protección** (1 hora):
   - Cifrado adicional datos críticos
   - Backup sistemas críticos
   - Activación sistemas redundantes
   - Comunicación equipos afectados

**Incidentes Sistemas IA:**
1. **Suspensión Decisiones Automatizadas**:
   - Activación supervisión humana 100%
   - Revisión decisiones recientes sospechosas
   - Bloqueo algoritmos comprometidos
   - Registro detallado acciones correctivas

2. **Verificación Integridad Modelos**:
   - Comparación checksums modelos
   - Validación datasets entrenamiento
   - Pruebas precisión/sesgo
   - Rollback versiones anteriores si necesario

### 3.4 NOTIFICACIONES OBLIGATORIAS

**AEPD - VIOLACIONES SEGURIDAD (72h máximo):**

**Información Obligatoria:**
- Naturaleza violación seguridad
- Categorías/número aproximado interesados
- Categorías/número aproximado registros
- Consecuencias probables violación
- Medidas adoptadas/propuestas
- Datos contacto DPD

**Plantilla Notificación AEPD:**
```
IDENTIFICACIÓN ORGANISMO:
- Ayuntamiento de Alfafar
- CIF: P4600500G  
- DPD: [nombre] - dpd@alfafar.es

DESCRIPCIÓN INCIDENTE:
- Fecha/hora detección: [timestamp]
- Fecha/hora estimada inicio: [timestamp]
- Tipo violación: [Acceso/Alteración/Pérdida]
- Descripción técnica: [detalles]

DATOS AFECTADOS:
- Ciudadanos afectados: [número]
- Categorías datos: [tributarios/identificativos/etc]
- Origen datos: [GTT/Gestiona/Sistema IA]
- Período temporal: [fechas]

MEDIDAS ADOPTADAS:
- Contención: [acciones inmediatas]
- Mitigación: [reducción riesgos]
- Comunicación: [si procede ciudadanos]
- Preventivas: [evitar recurrencia]

EVALUACIÓN RIESGOS:
- Probabilidad daño: [Alta/Media/Baja]
- Gravedad impacto: [Alta/Media/Baja]
- Reversibilidad: [Reversible/Irreversible]
- Medidas seguridad: [existentes/adicionales]
```

**AUTORIDADES IA - INCIDENTES GRAVES:**
- Autoridad Nacional IA (en desarrollo)
- Comisión Europea (incidentes transfronterizos)
- Otros Estados Miembros (si procede)

**CIUDADANOS AFECTADOS - SIN DEMORA INDEBIDA:**

**Criterios Comunicación Obligatoria:**
- Alto riesgo derechos y libertades
- Medidas técnicas protección insuficientes
- Impacto adverso probable
- Interés público información

**Contenido Comunicación Ciudadanos:**
```
ASUNTO: Incidente Seguridad Datos - Sistema Municipal Alfafar

Estimado/a ciudadano/a:

Le comunicamos que el [fecha] se detectó un incidente de seguridad 
en nuestro Sistema Municipal IA que podría haber afectado a sus 
datos personales.

DATOS AFECTADOS:
- [Especificar categorías sin detalles técnicos]
- [Período temporal]
- [Origen información]

MEDIDAS ADOPTADAS:
- [Contención inmediata]
- [Protección adicional]  
- [Colaboración autoridades]

SUS DERECHOS:
- Información adicional: ciudadano@alfafar.es
- Reclamación AEPD: www.aepd.es
- DPD Municipal: dpd@alfafar.es

RECOMENDACIONES:
- [Acciones ciudadano si procede]
- [Contacto dudas/consultas]

Atentamente,
Ayuntamiento de Alfafar
```

---

## 4. INVESTIGACIÓN Y ANÁLISIS FORENSE

### 4.1 PRESERVACIÓN EVIDENCIAS

**CADENA DE CUSTODIA:**
```yaml
Evidencias Digitales:
  - Logs sistemas: Copia inmutable + hash SHA-256
  - Memoria volátil: Dump completo si sistemas activos
  - Discos duros: Imagen bit-a-bit con write blockers
  - Tráfico red: Capturas PCAP período incidente
  - Base datos: Export consistente + logs transacciones

Documentación:
  - Screenshots: Pantallas evidencia visual
  - Fotos: Equipos físicos si procede
  - Testimonios: Declaraciones personal presente
  - Cronología: Timeline detallado eventos
  - Comunicaciones: Emails/llamadas relacionadas
```

**HERRAMIENTAS FORENSES:**
- **Autopsy**: Análisis imágenes disco
- **Volatility**: Análisis memoria RAM
- **Wireshark**: Análisis tráfico red
- **Log2timeline**: Creación timeline eventos
- **YARA**: Detección malware/patrones

### 4.2 ANÁLISIS CAUSA RAÍZ

**METODOLOGÍA 5 PORQUÉS:**
```
Ejemplo IIVTNU - Cálculo Erróneo Masivo:

¿Por qué se produjeron cálculos erróneos?
→ Algoritmo IA procesó mal valores catastrales

¿Por qué procesó mal los valores?
→ Dataset entrenamiento contenía datos corruptos

¿Por qué contenía datos corruptos?
→ Integración GTT no validó formato entrada

¿Por qué no validó el formato?
→ Controles calidad datos insuficientes

¿Por qué controles insuficientes?
→ Procedimientos validación no definidos formalmente

CAUSA RAÍZ: Falta procedimientos validación datos entrada
```

**FACTORES ANÁLISIS:**
- **Técnicos**: Vulnerabilidades, configuraciones, parches
- **Humanos**: Errores, formación, procedimientos
- **Procesos**: Controles, validaciones, supervisión
- **Organizativos**: Roles, responsabilidades, comunicación
- **Externos**: Ataques, proveedores, integraciones

### 4.3 IMPACTO Y EVALUACIÓN DAÑOS

**DIMENSIONES IMPACTO:**

**Ciudadanos Afectados:**
- Número total y por categorías
- Gravedad afectación individual
- Daños materiales/morales
- Tiempo exposición datos
- Posibilidad mitigación

**Servicios Municipales:**
- Tiempo inactividad por servicio
- Transacciones perdidas/erróneas
- Coste recuperación
- Reputación institucional
- Confianza ciudadana

**Cumplimiento Normativo:**
- Obligaciones RGPD incumplidas
- Requisitos AI Act no satisfechos
- Nivel ENS comprometido
- Posibles sanciones/multas
- Auditorías adicionales requeridas

**Económico:**
- Costes respuesta incidente
- Pérdida ingresos municipales
- Compensaciones ciudadanos
- Inversiones seguridad adicionales
- Recursos humanos dedicados

---

## 5. RECUPERACIÓN Y CONTINUIDAD

### 5.1 PLAN DE RECUPERACIÓN

**FASES RECUPERACIÓN:**

**FASE 1 - ESTABILIZACIÓN (0-4h):**
- Contención completa incidente
- Verificación no propagación
- Sistemas críticos operativos
- Comunicaciones esenciales activas
- Equipo respuesta coordinado

**FASE 2 - RESTAURACIÓN SERVICIOS (4-24h):**
- Backup sistemas desde punto limpio
- Validación integridad datos
- Pruebas funcionalidad crítica
- Activación sistemas redundantes
- Comunicación estado servicios

**FASE 3 - NORMALIZACIÓN (1-7 días):**
- Restauración completa servicios
- Monitorización intensiva
- Validación procesos tributarios
- Comunicación normalidad
- Documentación lecciones aprendidas

**FASE 4 - FORTALECIMIENTO (1-4 semanas):**
- Implementación mejoras seguridad
- Actualización procedimientos
- Formación adicional personal
- Auditoría independiente
- Certificación recuperación

### 5.2 CRITERIOS RECUPERACIÓN

**SERVICIOS CRÍTICOS - RPO/RTO:**
```yaml
IIVTNU (Plusvalía):
  RPO: 4 horas (pérdida datos máxima)
  RTO: 2 horas (tiempo recuperación)
  
IBI (Bienes Inmuebles):
  RPO: 8 horas
  RTO: 4 horas
  
Portal Ciudadano:
  RPO: 1 hora  
  RTO: 30 minutos
  
Sistema IA:
  RPO: 24 horas
  RTO: 8 horas
```

**VERIFICACIONES INTEGRIDAD:**
- **Base Datos**: Checksums, transacciones, consistencia
- **Modelos IA**: Validación precisión, ausencia sesgo
- **Integraciones**: GTT, Gestiona, Correos.es funcionales
- **Certificados**: SSL/TLS válidos y confiables
- **Usuarios**: Credenciales, permisos, autenticación

### 5.3 COMUNICACIÓN RECUPERACIÓN

**COMUNICACIÓN INTERNA:**
- **Personal Municipal**: Estado servicios, procedimientos temporales
- **Concejales**: Briefing situación, medidas adoptadas
- **Alcalde**: Decisiones estratégicas, comunicación externa
- **Proveedores**: Coordinación recuperación sistemas

**COMUNICACIÓN EXTERNA:**
- **Ciudadanos**: Portal web, redes sociales, bandos
- **AEPD**: Actualización estado resolución
- **Medios**: Rueda prensa si impacto público
- **Otros Ayuntamientos**: Alerta si vulnerabilidad común

---

## 6. LECCIONES APRENDIDAS Y MEJORA CONTINUA

### 6.1 ANÁLISIS POST-INCIDENTE

**INFORME FINAL OBLIGATORIO (máximo 30 días):**

**RESUMEN EJECUTIVO:**
- Descripción incidente y impacto
- Cronología eventos principales
- Medidas adoptadas y efectividad
- Coste total y tiempo recuperación
- Recomendaciones principales

**ANÁLISIS DETALLADO:**
```yaml
Detección:
  - Tiempo hasta detección
  - Efectividad monitorización
  - Fuente detección inicial
  - Alertas perdidas/falsas

Respuesta:
  - Tiempos escalado y activación
  - Efectividad comunicaciones
  - Coordinación equipos
  - Disponibilidad recursos

Contención:
  - Rapidez aislamiento
  - Efectividad medidas
  - Prevención propagación
  - Preservación evidencias

Recuperación:
  - Cumplimiento RPO/RTO
  - Integridad restauración
  - Validación funcionamiento
  - Satisfacción usuarios
```

**CAUSA RAÍZ Y FACTORES CONTRIBUYENTES:**
- Factor técnico principal
- Factores humanos involucrados
- Deficiencias procedimientos
- Aspectos organizativos
- Factores externos

### 6.2 PLAN DE MEJORAS

**MEJORAS TÉCNICAS:**
- Actualizaciones seguridad prioritarias
- Nuevas herramientas monitorización
- Redundancia sistemas críticos
- Automatización respuesta
- Validaciones datos adicionales

**MEJORAS ORGANIZATIVAS:**
- Revisión procedimientos
- Formación personal adicional
- Clarificación roles/responsabilidades
- Comunicación interna mejorada
- Escalado optimizado

**MEJORAS NORMATIVAS:**
- Actualización políticas seguridad
- Nuevos controles RGPD/AI Act
- Procedimientos documentados
- Métricas cumplimiento
- Auditorías programadas

### 6.3 INDICADORES DE MEJORA

**KPIs GESTIÓN INCIDENTES:**
```yaml
Detección:
  - MTTD (Mean Time To Detection): <30 min objetivo
  - Falsos positivos: <5% alertas
  - Cobertura monitorización: >95% activos

Respuesta:
  - MTTR (Mean Time To Response): <15 min críticos
  - MTTS (Mean Time To Stabilize): <4h críticos
  - Efectividad contención: >90% casos

Recuperación:
  - Cumplimiento RPO: >95% casos
  - Cumplimiento RTO: >95% casos
  - Satisfacción usuarios: >85% encuestas

Aprendizaje:
  - Recurrencia incidentes: <10% anual
  - Mejoras implementadas: >80% recomendaciones
  - Tiempo análisis: <30 días por incidente
```

---

## 7. PROCEDIMIENTOS ESPECÍFICOS POR TIPO

### 7.1 RANSOMWARE / CIFRADO MALICIOSO

**RESPUESTA INMEDIATA (0-15 min):**
1. **NO pagar rescate** - Política municipal clara
2. **Aislamiento completo** sistemas afectados
3. **Preservación evidencias** antes limpieza
4. **Activación backup** desde punto limpio anterior
5. **Comunicación INCIBE/CERT-ES** inmediata

**EVALUACIÓN IMPACTO:**
- Datos ciudadanos cifrados
- Sistemas críticos afectados
- Posibilidad recuperación backup
- Tiempo estimado restauración
- Necesidad recursos externos

**COMUNICACIÓN:**
- AEPD: Notificación 72h si datos personales
- Ciudadanos: Si servicios críticos >24h inactivos
- Medios: Transparencia sin detalles técnicos
- INCIBE: Colaboración investigación

### 7.2 FUGA DATOS TRIBUTARIOS

**CONTENCIÓN (0-30 min):**
1. **Identificación alcance** - Ciudadanos/datos específicos
2. **Revocación accesos** - Credenciales comprometidas
3. **Monitorización** - Búsqueda datos filtrados online
4. **Evidencias** - Logs acceso, vectores exfiltración
5. **Evaluación legal** - Implicaciones RGPD específicas

**ANÁLISIS ESPECÍFICO:**
- **Categorías datos**: IIVTNU, IBI, identificativos, económicos
- **Período exposición**: Desde primera filtración
- **Vectores ataque**: Email, web, insider, social engineering
- **Destinatarios**: Identificación si posible
- **Uso malicioso**: Monitorización indicios

**NOTIFICACIONES ESPECIALES:**
- **AEAT**: Si datos tributarios estatales afectados
- **Notarios**: Si escrituras comprometidas
- **Ciudadanos**: Comunicación personalizada riesgos
- **Seguros**: Activación póliza ciberseguridad si existe

### 7.3 ALGORITMO IA SESGADO/DISCRIMINATORIO

**SUSPENSIÓN INMEDIATA:**
1. **Parada decisiones automatizadas** afectadas
2. **Revisión manual** decisiones recientes sospechosas
3. **Análisis sesgo** - Grupos protegidos afectados
4. **Preservación modelos** - Versiones actuales y anteriores
5. **Supervisión humana** 100% hasta resolución

**EVALUACIÓN DISCRIMINACIÓN:**
- **Grupos afectados**: Edad, género, nacionalidad, etc.
- **Tipo sesgo**: Estadístico, histórico, representación
- **Magnitud impacto**: Ciudadanos/decisiones afectadas
- **Gravedad consecuencias**: Económicas, derechos, acceso servicios
- **Reversibilidad**: Posibilidad corrección retroactiva

**MEDIDAS CORRECTIVAS:**
- **Reentrenamiento modelo** con datos balanceados
- **Validación exhaustiva** ausencia sesgos
- **Revisión decisiones** período determinado
- **Compensación**: Si procede ciudadanos afectados
- **Documentación AI Act**: Actualización sistema gestión riesgos

### 7.4 COMPROMISO INFRAESTRUCTURA DOCKER

**ANÁLISIS CONTENEDORES:**
1. **Inventario contenedores** activos y comprometidos
2. **Aislamiento swarm** - Separación nodos afectados
3. **Análisis imágenes** - Malware, backdoors, modificaciones
4. **Verificación integridad** - Checksums, certificados
5. **Logs orchestración** - Actividad sospechosa cluster

**RECUPERACIÓN SWARM:**
- **Backup configuración** cluster antes limpieza
- **Recreación nodos** desde imágenes limpias
- **Restauración servicios** orden prioridad críticos
- **Validación seguridad** - Secrets, certificados, redes
- **Monitorización intensiva** post-recuperación

---

## 8. HERRAMIENTAS Y RECURSOS

### 8.1 HERRAMIENTAS TÉCNICAS

**DETECCIÓN Y MONITORIZACIÓN:**
```yaml
SIEM/Log Management:
  - ELK Stack (Elasticsearch, Logstash, Kibana)
  - Graylog (alternativa open source)
  - OSSIM (SIEM open source)
  
Monitorización Infraestructura:
  - Nagios/Icinga: Estado servicios
  - Zabbix: Métricas rendimiento
  - Prometheus + Grafana: Métricas tiempo real
  
Análisis Forense:
  - Autopsy: Análisis discos
  - Volatility: Análisis memoria
  - YARA: Detección malware
  - Wireshark: Análisis red
```

**GESTIÓN INCIDENTES:**
- **OTRS/OSTicket**: Ticketing y seguimiento
- **TheHive**: Plataforma respuesta incidentes
- **MISP**: Compartición indicators compromise
- **Cortex**: Análisis observables automatizado

### 8.2 DOCUMENTACIÓN Y PLANTILLAS

**PLANTILLAS OBLIGATORIAS:**
- Notificación AEPD violación seguridad
- Comunicación ciudadanos afectados
- Informe análisis post-incidente
- Plan comunicación crisis
- Checklist respuesta por tipo incidente

**DOCUMENTACIÓN TÉCNICA:**
- Procedimientos backup/restore
- Configuración herramientas SIEM
- Inventario activos críticos
- Contactos emergencia 24/7
- Escalado autoridades/proveedores

### 8.3 CONTACTOS EMERGENCIA

**INTERNOS 24/7:**
```yaml
Coordinador ERI: 
  - José (Inspección): +34 XXX XXX XXX
  
Técnico Sistemas:
  - Informática Municipal: +34 XXX XXX XXX
  
Responsable Legal:
  - Secretario General: +34 XXX XXX XXX
  
DPD:
  - [Nombre]: dpd@alfafar.es
```

**EXTERNOS:**
```yaml
Emergencias:
  - INCIBE-CERT: 112 (emergencias ciberseguridad)
  - Guardia Civil UCO: 062
  - Policía Nacional UDI: 091
  
Reguladores:
  - AEPD: +34 901 100 099
  - Subdelegación Gobierno: +34 XXX XXX XXX
  
Proveedores:
  - Soporte Docker: [según contrato]
  - Cloud Provider: [según SLA]
  - Proveedor SIEM: [24/7 si contratado]
```

---

## 9. CUMPLIMIENTO Y AUDITORÍA

### 9.1 REGISTRO OBLIGATORIO INCIDENTES

**INFORMACIÓN MÍNIMA REGISTRAR:**
```yaml
Identificación:
  - ID único incidente
  - Fecha/hora detección
  - Fuente detección
  - Clasificación inicial/final
  
Descripción:
  - Naturaleza incidente
  - Sistemas/datos afectados
  - Causa raíz identificada
  - Vector ataque (si aplicable)
  
Respuesta:
  - Medidas contención adoptadas
  - Tiempo respuesta por fase
  - Recursos involucrados
  - Efectividad medidas
  
Impacto:
  - Ciudadanos afectados
  - Datos comprometidos
  - Servicios interrumpidos
  - Coste total
  
Resolución:
  - Medidas correctivas
  - Tiempo recuperación
  - Validación resolución
  - Lecciones aprendidas
```

**CONSERVACIÓN REGISTROS:**
- **RGPD**: Mínimo 3 años para violaciones datos personales
- **AI Act**: 10 años para sistemas alto riesgo
- **ENS**: Según nivel seguridad aplicable
- **Auditoría**: Disponible para inspecciones

### 9.2 MÉTRICAS CUMPLIMIENTO

**INDICADORES RGPD:**
- % notificaciones AEPD en plazo 72h: >95%
- % comunicaciones ciudadanos sin demora: >90%
- Tiempo medio resolución violaciones: <30 días
- % incidentes con causa raíz identificada: 100%

**INDICADORES AI ACT:**
- % incidentes graves notificados: 100%
- Tiempo medio supervisión humana activada: <1h
- % decisiones revisadas post-incidente: 100%
- Actualizaciones sistema gestión riesgos: <7 días

**INDICADORES OPERATIVOS:**
- MTTD (detección): <30 min críticos
- MTTR (respuesta): <15 min críticos  
- MTBF (entre fallos): >90 días
- Disponibilidad servicios: >99.5%

### 9.3 AUDITORÍAS PERIÓDICAS

**AUDITORÍA ANUAL OBLIGATORIA:**
- Revisión procedimientos gestión incidentes
- Efectividad medidas técnicas/organizativas
- Cumplimiento notificaciones obligatorias
- Análisis tendencias y mejoras
- Validación competencias equipos respuesta

**AUDITORÍA POST-INCIDENTE:**
- Análisis respuesta específica
- Identificación gaps procedimientos
- Validación tiempos respuesta
- Efectividad comunicaciones
- Propuesta mejoras concretas

---

## 10. ANEXOS

### ANEXO A: CHECKLIST RESPUESTA RÁPIDA

**PRIMEROS 15 MINUTOS:**
- [ ] Detección confirmada incidente
- [ ] Clasificación inicial gravedad
- [ ] Notificación Coordinador ERI
- [ ] Preservación evidencias iniciales
- [ ] Medidas contención inmediatas
- [ ] Evaluación propagación
- [ ] Activación equipo respuesta

**PRIMERA HORA:**
- [ ] Análisis alcance completo
- [ ] Clasificación final incidente
- [ ] Plan respuesta activado
- [ ] Comunicación equipo directivo
- [ ] Evaluación necesidad notificación AEPD
- [ ] Documentación cronología eventos
- [ ] Coordinación recursos adicionales

**PRIMERAS 24 HORAS:**
- [ ] Contención completa verificada
- [ ] Análisis causa raíz iniciado
- [ ] Plan recuperación activado
- [ ] Comunicación stakeholders
- [ ] Notificación AEPD si obligatoria
- [ ] Preservación evidencias completa
- [ ] Evaluación impacto preliminar

### ANEXO B: PLANTILLA CRONOLOGÍA INCIDENTES

```
CRONOLOGÍA INCIDENTE [ID] - [FECHA]

T+00:00 - [HH:MM] Detección inicial
  - Fuente: [automatizada/manual/externa]
  - Descripción: [qué se detectó]
  - Responsable: [quién detectó]

T+00:15 - [HH:MM] Clasificación inicial  
  - Gravedad: [crítico/alto/medio/bajo]
  - Sistemas afectados: [lista]
  - Datos en riesgo: [categorías]

T+00:30 - [HH:MM] Activación ERI
  - Coordinador notificado: [nombre]
  - Equipo convocado: [miembros]
  - Medidas inmediatas: [acciones]

[Continuar cronología con intervalos regulares]
```

### ANEXO C: FORMULARIO EVALUACIÓN IMPACTO

```yaml
EVALUACIÓN IMPACTO INCIDENTE

Datos Personales Afectados:
  - Número ciudadanos: [cantidad]
  - Categorías datos: [identificativos/tributarios/especiales]
  - Período exposición: [fecha inicio - fin]
  - Probabilidad acceso no autorizado: [alta/media/baja]

Servicios Municipales:
  - IIVTNU: [operativo/degradado/inactivo]
  - IBI: [operativo/degradado/inactivo]  
  - Portal Ciudadano: [operativo/degradado/inactivo]
  - GTT/Gestiona: [operativo/degradado/inactivo]

Riesgo Derechos Ciudadanos:
  - Discriminación: [sí/no/posible]
  - Decisiones erróneas: [número/tipo]
  - Exposición información: [gravedad]
  - Afectación procedimientos: [descripción]

Impacto Económico:
  - Coste respuesta: [estimado €]
  - Pérdida ingresos: [estimado €]
  - Recursos dedicados: [horas-persona]
  - Inversiones adicionales: [requeridas €]
```

---

**DOCUMENTO:** 10_Gestion_Incidentes.md  
**VERSIÓN:** 1.0  
**FECHA:** 2 agosto 2025  
**RESPONSABLE:** José - Inspección Tributaria  
**ESTADO:** Completado  
**PRÓXIMA REVISIÓN:** agosto 2026