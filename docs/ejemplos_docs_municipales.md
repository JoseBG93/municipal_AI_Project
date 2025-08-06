# 📋 Ejemplos de Documentos Municipales Disponibles

## 🎯 Ubicación Principal
**Carpeta:** `data/mcp_json/`

---

## 🏛️ Ejemplos Principales (Completos y Detallados)

### 🏠 COMPRAVENTA
**Archivo:** `compraventa.json` (103 líneas, 3.4 KB)

**Características:**
- Estructura MCP completa para escritura de compraventa
- Incluye datos de comprador, vendedor, inmueble
- Cálculo automático de IIVTNU
- Validaciones fiscales y referencias catastrales
- Metadatos de procesamiento y confianza

### 👥 HERENCIA MÚLTIPLE  
**Archivo:** `herencia_multiple.json` (193 líneas, 5.2 KB)

**Características:**
- Herencia con 3 herederos (33.33% cada uno)
- Cálculo proporcional del ISD
- Inventario completo de bienes (inmueble, cuenta bancaria, vehículo)
- Cargas y deudas (hipoteca, gastos funerarios)
- Reducciones por parentesco directo
- Validaciones de reparto y plazos

### 🎁 DONACIÓN EXENTA
**Archivo:** `donacion_exenta.json` (165 líneas, 5.0 KB)

**Características:** 
- Donación entre familiares (padre → hija)
- Exención total de ISD por reducciones familiares
- Consentimiento conyugal incluido
- Validación automática de no sujeción a IIVTNU
- Documentación complementaria requerida
- Alertas de plazos y obligaciones formales

---

## 🔄 Ejemplos Sintéticos (Datos de Prueba)

### 📊 Distribución Equilibrada por Tipos
```
📄 30 archivos sintéticos con nomenclatura clara:
  🏠 10 compraventas (compraventa_001.json a compraventa_010.json)
  🎁 10 donaciones (donacion_001.json a donacion_010.json)
  👥 10 herencias (herencia_001.json a herencia_010.json)
```

### 🎲 Características de Datos Sintéticos
- **Nombres completos españoles:** Juan Pérez García, María González López, etc.
- **Direcciones de Alfafar:** Calle Mayor, Avenida Valencia, Plaza España, etc.
- **Valores variables:** Inmuebles de 40.000€ a 300.000€
- **NIFs españoles:** Formato válido con letra final
- **Referencias catastrales:** Formato español oficial
- **Fechas diversas:** Últimos 12 meses
- **Estructura consistente:** Acorde a ejemplos principales

---

## 🛠️ Generación de Nuevos Ejemplos

### Comando Rápido
```bash
# Generar 30 ejemplos sintéticos (10 de cada tipo)
python3 scripts/generate_synthetic_data.py

# Ver archivos generados por tipo
ls data/mcp_json/compraventa_*.json | wc -l  # Compraventas
ls data/mcp_json/donacion_*.json | wc -l     # Donaciones  
ls data/mcp_json/herencia_*.json | wc -l     # Herencias

# Ver contenido de un ejemplo
cat data/mcp_json/compraventa_001.json
```

### Script Mejorado
El script `generate_synthetic_data.py` ahora incluye:
- **Generación equilibrada:** Exactamente 10 de cada tipo
- **Nomenclatura clara:** Nombres que identifican el tipo de documento
- **Formato español:** NIFs, direcciones y referencias catastrales españolas
- **Estructura consistente:** Coherente con ejemplos principales
- **Datos realistas:** Nombres completos y direcciones de Alfafar

---

## 📋 Estructura Detallada por Tipo

### 🏠 Compraventa
**Campos principales:**
- `comprador` / `vendedor` (nombre, NIF, domicilio)
- `inmueble` (dirección, referencia catastral, valores)
- `compraventa_actual` / `compraventa_anterior`
- `calculo_iivtnu` (base imponible, cuota)
- `reglas_validacion` (incremento valor, plazos)

### 👥 Herencia
**Campos principales:**
- `causante` (datos del fallecido)
- `herederos[]` (múltiples herederos con porcentajes)
- `bienes_heredados[]` (inmuebles, cuentas, vehículos)
- `cargas_y_deudas[]` (hipotecas, gastos)
- `calculo_isd` (por heredero individual)
- `masa_hereditaria` (activo bruto/neto)

### 🎁 Donación
**Campos principales:**
- `donante` / `donatario` (con parentesco)
- `conyuge_donante` (consentimiento si aplica)
- `inmueble_donado` (descripción completa)
- `condiciones_donacion` (tipo, reservas, aceptación)
- `calculo_isd` (con reducciones familiares)
- `obligaciones_formales` (plazos, comunicaciones)

---

## 🔍 Comandos de Consulta

### Ver Contenido de Ejemplos
```bash
# Ver ejemplo completo de compraventa
cat data/mcp_json/compraventa.json

# Ver ejemplo completo de herencia
cat data/mcp_json/herencia_multiple.json

# Ver ejemplo completo de donación  
cat data/mcp_json/donacion_exenta.json
```

### Análisis de Campos
```bash
# Ver solo campos principales de un tipo
jq '.tipo_documento, .fecha_documento, .metadatos' data/mcp_json/herencia_multiple.json

# Contar herederos en herencia
jq '.herederos | length' data/mcp_json/herencia_multiple.json

# Ver reducciones en donación
jq '.calculo_isd.reducciones_aplicables' data/mcp_json/donacion_exenta.json
```

### Búsqueda en Contenido
```bash
# Buscar documentos por tipo
grep -l '"tipo_documento": "herencia"' data/mcp_json/*.json

# Buscar por valor monetario
grep -l '"valor_real": [0-9]*[0-9]{5,}' data/mcp_json/*.json
```

---

## 📈 Estadísticas Actuales

- **✅ 3 tipos principales completos:** Compraventa, Herencia, Donación
- **✅ 30 ejemplos sintéticos equilibrados:** 10 de cada tipo con nomenclatura clara
- **✅ 33 archivos JSON totales:** Cobertura completa de casos de uso
- **✅ Nomenclatura descriptiva:** Nombres que identifican claramente el tipo
- **✅ Formato español completo:** NIFs, direcciones y referencias españolas
- **✅ Generación automática:** Script optimizado para crear distribución equilibrada

---

**💡 Nota:** Todos los ejemplos incluyen metadatos de procesamiento, niveles de confianza y trazabilidad completa para uso en el sistema municipal AI. 