"""Clase CodificadorCesar que: 
(1) tenga método codificar_letra(letra, desplazamiento) que retorne la letra desplazada en el alfabeto (usar operador %); 
(2) tenga método codificar_palabra(palabra, desplazamiento) que reutilice para toda la palabra; 
(3) tenga un diccionario como atributo para historial de codificaciones."""
class CodificadorCesar:
    def __init__(self):
        self.historial = {}
        
    def codificar_letra(self, letra, desplazamiento):
        if letra.isalpha():
            base = ord("A") if letra.isupper() else ord("a")
            return chr((ord(letra) - base + desplazamiento) % 26 + base)
        return letra
    
    def codificar_palabra(self, palabra, desplazamiento):
        codificar = "".join(self.codificar_letra(letra, desplazamiento) for letra in palabra)
        self.historial[palabra] = codificar
        return codificar

codificado = CodificadorCesar()
print(codificado.codificar_palabra("hola", 3))
print(codificado.codificar_palabra("tangamandapio", 4))
print(codificado.historial)

print("-----------------------------------------------------------------------------------------------")

"""Ejercicio: ConversorVocales

Crea una clase ConversorVocales que:

(1) Método reemplazar_letra(letra)

Debe recibir una letra y retornar una nueva letra siguiendo estas reglas:

a → e
e → i
i → o
o → u
u → a

También debe funcionar con mayúsculas
(2) Método convertir_palabra(palabra)

Debe recibir una palabra y utilizar reemplazar_letra() para transformar cada letra.
(3) Atributo historial

La clase debe tener un diccionario:
"""
class ConversorVocales:
    def __init__(self):
        self.historial = {}

    def reemplazar_letra(self, letra):
        vocales = {"a": "e","e": "i","i": "o","o": "u","u": "a"}
        if letra.isupper():
            return vocales.get(letra.lower(), letra.lower()).upper()
        else:
            return vocales.get(letra, letra)

    def convertir_palabra(self, palabra):
        convertida = ""
        for letra in palabra:
            convertida += self.reemplazar_letra(letra)
        self.historial[palabra] = convertida
        return convertida

conversor = ConversorVocales()
print(conversor.reemplazar_letra("a"))
print(conversor.reemplazar_letra("m"))
print(conversor.convertir_palabra("hola"))
print(conversor.convertir_palabra("casa"))
print(conversor.convertir_palabra("HOLA"))
print(conversor.historial)