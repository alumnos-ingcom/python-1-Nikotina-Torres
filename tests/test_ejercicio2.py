################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest

from src.ejercicio2 import signo

"""
Probando la función cuya tarea es indicar si un número ingresado es 
positivo, negativo o cero.
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""

def test_signo_positivo():
    """
       El número a probar es 16, un número positivo.
    """
    numero = 16
    resultado = signo(numero)
    assert resultado == 1, "El resultado es incorrecto"
    assert isinstance(resultado, int), "El resultado debe ser un número entero"

def test_signo_negativo():
    """
       El número a probar es -12, un número negativo.
    """
    numero = -12
    resultado = signo(numero)
    assert resultado == -1, "El resultado es incorrecto"
    assert isinstance(resultado, int), "El resultado debe ser un número entero"

def test_signo_cero():
    """
       El número a probar es 0, un número nulo, o cero.
    """
    numero = 0
    resultado = signo(numero)
    assert resultado == 0, "El resultado es incorrecto"
    assert isinstance(resultado, int), "El resultado debe ser un número entero"
