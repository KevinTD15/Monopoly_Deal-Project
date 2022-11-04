import random as rd
from jugador import Jugador

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
            
    def SeleccionarJugada(self):
        a = rd.randint(0, 3)
        cantCartasAJugar = min(a, len(self.mano))
        cartasAJugar = rd.sample(self.mano, cantCartasAJugar)

        #for i in range(cantCartasAJugar):
        #    indice = rd.randint(0, len(self.mano) - 1)
        #    cartasAJugar.append(self.mano[indice])
        #    indices.append(indice)
                
        return cartasAJugar

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
        
    def SeleccionarJugada(self):
        pass