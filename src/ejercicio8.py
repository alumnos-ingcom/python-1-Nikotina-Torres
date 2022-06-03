################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
8. Números primos

Escribir una función que indique con True si un numero indicado es Primo.
"""

def es_primo(numero):
    '''
    Esta función devolverá True si el (numero) ingresado es primo, y False si no lo es.
    sintaxis: es_primo(numero)
    '''
    contador = 2
    primo = True
    if numero == 1:
        primo = False
    elif numero == 2:
        primo = True
    else:
        while contador < numero and primo is True:
            if numero%contador == 0:
                primo = False
            else:
                primo = True
            contador += 1
    return primo

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input("Ingresar numero entero... "))
    print(es_primo(numero))

if __name__ == "__main__":
    principal()
