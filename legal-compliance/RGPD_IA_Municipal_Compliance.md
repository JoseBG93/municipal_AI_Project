# Cumplimiento Normativo: IA y Cloud Computing en Administración Municipal

## 📋 Objetivo del documento

Este archivo establece las directrices legales y éticas para implementar el **Sistema Municipal de IA** del Ayuntamiento de Alfafar cumpliendo con toda la normativa vigente de protección de datos.

---

## 🇪🇺 MARCO NORMATIVO APLICABLE

### **1. Normativa Europea**
- **RGPD (Reglamento General de Protección de Datos)** - Reglamento (UE) 2016/679
- **Directiva ePrivacy** - Directiva 2002/58/CE
- **Reglamento de IA de la UE** - AI Act (2024)

### **2. Normativa Nacional (España)**
- **LOPD-GDD** - Ley Orgánica 3/2018 de Protección de Datos Personales y garantía de los derechos digitales
- **Ley 40/2015** - Régimen Jurídico del Sector Público
- **ENS** - Esquema Nacional de Seguridad (RD 311/2022)

### **3. Normativa Sectorial Municipal**
- **Ley 7/1985** - Bases del Régimen Local
- **Ley 39/2015** - Procedimiento Administrativo Común
- **Normativas autonómicas valencianas específicas**

---

## 🎯 PRINCIPIOS FUNDAMENTALES A CUMPLIR

### **1. Minimización de datos**
```
✅ CORRECTO: Recoger solo DNI, nombre, dirección para IBI
❌ INCORRECTO: Recoger datos familiares innecesarios
```

### **2. Limitación de finalidad**
```
✅ CORRECTO: Datos tributarios solo para gestión tributaria
❌ INCORRECTO: Usar datos tributarios para marketing municipal
```

### **3. Transparencia**
```
✅ CORRECTO: Informar claramente qué IA procesará los datos
❌ INCORRECTO: Procesamiento opaco sin información ciudadana
```

### **4. Responsabilidad proactiva**
```
✅ CORRECTO: Documentar medidas técnicas y organizativas
❌ INCORRECTO: Implementar sin análisis de riesgos previo
```

---

## 🏛️ ARQUITECTURA TÉCNICA CONFORME

### **Clasificación de datos por sensibilidad:**

#### **🔴 NIVEL CRÍTICO (On-premise obligatorio)**
- DNIs y datos identificativos
- Información tributaria (IBI, IAE, sanciones)
- Expedientes de embargos/procedimientos
- **UBICACIÓN**: Servidor municipal exclusivamente

#### **🟡 NIVEL MEDIO (Cloud controlado)**
- Documentos anonimizados para OCR
- Cálculos estadísticos agregados
- **UBICACIÓN**: Cloud europeo con contrato RGPD

#### **🟢 NIVEL BAJO (Cloud público)**
- Interfaces web públicas
- Servicios de información general
- **UBICACIÓN**: Cloud global con salvaguardas

### **Diseño técnico conforme:**

```yaml
# docker-compose.yml conforme RGPD
services:
  # DATOS CRÍTICOS - Solo local
  postgres:
    deploy:
      placement:
        constraints: [node.labels.security == high]
        # Solo servidores municipales físicos
  
  # PROCESAMIENTO - Cloud controlado  
  document_processor:
    environment:
      - DATA_ANONYMIZATION=true
      - CLOUD_REGION=eu-west-1
      - RGPD_MODE=strict
    deploy:
      placement:
        constraints: [node.labels.cloud == eu-compliant]
```

---

## 📝 DOCUMENTACIÓN OBLIGATORIA

### **1. Registro de Actividades de Tratamiento (RGPD Art. 30)**

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| Finalidad | Para qué procesas datos | Gestión tributaria municipal |
| Categorías | Qué tipos de datos | DNI, dirección, patrimonio |
| Destinatarios | Quién accede | Funcionarios tributarios |
| Transferencias | Envíos fuera UE | Solo proveedores UE |
| Plazos | Cuánto tiempo guardas | Según normativa tributaria |

