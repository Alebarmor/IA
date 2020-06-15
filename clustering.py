from imports import *

#VALORES INICIALES
umbral = 20
p = lista_puntos(r"C:\Users\Fernando\Downloads\IA-master\Puntos.txt")
c1 = Circulo(2, 2, 2)
c2 = Circulo(2, -2, 2)

distances1 = lista_distancias(p, c1)
distances2 = lista_distancias(p, c2)

#Método sencillo que comprueba que estén por debajo del umbral y asigna un punto a uno de los dos circulos
#Si la distancia de un punto a cualquiera de los circulos es la misma, se asigna a C1

# byV Intenta mejorar la representacion que es una kk
i = 0
n = len(p)
clusters = {}
while i < n:
    d1 = distances1[i]
    d2 = distances2[i]
    if (d1 < d2) and (d1 < umbral):
        clusters["P" + str(i+1)] = ["C1"]
        i += 1
    elif (d2 < d1) and (d2 < umbral):
        clusters["P" + str(i+1)] = ["C2"]
        i += 1
    elif (d1 == d2) and (d1 < umbral):
        clusters["P" + str(i+1)] = ["C1"]
        i += 1
    else:
        i += 1
        
print(clusters)

