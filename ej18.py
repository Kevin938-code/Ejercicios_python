import math

"""Clase CalculadorDistancia que: 
(1) tenga método distancia_euclidiana(p1, p2) que reciba dos tuplas (x,y) y calcule la distancia; 
(2) tenga método punto_mas_cercano(referencia, *puntos) que retorne el punto más cercano a referencia; 
(3) tenga un atributo lista para guardar todas las distancias calculadas."""

class CalculadorDistancia:
    def __init__(self):
        self.distancias = []
        
    def distancia_euclidiana(self, p1, p2):
        distancia = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
        self.distancias.append(distancia)
        return distancia
    
    def punto_mas_cercano(self, referencia, *puntos):
        return min(puntos, key=lambda punto: self.distancia_euclidiana(referencia, punto))

calcular = CalculadorDistancia()
print(calcular.distancia_euclidiana((0, 0), (3,4)))