# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 12:11:23 25

@author: GERARDO S
"""
n = input("introduce un valor numperico: ")

try:
    n = int(n)
    if n > 0:
        print("el número es entero y positivo.")
    else:
        print("error: el número debe ser positivo.")
except:
    print("error: debes ingresar un número entero.")

