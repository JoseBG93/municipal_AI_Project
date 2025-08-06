# MEMORIA CONTEXTUAL COMPLETA - PROYECTO SISTEMA MUNICIPAL IA ALFAFAR

## 🎯 INFORMACIÓN BÁSICA DEL PROYECTO

### Usuario y contexto profesional:
- **Nombre**: José
- **Puesto**: Auxiliar administrativo interino - Departamento de Inspección Tributaria
- **Ayuntamiento**: Alfafar (provincia de Valencia, España)
- **Especialidad diaria**: IIVTNU (Incremento del Valor de los Terrenos de Naturaleza Urbana)
- **Experiencia**: Manejo diario de escrituras, herencias, donaciones, documentación notarial/judicial

### Objetivo del proyecto:
Sistema integral de automatización para procesamiento de documentos notariales y cálculo automático de impuestos municipales usando IA/ML/DL, eliminando procesamiento manual, reduciendo errores y acelerando trámites fiscales.

---

## 📚 CONTEXTO EXTRAÍDO DEL CHAT "@Qué es Docker Swarm"

### Metodología de trabajo establecida:
- **Responder cada cuestión por separado** hasta comprensión total antes de pasar a la siguiente
- **Profundizar en conceptos** hasta que el usuario confirme entendimiento completo
- **Permitir debate y exploración** de cada tema antes de avanzar
- **No hacer bloques de respuestas** - una pregunta, una respuesta completa

### Contexto temporal crítico:
- **OBLIGATORIO**: Verificar fecha actual (día y hora) antes de mencionar cualquier fecha en documentos
- **No establecer cronogramas rígidos** - proyecto a largo plazo sin fechas fijas, ya que no hay dedicación exclusiva a este proyecto.
- **José no se dedica únicamente a esto** - tiene limitaciones de tiempo

---

## 🏛️ RÉGIMEN TRIBUTARIO MUNICIPAL COMPLETO

### Impuestos municipales (TODOS):
- **IIVTNU** (Plusvalía municipal - especialidad diaria de José)
- **IBI** (Impuesto sobre Bienes Inmuebles)
- **IAE** (Impuesto sobre Actividades Económicas)
- **ICIO** (Impuesto sobre Construcciones, Instalaciones y Obras)
- **IVTM** (Impuesto sobre Vehículos de Tracción Mecánica)

### Tasas municipales (TODAS):
- Expedición documentos administrativos
- Suministro de agua, alcantarillado, basuras/residuos
- Cementerio municipal, servicios funerarios
- Vado permanente en vía pública
- Ocupación vía pública con mesas y sillas (terrazas)
- Licencias urbanísticas, actividades, obras menores
- Servicios deportivos municipales
- Vigilancia y control de espectáculos públicos
- Dejallería municipal, residencia asistida
- Y todas las demás figuras tributarias del Ayuntamiento de Alfafar

### Marco normativo aplicable:
- **LRHL** (Ley Reguladora de las Haciendas Locales) - norma principal
- **Ordenanzas fiscales del Ayuntamiento de Alfafar** - regulación específica
- **Normativa específica** de cada figura tributaria
- **RGPD, LOPDGDD, AI Act** - compliance obligatorio

### IMPORTANTE: 
**NO enfocar solo en IIVTNU** aunque sea la especialidad diaria de José. El sistema debe contemplar **TODO el régimen tributario municipal** en ejemplos, casos de uso y desarrollo.

---

## 📄 ESTADO ACTUAL DEL PROYECTO (1 AGOSTO 2025)

**NOTA**: Estado detallado actualizado automáticamente en Rule6-ProjectMemory.mdc
- **Progreso**: 9/13 archivos completados (69%)
- **Último completado**: 09_Procedimientos_Operativos.md
- **Próximo**: 10_Gestion_Incidentes.md

**REORGANIZACIÓN COMPLETADA**: 6 archivos .txt integrados en estructura optimizada:
- ✅ Sistema_RAG_Completo.md
- ✅ Contexto_Proyecto_Completo.md
- ✅ Colaboracion_Formacion.md
- ✅ 05_Medidas_Tecnicas_Organizativas.md (ampliado)
- ✅ 09_Procedimientos_Operativos.md (nuevo)

