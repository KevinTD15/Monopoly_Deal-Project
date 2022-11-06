from abc import ABC, abstractclassmethod
from jugador import *
import random as rd
import juegoMD
from crupier import *

class Jugada(ABC):
    def __init__(self, jugador, mazo, descarte, jugadores = None):
        self.jugador = jugador
        self.mazo = mazo
        self.descarte = descarte
        self.jugadores = jugadores
    
    @abstractclassmethod
    def CrearJugada():
        pass
    
    @abstractclassmethod
    def DescartarCartas():
        pass
    
    @abstractclassmethod
    def UsarCarta():
        pass
    
    @abstractclassmethod
    def ResponderAJugada():
        pass
    
class JugadaRandom(Jugada):
    def __init__(self, jugador, mazo, descarte, jugada = None):
        super().__init__(jugador, mazo, descarte, jugada)
    
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
                
    def ResponderAJugada(self, jugadorActual, carta, monto):
        if(carta.subtipo == 'renta'):
            band = True
            for i in self.jugador.mano:
                if(i.nombre == 'diqno'):
                    usar = rd.randint(0, 1)
                    if(usar == 1):
                        self.descarte.append(i)
                        self.jugador.mano.remove(i)
                        band = False
                        juegoMD.JuegoMD.notificaciones.append(f'{self.jugador.nombre} usa la {i.tipo} {i.nombre} y niega el efecto de {carta.nombre} contra el') 
            if(band):
                
                pass
        elif(carta.subtipo == 'robarprop'):
            pass
        elif(carta.subtipo == 'robardinero'):
            pass
        else:
            pass
    
    def UsarCarta(self, carta):
        jugadorActual = self.jugador
        
        if(carta.tipo == 'propiedad'):
            if(len(jugadorActual.tablero[carta.color]) < carta.cantGrupo):
                jugadorActual.tablero[carta.color].append(carta)
                jugadorActual.mano.remove(carta)
                juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} pone la {carta.tipo} {carta.color} {carta.nombre} en su tablero') 
            else:
                pass
        elif(carta.tipo == 'dinero'):
            jugadorActual.tablero[carta.tipo].append(carta)
            jugadorActual.mano.remove(carta)
            juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} pone la carta de {carta.tipo} de $ {carta.nombre} en su tablero')        
        
        elif(carta.tipo == 'comodin'):
            if (len(carta.color) > 0):
                col = rd.sample(carta.color, 1)
                if(len(jugadorActual.tablero[col[0]]) > 0 and jugadorActual.tablero[col[0]][0].cantGrupo < len(jugadorActual.tablero[col[0]])):
                    jugadorActual.tablero[col[0]].append(carta)
                    juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} pone el {carta.tipo} {carta.nombre} en el grupo {col[0]}') 
                else:
                    jugadorActual.tablero['dinero'].append(carta)
                    juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} pone el {carta.tipo} {carta.nombre} como dinero') 
            else:
                col = rd.sample(sorted(jugadorActual.tablero), 1)
                if(len(jugadorActual.tablero[col[0]]) > 0 and col[0] != 'dinero' and jugadorActual.tablero[col[0]][0].cantGrupo < len(jugadorActual.tablero[col[0]])):                    
                    jugadorActual.tablero[col[0]].append(carta)
                    juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} pone el {carta.tipo} {carta.nombre} en el grupo {col[0]}') 
                else:
                    juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} no hace nada con el {carta.tipo} {carta.nombre}')                
            jugadorActual.mano.remove(carta)
        
        else:
            
            if(carta.subtipo == 'renta'):
                posiblePago = []
                for i in jugadorActual.tablero:
                    if(len(jugadorActual.tablero[i]) > 0 and len(carta.propiedades) == 0 and i != 'dinero'):
                        posiblePago.append(i)
                    elif(len(jugadorActual.tablero[i]) > 0 and i in carta.propiedades):
                        posiblePago.append(i)
                if(len(posiblePago) == 0):
                    jugadorActual.tablero['dinero'].append(carta)
                    juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} usa la carta {carta.tipo} {carta.nombre} como dinero')
                else:
                    col = rd.sample(posiblePago, 1)
                    monto = CalcularMonto(jugadorActual, col[0])
                    if(carta.todos):
                        juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} usa la carta {carta.tipo} {carta.nombre} contra todos')
                        for j in self.jugadores:
                            if (j != jugadorActual):
                                j.Responder(jugadorActual, self.mazo, self.descarte, carta, monto)
                    else:
                        jugs = self.jugadores.copy()
                        jugs.remove(jugadorActual)
                        jug = rd.sample(jugs, 1)
                        juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} usa la carta {carta.tipo} {carta.nombre} contra {jug[0].nombre}')
                        jug[0].Responder(jugadorActual, self.mazo, self.descarte, carta, monto)
                        pass
                self.descarte.append(carta)
                jugadorActual.mano.remove(carta)
            
            elif(carta.subtipo == 'construccion'):
                coloresTablero = sorted(jugadorActual.tablero).copy()
                coloresTablero.remove('dinero')
                col = rd.sample(coloresTablero, 1)
                if(carta.nombre == 'casa'):
                    if (len(jugadorActual.tablero[col[0]]) > 0 and len(jugadorActual.tablero[col[0]]) == jugadorActual.tablero[col[0]][0].cantGrupo):
                        jugadorActual.tablero[col[0]].append(carta)
                elif(carta.nombre == 'hotel'):
                    if (len(jugadorActual.tablero[col[0]]) > 0 and len(jugadorActual.tablero[col[0]]) == jugadorActual.tablero[col[0]][0].cantGrupo + 1):
                            jugadorActual.tablero[col[0]].append(carta)
                else:
                    jugadorActual.tablero['dinero'].append(carta)
                jugadorActual.mano.remove(carta)
                               
            elif(carta.subtipo == 'rapida'):
                pass
            
            elif(carta.subtipo == 'robarprop'):
                pass
            
            elif(carta.subtipo == 'robardinero'):
                pass
            
            else: #robar carta
                Crupier.RepartirCartas(False, jugadorActual, self.mazo, int(carta.cantCartasATomar), self.descarte)
                juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} usa la {carta.tipo} {carta.nombre} y toma {carta.cantCartasATomar} del mazo')                

def CalcularMonto(jugador, color):
    if(len(jugador.tablero[color]) <= jugador.tablero[color][0].cantGrupo):
        return jugador.tablero[color][0].renta[len(jugador.tablero[color]) - 1]
    else:
        acum = jugador.tablero[color][0].renta[len(jugador.tablero[color][0].renta) - 1]
        if(len(jugador.tablero[color]) == jugador.tablero[color][0].cantGrupo + 1):
            acum +=  jugador.tablero[color][len(jugador.tablero[color]) - 1].monto
        elif(len(jugador.tablero[color]) == jugador.tablero[color][0].cantGrupo + 2):
            acum +=  jugador.tablero[color][len(jugador.tablero[color]) - 2].monto
            acum +=  jugador.tablero[color][len(jugador.tablero[color]) - 1].monto
        return acum