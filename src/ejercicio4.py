################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
4. Suma lenta

Escribir una función que haga la suma entre dos números
enteros sin hacer la operación de manera directa.

Esto quiere decir que para hacer la suma entre 4 y 3,
las operaciones resultantes deberán ser 4+1+1+1.

La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.

"""
from ejercicio2 import signo

def suma_lenta(numero, otro_numero):
    """
    Esta función se encarga de sumarle uno a un (numero)
    tantas veces como lo especifique (otro_numero)
    sintaxis: suma_lenta(numero, otro_numero)
    """
    suma = 0
    resultado = numero
    if signo(otro_numero) == -1:
        while suma != otro_numero:
            resultado += - 1
            suma -= 1
        return resultado
    else:
        while suma != otro_numero:
            resultado += + 1
            suma += 1
        return resultado


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input("Ingese numero"))
    otro_numero = int(input("Ingese numero"))
    resultado = suma_lenta(numero, otro_numero)
    if signo(otro_numero) == 1:
        unos = otro_numero*"+1"
    else:
        unos = abs(otro_numero)*"+(-1)"
    print(f"{numero}{unos}={resultado}")

if __name__ == "__main__":
    principal()
