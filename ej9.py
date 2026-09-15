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
