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
