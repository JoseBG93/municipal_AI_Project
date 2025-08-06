# Lógica propuesta por el usuario
# ================================

# Target principal como lo propones
deploy: test package
	@echo "🚀 Desplegando aplicación verificada..."

# Tu lógica de dependencias
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