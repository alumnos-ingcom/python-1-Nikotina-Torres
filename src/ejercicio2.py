################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Números positivos y negativos

Escribir una función que reciba un número e indique si el mismo es positivo, negativo o cero utilizando sumas y restas.
"""
#Pre condiciones: Un número real
#Post condiciones: Una salida que especifique si el numero ingresado es negativo, cero o positivo


def signo(numero):
    if numero+numero < 0:
        return "Negativo";
    elif numero+numero > 0:
        return "Positivo";
    else:
        return "Cero";



def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero=float(input("Ingrese un número"))
    print(signo(numero))

if __name__ == "__main__":
    principal()

