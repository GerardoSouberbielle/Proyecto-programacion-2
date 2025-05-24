# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 00:12:56 2025

@author: Asus
"""

import numpy as np


matriz_coeficientes_A = np.array([[1, 1, 1],    # para x=1
                                  [1, 2, 5],    # para x=2
                                  [1, 4, 25]], dtype=float) # para x=4

vector_constante_b = np.array([6, 12, 36], dtype=float)

print("--- Sistema de Ecuaciones Lineales ---")
print("Matriz A (Coeficientes):\n", matriz_coeficientes_A)
print("Vector b (Términos Independientes):", vector_constante_b)
print("-" * 40, "\n")

# --- Funciones para Resolver y Analizar el Sistema ---

def resolver_gauss_jordan(A_mat, b_vec):
    """
    Resuelve el sistema Ax=b utilizando el método de Eliminación de Gauss-Jordan.
    """
    dimension_n = len(b_vec)
    matriz_aumentada_gj = np.column_stack((A_mat.copy(), b_vec.copy()))

    print("--- Solución por Eliminación de Gauss-Jordan ---")
    print("Matriz Aumentada Inicial:\n", matriz_aumentada_gj)

    for i in range(dimension_n):
        if matriz_aumentada_gj[i, i] == 0:
            pivot_encontrado = False
            for k in range(i + 1, dimension_n):
                if matriz_aumentada_gj[k, i] != 0:
                    matriz_aumentada_gj[[i, k]] = matriz_aumentada_gj[[k, i]] # Intercambiar filas
                    pivot_encontrado = True
                    break
            if not pivot_encontrado:
                print("Advertencia: No se pudo encontrar un pivote no nulo. La matriz podría ser singular.")
                return None

        matriz_aumentada_gj[i] = matriz_aumentada_gj[i] / matriz_aumentada_gj[i, i]

        # Eliminar elementos de otras filas (hacerlos cero)
        for j in range(dimension_n):
            if i != j:
                matriz_aumentada_gj[j] = matriz_aumentada_gj[j] - matriz_aumentada_gj[j, i] * matriz_a