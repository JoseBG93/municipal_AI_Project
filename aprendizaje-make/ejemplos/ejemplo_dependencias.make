# Ejemplo de dependencias en cadena
# =====================================

# Variables
APP_NAME := mi-app
BUILD_DIR := build

# Target final que depende de varios pasos
deploy: build test package
	@echo "🚀 Desplegando $(APP_NAME)..."
	@echo "✅ Despliegue completado"

# Construir la aplicación  
build: install-deps
	@echo "🔨 Construyendo $(APP_NAME)..."
	@mkdir -p $(BUILD_DIR)
	@echo "const app = 'Hello World';" > $(BUILD_DIR)/app.js

# Instalar dependencias
install-deps:
	@echo "📦 Instalando dependencias..."
	@echo "- react@18.0.0"
	@echo "- express@4.18.0"

# Ejecutar tests
test: build
	@echo "🧪 Ejecutando tests..."
	@echo "✅ Todos los tests pasaron"

# Empaquetar aplicación
package: build
	@echo "📦 Empaquetando aplicación..."
	@echo "✅ Paquete creado en $(BUILD_DIR)/package.zip"

# Limpiar archivos
clean:
	@echo "🧹 Limpiando archivos temporales..."
	@rm -rf $(BUILD_DIR)

.PHONY: deploy build install-deps test package clean 