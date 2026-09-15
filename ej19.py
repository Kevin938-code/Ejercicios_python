"""Clase Inventario que: 
(1) tenga método agregar_stock(producto, cantidad) que guarde en un diccionario; 
(2) tenga método restar_stock(producto, cantidad) que disminuya y retorne True si hay suficiente; 
(3) tenga método productos_bajo_stock(minimo) que retorne una lista de productos con cantidad < minimo."""
class Inventario:
    def __init__(self):
        self.stock = {}
        
    def agregar_stock(self, producto, cantidad):
        self.stock[producto] = self.stock.get(producto, 0) + cantidad
        return self.stock[producto]
        
    def restar_stock(self, producto, cantidad):
        if self.stock.get(producto, 0) >= cantidad:
            self.stock[producto] -= cantidad
            return True
        return False
    
    def productos_bajo_stock(self, minimo):
        return [producto for producto, cantidad in self.stock.items() if cantidad < minimo]
    
almacen = Inventario()
print(almacen.agregar_stock("pan", 50))
print(almacen.restar_stock("pan", 30))
print(almacen.productos_bajo_stock(25))
