################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio8 import es_primo

"""
Probando la funcion para saber si un numero ingresado es primo o no.
Se probará un valor primo y uno no primo.
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""

def test_es_primo_primo():
    """
       Se le introduce el valor 11, que es numero primo, debe retornar True
    """
    numero_primo = 11
    resultado = es_primo(numero_primo)
    assert isinstance(resultado, bool), "El resultado debe ser booleano"
    assert resultado == True, "El resultado debe ser verdadero"

def test_es_primo_no_primo():
    """
       Se le introduce el valor 22, que es divisible por otros numeros
       además de 1 y 22, por lo tanto debe retornar False.
    """
    numero_no_primo = 22
    resultado = es_primo(numero_no_primo)
    assert isinstance(resultado, bool), "El resultado debe ser booleano"
    assert resultado == False, "El resultado debe ser falso"
