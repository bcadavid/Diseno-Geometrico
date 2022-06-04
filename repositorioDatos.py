import csv

class RepositorioDatos:
  def __init__(self):
    self.nombreArchivoPuntosControl = "datos/puntosControl.txt"
    self.nombreArchivoNodos = "datos/nodos.txt"
    return

  def getNombreArchivoPuntosControl(self):
    return self.nombreArchivoPuntosControl
  
  def getNombreArchivoNodos(self):
    return self.nombreArchivoNodos
  
  def obtenerPuntosControl(self):
    #TODO: manejar excepciones
    with open(self.nombreArchivoPuntosControl, 'r') as archivo:
      lineas = csv.reader(archivo)
      puntosControl = self.convertirLineasAPuntos(lineas)
    return puntosControl
  
  def obtenerNodos(self):
    #TODO: manejar excepciones
    with open(self.nombreArchivoNodos, 'r') as archivo:
      lineas = csv.reader(archivo)
      knots = self.convertirLineasALista(lineas)
    return knots

  def convertirLineasALista(self, lineas):
    lista = []
    for linea in lineas:
      #TODO: manejar excepciones
      lista.append(float(linea[0]))
    return lista
  
  def convertirLineasAPuntos(self, lineas):
    puntos = []
    for linea in lineas:
        #TODO: manejar excepciones
        x = float(linea[0])
        y = float(linea[1])
        puntos.append([x, y])
    return puntos


