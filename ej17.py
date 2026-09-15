"""Clase AgrupadorEdades que: 
(1) tenga método clasificar_edad(edad) que retorne la categoría ("niño", "adolescente", "adulto", "mayor"); 
(2) tenga método agrupar_por_categoria(*edades) que retorne un diccionario con {categoría: [edades]}; 
(3) tenga método edad_promedio_categoria(categoria)."""
class AgrupadorEdades:
    def __init__(self):
        self.personas = {}
        
    def clasificar_edad(self, edad):
        if edad < 13 :
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 65:
            return "adulto"
        else:
            return "mayor"
        
    def agrupar_por_categoria(self, *edades):
        self.personas = {}
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            self.personas.setdefault(categoria, []).append(edad)
        return self.personas
        
    def edad_promedio_categoria(self, categoria):
        edades = self.personas.get(categoria, [])
        if not edades:
            return 0
        return sum(edades) / len(edades)
        
agrupar = AgrupadorEdades()
print(agrupar.agrupar_por_categoria(5, 15, 30, 17))
print(agrupar.edad_promedio_categoria("adulto"))
