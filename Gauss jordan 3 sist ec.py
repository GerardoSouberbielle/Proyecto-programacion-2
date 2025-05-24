# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 00:59:00 2025

@author: Asus
"""

import numpy as np


matriz_A_sistema = np.array([[1, 2, 1],
                             [3, 8, 1],
                             [0, 4, 1]], dtype=float)

vector_b_sistema = np.array([2, 12, 2], dtype=float)

print("--- Sistema de Ecuaciones a Resolver ---")
print("Matriz A:\n", matriz_A_sistema)
print("Vector b:", vector_b_sistema)
print("-" * 40, "\n")

# --- Métodos de Resolución ---

def resolver_con_gauss_jordan(A_mat, b_vec):
    
    n_dim = len(b_vec)
    matriz_aumentada = np.column_stack((A_mat.copy(), b_vec.copy()))

    print("### Solución por Eliminación de Gauss-Jordan ###")
    print("Matriz Aumentada Inicial:\n", matriz_aumentada)

    for i in range(n_dim):
        if matriz_aumentada[i, i] == 0:
            pivot_encontrado = False
            for k in range(i + 1, n_dim):
                if matriz_aumentada[k, i] != 0:
                    matriz_aumentada[[i, k]] = matriz_aumentada[[k, i]] # Intercambio de filas
                    pivot_encontrado = True
                    break
            if not pivot_encontrado:
                print("Advertencia: Pivote cero insalvable. La matriz puede ser singular.")
                return None

        matriz_aumentada[i] /= matriz_aumentada[i, i]

        for j in range(n_dim):
            if i != j:
                matriz_aumentada[j] -= matriz_aumentada[j, i] * matriz_aumentada[i]
    
    solucion_gj = matriz_aumentada[:, -1]
    print("Matriz Aumentada Final (Identidad a la izquierda):\n", matriz_aumentada)
    print("Solución (x):", np.round(solucion_gj, 6)) # Redondeo para claridad
    print("-" * 40, "\n")
    return solucion_gj

def resolver_con_inversa(A_mat, b_vec):
  
    print("### Solución por Matriz Inversa (np.linalg.inv) ###")
    try:
        inversa_A = np.linalg.inv(A_mat)
        print("Inversa de A:\n", np.round(inversa_A, 6))
        solucion_inv = inversa_A @ b_vec # Multiplicación matricial
        print("Solución (x):", np.round(solucion_inv, 6))
    except np.linalg.LinAlgError:
        print("Error: La matriz A no es invertible. Este método no es aplicable.")
    print("-" * 40, "\n")
    return solucion_inv

def resolver_con_cramer(A_mat, b_vec):
   
    print("### Solución por Regla de Cramer ###")
    det_A_principal = np.linalg.det(A_mat)

    if np.isclose(det_A_principal, 0):
        print("Error: El determinante de A es cero. La Regla de Cramer no es aplicable.")
        return None

    soluciones_cramer = []
    n_dim = len(b_vec)

    for i in range(n_dim):
        A_temporal_cramer = A_mat.copy()
        A_temporal_cramer[:, i] = b_vec
        det_Ai = np.linalg.det(A_temporal_cramer)
        soluciones_cramer.append(det_Ai / det_A_principal)
    
    print("Determinante de A:", np.round(det_A_principal, 6))
    print("Solución (x):", np.round(np.array(soluciones_cramer), 6))
    print("-" * 40, "\n")
    return np.array(soluciones)


