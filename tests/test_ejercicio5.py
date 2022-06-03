################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio5 import division_lenta

try:
    from ejercicio2 import signo
except ImportError as exc:
    from src.ejercicio2 import signo


"""
Realiza restas para obtener un cociente y resto entre dos números.
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""

def test_division_lenta_positivo():
    """
       Dividimos 11 entre 2, el cociente debe ser 5 y el resto 1
    """
    dividir = 11
    entre = 2
    cociente, resto = division_lenta(dividir, entre)
    assert cociente == 5, "El cociente está mal"
    assert resto == 1, "El resto está mal"

def test_division_lenta_negativo():
    """
       Dividimos -11 entre dos, el cociente debe ser -5 y el resto -1
    """
    dividir = -11
    entre = -2
    cociente, resto = division_lenta(dividir, entre)
    assert cociente == 5, "El cociente está mal"
    assert resto == -1, "El resto está mal"

def test_division_lenta_dividendo_negativo():
    """
       Dividimos -11 entre dos, el cociente debe ser -5 y el resto -1
    """
    dividir = -11
    entre = 2
    cociente, resto = division_lenta(dividir, entre)
    assert cociente == -5, "El cociente está mal"
    assert resto == -1, "El resto está mal"

def test_division_lenta_divisor_negativo():
    """
       Dividimos -11 entre dos, el cociente debe ser -5 y el resto -1
    """
    dividir = 11
    entre = -2
    cociente, resto = division_lenta(dividir, entre)
    assert cociente == -5, "El cociente está mal"
    assert resto == 1, "El resto está mal"
