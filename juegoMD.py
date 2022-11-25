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
    count = -1
                    
    def EjecutarTurnoMD():
        '''aqui es donde se lleva a cabo la ejecucion de un turno del juego'''
        if(JuegoMD._iniciarJuegoMD):
            JuegoMD._iniciarJuegoMD = False
            Crupier.BarajarMazo(JuegoMD._mazo)
            a = Crupier.RepartirCartas(True, JuegoMD._jugadores, JuegoMD._mazo, 5, JuegoMD.descarte)
            if(a):
                juegoMD.JuegoMD.final = True
                juegoMD.JuegoMD.ganador = 'Nadie'        
                juegoMD.JuegoMD.notificaciones.append('Se acabaron las cartas del mazo')
        else:
            if(JuegoMD._indiceJugadorActual >= len(JuegoMD._jugadores)):
                JuegoMD._indiceJugadorActual = 0
            
            jugadorActual = JuegoMD._jugadores[JuegoMD._indiceJugadorActual]
            JuegoMD.notificaciones.append(f'Turno de: {jugadorActual.nombre}')
            
            if(len(jugadorActual.mano) == 0):
                Crupier.RepartirCartas(False, jugadorActual, JuegoMD._mazo, 5, JuegoMD.descarte, JuegoMD._indiceJugadorActual)
                JuegoMD.notificaciones.append(f'Se le repartieron 5 cartas a: {jugadorActual.nombre}')
            else:
                #OJOO si pasas jugadoractual para q pasas el indiceactual y pq aqui se pasa descarte
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
        JuegoMD.count = -1
        JuegoMD._indiceJugadorActual = 0
        JuegoMD.descarte = []
        JuegoMD.notificaciones = []
        JuegoMD.final = False
        JuegoMD._iniciarJuegoMD = True
        JuegoMD.ganador = ''
        JuegoMD._mazo = Mazo.cartas.copy()
        for i in self._jugadores:
            i.mano.clear()
            for k in i.tablero:
                i.tablero[k].clear()
        while(not JuegoMD.final):
            JuegoMD.EjecutarTurnoMD()
            JuegoMD.count += 1
        
    def Reestablecer(self):
        self.count = -1
        self._indiceJugadorActual = 0
        self.descarte = []
        self.notificaciones = []
        self.final = False
        self._iniciarJuegoMD = True
        self.ganador = ''
        self._mazo = Mazo.cartas.copy()
        for i in self._jugadores:
            i.mano.clear()
            for k in i.tablero:
                i.tablero[k].clear()