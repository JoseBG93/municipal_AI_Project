# Marco Normativo Completo para IA Municipal
## Ayuntamiento de Alfafar - Sistema Municipal de Inteligencia Artificial

---

## 📋 OBJETIVO DEL DOCUMENTO

Este documento establece el **marco normativo exhaustivo** aplicable al Sistema Municipal de IA del Ayuntamiento de Alfafar, cubriendo desde normativa principal europea hasta reglamentación municipal específica, asegurando cumplimiento integral desde el primer día de implementación.

---

## 🇪🇺 NORMATIVA EUROPEA (DIRECTAMENTE APLICABLE)

### **1. RGPD - Reglamento General de Protección de Datos**
**Reglamento (UE) 2016/679**

#### **Artículos clave para el proyecto:**
- **Art. 5**: Principios relativos al tratamiento (licitud, lealtad, transparencia)
- **Art. 6**: Licitud del tratamiento (interés público, obligación legal)
- **Art. 9**: Tratamiento de categorías especiales (si aplicable a datos fiscales)
- **Art. 22**: Decisiones individuales automatizadas, incluida la elaboración de perfiles
- **Art. 30**: Registro de las actividades de tratamiento
- **Art. 35**: Evaluación de impacto relativa a la protección de datos
- **Art. 37**: Designación del delegado de protección de datos

#### **Desarrollos normativos específicos:**
- **Mecanismo de Coherencia (art. 63)**: Coordinación entre autoridades UE
- **Directrices EDPB**: Comité Europeo de Protección de Datos
  - Directrices 3/2018 sobre perfilado
  - Directrices 05/2020 sobre consentimiento
  - Directrices 10/2020 sobre evaluaciones de impacto

### **2. AI Act - Reglamento de Inteligencia Artificial**
**Reglamento (UE) 2024/1689 - Entrada en vigor progresiva hasta agosto 2026**

#### **Aplicación temporal:**
- **Febrero 2025**: Prohibiciones sistemas IA de alto riesgo
- **Agosto 2025**: Obligaciones modelos IA de propósito general
- **Agosto 2026**: Aplicación completa todos los sistemas

#### **Clasificación sistemas IA municipales:**
- **Riesgo Inaceptable**: Sistemas de puntuación social (PROHIBIDOS)
- **Alto Riesgo**: Detección fraude tributario, asignación servicios públicos
- **Riesgo Limitado**: Chatbots ciudadanos, OCR documentos
- **Riesgo Mínimo**: Filtros anti-spam, herramientas ofimáticas

#### **Obligaciones específicas:**
- **Art. 9**: Sistemas de gestión de riesgos
- **Art. 10**: Datos y gobernanza de datos
- **Art. 11**: Documentación técnica
- **Art. 12**: Mantenimiento de registros
- **Art. 13**: Transparencia e información a usuarios
- **Art. 14**: Supervisión humana
- **Art. 15**: Exactitud, robustez y ciberseguridad

### **3. Normativa Digital Complementaria**

#### **DSA/DMA - Digital Services/Markets Acts**
- **DSA**: Transparencia algoritmos plataformas (aplicable si servicios > 45M usuarios UE)
- **DMA**: Interoperabilidad servicios básicos (aplicable a gatekeepers)

#### **DGA - Data Governance Act (Reglamento 2022/868)**
- **Art. 5**: Reutilización categorías específicas datos sector público
- **Art. 12**: Servicios intermediación de datos
- **Aplicabilidad municipal**: Intercambio datos con otras administraciones

#### **Directiva Open Data (2019/1024)**
- **Art. 3**: Principio general reutilización
- **Art. 5**: Formatos disponibles y reutilizables
- **Aplicación municipal**: Datos tributarios agregados, estadísticas urbanas

### **4. ePrivacy - Confidencialidad Comunicaciones**
**Directiva 2002/58/CE (en proceso reemplazo por Reglamento ePrivacy)**

#### **Aplicación actual:**
- **Art. 5**: Confidencialidad comunicaciones electrónicas
- **Art. 6**: Tratamiento datos tráfico
- **Aplicabilidad municipal**: Comunicaciones ciudadano-ayuntamiento

---

## 🇪🇸 NORMATIVA NACIONAL ESPAÑOLA

### **1. LOPDGDD - Protección Datos y Derechos Digitales**
**Ley Orgánica 3/2018**

