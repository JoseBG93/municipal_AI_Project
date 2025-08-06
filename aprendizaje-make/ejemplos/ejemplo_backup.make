# Ejemplo con backup incluido
# ===========================

# Target principal modificado
deploy: build test package backup
	@echo "🚀 Desplegando con respaldo..."
	@echo "✅ Despliegue completado"

# Targets originales
build: install-deps
	@echo "🔨 Construyendo app..."

install-deps:
	@echo "📦 Instalando dependencias..."

test: build
	@echo "🧪 Ejecutando tests..."

package: build
	@echo "📦 Empaquetando aplicación..."

# Nuevo target backup
backup: test
	@echo "💾 Creando respaldo..."
	@echo "✅ Respaldo completado"

.PHONY: deploy build install-deps test package backup 