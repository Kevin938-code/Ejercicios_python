"""Clase RegistroNotas que: 
(1) tenga método registrar(estudiante, nota) que guarde en un diccionario; 
(2) tenga método estudiantes_aprobados(nota_minima) que retorne lista de estudiantes; 
(3) tenga método mejor_estudiante() que retorne nombre y nota del que tiene mayor calificación."""
class RegistroNotas:
    def __init__(self):
        self.estudiantes = {}

    def registrar(self, estudiante, nota):
        self.estudiantes[estudiante] = nota
    
    def estudiantes_aprobados(self, nota_minima):
        return [nombre for nombre, nota in self.estudiantes.items() if nota >= nota_minima]
    
    def mejor_estudiante(self):
        nombre = max(self.estudiantes, key=self.estudiantes.get)
        return (nombre, self.estudiantes[nombre])
registro = RegistroNotas()
registro.registrar("juan",80)
registro.registrar("adrian",65)
print(registro.mejor_estudiante())
