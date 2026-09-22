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

print("-----------------------------------------------------------------")
"""Ejercicio: AgrupadorSalarios

Crea una clase AgrupadorSalarios que:

(1) Método clasificar_salario(salario)

Debe retornar una categoría dependiendo del salario:

Si el salario es menor a 500 → "bajo"
Si el salario es menor a 1500 → "medio"
Si el salario es menor a 3000 → "alto"
Si es 3000 o más → "muy alto"
(2) Método agrupar_por_categoria(*salarios)

Debe recibir varios salarios y crear un diccionario agrupándolos según su categoría
(3) Método salario_promedio_categoria(categoria)

Debe calcular el promedio de los salarios que pertenecen a una categoría determinada."""

class AgrupadorSalarios:
    def __init__(self):
        self.salarios = {}

    def clasificar_salario(self, salario):
        if salario < 500:
            return "bajo"
        elif salario < 1500:
            return "medio"
        elif salario < 3000:
            return "alto"
        else:
            return "muy alto"

    def agrupar_por_categoria(self, *salarios):
        self.salarios = {}
        for salario in salarios:
            categoria = self.clasificar_salario(salario)
            self.salarios.setdefault(categoria, []).append(salario)
        return self.salarios

    def salario_promedio_categoria(self, categoria):
        salarios = self.salarios.get(categoria, [])
        if not salarios:
            return 0
        return sum(salarios) / len(salarios)

agrupar = AgrupadorSalarios()
print(agrupar.clasificar_salario(800))
print(agrupar.agrupar_por_categoria(400,800,2000,3500,1200,450,3000))
print(agrupar.salario_promedio_categoria("medio"))