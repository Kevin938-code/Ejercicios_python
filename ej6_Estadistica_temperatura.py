"""Clase GestorTemperatura que: 
(1) tenga método registrar_temperatura(temp) que guarde en una lista; 
(2) tenga método minima()`, `maxima()`, `promedio() que calculen estadísticas; 
(3) tenga método registrar_multiples(*temps) que reutilice el registro para varias temperaturas."""
class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def minimo(self):
        return min(self.temperaturas)
    
    def maximo(self):
        return max(self.temperaturas)
    
    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)
    
    def registrar_multiples(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)

gestion = GestorTemperatura()
gestion.registrar_multiples(20, 18, 30, 25)
print(f"minimo: {gestion.minimo()}, maximo: {gestion.maximo()}")
print(f"promedio: {gestion.promedio()}")

print("-------------------------------------------------------------")

"""Ejercicio: GestorCalificaciones
Crea una clase llamada GestorCalificaciones que permita registrar y analizar calificaciones de estudiantes.
    1. Método registrar_calificacion(nota)
Debe recibir una calificación y guardarla en una lista interna.
    2. Método nota_minima()
Debe retornar la calificación más baja de todas las almacenadas.
    3. Método nota_maxima()
Debe retornar la calificación más alta almacenada.
    4. Método promedio()
Debe calcular el promedio de todas las calificaciones almacenadas.
También debes pensar qué debería ocurrir si todavía no hay ninguna calificación registrada, para evitar una división entre cero.
    5. Método registrar_multiples(*notas)
Debe recibir varias calificaciones
y debe registrar cada una reutilizando registrar_calificacion().
"""
class GestorCalificaciones:
    def __init__(self):
        self.calificaciones = []

    def registrar_calificacion(self, nota):
        self.calificaciones.append(nota)

    def nota_minima(self):
        if self.calificaciones:
            return min(self.calificaciones)
        else:
            return 0

    def nota_maxima(self):
        if self.calificaciones:
            return max(self.calificaciones)
        else:
            return 0

    def promedio(self):
        if self.calificaciones:
            return sum(self.calificaciones) / len(self.calificaciones)
        else:
            return 0

    def registrar_multiples(self, *notas):
        for nota in notas:
            self.registrar_calificacion(nota)

gestion = GestorCalificaciones()
gestion.registrar_calificacion(20)
gestion.registrar_multiples(10,20,30,40,50)
print(gestion.calificaciones)
print(gestion.nota_maxima())
print(gestion.nota_minima())
print(gestion.promedio())
