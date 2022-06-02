################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio4 import suma_lenta

try:
    from ejercicio2 import signo
except ImportError as exc:
    from src.ejercicio2 import signo


"""
Se está probando la función de suma lenta, le sumará a la primera variable
1 tantas veces como se lo especifique la segunda variable.
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""

def test_suma_lenta_positivo():
    """
    A 5 se le sumara 1, 10 veces.
    """
    numero = 5
    cantidad_a_sumar = 10
    resultado = suma_lenta(numero, cantidad_a_sumar)
    assert resultado == 15, "La suma no es correcta"

def test_suma_lenta_negativo():
    """
    A -2 se le sumara 1, 10 veces.
    """
    numero = -2
    cantidad_a_sumar = -15
    resultado = suma_lenta(numero, cantidad_a_sumar)
    assert resultado == -17, "La suma negativa no es correcta"
