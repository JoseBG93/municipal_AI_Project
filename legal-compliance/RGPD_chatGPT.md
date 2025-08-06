# Cumplimiento Normativo: IA y Cloud Computing en Administración Municipal (Versión Ampliada)

## 📋 Objetivo del documento

Este archivo establece las directrices legales, técnicas y éticas para implementar el **Sistema Municipal de IA** del Ayuntamiento de Alfafar, asegurando el cumplimiento de la normativa vigente de protección de datos, derechos digitales y seguridad de la información.

---

## 🇪🇺 MARCO NORMATIVO APLICABLE

### **1. Normativa Europea**

* **RGPD (Reglamento General de Protección de Datos)** – Reglamento (UE) 2016/679. Incluye el Mecanismo de Coherencia (art. 63) y las directrices del Comité Europeo de Protección de Datos (EDPB) sobre perfilado, consentimiento y evaluaciones de impacto.
* **Directiva ePrivacy** – Directiva 2002/58/CE sobre confidencialidad en comunicaciones electrónicas. En proceso de reemplazo por un futuro Reglamento ePrivacy; revisar el estado en el Diario Oficial y guías de la Comisión Europea.
* **Reglamento de IA de la UE (AI Act)** – Aprobado en 2024, con entrada en vigor progresiva hasta agosto de 2026. Introduce clasificación por riesgo, requisitos de evaluación de conformidad y obligaciones de post‑market monitoring.
* **Reglamentos Digitales Adicionales**:

  * **DSA/DMA (Digital Services/Markets Acts)** – Transparencia de algoritmos en grandes plataformas.
  * **DGA (Data Governance Act)** – Gobernanza de intercambios de datos.
  * **Directiva 2019/1024** – Reutilización de datos del sector público (Open Data).

### **2. Normativa Nacional (España)**

* **LOPDGDD** – Ley Orgánica 3/2018 de Protección de Datos Personales y garantía de derechos digitales. Complementa el RGPD con derechos digitales (neutralidad, desconexión, testamento digital) y regula menores, honor de fallecidos y no discriminación algorítmica.
* **Ley 39/2015** – Procedimiento Administrativo Común. Obliga a la administración electrónica, registro y notificaciones digitales.
* **Ley 40/2015** – Régimen Jurídico del Sector Público. Define la "actuación administrativa automatizada" (art. 41) y designa responsabilidades sobre programación, supervisión y firma electrónica de actos automatizados.
* **Real Decreto 311/2022 (ENS)** – Esquema Nacional de Seguridad. Actualiza requisitos de seguridad para sistemas de información de la administración (niveles básico, medio y alto).
* **Ley 7/1985** – Bases del Régimen Local. Marco general de competencias municipales.

### **3. Normativa Sectorial Municipal**

* **Normativas Autonómicas** (Comunidad Valenciana):

  * **Decreto 90/2013** – Administración electrónica valenciana.
  * **Ley 13/2010 de Transparencia Valenciana** – Acceso a la información y obligaciones de publicidad activa.
  * **Orden 2/2019** – Estándares técnicos de interoperabilidad autonómica.

---

## 🎯 PRINCIPIOS FUNDAMENTALES A CUMPLIR

1. **Minimización de datos**: recopilar solo los datos estrictamente necesarios para la finalidad prevista. Implementar seudonimización o anonimización cuando sea posible.
2. **Limitación de finalidad**: usos específicos y documentados; evitar reutilizaciones no previstas.
3. **Transparencia y lealtad**: información clara y accesible (política de privacidad, portal IA). Derechos de acceso, rectificación, supresión, oposición, portabilidad y limitación.
4. **Responsabilidad proactiva (Accountability)**: registro de actividades, evaluaciones de impacto (EIPD), auditorías internas, plan de cumplimiento.
5. **Integridad y confidencialidad**: aplicación de medidas técnicas (cifrado AES‑256 en reposo, TLS 1.3 en tránsito) y organizativas (control de accesos, políticas de gestión de claves).
6. **Privacidad desde el diseño y por defecto (Privacy by Design & Default)**: arquitecturas y procesos pensados para proteger datos desde el primer boceto.
7. **Calidad de los datos**: garantizar exactitud, actualización y relevancia.

