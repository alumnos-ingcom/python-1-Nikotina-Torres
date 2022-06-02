################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio3 import compara

try:
    from ejercicio2 import signo
except ImportError as exc:
    from src.ejercicio2 import signo

"""
Se está probando una función que en base a dos numeros retorne:
-1 si el primero es menor que el segundo
0 si son iguales
1 si el primero es mayor que el segundo
"""

def test_compara_primero_mayor():
    """
       Compara el numero 12 con el 5, por lo tanto el resultado debería ser 1.
    """
    numero = 12
    otro_numero = 5
    resultado = compara(numero, otro_numero)
    assert resultado == 1, "El resultado está mal"
    assert isinstance(resultado, int), "El resultado debe ser un n° entero"
    
def test_compara_iguales():
    """
       Compara el numero 42 con el 42, por lo tanto el resultado debería ser 0.
    """
    numero = 42
    otro_numero = 42
    resultado = compara(numero, otro_numero)
    assert resultado == 0, "El resultado no es el correcto"
    assert isinstance(resultado, int), "El resultado debe ser un n° entero"

def test_compara_primero_menor():
    """
       Compara el numero 15 con el 23, por lo tanto el resultado debería ser -1.
    """
    numero = 15
    otro_numero = 23
    resultado = compara(numero, otro_numero)
    assert resultado == -1, "El resultado no es el correcto"
    assert isinstance(resultado, int), "El resultado debe ser un n° entero"