### **2. Evaluación de Impacto (RGPD Art. 35)**
**Obligatoria cuando hay IA y tratamiento sistemático**

```markdown
## EIPD - Sistema Municipal IA

### Descripción del tratamiento:
- OCR automático de escrituras de compraventa
- Cálculo automatizado de tributos municipales  
- Verificación de declaraciones con IA

### Riesgos identificados:
1. **Alto**: Decisiones automatizadas sobre sanciones
2. **Medio**: Almacenamiento cloud de documentos
3. **Bajo**: Cálculos tributarios estándar

### Medidas de mitigación:
1. Supervisión humana obligatoria para sanciones
2. Anonimización previa al cloud
3. Auditorías algorítmicas trimestrales
```

### **3. Análisis de Legitimación**

```markdown
## Base jurídica por servicio:

### document_processor (OCR):
- **Base legal**: RGPD Art. 6.1.e (misión de interés público)
- **Normativa específica**: Ley 58/2003 General Tributaria
- **Justificación**: Verificación documental tributaria

### tax_calculator:
- **Base legal**: RGPD Art. 6.1.c (obligación legal)  
- **Normativa específica**: Ordenanzas fiscales municipales
- **Justificación**: Cálculo obligatorio de tributos

### web_interface:
- **Base legal**: RGPD Art. 6.1.a (consentimiento)
- **Normativa específica**: Ley 39/2015 PAC
- **Justificación**: Servicio voluntario online
```

---

## 🔒 MEDIDAS TÉCNICAS OBLIGATORIAS

### **1. Seguridad by Design**

```bash
# Configuración Docker Swarm conforme
# Cifrado en tránsito
docker service create \
  --network encrypted \
  --secret postgres_password \
  postgres

# Cifrado en reposo  
volumes:
  postgres-data:
    driver: local
    driver_opts:
      type: ext4
      device: /dev/mapper/encrypted-volume
```

### **2. Auditoría y Logs**

```yaml
# logging.yml - Configuración obligatoria
version: '3.8'
services:
  audit-logger:
    image: elasticsearch:8.0
    environment:
      - RGPD_RETENTION=6_years
      - LOG_ANONYMIZATION=true
    volumes:
      - audit-logs:/var/log/audit
```

### **3. Controles de acceso**

```bash
# Roles funcionarios (ejemplo)
INSPECTOR_TRIBUTARIO:
  - read: expedientes_asignados
  - write: informes_propios
  - delete: ninguno

TECNICO_MUNICIPAL:
  - read: datos_anonimizados
  - write: configuracion_sistema
  - delete: logs_antiguos

CIUDADANO:
  - read: datos_propios
  - write: nuevas_declaraciones  
  - delete: ninguno
```

---

## ⚖️ DERECHOS DE LOS CIUDADANOS

### **Implementación técnica obligatoria:**

#### **1. Derecho de Acceso (RGPD Art. 15)**
```bash
# API endpoint obligatorio
GET /api/v1/citizen/{dni}/data
Response: {
  "personal_data": {...},
  "processing_purposes": [...],
  "automated_decisions": [...],
  "data_sources": [...]
}
```

#### **2. Derecho de Rectificación (RGPD Art. 16)**
```bash
# Proceso obligatorio
PUT /api/v1/citizen/{dni}/data
# + Workflow aprobación funcionario
# + Notificación cambios sistemas conectados
```

#### **3. Derecho de Portabilidad (RGPD Art. 20)**
```bash
# Export funcional obligatorio
GET /api/v1/citizen/{dni}/export
Response: JSON/XML estructurado reutilizable
```

#### **4. Derecho de Oposición a decisiones automatizadas (RGPD Art. 22)**
```bash
# Supervisión humana obligatoria para:
- Cálculos de sanciones > 300€
- Denegaciones de licencias
- Clasificaciones de riesgo tributario
```

---

## 🌍 TRANSFERENCIAS INTERNACIONALES

### **Proveedores cloud permitidos (Decisión de Adecuación UE):**

