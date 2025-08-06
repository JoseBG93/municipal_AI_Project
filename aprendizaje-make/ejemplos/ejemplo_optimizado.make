# Estructura optimizada (sin problemas)
# ====================================

# Target principal con dependencias limpias
deploy: test package backup
	@echo "🚀 Desplegando..."

# Targets con dependencias lógicas
backup: test
	@echo "💾 Respaldando..."

package: build
	@echo "📦 Empaquetando..."

test: build
	@echo "🧪 Testeando..."

build: install-deps
	@echo "🔨 Construyendo..."

install-deps:
	@echo "📦 Instalando dependencias..."

.PHONY: deploy build install-deps test package backup 