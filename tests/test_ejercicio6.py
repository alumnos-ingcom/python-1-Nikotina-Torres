################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio6 import ordenar_mayor_a_menor, ordenar_menor_a_mayor

try:
    from ejercicio3 import compara
except ImportError as exc:
    from src.ejercicio3 import compara


"""
Probando funcion de ordenar tres numeros de mayor a menor y de menor a mayor
Usando tanto numeros negativos como positivos.
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""

def test_ordenar_mayor_a_menor():
    """
       Una breve descripción del caso de prueba aplicado a la función
    """
    numero1 = -1
    numero2 = 1
    numero3 = -150
    resultado = ordenar_mayor_a_menor(numero1, numero2, numero3)
    assert resultado == (1, -1, -150), "Los numeros no estan bien ordenados"

def test_ordenar_menor_a_mayor():
    """
       Una breve descripción del caso de prueba aplicado a la función
    """
    numero1 = 152
    numero2 = 153
    numero3 = -152
    resultado = ordenar_menor_a_mayor(numero1, numero2, numero3)
    assert resultado == (-152, 152, 153), "Los numeros no estan bien ordenados"