#### **✅ PERMITIDOS SIN SALVAGUARDAS ADICIONALES:**
- **Alemania**: Hetzner, 1&1 IONOS
- **Francia**: OVH, Scaleway  
- **Países Bajos**: TransIP, Hosting.nl
- **España**: Arsys, Acens, Telefónica

#### **⚠️ PERMITIDOS CON CLÁUSULAS CONTRACTUALES TIPO:**
- **Estados Unidos**: AWS, Google Cloud, Microsoft Azure
  - Requiere: Standard Contractual Clauses (SCC)
  - Requiere: Transfer Impact Assessment (TIA)
  - Requiere: Medidas suplementarias de cifrado

#### **❌ PROHIBIDOS:**
- Proveedores sin sede UE sin salvaguardas
- Países sin decisión de adecuación sin SCC

### **Configuración técnica transferencias:**

```yaml
# docker-compose.yml - Solo proveedores conformes
services:
  document_processor:
    deploy:
      placement:
        constraints: 
          - node.labels.gdpr_region == eu
          - node.labels.adequacy_decision == true
```

---

## 🤖 REGULACIÓN ESPECÍFICA DE IA

### **Clasificación según AI Act de la UE:**

#### **🔴 RIESGO ALTO (Regulación estricta)**
```
❌ NO PERMITIDO:
- IA para scoring social ciudadanos
- Sistemas de identificación biométrica en tiempo real

⚠️ PERMITIDO CON SALVAGUARDAS:
- IA para detección anomalías tributarias
- Sistemas automatizados de sanciones
```

#### **🟡 RIESGO LIMITADO (Transparencia obligatoria)**
```
✅ PERMITIDO CON INFORMACIÓN:
- Chatbots de atención ciudadana
- OCR automatizado de documentos
- Cálculos automatizados de tributos
```

### **Requisitos técnicos obligatorios IA:**

```markdown
## 1. Supervisión humana
- Funcionario debe poder overridear decisiones IA
- IA no puede tomar decisiones finales en sanciones
- Revisión humana obligatoria en casos ambiguos

## 2. Transparencia algorítmica  
- Ciudadano debe conocer que hay IA involucrada
- Explicación comprensible de decisiones automatizadas
- Documentación pública de algoritmos utilizados

## 3. Precisión y robustez
- Testing regular de sesgos algorítmicos  
- Métricas de precisión documentadas
- Planes de contingencia si IA falla
```

---

## 📋 PROCEDIMIENTOS OPERATIVOS

### **1. Implementación gradual conforme:**

#### **Fase 1 (Meses 1-3): Fundamentos legales**
```bash
# Tareas obligatorias:
☐ Completar Registro de Actividades de Tratamiento
☐ Realizar Evaluación de Impacto (EIPD)  
☐ Designar Delegado de Protección de Datos (DPO)
☐ Redactar políticas de privacidad específicas
☐ Configurar sistema de gestión de consentimientos
```

#### **Fase 2 (Meses 4-6): Infraestructura técnica**
```bash
# Implementación conforme:
☐ Configurar cifrado end-to-end
☐ Implementar sistema de logs de auditoría
☐ Configurar controles de acceso granulares  
☐ Establecer procedimientos de backup conformes
☐ Testing de derechos ciudadanos (APIs)
```

#### **Fase 3 (Meses 7-12): IA y automatización**
```bash
# Despliegue controlado:
☐ Implementar supervisión humana obligatoria
☐ Configurar explicabilidad de decisiones
☐ Establecer métricas de precisión y sesgo
☐ Formación específica funcionarios
☐ Auditoría externa de cumplimiento
```

### **2. Contratos obligatorios con proveedores:**

