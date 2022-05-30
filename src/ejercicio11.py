################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
11. Multiplos de

Escribir una función que indique con True si un número
entero es multiplo de otro, utilizando sumas y restas.

"""
from ejercicio2 import signo

def es_multiplo(numero, multiplo):
    """
    Esta función se encarga de retornar True si el (numero) ingresado es multiplo de (multiplo)
    Sintaxis: es_multiplo(numero, multiplo)
    """

    if signo(numero) == 1 and signo(multiplo) == 1:
        if numero < multiplo:
            return False
        else:
            while numero > multiplo:
                numero -= multiplo
            if numero == multiplo:
                return True
            else:
                return False
    else:
        if numero > multiplo:
            return False
        while numero < multiplo:
            numero -= multiplo
        if numero == multiplo:
            return True
        else:
            return False

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input("Ingrese numero... "))
    multiplo = int(input("Ingrese multiplo... "))
    print(es_multiplo(numero, multiplo))
    
if __name__ == "__main__":
    principal()
