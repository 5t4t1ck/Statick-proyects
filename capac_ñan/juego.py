#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
import random
import sys

pilas = pilasengine.iniciar()

pilas.reiniciar_si_cambia(__file__)

VELOCIDAD = 5

class Wari(pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = pilas.imagenes.cargar_grilla("imagenes/corriendo.png",4)
        self.hacer("Esperando")
        self.escala = 0.25
        self.y = -160

    def definir_cuadro(self, indice):
        self.imagen.definir_cuadro(indice)

    def perder(self):
        self.comportamientos.perder = Perdiendo(self)
        mensaje_perdiendo = pilas.actores.Texto("Has perdido!!!")
        mensaje_perdiendo = 0
        mensaje_perdiendo = [1], 0.5

class Esperando(pilasengine.comportamientos.Comportamiento):
    '''Actor en posicion normal hasta que el usuario pulse alguna tecla'''

    def iniciar(self, receptor):
        self.receptor = receptor
        self.receptor.definir_cuadro(3)

    def actualizar(self):
        if pilas.escena_actual().control.izquierda:
            self.receptor.hacer_inmediatamente("Caminando")
        elif pilas.escena_actual().control.derecha:
            self.receptor.hacer_inmediatamente("Caminando")
        elif pilas.escena_actual().control.arriba:
            self.receptor.hacer_inmediatamente("Saltando")
        else:
            self.receptor.hacer_inmediatamente("Esperando")

class Caminando(pilasengine.comportamientos.Comportamiento):
    '''Accion de caminar del actor'''
    def iniciar(self, receptor):
        self.receptor = receptor
        self.cuadros = [0,0,0,0,1,1,1,1,2,2,2,2,0,0,0,0,1,1,1,1,2,2,2,2]
        self.paso = 0

    def actualizar(self):
        self.avanzar_animacion()

        if pilas.escena_actual().control.izquierda:
            self.receptor.espejado = False
            self.receptor.x -= VELOCIDAD
            if pilas.escena_actual().control.arriba:
                self.receptor.hacer_inmediatamente("Saltando")
        elif pilas.escena_actual().control.derecha:
            self.receptor.espejado = True
            self.receptor.x += VELOCIDAD
            if pilas.escena_actual().control.arriba:
                self.receptor.hacer_inmediatamente("Saltando")
        elif pilas.escena_actual().control.arriba:
            self.receptor.hacer_inmediatamente("Saltando")
        else:
            self.receptor.hacer_inmediatamente("Esperando")

    def avanzar_animacion(self):
        self.paso += 1
        if self.paso>=len(self.cuadros):
            self.paso = 0

        self.receptor.definir_cuadro(self.cuadros[self.paso])

class Saltando(pilasengine.comportamientos.Comportamiento):
    def iniciar(self, receptor):
        self.receptor = receptor
        self.y_inicial = self.receptor.y
        self.pos_final = 15
        self.cuadros = [2, 3]
        self.vy = 10

    def actualizar(self):
        self.receptor.y += self.vy
        self.vy -= 0.7

        self.receptor.definir_cuadro(self.cuadros[0])

        distancia_al_suelo = self.receptor.y - self.y_inicial
        self.receptor.altura_del_salto = distancia_al_suelo

        # Cuando llega al suelo, regresa al estado inicial.
        if distancia_al_suelo < 0:
            self.receptor.y = self.y_inicial
            self.receptor.altura_del_salto = 0
            self.receptor.hacer_inmediatamente("Esperando")

        # Si pulsa a los costados se puede mover.
        if pilas.escena_actual().control.derecha:
            self.receptor.x += VELOCIDAD
            self.receptor.espejado = True
        elif pilas.escena_actual().control.izquierda:
            self.receptor.x -= VELOCIDAD
            self.receptor.espejado = False

class EscenaWari(pilasengine.escenas.Escena):
    def iniciar(self):
        self.pilas.fondos.Fondo("imagenes/fondo.png")
        pilas.tareas.agregar(2, crear_enemigo)

class Enemigo(pilasengine.actores.Bomba):

    def iniciar(self):
        pilasengine.actores.Bomba.iniciar(self)
        self.izquierda = 320
        self.x = random.randint(-320, 320)
        self.y = random.randint(-120, -100)

    def actualizar(self):
        pilasengine.actores.Bomba.actualizar(self)

class Perdiendo(pilasengine.comportamientos.Comportamiento):

    def iniciar(self):
        self.w.definir_animacion([3])
        self.velocidad = -2

    def actualizar(self):
        self.w.rotacion += 7
        self.w.escala -= 0.01
        self.w.x -= self.velocidad
        self.velocidad +=0.2
        self.w.y -= 1

enemigos = []

def crear_enemigo():
    un_enemigo = Enemigo(pilas)
    enemigos.append(un_enemigo)
    return True

def cuando_toca_enemigo():
    w.perder()
    enemigo.eliminar()

pilas.escenas.vincular(EscenaWari)
pilas.comportamientos.vincular(Caminando)
pilas.comportamientos.vincular(Esperando)
pilas.comportamientos.vincular(Saltando)
pilas.actores.vincular(Wari)

w = pilas.actores.Wari()
ew = pilas.escenas.EscenaWari()
ew.agregar_actor(w)

pilas.colisiones.agregar(w, enemigos, cuando_toca_enemigo)
pilas.ejecutar()
