"""Clase Equipos que: 
(1) tenga método crear_equipo(nombre_equipo) que inicie un equipo como una lista vacía en un diccionario; 
(2) tenga método agregar_jugador(equipo, jugador) que añada el jugador al equipo; 
(3) tenga método equipo_mayor_integrantes() que retorne el nombre del equipo con más jugadores."""
class Equipos:
    def __init__(self):
        self.equipos = {}
    
    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []
    
    def agregar_jugador(self, equipo, jugador):
        self.equipos[equipo].append(jugador)
        
    def equipo_mayor_integrantes(self):
        return max(self.equipos, key=lambda equipo: len(self.equipos[equipo]))
    
eq = Equipos()
eq.crear_equipo("A")
eq.crear_equipo("B")
eq.agregar_jugador("A","Jose")
eq.agregar_jugador("B","adrian")
eq.agregar_jugador("A","anthony")
eq.agregar_jugador("A","alex")
print(eq.equipos)
print(eq.equipo_mayor_integrantes())

print("---------------------------------------------------------------")

"""Ejercicio: GestorCursos
Crea una clase llamada GestorCursos que permita administrar cursos y sus estudiantes.
    1. Método crear_curso(nombre_curso)
Debe crear un nuevo curso dentro de un diccionario, y cada curso debe comenzar con una lista vacía de estudiantes.
    2. Método agregar_estudiante(curso, estudiante)
Debe recibir:
El nombre del curso.
El nombre del estudiante.
Y debe agregar el estudiante a la lista correspondiente al curso.
La idea importante es que tendrás que acceder a una lista que está dentro de un diccionario y utilizar append().
    3. Método curso_mayor_estudiantes()
Debe recorrer todos los cursos y retornar el nombre del curso que tenga más estudiantes.
"""
class GestorCursos:
    def __init__(self):
        self.cursos = {}

    def crear_curso(self,nombre_curso):
        self.cursos[nombre_curso] = []

    def agregar_estudiante(self, curso, estudiante):
        self.cursos[curso].append(estudiante)
    
    def curso_mayor_estudiantes(self):
        mayor_estudiantes = None
        cantidad = 0
        
        for curso, estudiante in self.cursos.items():
            if len(estudiante) > cantidad:
                mayor_estudiantes = curso
                cantidad = len(estudiante)
        return mayor_estudiantes

gestor = GestorCursos()
gestor.crear_curso("software")
gestor.crear_curso("industrial")
gestor.crear_curso("bio-tecnologia")
gestor.agregar_estudiante("software","andres")
gestor.agregar_estudiante("software","julio")
gestor.agregar_estudiante("industrial","axel")
gestor.agregar_estudiante("bio-tecnologia","fernando")
print(gestor.cursos)
print(gestor.curso_mayor_estudiantes())