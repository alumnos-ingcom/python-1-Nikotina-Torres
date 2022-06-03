################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio9 import factores_primos

try:
    from ejercicio8 import es_primo
except ImportError as exc:
    from src.ejercicio8 import es_primo


"""
Se ingresará un número primo (no tiene facotres primos) y un número no primo,
para que la funcion lo descomponga en numeros primos que multiplicados den el
numero no primo
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""

def test_factores_primos_primo():
    """
       Una breve descripción del caso de prueba aplicado a la función
    """
    numero = 7
    resultado = factores_primos(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla"
    assert resultado == (7,), "El numero 7 no tiene factores primos"
    #esto quedo medio raro pero we

def test_factores_primos_no_primo():
    """
       Una breve descripción del caso de prueba aplicado a la función
    """
    numero = 12
    resultado = factores_primos(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla"
    assert resultado == (2, 2, 3), "Los factores no son correctos"
