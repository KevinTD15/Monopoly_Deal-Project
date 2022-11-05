from abc import ABC, abstractstaticmethod

class Jugador(ABC):
    
    mano = []
    tablero = {}
    
    def __init__(self, nombre, esBot):
        self.nombre = nombre
        self.esBot = esBot
        self.mano = Jugador.mano
        self.tablero = Jugador.tablero

    @abstractstaticmethod
    def EjecutarJugada(jugada, tipo): #tipo es si es random, ogloso, etc
        pass
    
    @abstractstaticmethod
    def SeleccionarJugada(posiblesJugadas, mazo, descarte):
        pass
    
    def Jugar(posiblesJugadas):
        return Jugador.SeleccionarJugada(posiblesJugadas)
    
    
    