# Estructura final elegida por el usuario (paralela)
# ==================================================

# Deploy después de package y backup (pueden ser paralelos)
deploy: package backup
	@echo "🚀 Desplegando con paquete y respaldo listos..."

# Backup del paquete final
backup: package
	@echo "💾 Respaldando paquete final..."

# Empaquetar después de testear
package: test
	@echo "📦 Empaquetando aplicación testeada..."

# Testear después de construir
test: build
	@echo "🧪 Testeando aplicación construida..."

# Construir con dependencias
build: install-deps
	@echo "🔨 Construyendo con dependencias..."

# Punto de partida
install-deps:
	@echo "📦 Instalando dependencias base..."

.PHONY: deploy backup package test build install-deps 