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


   
def test_convertir_a_fahrenheit(C):
    '''
    Probar convertir 50 grados centigrados a Fahrenheit 
    '''
    G = 50
    resultado = convertir_a_fahrenheit(G)
    assert isinstance(resultado, str) "el resultado tiene que ser decimal"
    
def test_convertir_a_centigrados(F):
    '''
    Probar convertir 50 grados Fahrenheit a centigrados
    '''
    G = 50
    resultado = convertir_a_centigrados(G)
    assert isinstance(resultado, str) "el resultado tiene que ser decimal"