#### **Acuerdo de Tratamiento de Datos (DPA)**
```markdown
## Cláusulas mínimas obligatorias:

### Art. 1 - Objeto y duración
- Proveedor actúa como encargado del tratamiento
- Ayuntamiento es responsable del tratamiento
- Duración limitada al contrato principal + eliminación

### Art. 2 - Obligaciones del encargado  
- Tratamiento solo según instrucciones documentadas
- Garantizar confidencialidad personal autorizado
- Implementar medidas técnicas y organizativas apropiadas
- Asistir al responsable en respuesta a ejercicio de derechos

### Art. 3 - Transferencias internacionales
- Prohibidas sin autorización expresa escrita
- Solo a países con decisión de adecuación
- Cláusulas contractuales tipo si es necesario

### Art. 4 - Subencargados
- Lista específica y autorizada por el ayuntamiento
- Mismo nivel de protección exigido
- Responsabilidad solidaria por incumplimientos

### Art. 5 - Auditorías
- Derecho de auditoría del ayuntamiento
- Acceso a documentación y instalaciones
- Informes periódicos de cumplimiento
```

---

## 🚨 GESTIÓN DE INCIDENTES

### **Procedimiento de brechas de seguridad:**

#### **1. Detección (0-1 horas)**
```bash
# Alertas automáticas configuradas:
- Acceso no autorizado a postgres
- Modificaciones masivas de datos
- Fallos de cifrado en transferencias
- Accesos desde ubicaciones anómalas
```

#### **2. Evaluación inicial (1-6 horas)**
```markdown
## Checklist obligatorio:
☐ ¿Hay datos personales involucrados?
☐ ¿Cuántos ciudadanos afectados?
☐ ¿Qué tipo de datos (sensibles/normales)?
☐ ¿Riesgo alto para derechos y libertades?
☐ ¿Origen del incidente (interno/externo)?
```

#### **3. Notificación AEPD (dentro de 72h)**
```markdown
## Contenido mínimo obligatorio:
- Naturaleza de la violación
- Categorías y número aproximado de interesados
- Categorías y número aproximado de registros
- Consecuencias probables de la violación
- Medidas adoptadas o propuestas
```

#### **4. Comunicación ciudadanos (si riesgo alto)**
```markdown
## Medio: Email + web municipal + registro  
## Contenido obligatorio:
- Descripción comprensible de la violación
- Punto de contacto (DPO del ayuntamiento)  
- Medidas adoptadas o propuestas
- Recomendaciones para los interesados
```

---

## 💼 ARGUMENTOS CONTRA "EXCUSAS" COMUNES

### **🔄 "La protección de datos impide modernizar"**

#### **Respuesta técnica:**
```markdown
❌ FALSO: RGPD promueve modernización responsable
✅ CIERTO: Permite innovación con salvaguardas

Ejemplos conformes exitosos:
- Estonia: administración 100% digital + máxima protección
- Dinamarca: IA tributaria + cumplimiento RGPD ejemplar
- Países Bajos: automatización municipal + transparencia total
```

#### **Argumentos legales:**
```markdown
• RGPD Art. 35: Evaluación de impacto FACILITA proyectos
• Privacy by Design: Ahorra costes a largo plazo  
• Modernización es OBLIGACIÓN según Ley 39/2015 PAC
```

### **🔄 "Es demasiado caro cumplir RGPD"**

#### **Análisis coste-beneficio:**
```markdown
## Costes de NO cumplir:
- Multas AEPD: Hasta 20M€ o 4% presupuesto anual
- Daño reputacional: Desconfianza ciudadana
- Costes legales: Procedimientos y recursos
- Paralización: Servicios bloqueados por infracciones

## Costes de SÍ cumplir:
- DPO: 30.000€/año
- Infraestructura: 10.000€ inicial  
- Formación: 5.000€/año
- Auditorías: 8.000€/año

TOTAL: 53.000€/año vs Riesgo 20.000.000€
```

### **🔄 "Los ciudadanos no entienden la IA"**

#### **Solución: Transparencia proactiva**
```markdown
## Portal público obligatorio: /transparencia-ia

### Información ciudadana comprensible:
"¿Cómo funciona el cálculo automático de IBI?"

1. Tu declaración → Sistema extrae datos automáticamente
2. IA compara con valores similares en Alfafar  
3. Funcionario revisa resultado antes de aprobar
4. Recibes notificación con explicación detallada
5. Puedes solicitar revisión humana siempre

"¿Mis datos están seguros?"
- Nunca saldrán de Europa
- Cifrados como datos bancarios
- Solo funcionarios autorizados acceden
- Derecho a copia/corrección/eliminación siempre
```

