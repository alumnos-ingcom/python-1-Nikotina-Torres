################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio11 import es_multiplo

try:
    from ejercicio2 import signo
except ImportError as exc:
    from src.ejercicio2 import signo

"""
Se probará un numero multiplo de 3 y un numero que no lo es.
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""

def test_es_multiplo_true():
    """
    Se probara el número 27, multiplo de 3.
    """
    numero = 27
    multiplo = 3
    resultado = es_multiplo(numero, multiplo)
    assert resultado is True, "27 SI es multiplo de 3"

def test_es_multiplo_false():
    """
    Se probará el numero 20, no es multiplo de 3.
    """
    numero = 20
    multiplo = 3
    resultado = es_multiplo(numero, multiplo)
    assert resultado is False, "20 NO es multiplo de 3"
