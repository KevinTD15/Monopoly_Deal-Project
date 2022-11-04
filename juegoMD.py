from math import inf
from cartasMD import *
from mazoCartas import *
from jugadorMD import *
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
    maxEval = -inf
    
    def BuscarGanador():
        #put your code here
        pass
    
    def EjecutarJugada(jugada):
        for i in jugada:
            JuegoMD.UsarCarta(i)
    
    def FinDeJuegoMD(): #no se si esto pinche
        count = 0
        tableroJugadorActual = JuegoMD._jugadores[JuegoMD._indiceJugadorActual].tablero
        for i in tableroJugadorActual:
            if(len(tableroJugadorActual[i]) >= 1 and i[0].tipo == 'propiedad' and len(i) == i.cantGrupo):
                count += 1
        return count == 3
    
    def OrganizarJugadas():
        #put your code here
        pass
    
    def PosiblesJugadas():
        jr, e1 = JugadaRandom(JuegoMD._jugadores[JuegoMD._indiceJugadorActual], JuegoMD._mazo, JuegoMD.descarte).CrearJugada()
        #cojer el maximo de las evaluaciones y actualizarlo
        pass
    
    def BarajarMazo():
        rd.shuffle(JuegoMD._mazo)
    
    def TomarCartas():
        for i in range(2):
            JuegoMD._jugadores[JuegoMD._indiceJugadorActual].mano.append(JuegoMD._mazo.pop(0))
    
    def RepartirCartas(aTodos : bool, indice = None): #poner que roba 5 en vez de 4
        if(aTodos):
            for j in JuegoMD._jugadores:
                for i in range(4):
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
        jugadorActual = JuegoMD._jugadores[JuegoMD._indiceJugadorActual]    
        if(carta.tipo == 'propiedad'):
            jugadorActual.tablero[carta.color].append(carta)
            jugadorActual.mano.remove(carta)
        elif(carta.tipo == 'dinero'):
            jugadorActual.tablero[carta.tipo].append(carta)
            jugadorActual.mano.remove(carta)
        else:
            jugadorActual.mano.remove(carta)
            #arreglar estoooooooooooo
            
    def EjecutarJuegoMD():
        '''aqui es donde se lleva a cabo la ejecucion de todo el JuegoMD'''
        if(JuegoMD._iniciarJuegoMD):
            JuegoMD._iniciarJuegoMD = False
            JuegoMD.BarajarMazo()
            JuegoMD.RepartirCartas(True)
        else:
            if(JuegoMD._indiceJugadorActual >= len(JuegoMD._jugadores)):
                JuegoMD._indiceJugadorActual = 0
            
            jugadorActual = JuegoMD._jugadores[JuegoMD._indiceJugadorActual]
            if(len(jugadorActual.mano) == 0):
                JuegoMD.RepartirCartas(False, JuegoMD._indiceJugadorActual)
            else:
                JuegoMD.TomarCartas()  
            
            if(jugadorActual is JugadorInteligente):
                jugada = JuegoMD.PosiblesJugadas()
            else:
                jugada = jugadorActual.SeleccionarJugada()
                
            JuegoMD.EjecutarJugada(jugada)
            JuegoMD.VerificarMano()
            JuegoMD._indiceJugadorActual += 1
            JuegoMD._jugadas.clear()
            JuegoMD.final = JuegoMD.FinDeJuegoMD()
                
            if(JuegoMD.final):
                JuegoMD.BuscarGanador()
            #else:
            #    JuegoMD.final = True
            #    #AKI FALTA UNA COSA
                
    def Simulador(self):
        while(not JuegoMD.final):
            JuegoMD.EjecutarJuegoMD()
            time.sleep(1)

        
#test
j = JuegoMD()
j1 = JugadorAleatorio('pepe', True)
j2 = JugadorAleatorio('jose', True)
j3 = JugadorInteligente('kevin', True)
j._jugadores.append(j1)
j._jugadores.append(j2)
j._jugadores.append(j3)
j.Simulador()
        
    

    