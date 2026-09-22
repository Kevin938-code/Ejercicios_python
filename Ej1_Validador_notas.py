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

print("------------------------------------------")

"""Ejercicio: Clase Inventario 
Crea una clase llamada Inventario que cumpla con lo siguiente:
    1. Método validar_precio(precio)
Debe recibir un precio y retornar:
True si el precio está entre 0 y 10000, incluyendo ambos valores.
False si está fuera de ese rango.
    2. Método cargar_precios(*args)
Debe recibir varios precios.
Cada precio debe pasar primero por validar_precio().
Si es válido → se agrega a una lista interna.
Si no es válido → se ignora.
Al terminar, debe retornar la lista interna.
    3. Método precio_promedio()
Debe calcular y retornar el promedio de los precios almacenados.
También debes contemplar el caso en que no haya precios almacenados, para evitar una división entre cero.
"""
class Inventario:
    def __init__(self):
        self.precios_validos = []
    
    def validar_precio(self, precio):
        return 0 <= precio <= 10000
    
    def cargar_precios(self, *args):
        for precio in args:
            if self.validar_precio(precio):
                self.precios_validos.append(precio)
        return self.precios_validos

    def precio_promedio(self):
        if self.precios_validos:
            return sum(self.precios_validos)/len(self.precios_validos)
        else:
            return "no hay precios almacenados"

inv = Inventario()
print(inv.cargar_precios())
print(inv.precio_promedio())