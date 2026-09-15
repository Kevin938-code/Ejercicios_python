"""Clase AnalizadorTexto que: (1) tenga método agregar_palabra(palabra) que agregue la palabra a un conjunto (para evitar duplicados) y a una lista (para el orden); 
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


