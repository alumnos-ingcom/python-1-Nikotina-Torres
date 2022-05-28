################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
1. Conversión de temperaturas

Se quiere transformar temperaturas en grados fahrenheit a grados
centígrados y viceversa.

Escribir las funciones para convertir la temperatura en grados
centigrados en fahrenheit como un número decimal,
utilice esta formula para calcular los grados centígrados y
retorne el resultado obtenido. Y viceversa.
"""
#Pre-condiciones: Dos números representando grados de temperatura
#en centigrados y fahrenheit, respectivamente.
#Post-condiciones: Los grados centigrados pasados a
#grados fahrenheit y viceversa, en decimal.

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    centigrados=float(input("Ingrese grados centigrados"))
    fahrenheit=float(input("Ingrese grados fahrenheit"))


    resultado_f = round(convertir_a_fahrenheit(centigrados),1)
    resultado_c = round(convertir_a_centigrados(fahrenheit),1)


    print(f"{centigrados}C° es igual a: {resultado_f} Fahrenheit")
    print(f"{fahrenheit}F° es igual a: {resultado_c} Centigrados")


def convertir_a_fahrenheit(c):
    '''
    Esta función se encarga de hacer la fórmula matemática
    para pasar de grados Centigrados a Fahrenheit
    (C son los grados en centigrados y el return lo devuelve como Fahrenheit)
    '''
    return (c * 9/5) + 32

def convertir_a_centigrados(f):
    '''
    Esta función se encarga de hacer la fórmula matemática para
    pasar de grados Fahrenheit a Centigrados
    (F son los grados en Fahrenheit y el return lo devuelve como Centigrados)
    '''
    return (f - 32) * 5/9

if __name__ == "__main__":
    principal()
