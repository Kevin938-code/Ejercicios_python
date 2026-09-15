"""Clase GestorPersonas que: 
(1) tenga método agregar_persona(nombre, edad) que guarde en un diccionario; 
(2) tenga método personas_mayores(edad_minima) que retorne una lista de nombres cuya edad sea ≥; 
(3) tenga método edad_promedio() que retorne el promedio de edades."""
class GestionarPersonas :
    def __init__(self):
        self.personas = {}
    
    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad
        
    def personas_mayores(self, edad_minima):
        return [nombre for nombre, edad in self.personas.items() if edad >= edad_minima]
    
    def edad_promedio(self):
        return sum(self.personas.values()) / len(self.personas)
    
gestion = GestionarPersonas()
gestion.agregar_persona("jose", 23)
gestion.agregar_persona("kevin", 18)
gestion.agregar_persona("kathy", 35)
print(gestion.personas_mayores(20))
print(gestion.edad_promedio())