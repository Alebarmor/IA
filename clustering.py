from imports import *
from imports_clustering import *

#VALORES INICIALES
umbral = 20
p = lista_puntos("D:\lordk\Descargas\Python\Proyecto\Puntos.txt")
c0 = Circulo(1, 2, 2)
c1 = Circulo(1, -2, 2)
c2 = Circulo(2, 5, 6)
c = [c0, c1, c2]

distances1 = lista_distancias(p, c1)
distances2 = lista_distancias(p, c2)
    
clusters = mapa_grados(p, c)
        
print(clusters)