from abc import ABC, abstractclassmethod, abstractproperty
import time
from jugada import Jugada
from jugador import Jugador

class Juego(ABC):
    _jugadores = [Jugador]
    _jugadas = [Jugada]
    _indiceJugadorActual = 0
    _manoJugador = [object]
    _iniciarJuego = True
    juega : Jugada
    final : bool
    
    def get_indiceGanador():
        pass
    IndiceGanador = abstractproperty(get_indiceGanador)
    
    def JugadorGanador(indiceGanador):
        '''devuelve el ganador'''
        if(indiceGanador == -1):
            raise Exception('El tiene que haber un ganador siempre')
        else:
            print(f'Gana el jugador {Juego._jugadores[Juego.IndiceGanador]}')
    
    @abstractclassmethod
    def BuscarGanador():
        '''pone en indiceGanador el indice del jugador ganador de la lista de jugadores'''
    
    @abstractclassmethod
    def RepartirCartas():
        '''reparte las cartas a cada uno de los jugadores'''
    
    @abstractclassmethod
    def FinDeJuego():
        '''devuelve en la propiedad Final true si termino el Juego'''
    
    @abstractclassmethod
    def PosiblesJugadas():
        '''genera posibles jugadas a ejecutar'''
    
    @abstractclassmethod
    def OrganizarJugadas(): #HEURISITICA!!!!!!!!!!
        '''evalua las jugadas para prepararlas para que los jugadores la seleccionen  en dependencia de su tipo'''
    
    @abstractclassmethod
    def EjecutarJugada():
        '''ejecuta la jugada del jugador correspondiente'''
        
    def EsJugadaValida(j : Jugada):
        for i in Juego._jugadas:
            if(j == i):
                return True
            return False          
    
    def EjecutarJuego():
        '''aqui es donde se lleva a cabo la ejecucion de todo el juego'''
        if(Juego._iniciarJuego):
            Juego._iniciarJuego = False
            Juego.RepartirCartas()
        else:
            if(Juego._indiceJugadorActual >= len(Juego._jugadores)):
                Juego._indiceJugadorActual = 0
                
            Juego.PosiblesJugadas()
            Juego.OrganizarJugadas()
            Juego.juega = Juego._jugadores[Juego._indiceJugadorActual].Jugar(Juego._jugadas)
            
            if(Juego.EsJugadaValida(Juego.juega)):
                Juego.EjecutarJugada()
                Juego._indiceJugadorActual += 1
                Juego._jugadas.clear()
                Juego.FinDeJuego()
                
                if(Juego.final):
                    Juego.BuscarGanador()
            else:
                Juego.final = True
                #AKI FALTA UNA COSA

    def Simulador():
        while(not Juego.final):
            Juego.EjecutarJuego()
            time.sleep(1)
    
    