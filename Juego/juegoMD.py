from Mazo.cartasMD import *
from Mazo.mazoCartas import *
from Jugador.jugadorMD import *
import random as rd
from Juego.crupier import *

class JuegoMD:

    _jugadores = []
    _indiceJugadorActual = 0
    _iniciarJuegoMD = True
    _mazo = Mazo.cartas
    descarte = []
    final = False
    ganador = 'Nadie'
    notificaciones = []
    count = -1
                    
    def EjecutarTurnoMD(self):
        '''aqui es donde se lleva a cabo la ejecucion de un turno del juego'''
        if(JuegoMD._iniciarJuegoMD):
            JuegoMD._iniciarJuegoMD = False
            Crupier.BarajarMazo(JuegoMD._mazo)
            a = Crupier.RepartirCartas(True, JuegoMD._jugadores, JuegoMD._mazo, 5, JuegoMD.descarte)
            if(a):
                JuegoMD.final = True
                JuegoMD.ganador = 'Nadie'        
                JuegoMD.notificaciones.append('Se acabaron las cartas del mazo')
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
            
            jugada = jugadorActual.SeleccionarJugada(JuegoMD._mazo, JuegoMD.descarte, JuegoMD._jugadores)
            
            jugadorActual.EjecutarJugada(jugada, JuegoMD._mazo, JuegoMD.descarte, JuegoMD._jugadores)

            Crupier.VerificarMano(jugadorActual, JuegoMD._mazo, JuegoMD.descarte, JuegoMD._jugadores)
            if(JuegoMD.final):
                return
            JuegoMD.final, JuegoMD.ganador = Crupier.FinDeJuegoMD(jugadorActual)
            JuegoMD._indiceJugadorActual += 1
                
    def EjecutarJuego(self):
        '''aqui es donde se lleva a cabo la ejecucion del juego'''
        self.Reestablecer()
        while(not self.final):
            JuegoMD.EjecutarTurnoMD(self)
            JuegoMD.count += 1
        
    def Reestablecer(self):
        self = JuegoMD
        JuegoMD.count = -1
        JuegoMD._indiceJugadorActual = 0
        JuegoMD.descarte = []
        JuegoMD.notificaciones = []
        JuegoMD.final = False
        JuegoMD._iniciarJuegoMD = True
        JuegoMD.ganador = 'Nadie'
        JuegoMD._mazo = Mazo.cartas.copy()
        for i in self._jugadores:
            i.mano.clear()
            for k in i.tablero:
                i.tablero[k].clear()