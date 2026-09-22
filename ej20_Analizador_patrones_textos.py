"""Clase AnalizadorPatrones que: 
(1) tenga método encontrar_palabras(texto, patron) que busque palabras que inicien con el patrón y retorne una lista; 
(2) tenga método agrupar_por_longitud(texto) que retorne un diccionario {longitud: [palabras]}; 
(3) tenga método palabras_unicas() usando un conjunto."""
class AnalizadorPatrones:
    def __init__(self):
        self.todas_las_palabras = set()
        
    def encontrar_palabras(self, texto, patron):
        palabras = texto.split()
        self.todas_las_palabras.update(palabras)
        return [palabra for palabra in palabras if palabra.startswith(patron)]
    
    def agrupar_por_longitud(self, texto):
        palabras = texto.split()
        self.todas_las_palabras.update(palabras)
        grupos = {}
        for palabra in palabras:
            grupos.setdefault(len(palabra), []).append(palabra)
        return grupos
        
    def palabras_unicas(self):
        return list(self.todas_las_palabras)
    
ap = AnalizadorPatrones()
print(ap.agrupar_por_longitud("el gato está aquí"))
