from Mazo.cartasMD import *
from Mazo.mazoCartas import *
from Jugador.jugadorMD import *
import random as rd
from Juego.crupier import *

instanciaOriginal = None
instanciaActual = None
monteCarloActivo = False
notificaciones = []
turnosJugadorMC = 0
class JuegoMD:

    _jugadores = []
    _indiceJugadorActual = 0
    _iniciarJuegoMD = True
    _mazo = Mazo.cartas
    descarte = []
    final = False
    ganador = 'Nadie'

    count = -1
                    
    def EjecutarTurnoMD(self):
        '''aqui es donde se lleva a cabo la ejecucion de un turno del juego'''
        global monteCarloActivo
        if(self._iniciarJuegoMD):
            self._iniciarJuegoMD = False
            Crupier.BarajarMazo(self._mazo)
            a = Crupier.RepartirCartas(True, self._jugadores, self._mazo, 5, self.descarte)
            if(a):
                self.final = True
                self.ganador = 'Nadie'        
                if juego.monteCarloActivo==False:
                    notificaciones.append('Se acabaron las cartas del mazo')
        else:
            if(self._indiceJugadorActual >= len(self._jugadores)):
                self._indiceJugadorActual = 0
            
            jugadorActual = self._jugadores[self._indiceJugadorActual]
            if juego.monteCarloActivo==False:
                notificaciones.append(f'Turno de: {jugadorActual.nombre}')
            
            if(len(jugadorActual.mano) == 0):
                Crupier.RepartirCartas(False, jugadorActual, self._mazo, 5, self.descarte, self._indiceJugadorActual)
                if juego.monteCarloActivo==False:
                    notificaciones.append(f'Se le repartieron 5 cartas a: {jugadorActual.nombre}')
            else:
                Crupier.RepartirCartas(False, jugadorActual, self._mazo, 2, self.descarte, self._indiceJugadorActual)
                if juego.monteCarloActivo==False:
                    notificaciones.append(f'{jugadorActual.nombre} toma 2 cartas del mazo')
            
            jugada = jugadorActual.SeleccionarJugada(self._mazo, self.descarte, self._jugadores)
            
            jugadorActual.EjecutarJugada(jugada, self._mazo, self.descarte, self._jugadores)

            Crupier.VerificarMano(jugadorActual, self._mazo, self.descarte, self._jugadores)
            if(self.final):
                return
            self.final, self.ganador = Crupier.FinDeJuegoMD(jugadorActual)
            self._indiceJugadorActual += 1
                
    def EjecutarJuego(self):
        '''aqui es donde se lleva a cabo la ejecucion del juego'''
        self.Reestablecer()
        while(not self.final):
            self.ImprimirNotificaciones()
            self.EjecutarTurnoMD()
            self.count += 1
        
    def Reestablecer(self):
        self.count = -1
        self._indiceJugadorActual = 0
        self.descarte = []
        self.final = False
        self._iniciarJuegoMD = True
        self.ganador = 'Nadie'
        self._mazo = Mazo.cartas.copy()
        for i in self._jugadores:
            i.mano.clear()
            for k in i.tablero:
                i.tablero[k].clear()
                
    def EjecutarSimulacion(self, dic, cp):
        global instanciaOriginal
        global instanciaActual
        instanciaActual = None
        total = 0
        for i in range(cp):
            notificaciones.append('COMIENZO DEL JUEGO')
            if monteCarloActivo==False:
                instanciaOriginal=self
            self.EjecutarJuego()       
            dic[self.ganador] += 1
            total += 1
            #notificaciones.clear()  
            notificaciones.append(f'Gano: {self.ganador} en {self.count} turnos')
            notificaciones.append(f'*************************           FIN DEL JUEGO {i+1}')
            for i in notificaciones:
                print(i)
            notificaciones.clear()
        self.ImprimirNotificaciones()
        return dic

    def ImprimirNotificaciones(self):
        for i in notificaciones:
            print(i)
        notificaciones.clear()