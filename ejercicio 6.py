"""
Crear la clase Punto en el plano que contiene:
2 atributos (x, y) que representan las coordenadas del Punto en el plano
El constructor de la clase Punto que recibe x e y que son las coordenadas
Por defecto setear x e y en el centro de coordenadas
Los métodos getter y setter de los atributos
El método toString()
Método cuadrante() que devuelve un nro entre 0 y 4 que indica el cuadrante en el cual se encuentra el Punto.
Método distanciaAlCentro() que devuelve un número que representa la distancia entre el punto y el centro de coordenadas.
 (x1 - x2) al cuadrado + (y1 - y2) al cuadrado -> aplicar raiz cuadrada

"""
import math

class Punto:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def set_origen(self):
        y=0
        x=0

    def set_y(self,y):
        self.y = y

    def set_x(self,x ):
        self.x = x

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "primer cuadrante"
        elif self.x > 0 and self.y >= 0:
            return "primer cuadrante"
        elif self.x <= 0 and self.y >=0:
            return "segundo cuadrante"
        elif self.x<= 0 and self.y < 0:
            return "tercer cuadrante"
        elif self.x<0 and self.y <= 0:
            return "cuarto cuadrante"
        else:
            return "error"

    def distanciaAlCentro(self,y,x):
        x1= x
        x2= self.x
        y1= y
        y2= self.y
        formula_ala2 = (x1 - x2)**2 + (y1 - y2)**2
        return math.sqrt(formula_ala2)

    def __str__(self):
        jamon = "x={} y={}".format(self.x,self.y)
        return jamon

el_punto = Punto(0,0)
print(el_punto.cuadrante())
