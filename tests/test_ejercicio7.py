################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio7 import sexadecimal_a_decimal, decimal_a_sexadecimal

"""
Describir aquí que es lo que se esta probando.
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""

def test_sexadecimal_a_decimal():
    """
       Se pasarán y sumaran 126 horas y 12 minutos a segundos.
       Por lo que el resultado debe ser 454376 segundos en total
    """
    horas = 126
    minutos = 12
    segundos = 56
    resultado = sexadecimal_a_decimal(horas, minutos, segundos)
    assert resultado == 454376, "Los segundos totales están mal"

def test_decimal_a_sexadecimal():
    """
       Se pasarán y sumaran 126 horas y 12 minutos a segundos.
       Por lo que el resultado debe ser 454376 segundos en total
    """
    horas = 12.34
    horas, minutos, segundos = decimal_a_sexadecimal(horas)
    assert segundos == 24, "Los segundos están mal"
    assert minutos == 20, "Los minutos están mal"
    assert horas == 12, "Las horas están mal"


