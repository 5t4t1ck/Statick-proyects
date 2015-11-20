#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine

pilas = pilasengine.iniciar()

# Definimos las teclas que moverán al personaje
teclas = {pilas.simbolos.a:'izquierda', pilas.simbolos.s:'derecha'}
# Creamos un control personalizado con esas teclas
mandos = pilas.control.Control(teclas)

class Wari(pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = pilas.imagenes.cargar_grilla("imagenes/corriendo.png",4)
        self.cuadro = 3
        self.aprender(pilas.habilidades.MoverseConElTeclado,control=mandos)

    def actualizar(self):
        # Miramos si se han pulsado las teclas adecudas para cambiar, en
        # su caso, la imagen de la grilla y hacia dónde mira
        if self.cuadro > 2:
            self.cuadro = 0

        if mandos.izquierda:
#            self.x -= VELOCIDAD
            if self.espejado:
                self.espejado = False
            self.cuadro += 1
            if self.cuadro == 3:
                self.cuadro = 0
        elif mandos.derecha:
#            self.x += VELOCIDAD
            if not self.espejado:
                self.espejado = True
            self.cuadro += 1
            if self.cuadro == 3:
                self.cuadro = 0
        else:
            self.cuadro = 3

        self.imagen.definir_cuadro(self.cuadro)

pilas.actores.vincular(Wari)

persona = pilas.actores.Wari()
pilas.ejecutar()
