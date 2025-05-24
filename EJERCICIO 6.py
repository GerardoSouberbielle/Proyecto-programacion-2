# -*- coding: utf-8 -*-
"""
Created on Mon Feb  10 13:01:2025

@author: GERARDO S 
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 20, 100)
plt.plot(x, x**2, label="x^2")
plt.plot(x, x**3, label="x^3")
plt.plot(x, x, label="x")
plt.xlabel("x")
plt.ylabel("y")
plt.title("funciones x^2, x^3 y x")
plt.legend()
plt.grid(True)
plt.show()