################
# Nombre - @Nikotina-Torres
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
7. Transformación de un número

Escribir un programa que permita transformar un número solicitado expresado en
grados, minutos y segundos a segundos a segundos. Y otra que haga el cambio en el
sentido contrario, devolviendo una tuple.

Recuerden que un grado son 60 minutos y un minuto son 60 segundos.
"""

def sexadecimal_a_decimal(horas, minutos, segundos):
    """
    Esta función se encarga de pasar (horas) y (minutos) especificados, a segundos
    ademas de sumar los (segundos) previamente especificados a toda la operación.
    sintaxis: sexadecimal_a_decimal(horas, minutos, segundos)
    """
    horas = horas*60
    minutos = (minutos + horas) * 60
    segundos = segundos + minutos
    return segundos

def decimal_a_sexadecimal(numero):
    """
    Esta función se encarga de descomponer un número en: grados o horas, minutos y segundos.
    sintaxis: decimal_a_sexadecimal(numero)
    """
    grados = round(numero)
    minutos_ent = round((numero - grados), 4)*60
    minutos = round(minutos_ent)
    segundos = round((minutos_ent - round(minutos))*60)
    return (grados, minutos, segundos)



def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    horas = int(input("Ingrese horas... "))
    minutos = int(input("Ingrese minutos... "))
    segundos = int(input("Ingrese segundos... "))
    total_segundos = sexadecimal_a_decimal(horas, minutos, segundos)
    print(f"{horas} horas, {minutos} minutos y {segundos} segundos son {total_segundos} segundos en total")

    numero = float(input("Ingrese grados... "))
    tuple_sexagecimal = decimal_a_sexadecimal(numero)
    print(f"{numero} son {tuple_sexagecimal[0]}° {tuple_sexagecimal[1]}' {tuple_sexagecimal[2]}''")

if __name__ == "__main__":
    principal()
