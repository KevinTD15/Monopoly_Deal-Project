import pstats
from jugador import Jugador

class JugadorAleatorio(Jugador):
    
    def __init__(self, nombre, esBot):
        super().__init__(nombre, esBot)
        self.tablero = Jugador.tablero
        self.mano = Jugador.mano
            
    def SeleccionarJugada(args):
        pass
        