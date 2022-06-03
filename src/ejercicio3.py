################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
3. Comparación de números

Escribir una función que utilizando sumas y restas, reciba dos valores y retorne:

    Retornar -1 si el primero es menor que el segundo
    Retornar 0 si son iguales
    Retornar 1 si el primero es mayor que el segundo

"""
from src.ejercicio2 import signo

def compara(numero, otro_numero):
    """
    Comparar un numero con otro numero
    Se retornará 1 si el primero es mayor que el segundo
    Se retornará -1 si el segundo es mayor que el primero
    Se retornará 0 si los dos números son iguales
    """
    suma = 0
    if signo(otro_numero) == 1:
        while suma != otro_numero:
            suma+=1
    else:
        while suma != otro_numero:
            suma-=1
    if suma < numero:
        return 1
    elif suma > numero:
        return -1
    else:
        return 0

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = float(input("Ingrese numero"))
    numero2 = float(input("Ingrese numero"))
    print(compara(numero,numero2))

if __name__ == "__main__":
    principal()
