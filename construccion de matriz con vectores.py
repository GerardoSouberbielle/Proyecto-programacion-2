# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 02:34:00 2025

@author: Asus
"""

import random


tamanio_dimension = 3 # Valor fijo para pruebas rápidas

try:
  
    if tamanio_dimension > 0:
        lista_numeros_base = [random.randint(1, 9) for _ in range(tamanio_dimension)]
        print(f"Lista base generada: {lista_numeros_base}")

        matriz_resultante = []
        for i in range(tamanio_dimension):
            fila_actual = [elemento * (i + 1) for elemento in lista_numeros_base]
            matriz_resultante.append(fila_actual)

        print("\nMatriz de múltiplos (por fila):")
        for indice_fila, fila in enumerate(matriz_resultante):
            print(f"Fila {indice_fila + 1}: {fila}") # Mostramos el número de fila para más claridad
    else:
        print("Error: La dimensión debe ser un número entero positivo.")

except ValueError:
    print("Error: Entrada no válida. Asegúrate de introducir un número entero.")