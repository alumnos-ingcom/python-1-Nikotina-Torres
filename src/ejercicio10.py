################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
10. Palíndromo

Escribir una función que indique con True si una palabra o frase ingresada se trata de
un palindromo
Palíndromo, es si se lee igual de derecha a izquierda que de izquierda a derecha.

"""

def es_palindromo(texto):
    """
    Esta función se encarga de devolver True si la palabra es un palíndromo, y False si no lo es.
    sintaxis: es_palindromo(texto)
    """
    lista_letras = list(texto)
    contador = 0
    contador_negativo = -1
    while contador != len(lista_letras):
        if texto[contador] == texto[contador_negativo]:
            contador += 1
            contador_negativo -= 1
            resultado = True
        else:
            resultado = False
            contador += 1
            contador_negativo -= 1
    return resultado


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    palabra = "neuquen"
    resultado = es_palindromo(palabra)
    if resultado is True:
        print("La palabra es un palíndromo")
    else:
        print("La palabra NO es un palíndromo")

if __name__ == "__main__":
    principal()
