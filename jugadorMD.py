from jugador import Jugador
from jugada import *

class JugadorAleatorio(Jugador):
    
    def __init__(self, nombre, esBot):
        super().__init__(nombre, esBot)
        self.tablero = {
            'carmelita' : [],
            'azulClaro' : [],
            'morado' : [],
            'anaranjado' : [],
            'rojo' : [],
            'amarillo' : [],
            'verde' : [],
            'azul' : [],
            'negro' : [],
            'blanco' : [],
            'dinero' : []
        }
        self.mano = []

    def DescartarCartas(self,mazo, descarte):
        JugadaRandom(self, mazo, descarte).DescartarCartas()
        
    def SeleccionarJugada(self, mazo, descarte):
        jugada = JugadaRandom(self, mazo, descarte).CrearJugada()
        return jugada
    
    def EjecutarJugada(self, jugada, mazo, descarte, jugadores):
        j = JugadaRandom(self, mazo, descarte, jugadores)
        for i in jugada:
            j.UsarCarta(i)
            
    def Responder(self, jugadorActual, mazo, descarte, carta):
        j = JugadaRandom(self, mazo, descarte)
        j.ResponderAJugada(jugadorActual, carta)
        
class JugadorInteligente(Jugador):
    def __init__(self, nombre, esBot):
        super().__init__(nombre, esBot)
        self.tablero = {
            'carmelita' : [],
            'azulClaro' : [],
            'morado' : [],
            'anaranjado' : [],
            'rojo' : [],
            'amarillo' : [],
            'verde' : [],
            'azul' : [],
            'negro' : [],
            'blanco' : [],
            'dinero' : []
        }
        self.mano = []
        
    def EvaluarJugada():
        pass
    
    def PosiblesJugadas(self, mazo, descarte):
        jr = JugadaRandom(self, mazo, descarte).CrearJugada()
    #cojer el maximo de las evaluaciones y actualizarlo
    pass
    
    def SeleccionarJugada(self, mazo, descarte):
        jugada = self.PosiblesJugadas(mazo, descarte)
        return jugada
    
    def EjecutarJugada(self, jugada):
        for i in jugada:
            self.UsarCarta(i)
    
    def Responder():
        pass