### **🔄 "Es demasiado complejo técnicamente"**

#### **Solución: Implementación incremental**
```bash
# Mes 1: Solo servicios locales
docker-compose up postgres redis web_interface

# Mes 3: Añadir OCR local  
docker service create document_processor_local

# Mes 6: Añadir cloud conforme UE
docker service create --constraint="node.region==eu" document_processor_cloud

# Mes 12: IA con supervisión humana
docker service create --env="HUMAN_OVERSIGHT=required" tax_calculator_ai
```

---

## 📊 MÉTRICAS DE CUMPLIMIENTO

### **KPIs obligatorios de seguimiento:**

#### **1. Técnicos**
```markdown
- Tiempo respuesta ejercicio derechos: < 1 mes
- Disponibilidad servicios ciudadanos: > 99.5%
- Incidentes seguridad: 0 de alto impacto/año
- Auditorías algoritmos: 4 veces/año mínimo
```

#### **2. Legales**  
```markdown
- Evaluaciones impacto realizadas: 100% servicios IA
- Contratos DPA firmados: 100% proveedores
- Formaciones RGPD personal: 100% funcionarios/año
- Quejas AEPD: 0 confirmadas/año
```

#### **3. Ciudadanos**
```markdown
- Satisfacción transparencia: > 80%
- Tiempo resolución consultas DPO: < 15 días
- Ejercicio derechos completado: 100% en plazo
- Quejas por decisiones automatizadas: < 1%
```

---

## 🎓 FORMACIÓN OBLIGATORIA PERSONAL

### **Programa específico por rol:**

#### **👥 Funcionarios generales (4h/año)**
```markdown
Módulo 1: Principios básicos RGPD (1h)
- Qué son datos personales
- Bases legales para tratamiento
- Derechos ciudadanos básicos

Módulo 2: Seguridad información (1h)  
- Contraseñas seguras y 2FA
- Identificación phishing
- Procedimiento incidentes

Módulo 3: IA responsable (1h)
- Cuándo hay decisión automatizada
- Cómo explicar decisiones ciudadanos
- Cuándo derivar a supervisión humana

Módulo 4: Casos prácticos municipales (1h)
- Ejercicio derechos paso a paso
- Consultas frecuentes ciudadanos
- Escalado a DPO cuando necesario
```

#### **👨‍💻 Personal técnico (12h/año)**
```markdown
Módulo 1: Privacy by Design (3h)
- Minimización datos en arquitectura
- Cifrado y anonimización técnica
- Controles acceso granulares

Módulo 2: Seguridad Docker/Cloud (3h)
- Configuración segura contenedores
- Redes cifradas y secretos
- Monitorización y alertas

Módulo 3: Auditoría y logs (3h)
- Qué registrar y durante cuánto tiempo
- Anonimización logs para análisis
- Reporting compliance automático

Módulo 4: Gestión incidentes técnicos (3h)
- Detección automática brechas
- Procedimientos contención
- Evidencias forenses preservación
```

#### **⚖️ DPO y responsables (20h/año)**
```markdown
Módulo 1: Marco legal actualizado (5h)
- Novedades RGPD y AI Act
- Jurisprudencia TJUE relevante  
- Criterios AEPD específicos

Módulo 2: Evaluaciones impacto (5h)
- Metodología EIPD completa
- Casos específicos IA municipal
- Herramientas evaluación automatizada

Módulo 3: Auditorías y certificación (5h)
- Preparación auditorías AEPD
- Estándares ISO 27001/27701
- Documentación compliance

Módulo 4: Gestión stakeholders (5h)
- Comunicación ciudadanos incidentes
- Relación proveedores/encargados
- Coordinación otros ayuntamientos
```

