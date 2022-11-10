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

    def DescartarCartas(self,mazo, descarte):
        JugadaRandom(self, mazo, descarte).DescartarCartas()
        
    def SeleccionarJugada(self, mazo, descarte,jugadores):
        j = JugadaRandom(self, mazo, descarte,jugadores)
        jugada = j.CrearJugada()
        cartasConUso = []
        for i in jugada:
            cartasConUso.append(j.ComoUsarCarta(i, jugada))
        return cartasConUso
    
    def EjecutarJugada(self, jugada, mazo, descarte, jugadores):
        j = JugadaRandom(self, mazo, descarte, jugadores)
        for i in jugada:
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
        valor = 0
        for i in jugada:
            if(i.tipo == 'propiedad'):
                ranking = RankingPropiedades(jugadorActual)
                for k in ranking:
                    if(i.color in ranking[k] and k != 0):
                        valor += 1 / k
        return 0
    
    def PosiblesJugadas(self, mazo, descarte, jugadores):
        listaJugadas = []
        for i in range(5):
            j = JugadaRandom(self, mazo, descarte,jugadores)
            jugada = j.CrearJugada()
            cartasConUso = []
            for i in jugada:
                cartasConUso.append(j.ComoUsarCarta(i, jugada))
            listaJugadas.append([self, cartasConUso])

        #listaJugadas.append(JugadaRandom(self, mazo, descarte, jugadores))
        max = -1000 #poner el min value
        result = {}
        for i in listaJugadas:
            ev = i[0].EvaluarJugada(i[1])
            result[ev] = i
            if(ev > max):
                max = ev
        return result[max]   
    pass
    
    def SeleccionarJugada(self, mazo, descarte, jugadores):
        jugada = self.PosiblesJugadas(mazo, descarte, jugadores)
        return jugada
    
    def EjecutarJugada(self, jugada):
        for i in jugada:
            self.UsarCarta(i)
    
    def Responder():
        pass