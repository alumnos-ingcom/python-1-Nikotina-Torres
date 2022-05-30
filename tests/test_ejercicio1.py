################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio1 import convertir_a_fahrenheit, convertir_a_centigrados
"""
Probando funciones para convertir entre grados centigrados a Fahrenheit,
y viceversa. Usando tanto valores positivos como negativos.
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""

def test_convertir_a_fahrenheit_positivo():
    '''
    Los grados centigrados son 78, el resultado debe 
    ser igual a 172.4
    '''
    grados = 78
    resultado = convertir_a_fahrenheit(grados)
    assert isinstance(resultado, float), "el resultado debe ser decimal"
    assert resultado == 172.4, "el resultado no es correcto"
    
def test_convertir_a_fahrenheit_negativo():
    '''
    Los grados centigrados son -79, el resultado debe 
    ser igual a -110.2
    '''
    grados = -79
    resultado = convertir_a_fahrenheit(grados)
    assert isinstance(resultado, float), "el resultado debe ser decimal"
    assert resultado == -110.2, "el resultado no es correcto"

def test_convertir_a_centigrados_positivo():
    '''
    Los grados Fahrenheit son 78, el resultado debe
    ser igual a 25.6
    '''
    grados = 78
    resultado = convertir_a_centigrados(grados)
    assert isinstance(resultado, float), "el resultado debe ser decimal"
    assert resultado == 25.6, "el resultado no es correcto"


def test_convertir_a_centigrados_negativo():
    '''
    Los grados Fahrenheit son -79, el resultado debe
    ser igual a -110.2
    '''
    grados = -79
    resultado = convertir_a_centigrados(grados)
    assert isinstance(resultado, float), "el resultado debe ser decimal"
    assert resultado == -61.7, "el resultado no es correcto"
