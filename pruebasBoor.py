import matplotlib.pyplot as plt

from repositorioDatos import RepositorioDatos
from boor import Boor

#Borrar
import numpy as np
import math as m

repo = RepositorioDatos()
controlPoints = repo.obtenerPuntosControl()
nodos = repo.obtenerNodos()

#TODO: Pedir al usuario por teclado o similar
gradoBSpline = 3

boor = Boor(controlPoints, nodos, gradoBSpline)
(xs, ys) = boor.calcularPuntos()

cxs = [controlPoints[i][0] for i in range(len(controlPoints))]
cys = [controlPoints[i][1] for i in range(len(controlPoints))]
plt.plot(cxs, cys,'.')
plt.plot(xs, ys)
plt.show()
