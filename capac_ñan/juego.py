#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine

pilas = pilasengine.iniciar()

# Definimos las teclas que moverán al personaje
#teclas = {pilas.simbolos.a:'izquierda', pilas.simbolos.s:'derecha'}
# Creamos un control personalizado con esas teclas
#mandos = pilas.control.Control(teclas)


class Wari(pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = pilas.imagenes.cargar_grilla("imagenes/corriendo.png",16)
        self.cuadro = 0
        self.aprender(pilas.habilidades.MoverseConElTeclado)

    def actualizar(self):
        pass

pilas.actores.vincular(Wari)

persona = pilas.actores.Wari()
pilas.ejecutar()
