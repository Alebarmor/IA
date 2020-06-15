import math
import random

#Clase PUNTO
class Punto(object):

        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y

        def distancia_al_origen(self):
            return math.hypot(self.x, self.y)

        def __eq__(self, otro):
            return self.x == otro.x and self.y == otro.y

        def __str__(self):
            return "({0.x!r}, {0.y!r})".format(self)

        def distancia_punto_punto(self, p):
            xs = (p.x - self.x)**2
            ys = (p.y - self.y)**2
            sum = xs + ys
            return math.sqrt(sum)
        
        def __repr__(self):
            return str(self)
            

#STR to PUNTO        
def point(str):
    str = str.replace("(", "")
    str = str.replace(")", "")
    s = str.split(",")
    x = int(s[0])
    y = int(s[1])
    return Punto(x,y)

#Clase CIRCULO
class Circulo(Punto):

        def  __init__(self, radio, x, y):
            super().__init__(x, y)
            self.radio = radio

        def distancia_del_borde_al_origen(self):
            return abs(self.distancia_al_origen() - self.radio)

        def area(self):
            return math.pi * (self.radio**2)

        def circunferencia(self):
            return 2 * math.pi * self.radio

        def __eq__(self, otro):
            return self.radio == (otro.radio and
            super().__eq__(otro,self))

        def __str__(self):
            return "Círculo({0.radio!r}, {0.x!r}, {0.y!r})".format(self)

        def distancia_circulo_punto(self, t):
            p = Punto(self.x,self.y)
            d = p.distancia_punto_punto(t)    
            return abs(d - self.radio)
        
        def __repr__(self):
            return str(self)

#Obtener lista PUNTOS de un TXT        
def lista_puntos(str):
    puntos = open(str, "r")
    with puntos as p:
        lines = p.read().splitlines()
    i = 0
    n = len(lines)
    lista_puntos = []
    while i < n:
        p = lines[i]
        punto = point(p)
        lista_puntos.append(punto)
        i += 1
    return lista_puntos

#Obetener lista distancias
def lista_distancias(l, c):
    i = 0
    n = len(l)
    res = []
    while i < n:
        d = c.distancia_circulo_punto(l[i])
        res.append(d)
        i += 1
    return res


#metodo que dado una lista de puntos devuelva una lista de posibles circulos(a especificar)
# p = lista de puntos, c=numero de circulos, r=radio maximo
def posibles_centros_aleatorios(p, c, r):
    i=0
    l=lado_cuadrado(p)
    maximo=l[0]
    minimo=l[1]
    res=[]
    
    while i<c:
       x=random.randint( minimo,  maximo)   
       y=random.randint( minimo,  maximo)
       radio=random.randint(1,r)
       circulo=Circulo(radio, x, y)
       res.append(circulo)
       i += 1
       
    return res


#metodo para calcular los valores minimo y maximo(p=lista de puntos)
def lado_cuadrado(p):
    maximo=120
    minimo=120
    
    for e in p:
        if e.y > maximo or maximo==120: maximo=e.y
        if e.x > maximo: maximo=e.x
        if e.y < minimo or minimo==120: minimo=e.y
        if e.x < minimo: minimo=e.x
        
    lista = [maximo, minimo]
        
    return lista