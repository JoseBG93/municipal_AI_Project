# Lógica del usuario optimizada (sin redundancias)
# ================================================

# Target principal optimizado
deploy: package backup
	@echo "🚀 Desplegando aplicación verificada y respaldada..."

# Cadena de dependencias optimizada
backup: package
	@echo "💾 Respaldando paquete final..."

package: test
	@echo "📦 Empaquetando aplicación testeada..."

test: build
	@echo "🧪 Testeando aplicación construida..."

build: install-deps
	@echo "🔨 Construyendo con dependencias..."

install-deps:
	@echo "📦 Instalando dependencias base..."

.PHONY: deploy backup package test build install-deps 