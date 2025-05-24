# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 00:02:23 2025

@author: Asus
"""
import random


tamanio_vector = 6 # Cambiado de 'N' a 'tamanio_vector'

# Intenta convertir la entrada a entero y maneja errores si no es un número válido
try:

    # Verifica si el tamaño del vector es positivo
    if tamanio_vector > 0:
        # Genera una lista de números aleatorios entre 1 y 9
        # Cambiado de 'v' a 'vector_resultante'
        vector_resultante = [random.randint(1, 9) for _ in range(tamanio_vector)]
        print(f"Vector generado: {vector_resultante}")
    else:
        # Mensaje de error si el número no es positivo
        print("Error: El número introducido debe ser un entero positivo.")

except ValueError:
    # Mensaje de error si la entrada no es un número
    print("Error: Entrada no válida. Por favor, introduce un número entero.")