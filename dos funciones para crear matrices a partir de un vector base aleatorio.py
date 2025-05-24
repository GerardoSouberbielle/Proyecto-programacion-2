# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 00:47:20 2025

@author: Asus
"""

import random

# --- Funciones para la Generación de Matrices ---

def generar_matriz_multiplicada_por_filas(dimension):
    """
    Genera un vector base aleatorio y una matriz donde cada elemento
    de la matriz es el elemento correspondiente del vector base
    multiplicado por (índice_fila + 1).
    """
    vector_base = [random.randint(1, 9) for _ in range(dimension)]
    print(f"Vector base (para multiplicación por filas): {vector_base}")

    matriz_por_filas = []
    for i in range(dimension): # i representa el factor de multiplicación de la fila (1, 2, 3...)
        fila_actual = [elemento_vector * (i + 1) for elemento_vector in vector_base]
        matriz_por_filas.append(fila_actual)

    print("Matriz resultante (multiplicada por filas):")
    for fila in matriz_por_filas:
        print(fila)

def generar_matriz_multiplicada_por_columnas(dimension):
    """
    Genera un vector base aleatorio y una matriz donde cada elemento
    de la matriz en la posición (i, j) es el elemento ve[i]
    multiplicado por (j + 1).
    """
    vector_ejemplo = [random.randint(1, 9) for _ in range(dimension)]
    print(f"\nVector base (para multiplicación por columnas): {vector_ejemplo}")

    
    matriz_por_columnas = []
    for i in range(dimension): # Itera sobre los elementos del vector
        fila_generada = [vector_ejemplo[i] * (j + 1) for j in range(dimension)]
        matriz_por_columnas.append(fila_generada)

    print("Matriz resultante (multiplicada por columnas):")
    for fila in matriz_por_columnas:
        print(fila)


dimension_principal = 4 # Valor fijo para pruebas

try:
  

    if dimension_principal > 0:
        generar_matriz_multiplicada_por_filas(dimension_principal)
        generar_matriz_multiplicada_por_columnas(dimension_principal)
    else:
        print("Error: La dimensión debe ser un número entero positivo.")
except ValueError:
    print("Error: La entrada no es un número entero válido.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")