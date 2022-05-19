"""
Crear la clase Segmento que contiene:
2 atributos del tipo Punto que representan los extremos del Segmento,
El constructor de la clase Segmento que recibe dos parámetros del tipo Punto para los extremos
Sobrecarga del constructor que recibe 4 float que representan las coordenadas de los dos Puntos extremos del segmento
Los métodos getter y setter de los atributos
El método toString()
Un método longitudSegmento() que devuelve un número float que representa la longitud del segmento
"""

class Segmento:
    def __init__(self, punto1, punto2):
        self.extremo1 = punto1
        self.extremo2 = punto2

    def extremo1(self):
        