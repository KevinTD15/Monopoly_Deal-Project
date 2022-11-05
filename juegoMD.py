from math import inf
from cartasMD import *
from mazoCartas import *
from jugadorMD import *
from jugada import *
import time
import random as rd

class JuegoMD:

    _jugadores = []
    _jugadas = []
    _indiceJugadorActual = 0
    _manoJugador = []
    _iniciarJuegoMD = True
    _mazo = Mazo.cartas
    descarte = []
    final = False
    ganador : str
    maxEval = -inf
    notificaciones = []
    
    def FinDeJuegoMD(): #no se si esto pinche
        count = 0
        jugadorActual = JuegoMD._jugadores[JuegoMD._indiceJugadorActual]
        tableroJugadorActual = jugadorActual.tablero
        for i in tableroJugadorActual:
            if(i == 'dinero'):
                break
            if(len(tableroJugadorActual[i]) >= 1 and len(tableroJugadorActual[i]) == tableroJugadorActual[i][0].cantGrupo):
                count += 1
        fin = count >= 3
        return fin, jugadorActual.nombre
    
    #def OrganizarJugadas():
    #    #put your code here
    #    pass
    
    def BarajarMazo():
        rd.shuffle(JuegoMD._mazo)
    
    def TomarCartas():
        jugadorActual = JuegoMD._jugadores[JuegoMD._indiceJugadorActual]
        if(len(JuegoMD._mazo) < 2):
            JuegoMD._mazo.extend(JuegoMD.descarte)
            JuegoMD.descarte.clear()
            JuegoMD.BarajarMazo()
        else:
            for i in range(2):
                jugadorActual.mano.append(JuegoMD._mazo.pop(0))
    
    def RepartirCartas(aTodos : bool, indice = None): #poner que roba 5 en vez de 8
        if(aTodos):
            for j in JuegoMD._jugadores:
                for i in range(8):
                    j.mano.append(JuegoMD._mazo.pop(0))
        else:
            for i in range(2):
                JuegoMD._jugadores[indice].mano.append(JuegoMD._mazo.pop(0))
         
    def VerificarMano():
        jugadorActual = JuegoMD._jugadores[JuegoMD._indiceJugadorActual]
        cantCartasEnMano = jugadorActual.mano
        if(len(cantCartasEnMano) > 7):
            jugadorActual.DescartarCartas(JuegoMD._mazo, JuegoMD.descarte)
                       
            
    #def JugadorGanador(indiceGanador):
    #    '''devuelve el ganador'''
    #    if(indiceGanador == -1):
    #        raise Exception('El tiene que haber un ganador siempre')
    #    else:
    #        print(f'Gana el jugador {JuegoMD._jugadores[JuegoMD.indiceGanador]}')
                    
    def EjecutarTurnoMD():
        '''aqui es donde se lleva a cabo la ejecucion de todo el JuegoMD'''
        if(JuegoMD._iniciarJuegoMD):
            JuegoMD._iniciarJuegoMD = False
            JuegoMD.BarajarMazo()
            JuegoMD.RepartirCartas(True)
        else:
            if(JuegoMD._indiceJugadorActual >= len(JuegoMD._jugadores)):
                JuegoMD._indiceJugadorActual = 0
            
            jugadorActual = JuegoMD._jugadores[JuegoMD._indiceJugadorActual]
            JuegoMD.notificaciones.append(f'Turno de: {jugadorActual.nombre}')
            
            if(len(jugadorActual.mano) == 0):
                JuegoMD.RepartirCartas(False, JuegoMD._indiceJugadorActual)
                JuegoMD.notificaciones.append(f'Se le repartieron 5 cartas a: {jugadorActual.nombre}')
            else:
                JuegoMD.TomarCartas()
                JuegoMD.notificaciones.append(f'{jugadorActual.nombre} toma 2 cartas del mazo')
            
            jugada = jugadorActual.SeleccionarJugada(JuegoMD._mazo, JuegoMD.descarte)
            
            jugadorActual.EjecutarJugada(jugada, JuegoMD._mazo, JuegoMD.descarte)
            JuegoMD.VerificarMano()
            JuegoMD._jugadas.clear()
            JuegoMD.final, JuegoMD.ganador = JuegoMD.FinDeJuegoMD()
            JuegoMD._indiceJugadorActual += 1
                
    def EjecutarJuego(self):
        while(not JuegoMD.final):
            JuegoMD.EjecutarTurnoMD()
        self.notificaciones.append(f'Gano: {self.ganador}')
        

        
    

    