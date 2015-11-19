import pilasengine

pilas = pilasengine.iniciar()

class gorro_Navidad(pilasengine.actores.Actor):

    def iniciar(self):
        #self.imagen = "imagenes/gorro.png"
        self.y = 300
        self.x = pilas.azar(-250, 250)
        self.velocidad = 0
        self.radio_de_colision = 50
        self.escala = 0.70

    def actualizar(self):
        self.velocidad += 0.05
        self.y -= self.velocidad
        self.rotacion += 2

        if self.y < -400:
            self.eliminar()

gorro = gorro_Navidad(pilas)
fondo = pilas.fondos.Fondo()
fondo.imagen = pilas.imagenes.cargar("imagenes/fondo.png")
pilas.ejecutar()
