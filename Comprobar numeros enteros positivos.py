"""
Created on Fri Apr 12 18:15:09 2025

@author: Asus
"""
numero_ingresado_str = "5" # Cambiado de 'N' a 'numero_ingresado_str' y el valor de 3 a 5

try:
    # Intenta convertir la entrada a un número entero.
    valor_entero = int(numero_ingresado_str) # Cambiado de 'N' a 'valor_entero'

    # Verifica si el número es positivo.
    if valor_entero > 0:
        print(f"El número {valor_entero} es un entero y es positivo. ¡Excelente!")
    elif valor_entero == 0:
        print(f"El número {valor_entero} es cero, que no es ni positivo ni negativo.")
    else:
        print(f"Error: El número {valor_entero} es un entero, pero es negativo.")

except ValueError:
    # Maneja el caso en que la entrada no es un número entero válido.
    print(f"Error: '{numero_ingresado_str}' no es un número entero válido. Por favor, introduce un valor numérico.")

