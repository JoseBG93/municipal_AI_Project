# Ejemplo de paralelización en Make
# ==================================

# Target principal con tareas independientes
all: tarea-a tarea-b tarea-c
	@echo "🎉 Todas las tareas completadas"

# Tareas independientes (pueden ejecutarse en paralelo)
tarea-a:
	@echo "🔵 Iniciando tarea A..."
	@sleep 2
	@echo "✅ Tarea A completada"

tarea-b:
	@echo "🟢 Iniciando tarea B..."
	@sleep 2  
	@echo "✅ Tarea B completada"

tarea-c:
	@echo "🟡 Iniciando tarea C..."
	@sleep 2
	@echo "✅ Tarea C completada"

# Comparación: tareas secuenciales
secuencial: tarea-x
	@echo "🎯 Secuencial completado"

tarea-x: tarea-y
	@echo "🔴 Tarea X (depende de Y)"

tarea-y: tarea-z  
	@echo "🟠 Tarea Y (depende de Z)"

tarea-z:
	@echo "🟣 Tarea Z (independiente)"

.PHONY: all tarea-a tarea-b tarea-c secuencial tarea-x tarea-y tarea-z 