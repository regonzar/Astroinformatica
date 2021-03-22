import numpy as np

def createandsort (n):
 rand = np.random.RandomState(42) #semilla para reproducir mismos numeros
 a = rand.rand(n) #array de n elementos random
 return a.sort() #Ordena de menor a menor (nlogn nro de operaciones)

