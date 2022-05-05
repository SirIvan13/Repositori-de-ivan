class TuboDePelotas:
   def __init__(self,capacidad_maxima,marca,isAbierto,cantidad):
       self.capacidad_maxima = capacidad_maxima
       self.marca = marca
       self.isAbierto = isAbierto
       self.cantidad = cantidad

   def abrir(self):
       self.isAbierto = True  # Asignar un atributo

   def cerrar(self):
       self.isAbierto = False

   def mover_tapa(self):
       not self.isAbierto

   def agregar_pelota(self):
       if self.cantidad + 1 <= self.capacidad_maxima:
           self.cantidad + 1

   def quitar_pelota(self):
       if self.cantidad - 1 >= 0:
           self.cantidad - 1

      #Sobre escritura
   def __str__(self):
       jamon = "capacidad maxima: {} \nmarca: {}\n\rcantidad: {}\n\rEsta abierto: {}".format(self.capacidad_maxima,self.marca,self.cantidad,self.isAbierto)
       return jamon

#   def __eq__(self, otherTubo):
#      return self.capacidad_maxima == otherTubo.capacidad_maxima

   def get_marca(self):
       return self.marca

   def set_marca(self,marca):
       self.marca = marca

tubo_De_Pelotas = TuboDePelotas(10,"addivas",False,8)
tubo_De_PelotasB = TuboDePelotas(14,"addivas",False,7)
tubo_De_Pelotas.set_marca("Niqe")
print(tubo_De_Pelotas.get_marca())


#instanciar es crear un objeto a partir de nuestra plantilla
#nuestra plantilla es la clase
