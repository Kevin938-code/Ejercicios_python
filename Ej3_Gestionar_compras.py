"""Clase CarroCompras que: (1) tenga método agregar_articulo(nombre, precio) que guarde en un diccionario {nombre: precio}; 
(2) tenga método total_carrito() que retorne la suma de todos los precios; 
(3) tenga método articulos_por_rango(precio_min, precio_max) que retorne una lista con artículos dentro del rango."""
class CarroCompras:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, precio):
        self.productos[nombre] = precio

    def total_carrito(self):
        return sum(self.productos.values())

    def articulos_por_rango(self, precio_min, precio_max):
        return [nombre for nombre, precio in self.productos.items() if precio_min <= precio <= precio_max]

carrito = CarroCompras()
carrito.agregar_producto("manzanas", 3.5)
carrito.agregar_producto("bananas", 2.0)
carrito.agregar_producto("naranjas", 4.0)
print(carrito.total_carrito())
print(carrito.articulos_por_rango(2.0, 3.5))