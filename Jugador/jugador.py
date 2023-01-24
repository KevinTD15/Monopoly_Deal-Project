from abc import ABC, abstractstaticmethod
from utiles import *

class Jugador(ABC):
    
    mano = []
    tablero = {}
    colorCantGrupo = {}
    
    def __init__(self, nombre, esBot):
        self.nombre = nombre
        self.esBot = esBot
        self.mano = Jugador.mano
        self.tablero = Jugador.tablero

    @abstractstaticmethod
    def EjecutarJugada(): #tipo es si es random, ogloso, etc
        pass
    
    @abstractstaticmethod
    def Responder():
        pass
    
    @abstractstaticmethod
    def SeleccionarJugada():
        pass
    
    @abstractstaticmethod
    def DescartarCartasJ():
        pass
    
    def Jugar(posiblesJugadas):
        return Jugador.SeleccionarJugada(posiblesJugadas)
    
    def AnadirPropiedadMano(jugadorActual,carta):
        if(len(jugadorActual.tablero[carta.color]) < carta.cantGrupo):
            jugadorActual.tablero[carta.color].append(carta)

        elif(len(jugadorActual.tablero[carta.color]) > 0 and len(jugadorActual.tablero[carta.color]) >= jugadorActual.tablero[carta.color][0].cantGrupo):
            for k in jugadorActual.tablero[carta.color]:
                if(k.tipo == 'comodin'):
                    jugadorActual.tablero[carta.color].insert(0, carta)
                    jugadorActual.tablero['comodines'].append(k)
                    k.enUso = None
                    jugadorActual.tablero[carta.color].remove(k)
                    if jugadorActual.tablero[carta.color][0].tipo == 'comodin':
                        a=5
                    break
        jugadorActual.mano.remove(carta)
     
    def AnadirPropiedad(jugadorObjetivo, jugadorActual,carta ):
        if carta in jugadorObjetivo.tablero[carta.color]:   #QUITAR
            if(len(jugadorActual.tablero[carta.color]) > 0 and len(jugadorActual.tablero[carta.color]) >= jugadorActual.tablero[carta.color][0].cantGrupo): #jugadorActual.tablero[carta.color][0].cantGrupo):
                for k in jugadorActual.tablero[carta.color]:
                    if(k.tipo == 'comodin'):
                        jugadorActual.tablero[carta.color].insert(0, carta)
                        jugadorObjetivo.tablero[carta.color].remove(carta)
                        jugadorActual.tablero['comodines'].append(k)
                        k.enUso = None
                        jugadorActual.tablero[carta.color].remove(k)   
                        if jugadorActual.tablero[carta.color][0].tipo == 'comodin': #quitar
                            a=5   
                        break             
            else:
                jugadorActual.tablero[carta.color].append(carta)
                jugadorObjetivo.tablero[carta.color].remove(carta)
                #print(f' jugadorActual {jugadorActual} anade {carta.tipo} {carta.nombre}')
                #print(f' jugadorObjetivo {jugadorObjetivo} elimina {carta.tipo} {carta.nombre}')
    
    def AnadirConstruccion(jugadorObjetivo, jugadorActual, carta):
        if(carta in jugadorObjetivo.tablero[carta.colorC]): 
            jugadorActual.tablero[carta.colorC].append(carta)
            jugadorObjetivo.tablero[carta.colorC].remove(carta)
    
    def AnadirDinero(jugadorObjetivo, jugadorActual,carta):
        if(carta in jugadorObjetivo.tablero['dinero']): #QUITAR ESTO!!!!!!!!!!!!!!!
            jugadorActual.tablero['dinero'].append(carta)
            jugadorObjetivo.tablero['dinero'].remove(carta)
        
    def AnadirComodin(jugadorObjetivo, jugadorActual,carta):
        if(carta.enUso != None and carta.enUso != 'dinero' and len(jugadorActual.tablero[carta.enUso]) > 0):
            if carta in jugadorObjetivo.tablero[carta.enUso]:
                jugadorActual.tablero[carta.enUso].append(carta)
                jugadorObjetivo.tablero[carta.enUso].remove(carta)
        elif(carta.enUso == None or len(jugadorActual.tablero[carta.enUso]) == 0):
            if carta in jugadorObjetivo.tablero['comodines']: #QUITAT
                jugadorActual.tablero['comodines'].append(carta)
                jugadorObjetivo.tablero['comodines'].remove(carta)
                carta.enUso = None
        else:
            jugadorActual.tablero['dinero'].append(carta)
            if carta in jugadorObjetivo.tablero['dinero']:
                jugadorObjetivo.tablero['dinero'].remove(carta)
        
    def AnadirSimple(jugadorObjetivo, jugadorActual,carta):
        jugadorActual.tablero[carta.tipo].append(carta)
        jugadorObjetivo.tablero[carta.tipo].remove(carta)  
    

    def AcomodarTablero(jugadorActual): #####COMPLETAR ESTOOOOOOOOOOOOOOOOOOOO
        jugador = jugadorActual

        for i in jugadorActual.tablero:
            if(i != 'dinero' and i != 'comodines' and len(jugadorActual.tablero[i]) > 0):
                if(len(jugadorActual.tablero[i]) == 1 and jugadorActual.tablero[i][0].tipo == 'accion'):
                    jugadorActual.tablero[i][0].colorc = None
                    jugadorActual.tablero['dinero'].append(jugadorActual.tablero[i][0])
                    jugadorActual.tablero[i].remove(jugadorActual.tablero[i][0])
                elif(len(jugadorActual.tablero[i]) == 1 and jugadorActual.tablero[i][0].tipo == 'comodin'):
                    jugadorActual.tablero[i][0].enUso = None
                    jugadorActual.tablero['comodines'].append(jugadorActual.tablero[i][0])
                    jugadorActual.tablero[i].remove(jugadorActual.tablero[i][0])
                elif(len(jugadorActual.tablero[i]) > 1 and jugadorActual.tablero[i][0].tipo == 'comodin'):
                        band = False
                        for k in range(len(jugadorActual.tablero[i])):
                            if(jugadorActual.tablero[i][k].tipo == 'propiedad'):
                                tmp = jugadorActual.tablero[i][0]
                                prop = jugadorActual.tablero[i][k]
                                jugadorActual.tablero[i].remove(prop)
                                jugadorActual.tablero[i].remove(tmp)
                                jugadorActual.tablero[i].insert(0, prop)
                                jugadorActual.tablero[i].insert(k, tmp)
                                band = True
                                break
                        if(not band):
                            for k in jugadorActual.tablero[i]:
                                jugadorActual.tablero['comodines'].append(k)
                                k.enUso = None
                            jugadorActual.tablero[i].clear()
                elif(len(jugadorActual.tablero[i]) > jugadorActual.tablero[i][0].cantGrupo  and jugadorActual.tablero[i][len(jugadorActual.tablero[i]) - 1].tipo != 'accion'):
                        for k in jugadorActual.tablero[i]:
                            if(k.tipo == 'comodin' and len(jugadorActual.tablero[i]) > jugadorActual.tablero[i][0].cantGrupo ):
                                k.enUso = None
                                jugadorActual.tablero['comodines'].append(k)
                                jugadorActual.tablero[i].remove(k)
                elif(len(jugadorActual.tablero[i]) > jugadorActual.tablero[i][0].cantGrupo and jugadorActual.tablero[i][len(jugadorActual.tablero[i]) - 1].tipo == 'accion'):
                    cantConst = CantidadDeConstrucciones(jugadorActual.tablero[i])
                    if(jugadorActual.tablero[i][0].cantGrupo + cantConst < len(jugadorActual.tablero[i])):
                        for k in jugadorActual.tablero[i]:
                            if(k.tipo == 'comodin' and len(jugadorActual.tablero[i]) > jugadorActual.tablero[i][0].cantGrupo + cantConst < len(jugadorActual.tablero[i])):
                                k.enUso = None
                                jugadorActual.tablero['comodines'].append(k)
                                jugadorActual.tablero[i].remove(k)



