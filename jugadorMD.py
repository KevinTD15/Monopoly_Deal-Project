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
        self.colorCantGrupo = {
            'carmelita' : 2,
            'azulClaro' : 3,
            'morado' : 3,
            'anaranjado' : 3,
            'rojo' : 3,
            'amarillo' : 3,
            'verde' : 3,
            'azul' : 2,
            'negro' : 4,
            'blanco' : 2,
        }
        self.mano = []

    def DescartarCartasJ(self,mazo, descarte):
        j = JugadaRandom(self, mazo, descarte)
        cart = j.CartasADescartar()
        j.DescartarCartas(cart)        
        
    def SeleccionarJugada(self, mazo, descarte,jugadores):
        j = JugadaRandom(self, mazo, descarte,jugadores)
        jugada = j.CrearJugada()
        cartasConUso = []
        for i in jugada:
            cartasConUso.append(j.ComoUsarCarta(i, jugada))
        cartasConUso.append(j.ComodinesAReponer())
        return cartasConUso
    
    def EjecutarJugada(self, jugada, mazo, descarte, jugadores):
        j = JugadaRandom(self, mazo, descarte, jugadores)
        for i in jugada:
            if(i == jugada[len(jugada) - 1]):
                break
            if(i != None):
                j.UsarCarta(i[0], i, jugada)
            
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
        self.colorCantGrupo = {
            'carmelita' : 2,
            'azulClaro' : 3,
            'morado' : 3,
            'anaranjado' : 3,
            'rojo' : 3,
            'amarillo' : 3,
            'verde' : 3,
            'azul' : 2,
            'negro' : 4,
            'blanco' : 2,
        }
        self.mano = []
        
        
    def EvaluarJugada(jugadorActual, jugada):
        '''HEURISTICA DE PROPIEDADES'''
        valor = 0
        for i in jugada:
            if(type(i) != list):
                if(i[0].tipo == 'propiedad'):
                    ranking = RankingPropiedades(jugadorActual)
                    for k in ranking:
                        if(i[0].color in ranking[k] and k != 0):
                            valor += 1 / k
                            ranking[k - 1].append(i[0].color)
                            ranking[k].remove(i[0].color)
                            break
                elif(i[0].tipo == 'comodin'):
                    pass
                #poner aki las cosas!!!!!!!!!!!!
        return 0
    
    def PosiblesJugadas(self, mazo, descarte, jugadores):
        listaJugadas = []
        for i in range(5): #Poner otro numero!!!!!!!!!!!
            j = JugadaRandom(self, mazo, descarte,jugadores)
            jugada = j.CrearJugada()
            cartasConUso = []
            for i in jugada:
                cartasConUso.append(j.ComoUsarCarta(i, jugada))
            cartasConUso.append(j.ComodinesAReponer())
            listaJugadas.append([self, cartasConUso])
        max = -1000 #poner el min value
        result = {}
        for i in listaJugadas:
            ev = i[0].EvaluarJugada(i[1])
            result[ev] = i
            if(ev > max):
                max = ev
        return result[max][1]  
    pass
    
    def SeleccionarJugada(self, mazo, descarte, jugadores):
        jugada = self.PosiblesJugadas(mazo, descarte, jugadores)
        return jugada
    
    def EjecutarJugada(self, jugada, mazo, descarte, jugadores):
        j = JugadaRandom(self, mazo, descarte, jugadores)
        for i in jugada:
            if(i == jugada[len(jugada) - 1]):
                break
            if(i != None):
                j.UsarCarta(i[0], i, jugada)
                
    def DescartarCartasJ(self,mazo, descarte):
        j = JugadaRandom(self, mazo, descarte)
        cartasADescartar = []
        for i in range(5):
            cartasADescartar.append(j.CartasADescartar())
        max = -1000 #poner el min value
        result = {}
        for i in cartasADescartar:
            ev = i[0].EvaluarJugada(i[1])
            result[ev] = i
            if(ev > max):
                max = ev
        return result[max][1] 
            
            
    
    def Responder():
        pass