#### **Derechos digitales específicos (Título X):**
- **Art. 79**: Derecho a la neutralidad de internet
- **Art. 80**: Derecho de acceso universal a internet
- **Art. 81**: Derecho a la ciberseguridad
- **Art. 82**: Derecho a la educación digital
- **Art. 83**: Protección de menores en internet
- **Art. 84**: Derecho de rectificación en internet
- **Art. 85**: Derecho al olvido en búsquedas de internet
- **Art. 86**: Derecho a la portabilidad en servicios de redes sociales
- **Art. 87**: Derecho al testamento digital
- **Art. 88**: Derechos digitales en el ámbito laboral
- **Art. 89**: Derecho a la desconexión digital en el ámbito laboral
- **Art. 90**: Derecho a la intimidad y uso de dispositivos digitales en el ámbito laboral
- **Art. 91**: Derecho a la intimidad frente al uso de dispositivos de videovigilancia y de grabación de sonidos en el lugar de trabajo
- **Art. 92**: Derecho a la intimidad frente al uso de sistemas de geolocalización en el ámbito laboral

#### **Disposiciones específicas administración pública:**
- **Art. 77**: Tratamiento con fines de archivo en interés público, fines de investigación científica o histórica o fines estadísticos
- **Disposición Adicional 7ª**: Identificación y autenticación para acceso a servicios electrónicos

### **2. Régimen Jurídico del Sector Público**
**Ley 40/2015**

#### **Actuación administrativa automatizada (Art. 41):**
```
1. Las Administraciones Públicas podrán dictar actos administrativos a través de medios electrónicos, siempre que se garantice la identificación del órgano competente, así como del responsable del procedimiento.

2. En caso de actuación administrativa automatizada deberá establecerse previamente el órgano u órganos competentes, según los casos, para la definición de las especificaciones, programación, mantenimiento, supervisión y control de calidad y, en su caso, auditoría del sistema de información y de su código fuente.

3. Asimismo, se indicará el órgano que debe ser considerado responsable a los efectos de impugnación.
```

#### **Aplicación al sistema municipal:**
- **Órgano competente**: Concejalía de Nuevas Tecnologías + Secretaría Municipal
- **Responsable técnico**: Jefe Sistemas Información Municipal
- **Responsable auditoría**: Intervención Municipal + DPO
- **Responsable impugnación**: Alcaldía-Presidencia

### **3. Procedimiento Administrativo Común**
**Ley 39/2015**

#### **Administración electrónica obligatoria:**
- **Art. 14.2**: Derecho y obligación de relacionarse electrónicamente
- **Art. 16**: Registros electrónicos
- **Art. 26**: Obligatoriedad medios electrónicos para ciertos sujetos
- **Art. 38**: Presentación documentos y requisitos

#### **Aplicación específica IA municipal:**
- Sistema debe permitir registro electrónico 24/7
- Decisiones automatizadas requieren recurso humano inmediato
- Notificaciones automatizadas deben cumplir art. 40-46

### **4. Esquema Nacional de Seguridad (ENS)**
**Real Decreto 311/2022**

#### **Niveles de seguridad aplicables:**
- **Nivel BÁSICO**: Información municipal general
- **Nivel MEDIO**: Datos tributarios, expedientes administrativos  
- **Nivel ALTO**: Datos especialmente protegidos, infraestructuras críticas

#### **Medidas obligatorias para IA municipal:**
- **mp.com.1**: Política de seguridad
- **mp.com.2**: Normativa de seguridad
- **mp.com.3**: Procedimientos de seguridad
- **mp.op.1**: Control de acceso
- **mp.op.2**: Autenticación
- **mp.op.5**: Gestión de vulnerabilidades
- **mp.op.6**: Auditoría de la seguridad

### **5. Normativa Tributaria Específica**
**Ley 58/2003 - General Tributaria**

#### **Base legal para tratamiento datos tributarios:**
- **Art. 94**: Deber de información de las Administraciones públicas
- **Art. 95**: Suministro de información por otros obligados
- **Aplicación IA**: Verificación automática declaraciones, detección inconsistencias

---

## 🏛️ NORMATIVA AUTONÓMICA (COMUNIDAD VALENCIANA)

### **1. Administración Electrónica Valenciana**
**Decreto 90/2013**

#### **Disposiciones aplicables:**
- **Art. 12**: Interoperabilidad entre administraciones
- **Art. 15**: Reutilización de sistemas y aplicaciones
- **Aplicación municipal**: Integración con sistemas autonómicos

### **2. Transparencia Valenciana**
**Ley 13/2010**

#### **Obligaciones transparencia:**
- **Art. 5**: Información institucional, organizativa y de planificación
- **Art. 6**: Información de relevancia jurídica
- **Art. 7**: Información económica, presupuestaria y estadística
- **Aplicación IA**: Portal transparencia algoritmos municipales

### **3. Estándares Técnicos Interoperabilidad**
**Orden 2/2019**

#### **Requisitos técnicos:**
- **Anexo I**: Esquemas de metadatos
- **Anexo II**: Catálogo de estándares
- **Aplicación municipal**: APIs conformes estándares autonómicos

---

## 🏛️ NORMATIVA MUNICIPAL ESPECÍFICA

### **1. Bases del Régimen Local**
**Ley 7/1985**

