# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 00:12:01 2025

@author: Asus
"""

import numpy as np


matriz_A = np.array([[4, -2, 1],
                     [-2, 4, -2],
                     [1, -2, 4]], dtype=float)

vector_b = np.array([11, -16, 17], dtype=float)

print("--- Sistema de Ecuaciones ---")
print("Matriz A:\n", matriz_A)
print("Vector b:", vector_b)
print("-" * 30, "\n")


def resolver_gauss_jordan(A_matriz, b_vector):
    """
    Resuelve un sistema de ecuaciones lineales Ax=b usando el método de Gauss-Jordan.
    """
    n_dimension = len(b_vector)
    # Crear la matriz aumentada [A|b]
    matriz_aumentada = np.column_stack((A_matriz.copy(), b_vector.copy()))

    print("--- Método de Gauss-Jordan ---")
    print("Matriz Aumentada Inicial:\n", matriz_aumentada)

    for i in range(n_dimension):
        if matriz_aumentada[i, i] == 0:
            for j in range(i + 1, n_dimension):
                if matriz_aumentada[j, i] != 0:
                    matriz_aumentada[[i, j]] = matriz_aumentada[[j, i]] # Intercambio de filas
                    break
            else: 
                print("Advertencia: No se pudo resolver por Gauss-Jordan (matriz singular o problemas de pivoteo).")
                return None

        matriz_aumentada[i] = matriz_aumentada[i] / matriz_aumentada[i, i]

        for j in range(n_dimension):
            if i != j:
                matriz_aumentada[j] = matriz_aumentada[j] - matriz_aumentada[j, i] * matriz_aumentada[i]
    
    solucion_gauss = matriz_aumentada[:, -1]
    print("Matriz Aumentada Final (Identidad a la izquierda):\n", matriz_aumentada)
    print("Solución por Gauss-Jordan (x):", solucion_gauss)
    print("-" * 30, "\n")
    return solucion_gauss

def resolver_por_inversa(A_matriz, b_vector):
    
    print("--- Solución Usando la Inversa de la Matriz ---")
    try:
        inversa_A = np.linalg.inv(A_matriz)
        print("Matriz Inversa de A:\n", inversa_A)
        solucion_inversa = inversa_A @ b_vector # Multiplicación matricial
        print("Solución por Inversa (x):", solucion_inversa)
    except np.linalg.LinAlgError:
        print("Error: La matriz A no es invertible. No se puede usar este método.")
    print("-" * 30, "\n")
    return solucion_inversa

def resolver_regla_cramer(A_matriz, b_vector):
   
    print("--- Solución Usando la Regla de Cramer ---")
    det_A_original = np.linalg.det(A_matriz)

    if det_A_original == 0:
        print("Error: El determinante de A es cero. La Regla de Cramer no es aplicable.")
        return None