---

## 🐳 DOCKER SWARM - CONOCIMIENTO TÉCNICO COMPLETO

### Conceptos fundamentales dominados:
1. **Cluster**: Conjunto de servidores físicos/cloud coordinados
2. **Manager**: Mínimo 1, números impares si múltiples (1, 3, 5, 7) para evitar split-brain
3. **Workers**: Ejecutan contenedores asignados por Manager
4. **Réplicas**: Copias de un servicio específico, NO de docker-compose completo
5. **Balanceo**: Solo para NUEVAS requests, no redistribuye trabajo en curso
6. **Stateful vs Stateless**: Datos permanentes (postgres) vs operaciones temporales (document_processor)
7. **Split-brain**: Problema de múltiples managers pares tomando decisiones contradictorias

### Arquitectura Docker Swarm municipal acordada:
- **Configuración óptima para Alfafar**: 1 Manager+Worker + 1 Worker (2 servidores físicos)
- **Distribución automática**: Manager asigna contenedores según carga/restricciones
- **Escalado manual**: Usuario decide número de réplicas, Manager las distribuye
- **Alta disponibilidad**: Tolerancia a fallos de hardware/servicios individuales

### Segregación por sensibilidad datos (arquitectura híbrida):
- **🔴 NIVEL CRÍTICO (On-Premise)**: DNI, escrituras originales, valores reales, referencias catastrales
- **🟡 NIVEL MEDIO (Cloud UE)**: Datos anonimizados para IA/OCR, procesamiento ML
- **🟢 NIVEL PÚBLICO (Cloud Global)**: Servicios ciudadanos sin datos sensibles

---

## 🛠️ STACK TECNOLÓGICO DEL PROYECTO

### Microservicios principales:
- **document_processor**: OCR + extracción datos (Tesseract + Custom NER)
- **tax_calculator**: Cálculos automáticos impuestos/tasas (todas las figuras tributarias)
- **integration_layer**: Conectores GTT/Gestiona + APIs municipales
- **web_interface**: Frontend administrativo + portal ciudadano

### Tecnologías clave:
- **Backend**: Python + FastAPI + Celery (async processing)
- **Base de datos**: PostgreSQL + Redis cache
- **IA/ML**: spaCy, BERT fine-tuned, OpenAI LLMs
- **Contenedores**: Docker + Docker Swarm
- **Frontend**: Django Admin + Bootstrap + htmx
- **Seguridad**: Cifrado AES-256, certificados X.509, HSM

---

## ⚖️ COMPLIANCE Y ASPECTOS LEGALES CRÍTICOS

### Principios no negociables:
1. **Base legal específica** para cada uso IA
2. **Supervisión humana** en decisiones relevantes (sanciones >300€)
3. **Transparencia activa** hacia ciudadanos
4. **Minimización datos** estricta
5. **Auditabilidad completa** de decisiones
6. **Reversibilidad** todas las decisiones automatizadas
7. **Explicabilidad** comprensible para ciudadanos y funcionarios
8. **Seguridad by design** extremo a extremo

### Problemas identificados por José:
- **Resistencias internas**: "Excusa protección datos para no cambiar"
- **Falta formación**: Funcionarios necesitan capacitación IA
- **Miedo al cambio**: Por conveniencia o desconocimiento
- **Necesidad enfoque estratégico**: No solo defenderse → ATACAR con datos y casos de éxito

---

## 📋 TAREAS Y PROCESOS A AUTOMATIZAR

### Documentación tributaria:
- **Escrituras compraventa, herencias, donaciones** (principalmente)
- **Documentos judiciales/notariales** diversos
- **Autoliquidaciones** ciudadanos
- **Declaraciones actividades económicas**

