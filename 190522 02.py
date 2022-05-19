"""
class Bicicleta:
    RODADO = 26
    def __init__(self,marca):
        self.marca = marca

bici = Bicicleta("BiciFlash")
print(bici.RODADO)
"""
class Auto:
    PUERTAS = 5

    def __init__(self,marca,modelo,color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    @classmethod
    def get_auto_fiat(cls,modelo,color):
        return cls("Fiat",modelo,color)

    @classmethod
    def get_uno(cls,marca,color):
        return  cls(marca,"uno",color)

    @classmethod
    def get_uno_rojo(cls,marca):
        return cls(marca,"uno","Rojo")

    @classmethod
    def get_147(cls,marca,color):
        return cls(marca,"147",color)

    @classmethod
    def get_147_gris(cls,marca):
        return cls(marca,"147","Gris")

    def __str__(self):
        return ("marca: {} \nmodelo: {} \ncolor: {}").format(self.marca,self.modelo,self.color)

auto1 = Auto.get_auto_fiat(3,"Rojo")
print(auto1)