---

## 🏛️ ARQUITECTURA TÉCNICA CONFORME

### **Clasificación de datos por sensibilidad**

| Nivel      | Tipología                                                                        | Medidas principales                                               |
| ---------- | -------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| 🔴 Crítico | Identificativos (DNI, NIE), tributarios, biográficos, expedientes sancionadores. | On‑premise, cifrado FIPS 140‑2, HSM para gestión de claves.       |
| 🟡 Medio   | Documentos anonimizados, logs agregados, métricas estadísticas.                  | Nube UE con contrato CPT, anonimización previa, ARMored networks. |
| 🟢 Bajo    | Contenidos públicos (web municipal), APIs de consulta general.                   | Cloud público, API gateway, WAF, límites de rate, políticas CORS. |

### **Componentes y buenas prácticas**

* **Pseudonimización**: sustituir identificadores directos por códigos, manteniendo mapeo en entorno seguro.
* **Gestión de claves**: ciclo de vida en HSM, rotación periódica, backups seguros.
* **Segmentación de red**: DMZ para front‑end, VLANs separadas para datos críticos, IPS/IDS.
* **SDLC seguro**: análisis de dependencias, escaneo de contenedores (Clair/Trivy), code review, testing de vulnerabilidades.
* **Monitorización**: SIEM unificado (Elasticsearch/Kibana + Beats), alertas en tiempo real para accesos anómalos.

---

## 📝 DOCUMENTACIÓN OBLIGATORIA

1. **Registro de Actividades de Tratamiento (RGPD Art. 30)**

   * Incluir descripción de flujos de datos, finalidad, categorías, plazos de conservación (art. 5.1.e), cesiones y transfers.
   * Utilizar plantilla AEPD y adjuntar mapa de datos.
2. **Evaluación de Impacto (EIPD, RGPD Art. 35)**

   * Obligatoria para IA, perfilado, datos sensibles o a gran escala.
   * Utilizar herramienta CCN‑CERT o AEPD “Evalúa Riesgos IA”.
3. **Análisis de Legitimación**

   * Detallar bases legales (art. 6 RGPD y art. 9 si aplica datos especiales).
   * Citar Ley 58/2003 (General Tributaria) para OCR documental.
   * Especificar normas municipales/ordenanzas que habiliten tratamientos.
4. **Políticas internas**

   * Política de acceso y control de privilegios.
   * Procedimiento de gestión de consentimientos.
   * Plan de formación y concienciación.

---

## 🔒 MEDIDAS TÉCNICAS OBLIGATORIAS

1. **Seguridad by Design**: cifrado extremo a extremo, gestión segura de secretos (Vault), contenedores inmutables.
2. **Auditoría y Logs**: retención mínima 6 años, anonimización de IPs en logs, SIEM con alertas escalables.
3. **Control de Accesos**: RBAC/ABAC, federación eIDAS para funcionarios, MFA obligatorio.
4. **Gestión de Vulnerabilidades**: parcheo automático, escaneo semanal, programa de bug bounty interno.

---

## ⚖️ DERECHOS DE LOS CIUDADANOS

1. **Acceso (Art. 15)**: API REST con paginación, logs de consultas.
2. **Rectificación (Art. 16)**: workflow con aprobación y notificación a terceros sistemas.
3. **Supresión (Art. 17)**: flujos de borrado en cascada, validación DPO.
4. **Limitación (Art. 18)**: marcar datos en estado “retención limitada”.
5. **Portabilidad (Art. 20)**: export en formatos estándar JSON/XML.
6. **Oposición y derecho a no perfilado (Art. 21 y 22)**: formularios online con “switch humano” para revisión.
7. **Derecho de oposición a decisiones automatizadas**: gate de intervención humana y registro de solicitudes.

---

## 🌍 TRANSFERENCIAS INTERNACIONALES

* **Schrems II (C‑311/18)**: aplicar SCC v4 y TIA según directrices del EDPB.
* **Proveedores UE**: Arsys, OVH, Hetzner.
* **Fuera UE**: AWS, Azure, GCP con SCC, cifrado de extremo a extremo y auditorías TIA.
* **Prohibiciones**: jurisdicciones sin adecuación ni SCC.

