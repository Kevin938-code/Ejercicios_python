"""Clase ContadorFrecuencia que: 
(1) tenga método agregar_elemento(elemento) que guarde en un diccionario contando repeticiones; 
(2) tenga método elemento_mas_frecuente() que retorne el elemento con mayor frecuencia; 
(3) tenga método frecuencia_elemento(elemento) que retorne cuántas veces aparece."""
class ContadorFrecuencia:
    def __init__(self):
        self.contador = {}
    
    def agregar_elemento(self, elemento):
        self.contador[elemento] = self.contador.get(elemento, 0) + 1
    
    def elemento_mas_frecuente(self):
        return max(self.contador, key=self.contador.get)
    
    def frecuencia_elemento(self, elemento):
        return self.contador.get(elemento, 0)
    
contar  = ContadorFrecuencia()
contar.agregar_elemento("a")
contar.agregar_elemento("b")
contar.agregar_elemento("a")
print(contar.contador)
print(contar.elemento_mas_frecuente())

print("--------------------------------------------------")
"""Ejercicio: ContadorVotos

Crea una clase llamada ContadorVotos que:

(1) Método registrar_voto(opcion)

Debe guardar en un diccionario cuántos votos ha recibido cada opción.
(2) Método opcion_mas_votada()

Debe retornar la opción que tenga mayor cantidad de votos.
(3) Método votos_opcion(opcion)

Debe recibir una opción y retornar cuántos votos tiene.
"""
class ContarVotos:
    def __init__(self):
        self.votos = {}
        
    def registrar_voto(self, opcion):
        if opcion in self.votos:
            self.votos[opcion] += 1
        else:
            self.votos[opcion] =1

    def opcion_mas_votada(self):
        if not self.votos:
            return None
        
        return max(self.votos, key=self.votos.get)
    
    def votos_opcion(self, opcion):
        return self.votos.get(opcion, 0)
    
contar = ContarVotos()
contar.registrar_voto("A")
contar.registrar_voto("B")
contar.registrar_voto("A")
contar.registrar_voto("B")
contar.registrar_voto("A")
contar.registrar_voto("A")
print(contar.votos_opcion("A"))
print(contar.votos_opcion("B"))
print(contar.votos_opcion("C"))
print(contar.opcion_mas_votada())