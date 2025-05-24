# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 12:41:48 2025

@author: GERARDO S
"""

import random

def multiplosfila(n):
    v = [random.randint(1, 9) for _ in range(n)]
    print("vector generado (fila):", v)
    m = []
    for i in range(n):
        fila = [v[j] * (i + 1) for j in range(n)]
        m.append(fila)
    for f in m:
        print(f)

def multiploscolumna(n):
    v = [random.randint(1, 9) for _ in range(n)]
    print("vector generado (columna):", v)
    m = []
    for i in range(n):
        columna = [v[i] * (j + 1) for j in range(n)]
        m.append(columna)
    for f in zip(*m):
        print(list(f))

n = int(input("introduce un número entero y positivo: "))

if n > 0:
    multiplosfila(n)
    multiploscolumna(n)
else:
    print("error: el número debe ser entero y positivo.")
