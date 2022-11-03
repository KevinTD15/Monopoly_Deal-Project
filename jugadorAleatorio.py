import pstats
from jugador import Jugador

class JugadorAleatorio(Jugador):
    def __init__(self, nombre):
        if(nombre == ''):
            raise Exception('Los jugadores tiene que tener nombre')
        else:
            self.nombre = nombre
            
    def SeleccionarJugada(args):
        pass
        