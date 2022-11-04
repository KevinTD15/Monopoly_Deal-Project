from abc import ABC, abstractstaticmethod

class Jugador(ABC):
    
    mano = []
    tablero = {
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
    
    def __init__(self, nombre, esBot):
        self.nombre = nombre
        self.esBot = esBot
        self.mano = []
        self.tablero = {}
        
    @abstractstaticmethod
    def SeleccionarJugada(posiblesJugadas):
        pass
    
    def Jugar(posiblesJugadas):
        return Jugador.SeleccionarJugada(posiblesJugadas)
    
    
    