---

## 🤖 REGULACIÓN ESPECÍFICA DE IA (AI Act)

### **Clasificación de riesgos**

* **Alto riesgo**: detección de fraude tributario automática, scoring social, sistemas biométricos. Requiere CE marking, calidad de datos, pruebas de no discriminación.
* **Riesgo limitado**: chatbots, OCR, análisis de texto. Obligación de informar al interesado.
* **Mínimo riesgo**: filtros anti‑spam, IA en juegos. Sin requisitos adicionales.

### **Requisitos clave**

* Documentación técnica y registro de versiones (post‑market monitoring).
* Plan de actualización continua y gestión de sesgos.
* Evaluación de conformidad y auditorías de terceros.

---

## 📋 PROCEDIMIENTOS OPERATIVOS

### **Fases del proyecto**

1. **Meses 1-3**: análisis legal preliminar, Registro Art. 30, designación DPO.
2. **Meses 4-6**: infraestructura segura, cifrado, controles de acceso, logging.
3. **Meses 7-12**: despliegue IA con EIPD, pilotos internos, supervisión humana.
4. **Posterior**: auditorías externas, revisión legal cada 6 meses, actualización de EIPD.

### **Gestión de cambios**

* Control de versiones de modelos y pipelines.
* Entorno de pruebas aislado (sandbox) y protocolo de rollback.
* Comunicación interna y gestión de incidencias (ITIL).

---

## 🚨 GESTIÓN DE INCIDENTES

1. **Detección y clasificación**: MTTD < 2 h, MTTR < 24 h.
2. **Evaluación inicial**: checklist de riesgos y afectados.
3. **Notificación AEPD (72 h)**: formato CNIL/AEPD.
4. **Comunicación a ciudadanos**: plantilla estándar, canales múltiple.
5. **Informe post‑mortem**: lecciones aprendidas, KPIs.

---

## 📊 MÉTRICAS DE CUMPLIMIENTO

| Categoría  | Métrica                                | Objetivo         |
| ---------- | -------------------------------------- | ---------------- |
| Técnicas   | Disponibilidad de servicios            | > 99.5%          |
|            | Incidentes de seguridad críticos       | 0/año            |
| Legales    | EIPD completadas                       | 100% IA          |
|            | Contratos DPA firmados                 | 100% proveedores |
| Ciudadanos | Tiempo respuesta ejercicio derechos    | < 30 días        |
|            | Satisfacción transparencia (encuestas) | > 80%            |

---

## 🎓 FORMACIÓN OBLIGATORIA

1. **Funcionarios generales** (4 h/año): RGPD, derechos digitales, uso básico de IA.
2. **Técnicos TI** (12 h/año): Privacy by Design, seguridad cloud, auditoría de contenedores.
3. **DPO y responsables** (20 h/año): Jurisprudencia reciente, AI Act, EIPD avanzada.
4. **Certificaciones recomendadas**: CIPP/E, CIPM, ISO 27001 Lead Implementer.

---

## 💼 CONTACTOS Y RECURSOS

* **AEPD**: [www.aepd.es](http://www.aepd.es) | [dpo@ayuntamiento-alfafar.es](mailto:dpo@ayuntamiento-alfafar.es)
* **CCN‑CERT**: [ccn-cert@cni.es](mailto:ccn-cert@cni.es)
* **Plantillas AEPD/EIPD**: aepd.es/guias
* **Sala de Innovación Local**: sandbox municipal para IA.

---

## ✅ CONCLUSIONES Y RECOMENDACIONES

* **Viabilidad**: proyecto viable con mecanismos de privacidad y seguridad.
* **Estrategia**: adoptar Privacy by Design, supervisión humana y transparencia.
* **Revisión continua**: actualizar cada 6 meses y tras cambios legales.
* **Implicación ciudadana**: portal de transparencia IA y feedback ciudadano.

---

*Última actualización: Julio 2025. Próxima revisión: Enero 2026.*
