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