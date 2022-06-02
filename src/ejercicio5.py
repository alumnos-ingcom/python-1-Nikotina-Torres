################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
5. Divisiones

Escribir una función que mediante restas sucesivas,
obtenga el valor del cociente y resto de dos números enteros.

"""
from src.ejercicio2 import signo

def division_lenta(dividendo, divisor):
    """
    Realiza una division indicando el cociente y resto resultante
    sintaxis: division_lenta(int, int)
    """
    cociente = 0
    if signo(dividendo) == 1 and signo(divisor) == 1:
        while dividendo - divisor >= 0:
            cociente += 1
            dividendo = dividendo - divisor
        return cociente, dividendo
    elif signo(dividendo) == -1 and signo(divisor) == 1:
        while dividendo + divisor <= 0:
            cociente -= 1
            dividendo = dividendo + divisor
        return cociente, dividendo
    elif signo(dividendo) == 1 and signo(divisor) == -1:
        while dividendo + divisor >= 0:
            cociente -= 1
            dividendo = dividendo + divisor
        return cociente, dividendo
    elif signo(dividendo) == -1 and signo(divisor) == -1:
        while dividendo - divisor <= 0:
            cociente += 1
            dividendo = dividendo - divisor
        return cociente, dividendo


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    dividendo = int(input("Ingrese numero a dividir... "))
    divisor = int(input("Ingrese numero que divide... "))
    cociente, resto = division_lenta(dividendo, divisor)
    print(f"Cociente: {cociente} resto: {resto}")


if __name__ == "__main__":
    principal()