### Extracción datos clave:
- **Identificación personas**: DNI, nombres, direcciones fiscales
- **Datos inmuebles**: Referencias catastrales, superficies, valores, ubicaciones
- **Importes económicos**: Precios transmisión, valoraciones, bases imponibles
- **Fechas relevantes**: Otorgamiento, transmisión, inicio actividades
- **Conceptos tributarios**: Bonificaciones, exenciones, tipos gravamen

### Integración sistemas municipales:
- **GTT** (gestión tributaria) - sistema principal trabajo diario
- **Gestiona** (registro y tramitación)
- **Bases catastrales** - verificación cruzada datos
- **Correos.es** - PEE (Pruebas Entrega Electrónica)

### Cálculos automáticos todas las figuras:
- **IIVTNU**: Incrementos valor, coeficientes actualización, liquidaciones
- **IBI**: Valores catastrales, bonificaciones, cuotas anuales
- **IAE**: Epígrafes, tarifas, reducciones actividades
- **ICIO**: Presupuestos obra, tipos gravamen, licencias
- **IVTM**: Potencias fiscales, antigüedad vehículos, exenciones
- **Tasas**: Ocupaciones vía pública, servicios municipales, tasas específicas

---

## 🎯 OBJETIVOS Y MÉTRICAS ESPERADAS

### Impacto operativo:
- **Reducción 90%** tiempo procesamiento documentos
- **Precisión >95%** en extracción de datos
- **Ahorro 80%** costes administrativos
- **Incremento 300%** productividad funcionarios
- **Reducción 95%** errores humanos

### Beneficios ciudadanos:
- **Trámites más rápidos** - menos tiempo espera
- **Mayor precisión** - menos errores liquidaciones
- **Transparencia algoritmos** - comprensión decisiones automatizadas
- **Portal autoservicio** - consultas 24/7

---

## 💡 LECCIONES APRENDIDAS Y CONFIGURACIONES CLAVE

### Comportamiento del asistente:
- **Una pregunta → una respuesta completa**
- **Confirmar comprensión antes de avanzar**
- **Incluir ejemplos de TODAS las figuras tributarias**
- **No cronogramas rígidos - José va a su ritmo**
- **Enfoque realista - administración pública real**

### Aspectos técnicos críticos:
- **Docker Swarm NO maneja docker-compose como unidades** - maneja servicios individuales
- **Manager distribuye contenedores**, no "Docker Composes completos"
- **Números pares de managers = problemático** (split-brain)
- **Redis = cache temporal**, no backup permanente
- **Stateful services = 1 réplica típicamente** (complejidad sincronización)

### Contexto municipal real:
- **Ayuntamiento Alfafar** - características específicas municipio valenciano
- **Época declaraciones** - picos demanda estacionales
- **Personal limitado** - 2 funcionarios técnicos
- **Presupuesto controlado** - soluciones coste-efectivas
- **Normativa estricta** - compliance obligatorio desde día 1

---

## 🔄 INSTRUCCIONES PARA PRÓXIMOS CHATS

### PROTOCOLO AL INICIAR NUEVO CHAT:
**NOTA**: Protocolo detallado está automatizado en Rule6-ProjectMemory.mdc
1. **Verificar fecha/hora** → **Revisar estado proyecto** → **Proceder con trabajo**
2. **Metodología**: Respuestas separadas hasta comprensión total
3. **Enfoque**: TODO el régimen tributario municipal, no solo IIVTNU

### Configuración específica aplicar:
- **Lenguaje**: Español, terminología administrativa española
- **Ejemplos**: Siempre incluir múltiples figuras tributarias
- **Analogías**: Usar contexto funcionario público cuando sea útil
- **Profundidad**: Explorar conceptos hasta comprensión total confirmada
- **Realismo**: Considerar limitaciones administrativas reales

---

**📅 Memoria actualizada**: 1 agosto 2025, 11:00h  
**🔄 Estado actual**: Ver Rule6-ProjectMemory.mdc (actualizado automáticamente)
**📧 Responsable**: José - Inspección Tributaria Alfafar  
**🎯 Versión**: 1.1 - Optimizada sin redundancias con Rule6