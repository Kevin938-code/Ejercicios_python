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

print("------------------------------------------------------------------")
"""Ejercicio: GestorProductos
Crea una clase llamada GestorProductos que permita registrar productos y sus precios.
    1. Método agregar_producto(nombre, precio)
Debe recibir:
nombre del producto.
precio del producto.
Y guardarlos en un diccionario
    2. Método productos_mayor_precio(precio_minimo)
Debe recibir un precio mínimo y retornar una lista con los nombres de los productos cuyo precio sea mayor o igual al precio indicado.
    3. Método precio_promedio()
Debe retornar el promedio de los precios almacenados
También debes controlar el caso en que todavía no haya productos, para evitar dividir entre cero.
"""
class GestorProductos:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, precio):
        self.productos[nombre] = precio

    def productos_mayor_precio(self, precio_minimo):
        productos_validos = []
        for nombre, precio in self.productos.items():
            if precio >= precio_minimo:
                productos_validos.append(nombre)
        return productos_validos

    def precio_promedio(self):
        if self.productos:
            return sum(self.productos.values())/len(self.productos)
        else:
            return 0

gestionar = GestorProductos()
gestionar.agregar_producto("leche", 1.00)
gestionar.agregar_producto("azucar", 0.60)
gestionar.agregar_producto("mortadela", 3.50)
gestionar.agregar_producto("atun", 2.80)
print(gestionar.productos)
print(gestionar.productos_mayor_precio(2))
print(gestionar.precio_promedio())