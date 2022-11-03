from cartasMD import *
from mazoCartas import *
from jugador import *
from jugada import *
import time
import random as rd

class JuegoMD:

    _jugadores = [Jugador]
    _jugadas = [Jugada]
    _indiceJugadorActual = 0
    _manoJugador = [object]
    _iniciarJuegoMD = True
    _mazo = Mazo.cartas
    descarte = []
    juega : Jugada
    final = False
    indiceGanador : int
    
    def BuscarGanador():
        #put your code here
        pass
    
    def EjecutarJugada():
        #put your code here
        pass
    
    def FinDeJuegoMD():
        #put your code here
        pass
    
    def OrganizarJugadas():
        #put your code here
        pass
    
    def PosiblesJugadas():
        #put your code here
        pass
    
    def BarajarMazo():
        rd.shuffle(JuegoMD._mazo)
    
    def TomarCartas():
        for i in range(2):
            JuegoMD._jugadores[JuegoMD._indiceJugadorActual].mano.append(JuegoMD._mazo.pop(0))
    
    def RepartirCartas(): #poner que roba 5 en vez de 2
        for j in JuegoMD._jugadores:
            for i in range(2):
                j.mano.append(JuegoMD._mazo.pop(0))
                
    def VerificarMano():
        if(len(JuegoMD._jugadores[JuegoMD._indiceJugadorActual].mano) > 7):
            pass #IA            
            
    def JugadorGanador(indiceGanador):
        '''devuelve el ganador'''
        if(indiceGanador == -1):
            raise Exception('El tiene que haber un ganador siempre')
        else:
            print(f'Gana el jugador {JuegoMD._jugadores[JuegoMD.indiceGanador]}')
            
    def EjecutarJuegoMD():
        '''aqui es donde se lleva a cabo la ejecucion de todo el JuegoMD'''
        if(JuegoMD._iniciarJuegoMD):
            JuegoMD._iniciarJuegoMD = False
            JuegoMD.BarajarMazo()
            JuegoMD.RepartirCartas()
        else:
            if(JuegoMD._indiceJugadorActual >= len(JuegoMD._jugadores)):
                JuegoMD._indiceJugadorActual = 0
            
            JuegoMD.TomarCartas()  
            JuegoMD.PosiblesJugadas()
            JuegoMD.OrganizarJugadas()
            JuegoMD.juega = JuegoMD._jugadores[JuegoMD._indiceJugadorActual].Jugar(JuegoMD._jugadas)
            
            if(JuegoMD.EsJugadaValida(JuegoMD.juega)):
                JuegoMD.EjecutarJugada()
                JuegoMD.VerificarMano()
                JuegoMD._indiceJugadorActual += 1
                JuegoMD._jugadas.clear()
                JuegoMD.FinDeJuegoMD()
                
                if(JuegoMD.final):
                    JuegoMD.BuscarGanador()
            else:
                JuegoMD.final = True
                #AKI FALTA UNA COSA
                
    def Simulador(self):
        while(not JuegoMD.final):
            JuegoMD.EjecutarJuegoMD()
            time.sleep(1)

        
#test
j = JuegoMD()
j.Simulador()
        
    

    