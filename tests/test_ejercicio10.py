################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio10 import es_palindromo

"""
Se probará una palabra palíndroma y una que no lo es.
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""

def test_es_palindromo_true():
    """
       Se prueba la palabra reconocer, que es palíndroma
    """
    palabra = "reconocer"
    resultado = es_palindromo(palabra)
    assert resultado is True, "La palabra es palíndroma"

def test_es_palindromo_false():
    """
       Se prueba la palabra manzana, no es palíndroma
    """
    palabra = "manzana"
    resultado = es_palindromo(palabra)
    assert resultado is False, "La palabra no es palíndroma"
