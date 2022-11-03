from abc import ABC, abstractstaticmethod

class Jugador(ABC):

    def __init__(self, nombre):
        self.nombre = nombre
        
    @abstractstaticmethod
    def SeleccionarJugada(posiblesJugadas):
        pass
    
    def Jugar(posiblesJugadas):
        return Jugador.SeleccionarJugada(posiblesJugadas)
    
    
    