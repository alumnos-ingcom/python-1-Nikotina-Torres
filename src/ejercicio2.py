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
numero=float(input("Ingrese un número"))

def signo(numero):
    if numero+numero < 0:
        return "Negativo";
    elif numero+numero > 0:
        return "Positivo";
    else:
        return "Cero";
print(signo(numero))

