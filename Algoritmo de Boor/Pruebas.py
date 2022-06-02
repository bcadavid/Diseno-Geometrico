import numpy as np
import math as m
import matplotlib.pyplot as plt
from deBoor import  deBoor
points = np.array([[i, m.sin(i)] for i in range(0, 11)])
knots = np.array([0, 0, 0, 0, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0, 1.0, 1.0, 1.0])
p = 3
cant_divisiones = 10
X = []
Y = []
trazadores = []
maxpoints = len(knots) #maxima cantidad de nodos
for rango in range(p,maxpoints-p-1):
    divisiones = np.linspace(knots[rango],knots[rango+1],cant_divisiones)      
    for punto in divisiones:
        result = deBoor(rango, punto, knots, points, p)
        X.append(result[0])
        Y.append(result[1])
plt.plot(points[:,0], points[:,1],'.')
plt.plot(X,Y)
plt.show()
