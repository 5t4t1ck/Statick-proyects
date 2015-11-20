import pilasengine

pilas = pilasengine.iniciar()

class personaje(pilasengine.actores.Actor):

    def iniciar(self):
	self.imagen = "imagenes/corriendo.png"
	
    def actualizar(self):
        pass

wari = personaje(pilas)

pilas.ejecutar()
