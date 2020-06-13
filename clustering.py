from imports import *
import random

#VALORES INICIALES
umbral = 0.5
p = lista_puntos("D:\lordk\Descargas\Python\Proyecto\puntos1.txt")
c0 = Circulo(2, 9, 5)
c1 = Circulo(1, 2, 2)
c = [circulo_aleatorio(2), circulo_aleatorio(1)]

clusters = mapa_grados(p, c)

print(clusters)