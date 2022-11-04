from cartasMD import *
from mazoCartas import *
from jugadorAleatorio import *
from jugada import *
import time
import random as rd

class JuegoMD:

    _jugadores = []
    _jugadas = []
    _indiceJugadorActual = 0
    _manoJugador = []
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
    
    def FinDeJuegoMD(): #no se si esto pinche
        count = 0
        for i in JuegoMD._jugadores[JuegoMD._indiceJugadorActual].tablero:
            if(len(i) >= 1 and i[0].tipo == 'propiedad' and len(i) == i.cantGrupo):
                count += 1
        return count == 3
    
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
    
    def RepartirCartas(aTodos : bool, indice = None): #poner que roba 5 en vez de 2
        if(aTodos):
            for j in JuegoMD._jugadores:
                for i in range(2):
                    j.mano.append(JuegoMD._mazo.pop(0))
        else:
            for i in range(2):
                JuegoMD._jugadores[indice].mano.append(JuegoMD._mazo.pop(0))
                
    def VerificarMano():
        if(len(JuegoMD._jugadores[JuegoMD._indiceJugadorActual].mano) > 7):
            pass #IA            
            
    def JugadorGanador(indiceGanador):
        '''devuelve el ganador'''
        if(indiceGanador == -1):
            raise Exception('El tiene que haber un ganador siempre')
        else:
            print(f'Gana el jugador {JuegoMD._jugadores[JuegoMD.indiceGanador]}')
            
    def UsarCarta(carta):        
        if(carta.tipo == 'propiedad'):
            JuegoMD._jugadores[JuegoMD._indiceJugadorActual].tablero[carta.color] = carta
        elif(carta.tipo == 'dinero'):
            JuegoMD._jugadores[JuegoMD._indiceJugadorActual].tablero[carta.tipo] = carta
        else:
            pass
            
    def EjecutarJuegoMD():
        '''aqui es donde se lleva a cabo la ejecucion de todo el JuegoMD'''
        if(JuegoMD._iniciarJuegoMD):
            JuegoMD._iniciarJuegoMD = False
            JuegoMD.BarajarMazo()
            JuegoMD.RepartirCartas(True)
        else:
            if(JuegoMD._indiceJugadorActual >= len(JuegoMD._jugadores)):
                JuegoMD._indiceJugadorActual = 0
            
            if(len(JuegoMD._jugadores[JuegoMD._indiceJugadorActual].mano) == 0):
                JuegoMD.RepartirCartas(False, JuegoMD._indiceJugadorActual)
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
j1 = JugadorAleatorio('pepe', True)
j2 = JugadorAleatorio('jose', True)
j._jugadores.append(j1)
j._jugadores.append(j2)
j.Simulador()
        
    

    