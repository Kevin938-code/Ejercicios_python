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

print("-------------------------------------------------------------------------------------------")
"""Ejercicio: RegistroProductos

Crea una clase llamada RegistroProductos que:

(1) Método registrar(producto, precio)

Debe guardar cada producto y su precio en un diccionario.
(2) Método productos_caros(precio_minimo)

Debe retornar una lista con los nombres de los productos cuyo precio sea mayor o igual al precio mínimo.
(3) Método producto_mas_caro()

Debe retornar una tupla con:

(nombre_producto, precio)del producto que tenga el precio más alto.
"""
class RegistroProductos:
    def __init__(self):
        self.productos = {}

    def registrar(self, producto, precio):
        self.productos[producto] = precio

    def productos_caros(self, precio_minimo):
        return [nombre for nombre, precio in self.productos.items() if precio >= precio_minimo]

    def producto_mas_caro(self):
        nombre = max(self.productos, key=self.productos.get)
        return (nombre, self.productos[nombre])

registro = RegistroProductos()
registro.registrar("pan", 1.50)
registro.registrar("leche", 2.00)
registro.registrar("arroz", 3.50)
registro.registrar("atun", 4.25)
registro.registrar("huevos", 3.00)
print(registro.productos)
print(registro.productos_caros(3))
print(registro.producto_mas_caro())