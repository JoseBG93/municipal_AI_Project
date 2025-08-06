# Tu estructura original (con problemas)
# =====================================

# Dependencias como las escribiste
deploy: build install-deps test package
	@echo "🚀 Desplegando..."

package: test
	@echo "📦 Empaquetando..."

backup: test
	@echo "💾 Respaldando..."

# Targets base
build: install-deps
	@echo "🔨 Construyendo..."

install-deps:
	@echo "📦 Instalando dependencias..."

test: build
	@echo "🧪 Testeando..."

# Duplicación (Make usará solo esta última definición)
backup: test
	@echo "💾 Respaldando (definición duplicada)..."

.PHONY: deploy build install-deps test package backup 