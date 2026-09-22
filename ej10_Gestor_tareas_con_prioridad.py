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

print("--------------------------------------------------------")
"""Ejercicio: Clase Peliculas

Crea una clase llamada Peliculas que:

(1) Método agregar_pelicula(nombre, genero)

Debe guardar cada película en una lista de tuplas con esta estructura:
(nombre, genero)
2) Método peliculas_accion()

Debe retornar solamente los nombres de las películas cuyo género sea "accion".
(3) Método eliminar_pelicula(nombre)

Debe recibir el nombre de una película y eliminar de la lista la tupla correspondiente.
"""
class ClasePeliculas:
    def __init__(self):
        self.lista_tuplas = []
        
    def agregar_pelicula(self, nombre,genero):
        self.lista_tuplas.append((nombre, genero))
        
    def peliculas_accion(self):
        accion=[]
        for pelicula in self.lista_tuplas:
            if pelicula[1] == "accion":
                accion.append(pelicula[0])
        return accion
    
    def eliminar_pelicula(self, nombre):
        for pelicula in self.lista_tuplas:
            if pelicula[0] == nombre:
                self.lista_tuplas.remove(pelicula)
        return self.lista_tuplas

clases = ClasePeliculas()
clases.agregar_pelicula("superman","accion")
clases.agregar_pelicula("127 horas","drama")
clases.agregar_pelicula("it","terror")
print(clases.lista_tuplas)
print(clases.eliminar_pelicula("superman"))