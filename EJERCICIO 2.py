# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 12:00:02 2025

@author: GERARDO S
"""
from random import randint

n = int(input("introduce un valor numérico: "))

if n > 0:
    v = []
    for i in range(n):
        v.append(randint(1, 9))
    print("vector generado:", v)
else:
    print("error: el número debe ser entero y positivo.")