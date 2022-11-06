from cartasMD import *
from mazoCartas import *
from jugadorMD import *
import random as rd
from crupier import *

class JuegoMD:

    _jugadores = []
    _indiceJugadorActual = 0
    _iniciarJuegoMD = True
    _mazo = Mazo.cartas
    descarte = []
    final = False
    ganador : str
    notificaciones = []
                    
    def EjecutarTurnoMD():
        '''aqui es donde se lleva a cabo la ejecucion de un turno del juego'''
        if(JuegoMD._iniciarJuegoMD):
            JuegoMD._iniciarJuegoMD = False
            Crupier.BarajarMazo(JuegoMD._mazo)
            Crupier.RepartirCartas(True, JuegoMD._jugadores, JuegoMD._mazo, 5, JuegoMD.descarte)
        else:
            if(JuegoMD._indiceJugadorActual >= len(JuegoMD._jugadores)):
                JuegoMD._indiceJugadorActual = 0
            
            jugadorActual = JuegoMD._jugadores[JuegoMD._indiceJugadorActual]
            JuegoMD.notificaciones.append(f'Turno de: {jugadorActual.nombre}')
            
            if(len(jugadorActual.mano) == 0):
                Crupier.RepartirCartas(False, jugadorActual, JuegoMD._mazo, 5, JuegoMD.descarte, JuegoMD._indiceJugadorActual)
                JuegoMD.notificaciones.append(f'Se le repartieron 5 cartas a: {jugadorActual.nombre}')
            else:
                Crupier.RepartirCartas(False, jugadorActual, JuegoMD._mazo, 2, JuegoMD.descarte, JuegoMD._indiceJugadorActual)
                JuegoMD.notificaciones.append(f'{jugadorActual.nombre} toma 2 cartas del mazo')
            
            jugada = jugadorActual.SeleccionarJugada(JuegoMD._mazo, JuegoMD.descarte)
            
            jugadorActual.EjecutarJugada(jugada, JuegoMD._mazo, JuegoMD.descarte, JuegoMD._jugadores)
            Crupier.VerificarMano(jugadorActual, JuegoMD._mazo, JuegoMD.descarte)
            JuegoMD.final, JuegoMD.ganador = Crupier.FinDeJuegoMD(jugadorActual)
            JuegoMD._indiceJugadorActual += 1
                
    def EjecutarJuego(self):
        '''aqui es donde se lleva a cabo la ejecucion del juego'''
        count = -1
        while(not JuegoMD.final):
            JuegoMD.EjecutarTurnoMD()
            count += 1
        self.notificaciones.append(f'Gano: {self.ganador} en {count} turnos')
        

        
    

    