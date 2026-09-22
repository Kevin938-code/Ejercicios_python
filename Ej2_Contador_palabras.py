"""Clase AnalizadorTexto que: 
(1) tenga método agregar_palabra(palabra) que agregue la palabra a un conjunto (para evitar duplicados) y a una lista (para el orden); 
(2) tenga método contar_palabras() que retorne cuántas palabras únicas hay; 
(3) tenga método agregar_multiples(*args) que reutilice agregar_palabra para varios."""
class AnalizadorTexto:
    def __init__(self):
        self.palabras_ordenadas = []
        self.palabras_unicas = set()

    def agregar_palabra(self, palabra):
        self.palabras_unicas.add(palabra)
        self.palabras_ordenadas.append(palabra)
    
    def contar_palabras(self):
        return len(self.palabras_unicas)
    
    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)

texto = AnalizadorTexto()
texto.agregar_multiples("hola", "mundo", "hola", "python")
print(texto.contar_palabras())


print("-------------------------------------------------------")
"""Ejercicio: Clase RegistroNombres
Crea una clase llamada RegistroNombres que permita registrar nombres.
    1. agregar_nombre(nombre)
Debe agregar el nombre a:
Un conjunto, para evitar nombres duplicados.
Una lista, para conservar el orden en que fueron registrados.
    2. contar_nombres()
Debe retornar la cantidad de nombres únicos registrados.
    3. agregar_multiples(*args)
Debe permitir agregar varios nombres de una sola vez.
Importante: no debes repetir dentro de este método la lógica de agregar al conjunto y a la lista.
Debes reutilizar agregar_nombre().
"""
class RegistroNombres :
    def __init__(self):
        self.nombres = []
        self.nombres_unicos = set()

    def agregar_nombre(self, nombre):
        self.nombres.append(nombre)
        self.nombres_unicos.add(nombre)

    def contar_nombres(self):
        return len(self.nombres_unicos)

    def agregar_multiples(self, *args):
        for nombre in args:
            self.agregar_nombre(nombre)

registro = RegistroNombres()
registro.agregar_nombre("Jose")
registro.agregar_multiples("Jose","Juan","Adrian","Juan")
print(registro.nombres)
print(registro.nombres_unicos)
print(registro.contar_nombres())


print("-------------------------------------------------------")
"""Ejercicio: RegistroProductos
Crea una clase llamada RegistroProductos que permita registrar productos, pero ahora solo debe aceptar productos válidos.
    1. __init__()
La clase debe tener:
Una lista llamada productos para conservar el orden de registro.
Un conjunto llamado productos_unicos para evitar duplicados.
    2. validar_producto(producto)
Debe recibir un nombre de producto y retornar:
True si el nombre tiene al menos 3 caracteres.
False si tiene menos de 3 caracteres.
    3. agregar_producto(producto)
Debe:
Validar el producto utilizando validar_producto().
Si es válido:
agregarlo a la lista productos;
agregarlo al conjunto productos_unicos.
Si no es válido, no debe agregarlo a ninguna estructura.
    4. contar_productos()
Debe retornar la cantidad de productos únicos válidos.
    5. agregar_multiples(*args)
Debe recibir varios productos y utilizar agregar_producto() para procesarlos.
No repitas la lógica de validación aquí.
"""
class ProductosValidos:
    def __init__(self):
        self.productos = []
        self.productos_unicos = set()

    def validar_producto(self, producto):
        return len(producto) >= 3
    
    def agregar_producto(self, producto):
        if self.validar_producto(producto):
            self.productos.append(producto)
            self.productos_unicos.add(producto)

    def contar_productos(self):
        return len(self.productos_unicos)

    def agregar_multiples(self, *args):
        for producto in args:
            self.agregar_producto(producto)

validar = ProductosValidos()
validar.agregar_producto("Pan")
validar.agregar_multiples("Pan","sal","pc","azucar","tv")
print(validar.productos)
print(validar.productos_unicos)
print(validar.contar_productos())