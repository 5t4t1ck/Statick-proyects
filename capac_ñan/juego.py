#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine

pilas = pilasengine.iniciar()

# Definimos las teclas que moverán al personaje
teclas = {pilas.simbolos.a:'izquierda', pilas.simbolos.s:'derecha'}
# Creamos un control personalizado con esas teclas
mandos = pilas.control.Control(teclas)

VELOCIDAD = 5

class Wari(pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = pilas.imagenes.cargar_grilla("imagenes/corriendo.png",4)
        self.hacer("Esperando")
        self.escala = 0.25

    def definir_cuadro(self, indice):
        self.imagen.definir_cuadro(indice)

class Esperando(pilasengine.comportamientos.Comportamiento):
    '''Actor en posicion normal hasta que el usuario pulse alguna tecla'''

    def iniciar(self, receptor):
        self.receptor = receptor
        self.receptor.definir_cuadro(3)

    def actualizar(self):
        if mandos.izquierda:
            self.receptor.hacer_inmediatamente("Caminando")
        elif mandos.derecha:
            self.receptor.hacer_inmediatamente("Caminando")

class Caminando(pilasengine.comportamientos.Comportamiento):
    '''Accion de caminar del actor'''
    def iniciar(self, receptor):
        self.receptor = receptor
        self.cuadros = [0,0,0,0,1,1,1,1,2,2,2,2,0,0,0,0,1,1,1,1,2,2,2,2]
        self.paso = 0

    def actualizar(self):
        self.avanzar_animacion()

        if mandos.izquierda:
            self.receptor.espejado = False
            self.receptor.x -= VELOCIDAD
        elif mandos.derecha:
            self.receptor.espejado = True
            self.receptor.x += VELOCIDAD
        else:
            self.receptor.hacer_inmediatamente("Esperando")


    def avanzar_animacion(self):
        self.paso += 1
        if self.paso>=len(self.cuadros):
            self.paso = 0

        self.receptor.definir_cuadro(self.cuadros[self.paso])


class EscenaWari(pilasengine.escenas.Escena):
    def iniciar(self):
        self.pilas.fondos.Fondo("imagenes/fondo.png")
#        self.pilas.actores.Wari()

pilas.fondos.Fondo("imagenes/fondo.png")
pilas.comportamientos.vincular(Caminando)
pilas.comportamientos.vincular(Esperando)
#pilas.escenas.vincular(EscenaWari)
pilas.actores.vincular(Wari)

#pilas.escenas.EscenaWari()
pilas.actores.Wari()

pilas.ejecutar()
