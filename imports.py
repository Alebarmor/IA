import math

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
            

#STR to PUNTO        
def point(str):
    str = str.replace("(", "")
    str = str.replace(")", "")
    s = str.split(",")
    x = s[0]
    y = s[1]
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

#Obtener PUNTOS de un TXT        
def lista_puntos(str):
    puntos = open(str, "r")
    with puntos as p:
        lines = p.read().splitlines()
    i = 0
    n = len(lines)
    lista_puntos = []
    while i < n:
        punto = lines[i]
        lista_puntos.append(punto)
        i += 1
    return lista_puntos