################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
6. Ordenar 3 valores

Escribir una función que a partir de tres variables de tipo entero retorne una
tupla con dichos valores ordenados de menor a mayor. Y Viceversa

"""
from src.ejercicio3 import compara

def ordenar_mayor_a_menor(uno, dos, tres):
    """
    Esta función se encarga de ordenar tres numeros de mayor a menor
    la salida de la función será una tupla ordenada.
    sintaxis: ordenar_mayor_a_menor(numero, numero2, numero3)
    """
    tupla= (uno, dos, tres)
    if uno > dos and uno > tres:
        tupla= (uno, dos, tres)
        if compara(dos, tres) == 1:
            tupla= (uno, dos, tres)
        else:
            tupla= (uno, tres, dos)
    elif dos > uno and dos > tres:
        tupla = dos, uno, tres
        if compara(uno, tres) == 1 :
            tupla = dos, uno, tres
        else:
            tupla = dos, tres, uno
    else:
        tupla= (tres, dos, uno)
        if compara(uno, dos) == 1:
            tupla= (tres, uno, dos)
        else:
            tupla= (tres, dos, uno)
    return tupla

def ordenar_menor_a_mayor(uno, dos, tres):
    """
    Esta función se encarga de ordenar tres numeros de menor a mayor
    la salida de la función será una tupla ordenada.
    sintaxis: ordenar_menor_a_mayor(numero, numero2, numero3)
    """
    tupla= (uno, dos, tres)
    if uno > dos and uno > tres:
        tupla= (tres, dos, uno)
        if compara(dos, tres) == 1:
            tupla= (tres, dos, uno)
        else:
            tupla= (dos, tres, uno)
    elif dos > uno and dos > tres:
        tupla= (uno, tres, dos)
        if compara(uno, tres) == 1 :
            tupla= (tres, uno, dos)
        else:
            tupla= (uno, tres, dos)
    else:
        tupla= (uno, dos, tres)
        if compara(uno, dos) == 1:
            tupla= (dos, uno, tres)
        else:
            tupla= (uno, dos, tres)
    return tupla

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero1 = int(input("Ingrese un numero... "))
    numero2 = int(input("Ingrese un numero... "))
    numero3 = int(input("Ingrese un numero... "))
    tupla1 = ordenar_mayor_a_menor(numero1, numero2, numero3)
    tupla2 = ordenar_menor_a_mayor(numero1, numero2, numero3)
    print(f"{type(tupla1)}: mayor: {tupla1[0]} medio: {tupla1[1]} menor: {tupla1[2]}")
    print(f"{type(tupla2)}: menor: {tupla2[0]} medio: {tupla2[1]} mayor: {tupla2[2]}")

if __name__ == "__main__":
    principal()
