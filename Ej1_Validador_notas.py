"""Clase Calificador que: (1) tenga método validar_nota(nota) que retorne True si 0 ≤ nota ≤ 100, False en caso contrario; 
(2) tenga método cargar_notas(*args) que reciba múltiples notas, las valide, agregue solo las válidas a una lista interna, y retorne esa lista; 
(3) tenga método promedio() que retorne el promedio de notas almacenadas"""
class Calificador:
    def __init__(self):
        self.notas=[]

    def validar_nota(self,nota):
        return 0 <= nota <= 100
    
    def cargar_notas(self,*args):
        
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas

    def promedio(self):
        return sum(self.notas)/len(self.notas)


cal = Calificador()
print(cal.cargar_notas(-60,80,40,200))
print(cal.promedio())