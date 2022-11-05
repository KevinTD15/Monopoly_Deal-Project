from abc import ABC, abstractclassmethod
from jugador import *
import random as rd
import juegoMD

class Jugada(ABC):
    def __init__(self, jugador, mazo, descarte) -> None:
        self.jugador = jugador
        self.mazo = mazo
        self.descarte = descarte
    
    @abstractclassmethod
    def CrearJugada():
        pass
    
    @abstractclassmethod
    def DescartarCartas():
        pass
    
    @abstractclassmethod
    def UsarCarta():
        pass
    
class JugadaRandom(Jugada):
    def __init__(self, jugador, mazo, descarte) -> None:
        super().__init__(jugador, mazo, descarte)
    
    def CrearJugada(self):
        a = rd.randint(0, 3)
        cantCartasAJugar = min(a, len(self.jugador.mano))
        cartasAJugar = rd.sample(self.jugador.mano, cantCartasAJugar)
                
        return cartasAJugar
    
    def DescartarCartas(self): #ver xq descarto propiedades
        cantCartasADescartar = len(self.jugador.mano) - 7
        indicesUsados = []
        for i in range(cantCartasADescartar):
            a = rd.randint(0, len(self.jugador.mano) - 1)
            if(a in indicesUsados or self.jugador.mano[a].tipo == 'propiedad'):
                i -= 1
            else:
                juegoMD.JuegoMD.notificaciones.append(f'{self.jugador.nombre} descarta {self.jugador.mano[a].tipo} {self.jugador.mano[a].nombre}') 
                indicesUsados.append(a)
                self.descarte.append(self.jugador.mano.pop(a))
    
    def UsarCarta(self, carta):
        jugadorActual = self.jugador
        juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} intentara jugar la {carta.tipo} {carta.nombre}') 
        if(carta.tipo == 'propiedad'):
            jugadorActual.tablero[carta.color].append(carta)
            jugadorActual.mano.remove(carta)
        elif(carta.tipo == 'dinero'):
            jugadorActual.tablero[carta.tipo].append(carta)
            jugadorActual.mano.remove(carta)
        elif(carta.tipo == 'comodin'):
            if (len(carta.color) > 0):
                col = rd.sample(carta.color, 1)
                if (col[0] in jugadorActual.tablero and len(jugadorActual.tablero[col[0]]) > 0 and len(jugadorActual.tablero[col[0]]) < 3):
                    jugadorActual.tablero[col[0]].append(carta)
                else:
                    jugadorActual.tablero['dinero'].append(carta)
            else:
                col = rd.sample(sorted(jugadorActual.tablero), 1)
                if (col[0] in jugadorActual.tablero and len(jugadorActual.tablero[col[0]]) > 0 and len(jugadorActual.tablero[col[0]]) < 3):
                    jugadorActual.tablero[col[0]].append(carta)
                else:
                    pass               
            jugadorActual.mano.remove(carta)
        else:
            if(carta.subtipo == 'renta'):
                pass
            elif(carta.subtipo == 'construccion'):
                pass
            elif(carta.subtipo == 'rapida'):
                pass
            elif(carta.subtipo == 'robarprop'):
                pass
            elif(carta.subtipo == 'robardinero'):
                pass
            else: #robar carta
                pass
            
    