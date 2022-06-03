################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
9. Factores Primos

Escribir una función que retorne una tuple con factores primos de un numero entero positivo.
"""
from src.ejercicio8 import es_primo

def factores_primos(numero):
    """
    Esta función se encarga de descomponer un (numero) no primo en factores primos
    Es decir, los numeros primos más pequeños que multiplicados den el (numero) inicial.
    sintaxis: factores_primos(numero)
    """
    contador = 1
    resultado = []
    while numero != 1:
        if es_primo(contador) is True:
            if numero%contador == 0:
                numero = numero/contador
                resultado.append(contador)
                contador = 1
            else:
                contador += 1
        else:
            contador += 1
    return tuple(resultado)


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = abs(int(input("Ingrese un numero entero positivo... ")))
    tupla_factores = factores_primos(numero)
    print(f"Los factores primos de {numero} son:")
    print(f"{tupla_factores}")

if __name__ == "__main__":
    principal()