---

## 📞 CONTACTOS Y RECURSOS

### **Organismos oficiales:**
- **AEPD**: www.aepd.es | consulta@aepd.es | 901 100 099
- **CCN-CERT**: www.ccn-cert.cni.es | ccn-cert@cni.es
- **Colegio Profesional DPO Valencia**: www.cpdpv.es

### **Recursos técnicos específicos:**
- **Guía AEPD IA**: "Directrices sobre decisiones automatizadas"
- **Kit RGPD Administraciones**: aepd.es/guias/guia-rgpd-para-responsables-de-tratamiento.pdf
- **ENS para Ayuntamientos**: ccn-cert.cni.es/esquema-nacional-de-seguridad.html

### **Templates y herramientas:**
- **Registro actividades**: Plantilla AEPD específica
- **EIPD automatizada**: Herramienta online CCN-CERT
- **DPA tipo**: Cláusulas AEPD + AI Act

---

## ✅ CHECKLIST FINAL DE CUMPLIMIENTO

### **Antes del go-live (obligatorio):**

#### **📋 Documentación legal**
```bash
☐ Registro Actividades Tratamiento completado
☐ Evaluación Impacto (EIPD) realizada y aprobada
☐ Política privacidad específica publicada
☐ Procedimientos ejercicio derechos definidos
☐ DPO designado y notificado AEPD
☐ Contratos DPA firmados con todos proveedores
☐ Análisis transferencias internacionales completado
☐ Procedimientos gestión incidentes aprobados
```

#### **🔧 Implementación técnica**
```bash
☐ Cifrado end-to-end configurado y testado
☐ Controles acceso implementados por roles
☐ Sistema logs auditoría funcionando  
☐ APIs derechos ciudadanos desplegadas
☐ Backups conformes RGPD configurados
☐ Monitorización seguridad activa
☐ Procedimientos recuperación ante desastres
☐ Testing penetración realizado y aprobado
```

#### **👥 Formación y procesos**
```bash
☐ Personal técnico formado en RGPD + IA
☐ Funcionarios formados en nuevos procedimientos
☐ Ciudadanos informados cambios (web + registro)
☐ Canales soporte DPO establecidos
☐ Métricas compliance definidas y funcionando
☐ Auditoría externa compliance realizada
☐ Plan comunicación crisis preparado
☐ Contactos AEPD/CCN-CERT establecidos
```

---

## 📝 CONCLUSIONES Y RECOMENDACIONES

### **Viabilidad del proyecto:**
**✅ TOTALMENTE VIABLE** cumplir RGPD + AI Act en proyecto municipal IA

### **Claves del éxito:**
1. **Planificación legal previa**: EIPD antes que código
2. **Privacy by Design**: Cumplimiento integrado, no añadido después  
3. **Transparencia proactiva**: Ciudadanos como aliados, no obstáculos
4. **Implementación incremental**: Complejidad técnica y legal gradual
5. **Formación específica**: Personal preparado = menos incidentes

### **ROI del cumplimiento:**
- **Coste cumplimiento**: ~50.000€/año
- **Beneficio modernización**: ~200.000€/año (eficiencia administrativa)
- **Coste NO cumplimiento**: Hasta 20.000.000€ (riesgo multas)
- **Beneficio ciudadano**: Servicios 24/7 + transparencia total

### **Argumentos definitivos contra excusas:**
1. **"Protección datos impide innovar"** → Estonia, Dinamarca lo demuestran falso
2. **"Es muy caro"** → Más caro es NO cumplir (multas millonarias)
3. **"Es muy complejo"** → Implementación gradual hace viable cualquier ayuntamiento
4. **"Ciudadanos no entienden"** → Transparencia proactiva genera confianza

---

**📧 Contacto DPO del proyecto**: dpo@ayuntamiento-alfafar.es
**📅 Última actualización**: Diciembre 2024
**🔄 Próxima revisión**: Marzo 2025

---

*Este documento es dinámico y debe actualizarse según evolución normativa y jurisprudencial.*