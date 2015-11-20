import pilasengine

pilas = pilasengine.iniciar()

class personaje(pilasengine.actores.Actor):

    def iniciar(self):
	#self.imagen = "imagenes/corriendo.png"
	    imagen = pilas.imagenes.cargar("imagenes/corriendo.png")
        imagen.self = personaje(imagen)

    def actualizar(self):
        pass

wari = personaje(pilas)

pilas.ejecutar()
