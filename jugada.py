from abc import ABC, abstractclassmethod
from jugador import *
import random as rd

class Jugada(ABC):
    def __init__(self, jugador, mazo, descarte) -> None:
        self.jugador = jugador
        self.mazo = mazo
        self.descarte = descarte
    
    @abstractclassmethod
    def CrearJugada():
        pass
    
    def EvaluarJugada(cartasAJugar): #Heuristica
        pass

class JugadaRandom(Jugada):
    def __init__(self, jugador, mazo, descarte) -> None:
        super().__init__(jugador, mazo, descarte)
    
    def CrearJugada(self):
        cantCartasAJugar = min(rd.randint(0, 3), len(self.jugador.mano))
        cartasAJugar = []

        for i in range(cantCartasAJugar):
            cartasAJugar.append(self.jugador.mano[rd.randint(0, len(self.jugador.mano))])
                
        eval = self.EvaluarJugada(cartasAJugar)
        
        return cartasAJugar, eval
            
    