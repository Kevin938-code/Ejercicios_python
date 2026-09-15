"""Clase Tareas que: 
(1) tenga método agregar_tarea(descripcion, prioridad) que guarde en una lista de tuplas (descripción, prioridad); 
(2) tenga método tareas_prioritarias() que retorne solo las de prioridad alta; 
(3) tenga método eliminar_completada(descripcion) que borre la tarea de la lista."""
class Tareas:
    def __init__(self):
        self.lista_tuplas = []
        
    def agregar_tarea(self, descripcion, prioridad):
        self.lista_tuplas.append((descripcion, prioridad))
        
    def tareas_prioritarias(self):
        return [tarea for tarea in self.lista_tuplas if tarea[1] == "alta"]
        
    def eliminar_completada(self, descripcion):
        for tarea in self.lista_tuplas:
            if tarea[0] == descripcion:
                self.lista_tuplas.remove(tarea)
                break
actividad = Tareas()
actividad.agregar_tarea("estudiar", "alta")
actividad.agregar_tarea("ejercitarse", "alta")
actividad.agregar_tarea("barrer", "media")
actividad.agregar_tarea("jugar", "baja")
print(actividad.lista_tuplas)
actividad.eliminar_completada("ejercitarse")
print(actividad.tareas_prioritarias())
print(actividad.lista_tuplas)