#### **Competencias municipales (Art. 25):**
- **25.2.a)**: Seguridad en lugares públicos
- **25.2.d)**: Servicios sociales de promoción y reinserción social
- **25.2.i)**: Información y promoción de la actividad turística de interés y ámbito local
- **25.2.j)**: Ferias, abastos, mercados, lonjas y comercio ambulante

#### **Aplicación IA municipal:**
- Videovigilancia inteligente (seguridad pública)
- Sistemas detección fraude social
- Chatbots información turística
- Optimización gestión mercados municipales

### **2. Reglamento Orgánico Municipal Alfafar**
**[Pendiente consulta BOP específico]**

#### **Órganos competentes identificados:**
- **Alcaldía**: Responsabilidad política sistema IA
- **Concejalía TIC**: Responsabilidad técnica
- **Secretaría**: Responsabilidad jurídica
- **Intervención**: Control presupuestario

### **3. Ordenanzas Fiscales Municipales Alfafar**

#### **Aplicación sistemas IA:**
- **IBI**: Verificación automática valoraciones catastrales
- **IAE**: Detección actividades no declaradas
- **Tasas urbanísticas**: Cálculo automático licencias
- **Multas tráfico**: Procedimientos automatizados

---

## 📚 NORMATIVA SECTORIAL COMPLEMENTARIA

### **1. Protección Datos Menores**
**LOPDGDD Art. 83 + RGPD Art. 8**

#### **Aplicación municipal:**
- Servicios digitales educativos municipales
- Consentimiento parental sistemas IA escolares
- Protección especial datos biométricos menores

### **2. Videovigilancia**
**Instrucción 1/2006 AEPD + LO 4/1997**

#### **IA en videovigilancia municipal:**
- Reconocimiento facial prohibido salvo excepciones
- Análisis comportamental limitado
- Retención imágenes máximo 1 mes
- Señalización específica sistemas inteligentes

### **3. Contratación Pública**
**Ley 9/2017 - Contratos del Sector Público**

#### **Contratación sistemas IA:**
- **Art. 122**: Medios probatorios capacidad solvencia
- **Art. 145**: Criterios adjudicación (incluir compliance RGPD)
- **Anexo IV**: Modelo europeo documento único contratación

---

## 🔄 NORMATIVA EN DESARROLLO/FUTURA

### **1. Reglamento ePrivacy**
**[Pendiente aprobación - sustituto Directiva 2002/58/CE]**

#### **Impacto previsto:**
- Consentimiento específico comunicaciones automatizadas
- Cookies y tecnologías similares
- Comunicaciones máquina-máquina (IoT municipal)

### **2. Normativa Española AI Act**
**[Desarrollo reglamentario en curso]**

#### **Previsiones:**
- Autoridad competente IA en España
- Procedimientos certificación conformidad
- Régimen sancionador específico

### **3. Normativa Ciberseguridad**
**Directiva NIS2 - Trasposición pendiente**

#### **Aplicación municipal:**
- Servicios públicos esenciales
- Requisitos notificación incidentes
- Medidas gestión riesgos ciberseguridad

---

## ✅ SÍNTESIS APLICABILIDAD DIRECTA

### **Normativa INMEDIATAMENTE aplicable:**
1. ✅ **RGPD**: Aplicación completa desde 2018
2. ✅ **LOPDGDD**: Aplicación completa desde 2018  
3. ✅ **Ley 39/2015**: Administración electrónica obligatoria
4. ✅ **Ley 40/2015**: Actuación administrativa automatizada
5. ✅ **ENS**: Medidas seguridad información
6. ✅ **AI Act**: Prohibiciones desde febrero 2025

### **Normativa PROGRESIVA:**
1. 🔄 **AI Act**: Aplicación completa agosto 2026
2. 🔄 **DGA**: Servicios intermediación datos 2024
3. 🔄 **Normativa autonómica**: Adaptaciones en curso

### **Normativa FUTURA a monitorizar:**
1. 📅 **ePrivacy Regulation**: Impacto comunicaciones
2. 📅 **NIS2**: Ciberseguridad servicios esenciales
3. 📅 **Desarrollo AI Act**: Reglamentación técnica

---

## 📞 REFERENCIAS NORMATIVAS OFICIALES

### **Fuentes principales:**
- **EUR-Lex**: eur-lex.europa.eu (normativa UE)
- **BOE**: boe.es (normativa nacional)
- **DOGV**: dogv.gva.es (normativa autonómica)
- **BOP Valencia**: bop.dival.es (normativa municipal)

### **Autoridades competentes:**
- **AEPD**: aepd.es (protección datos)
- **CCN-CERT**: ccn-cert.cni.es (ciberseguridad)
- **SETSI**: mineco.gob.es (telecomunicaciones)

---

**📅 Documento actualizado**: Diciembre 2024  
**🔄 Próxima revisión**: Marzo 2025  
**📧 Responsable**: DPO Ayuntamiento Alfafar