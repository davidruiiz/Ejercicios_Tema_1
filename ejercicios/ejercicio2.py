"""
Ejercicio 2
Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:
Guarda en una variable numero_magico el valor 12345679 (sin el 8)
Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9
Multiplica el numero_usuario por 9 en sí mismo
Multiplica el numero_magico por el numero_usuario en sí mismo
Finalmente muestra el valor final del numero_magico por pantalla
"""

from ast import main
import sys


numero_magico = 12345679

def excepcion(numero):  
    try:
        numero=int(numero) 
        if 1<=int(numero)<=9:
            return int(numero)
        else:
            raise ValueError("El número no está entre 1 y 9")
    except:
        raise ValueError("El caracter no aceptado")
    
def num(numero):
    numero=excepcion(numero)
    return f'Resultado: {numero*9*numero_magico}'

