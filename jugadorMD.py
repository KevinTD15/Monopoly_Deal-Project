from jugador import Jugador
from jugada import *
from utiles import *

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
            'dinero' : [],
            'comodines': [],
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
            j.UsarCarta(i, jugada)
            
    def Responder(self, jugadorActual, mazo, descarte, carta, monto):
        j = JugadaRandom(self, mazo, descarte)
        j.ResponderAJugada(jugadorActual, carta, monto)
        
        
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
            'dinero' : [],
            'comodines': []
        }
        self.mano = []
        
    def EvaluarJugada(jugadorActual, jugada):
        pass
    
    def PosiblesJugadas(self, mazo, descarte):
        listaJugadas = []
        listaJugadas.append(JugadaRandom(self, mazo, descarte).CrearJugada())
        max = -1000 #poner el min value
        result = {}
        for i in listaJugadas:
            ev = JugadorInteligente.EvaluarJugada(self, i)
            result[ev] = i
            if(ev > max):
                max = ev
        return result[max]   
    pass
    
    def SeleccionarJugada(self, mazo, descarte):
        jugada = self.PosiblesJugadas(mazo, descarte)
        return jugada
    
    def EjecutarJugada(self, jugada):
        for i in jugada:
            self.UsarCarta(i)
    
    def Responder():
        pass