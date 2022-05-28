################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio1 import convertir_a_fahrenheit, convertir_a_centigrados
"""
Probando funciones para convertir entre grados centigrados a Fahrenheit,
y viceversa.
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""


   
def test_convertir_a_fahrenheit():
    '''
    Los grados centigrados son 78, el resultado debe 
    ser igual a 172.4
    '''
    grados = 78
    resultado = convertir_a_fahrenheit(grados)
    assert isinstance(resultado, float), "el resultado debe ser decimal"
    assert resultado == 172.4, "el resultado no es correcto"
    
def test_convertir_a_centigrados():
    '''
    Los grados centigrados son 78, el resultado debe 
    ser igual a 25.6
    '''
    grados = 78
    resultado = convertir_a_centigrados(grados)
    assert isinstance(resultado, float), "el resultado debe ser decimal"
    assert round(resultado, 1) == 25.6, "el resultado no es correcto"
