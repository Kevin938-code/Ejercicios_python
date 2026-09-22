"""Clase AnalizadorString que: 
(1) tenga método solo_vocales(letra) que retorne True si es vocal; 
(2) tenga método contar_por_tipo(texto) que retorne un diccionario {'vocales': cant, 'consonantes': cant, 'digitos': cant} reutilizando métodos; 
(3) tenga atributo que guarde el texto más largo analizado."""
class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        return letra.lower() in "aeiou"
    
    def contar_por_tipo(self, texto):
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto
        diccionario = {'vocales': 0, 'consonantes': 0, 'digitos': 0}
        for caracter in texto :
            if caracter.isalpha():
                if self.solo_vocales(caracter):
                    diccionario['vocales'] += 1
                else:
                    diccionario['consonantes'] += 1
            elif caracter.isdigit():
                diccionario['digitos'] += 1
        return diccionario

textos = AnalizadorString()
print(textos.contar_por_tipo("JavaScript"))
print(textos.contar_por_tipo("123hola"))
print(textos.texto_mas_largo)

print("----------------------------------------------------")
"""Ejercicio: AnalizadorNumeros

Crea una clase llamada AnalizadorNumeros que permita analizar números.

1. Método es_positivo(numero)

Debe recibir un número y retornar:

True si el número es mayor que 0.
False si el número es 0 o negativo.
2. Método contar_por_tipo(*numeros)

Debe recibir varios números utilizando *args y retornar un diccionario con tres categoría
"positivos": cantidad,
"negativos": cantidad,
"ceros": cantidad
Importante:

Debes reutilizar es_positivo(numero) dentro de contar_por_tipo().

No vuelvas a escribir la lógica para determinar si un número es positivo.
3. Atributo mayor_numero

La clase debe tener un atributo que guarde el número más grande que haya sido analizado.
"""
class AnalizadorNumeros:
    def __init__(self):
        self.mayor = None
    
    def es_positivo(self, numero):
        return numero > 0

    def contar_por_tipo(self,*numeros):
        categoria_numero={'positivos': 0,'negativos': 0,'ceros': 0}
        for numero in numeros:
            if numero > self.mayor:
                self.mayor=numero
            if self.es_positivo(numero):
                categoria_numero['positivos'] +=1
            elif numero < 0:
                categoria_numero['negativos']+=1
            else:
                    categoria_numero['ceros']+=1
        return categoria_numero    

analiza = AnalizadorNumeros()
print(analiza.contar_por_tipo(5,0,-3,4,8,0))
print(analiza.mayor)