from abc import ABC, abstractclassmethod
#from Juego.juegoMD import Juego.juegoMD.JuegoMD
from Jugador.jugador import *
import random as rd
#from Juego import *
from Juego.crupier import *
import Juego.juegoMD
#import juegoMD
#from Juego.juegoMD import Juego.juegoMD.JuegoMD
from utiles import *

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
    def UsarDoblaRenta():
        pass
    
    #@abstractclassmethod
    #def ResponderAJugada():
    #    pass
    
    @abstractclassmethod
    def ComodinesAReponer():
        pass
    
    @abstractclassmethod
    def UsarDiQNo():
        pass
    
    @abstractclassmethod
    def ComoUsarCarta():
        pass
    
    def ReponerComodin(self, comAReponer):
        if(len(comAReponer) > 0):
            for k  in comAReponer:
                col = k[1]
                i = k[0]
                jugadorActual = self.jugador
                if i in jugadorActual.tablero['comodines']:
                    if(len(jugadorActual.tablero[col]) > 0 and len(jugadorActual.tablero[col]) < jugadorActual.tablero[col][0].cantGrupo):
                        i.enUso = col
                        jugadorActual.tablero[col].append(i)
                        lencol = len(jugadorActual.tablero[col])
                        Juego.juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} mueve su comodin {i.nombre} para el grupo {col} len {lencol} {jugadorActual.tablero[col][0]}') 
                        jugadorActual.tablero['comodines'].remove(i)
                    else:
                        i.enUso = None
    
    def DescartarCartas(self, cartasADescartar):
        if(type(cartasADescartar) != list):
            Juego.juegoMD.JuegoMD.final = True
            Juego.juegoMD.JuegoMD.ganador = 'Nadie'        
            Juego.juegoMD.JuegoMD.notificaciones.append(f'{cartasADescartar.nombre} tiene mas de 7 propiedades en la mano por lo que se anula el juego')
        else:
            for i in cartasADescartar:
                if i.tipo =='comodin':
                    Juego.juegoMD.JuegoMD.notificaciones.append(f'{self.jugador.nombre} descarta {i.tipo} {i.nombre} {i.enUso}') 
                else:
                    Juego.juegoMD.JuegoMD.notificaciones.append(f'{self.jugador.nombre} descarta {i.tipo} {i.nombre}') 

                self.descarte.append(i)
                self.jugador.mano.remove(i)
    
    def UsarCarta(self, carta, jugada, cartasAUsar):
        jugadorActual = self.jugador
        #self.ReponerComodin(cartasAUsar[len(cartasAUsar) - 1])
                
        if(carta.tipo == 'propiedad'):
            jugadorActual.AnadirPropiedadMano(carta)
            Juego.juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} pone la {carta.tipo} {carta.color} {carta.nombre} en su tablero') 
        
        elif(carta.tipo == 'dinero'):
            jugadorActual.tablero[carta.tipo].append(carta)
            jugadorActual.mano.remove(carta)
            Juego.juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} pone la carta de {carta.tipo} de $ {carta.nombre} en su tablero')        
        
        elif(carta.tipo == 'comodin'):
            col = jugada[1]
            if (len(carta.color) > 0):               
                if(len(jugadorActual.tablero[col]) > 0 and jugadorActual.tablero[col][0].cantGrupo > len(jugadorActual.tablero[col])):
                    jugadorActual.tablero[col].append(carta)
                    carta.enUso = col
                    lenDeColor =len(jugadorActual.tablero[col]) #quitar
                    Juego.juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} pone el {carta.tipo} {carta.nombre} en el grupo {col} len del color {lenDeColor} carta1 {jugadorActual.tablero[col][0].nombre}')#quitar lencolor 
                else:
                    jugadorActual.tablero['dinero'].append(carta)
                    carta.enUso = 'dinero'
                    Juego.juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} pone el {carta.tipo} {carta.nombre} como dinero') 
            else:
                if(len(jugadorActual.tablero[col]) > 0 and col != 'dinero' and jugadorActual.tablero[col][0].cantGrupo > len(jugadorActual.tablero[col])):                    
                    jugadorActual.tablero[col].append(carta)
                    carta.enUso = col
                    lenDeColor =len(jugadorActual.tablero[col])
                    Juego.juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} pone el {carta.tipo} {carta.nombre} en el grupo {col}  len del color {lenDeColor} carta1 {jugadorActual.tablero[col][0].nombre}') #quitar lencolor
                else:
                    Juego.juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} no hace nada con el {carta.tipo} {carta.nombre}')                
            jugadorActual.mano.remove(carta)
        
        else:
            
            if(carta.subtipo == 'renta'):
                if(jugada[1] == 'dinero'):
                    jugadorActual.tablero['dinero'].append(carta)
                    jugadorActual.mano.remove(carta)
                    Juego.juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} pone {carta.nombre} como dinero')
                elif(jugada[1] == 'mano'):
                    pass
                elif(jugada[3]):
                    Juego.juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} usa la accion doblaRenta y duplica el monto a pagar de {carta.nombre}')
                    for i in cartasAUsar:
                        if(i == cartasAUsar[len(cartasAUsar) - 1]):
                            break
                        if(i[0].nombre == 'doblaRenta'):
                            self.descarte.append(i[0])
                            jugadorActual.mano.remove(i[0])
                            cartasAUsar.remove(i)     
                elif(carta.todos):
                    monto = jugada[2]
                    Juego.juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} usa la carta {carta.tipo} {carta.nombre} contra todos')
                    self.descarte.append(carta)
                    jugadorActual.mano.remove(carta)
                    for j in self.jugadores:
                        if (j != jugadorActual):
                            j.Responder(jugadorActual, self.mazo, self.descarte, carta, monto)
                else:
                    monto = jugada[2]
                    jug = jugada[4]
                    jug.Responder(jugadorActual, self.mazo, self.descarte, carta, monto)
                    Juego.juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} usa la carta {carta.tipo} {carta.nombre} contra {jug.nombre}')                   
                    self.descarte.append(carta)
                    jugadorActual.mano.remove(carta)
            
            elif(carta.subtipo == 'construccion'):
                col = jugada[1]
                if(carta.nombre == 'casa'):
                    if (len(jugadorActual.tablero[col]) > 0 and len(jugadorActual.tablero[col]) == jugadorActual.tablero[col][0].cantGrupo):
                        jugadorActual.tablero[col].append(carta)
                        carta.colorC = col
                        Juego.juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} pone la carta {carta.tipo} {carta.nombre} en el grupo {carta.colorC}')
                elif(carta.nombre == 'hotel'):
                    if (len(jugadorActual.tablero[col]) > 0 and len(jugadorActual.tablero[col]) == jugadorActual.tablero[col][0].cantGrupo + 1):
                        jugadorActual.tablero[col].append(carta)
                        carta.colorC = col
                        Juego.juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} pone la carta {carta.tipo} {carta.nombre} en el grupo {carta.colorC}')
                else:
                    jugadorActual.tablero['dinero'].append(carta)
                    Juego.juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} pone la carta {carta.tipo} {carta.nombre} como dinero')
                jugadorActual.mano.remove(carta)
                               
            elif(carta.subtipo == 'rapida'):
                pass
            
            elif(carta.subtipo == 'robarprop'):
                propEnT, jugAsociado = PropiedadesEnTablero(jugadorActual, self.jugadores)
                if(len(propEnT) > 0):
                    if(carta.intercambio):
                        jug = jugada[3]
                        propsADar = jugada[2]
                        propsInter = jugada[1]  
                        Juego.juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} usa la carta {carta.tipo} {carta.nombre} contra {jug.nombre}')                         
                        jug.Responder(jugadorActual, self.mazo, self.descarte, carta, (propsADar, propsInter))
                    elif(carta.cuantas != None):
                        jug = jugada[2]
                        propsADar = jugada[1]            
                        Juego.juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} usa la carta {carta.tipo} {carta.nombre} contra {jug.nombre}')                                                 
                        jug.Responder(jugadorActual, self.mazo, self.descarte, carta, propsADar)
                    elif(carta.nombre == 'factorDecisivo'):
                        if(jugada[1] == 'dinero'):
                            jugadorActual.tablero['dinero'].append(carta)
                            jugadorActual.mano.remove(carta)
                            Juego.juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} pone la carta {carta.tipo} {carta.nombre} como dinero')
                        elif(jugada[1] == 'mano'):
                            pass
                        else:
                            jugadorObjetivo = jugada[2]
                            grupo = jugada[1]
                            Juego.juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} usa la carta {carta.tipo} {carta.nombre} contra {jugadorObjetivo.nombre}')
                            jugadorObjetivo.Responder(jugadorActual, self.mazo, self.descarte, carta, grupo)
                            a=5
                    else:
                        if(jugada[1] == 'dinero'):
                            jugadorActual.tablero['dinero'].append(carta)
                            jugadorActual.mano.remove(carta)
                            Juego.juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} pone la carta {carta.tipo} {carta.nombre} como dinero')
                        else:
                            pass #dejarla en la mano
                        
            elif(carta.subtipo == 'robardinero'):
                if(carta.todos):
                    Juego.juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} usa la carta {carta.tipo} {carta.nombre} contra todos')
                    for i in jugada[2]:
                        if (i != jugadorActual):
                            i.Responder(jugadorActual, self.mazo, self.descarte, carta, carta.monto)
                else:
                    jug = jugada[2] #jug = jugada[1]
                    Juego.juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} usa la carta {carta.tipo} {carta.nombre} contra {jug.nombre}')
                    jug.Responder(jugadorActual, self.mazo, self.descarte, carta, carta.monto)
            
            else: #robar carta
                Crupier.RepartirCartas(False, jugadorActual, self.mazo, int(carta.cantCartasATomar), self.descarte)
                Juego.juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} usa la {carta.tipo} {carta.nombre} y toma {carta.cantCartasATomar} del mazo')                
    
    def ResponderAJugada(self, respuesta):
        jugadorObjetivo = self.jugador
        carta = respuesta[0]
        if(carta.nombre == 'diqno' and respuesta[1] == True):
            Juego.juegoMD.JuegoMD.notificaciones.append(f'{self.jugador.nombre} usa la {carta.tipo} {carta.nombre} y niega el efecto contra el')
            self.descarte.append(respuesta[0])
            jugadorObjetivo.mano.remove(respuesta[0])
        elif(len(respuesta) == 3):
            if type(respuesta[2])==str:
                a = 5
            self.DarCartas(respuesta[1], respuesta[2])
        elif(len(respuesta) == 2):
            self.DarCartas(respuesta[1])
        elif(carta.tipo == 'accion'):
            if(carta.subtipo == 'robarprop'):
                if(carta.intercambio == True): #AKI FALTA LA OTRA MITAD CREO
                    for i in respuesta[3]:
                        if(i.tipo == 'propiedad'):
                            respuesta[1].AnadirPropiedad(self.jugador, i)
                        elif(i.tipo == 'accion'):
                            a = 5
                        elif(i.tipo == 'comodin'):
                            respuesta[1].AnadirComodin(self.jugador, i)

                elif(carta.cuantas != None):
                    propsADar = respuesta[2]
                    for i in propsADar:
                        if(i.tipo == 'propiedad'):
                            self.jugador.AnadirPropiedad(respuesta[2], i)
                        elif(i.tipo == 'comodin'):
                            self.jugador.AnadirComodin(respuesta[2], i)
                        else:
                            a = 5
                        Juego.juegoMD.JuegoMD.notificaciones.append(f'{self.jugador.nombre} le da la {i.tipo} {i.nombre} a {respuesta[2].nombre}')
                else:
                    respuesta[1].tablero[respuesta[2]].extend(propsADar)
                    self.jugador.tablero[respuesta[2]].clear()
        self.jugador.AcomodarTablero()
        # for i in self.jugador.tablero:
        #     if(len(self.jugador.tablero[i]) > 0):
        #         if self.jugador.tablero[i][0].tipo == 'comodin' and i != 'dinero' and i != 'comodines':
        #             Juego.juegoMD.JuegoMD.notificaciones.append(f'{self.jugador.nombre} en el color {i} tiene {self.jugador.tablero[i][0].nombre} en 0')
        
        if(type(respuesta[1]) != bool):
            respuesta[1].AcomodarTablero()
            # for i in respuesta[1].tablero:
            #     if(len(respuesta[1].tablero[i]) > 0):
            #         if respuesta[1].tablero[i][0].tipo == 'comodin' and i != 'dinero' and i != 'comodines':
            #             Juego.juegoMD.JuegoMD.notificaciones.append(f'{respuesta[1].nombre} en el color {i} tiene {respuesta[1].tablero[i][0].nombre} en 0')
        

    
    def DarCartas(self, jugadorActual, cartasADar = None):
        if(cartasADar != None):
            for i in cartasADar:
                if(type(i) != list):
                    if(i.tipo == 'propiedad'):
                        self.jugador.AnadirPropiedad(jugadorActual,i )
                        Juego.juegoMD.JuegoMD.notificaciones.append(f'{self.jugador.nombre} le da la {i.tipo} {i.nombre} a {jugadorActual.nombre}')
                    elif(i.tipo == 'comodin' ):
                        self.jugador.AnadirComodin(jugadorActual,i)
                        Juego.juegoMD.JuegoMD.notificaciones.append(f'{self.jugador.nombre} le da la {i.tipo} {i.nombre} a {jugadorActual.nombre} como comodin')             
                    elif i.tipo == 'accion':
                        if i.subtipo == 'construccion' and i.colorC != None:
                            self.jugador.AnadirConstruccion(jugadorActual, i)
                            Juego.juegoMD.JuegoMD.notificaciones.append(f'{self.jugador.nombre} le da la {i.tipo} {i.nombre} a {jugadorActual.nombre} como construccion')
                        else:
                            self.jugador.AnadirDinero(jugadorActual,i)
                            Juego.juegoMD.JuegoMD.notificaciones.append(f'{self.jugador.nombre} le da la {i.tipo} {i.nombre} a {jugadorActual.nombre} como dinero')
 
                    else:
                        self.jugador.AnadirDinero(jugadorActual,i)
                        Juego.juegoMD.JuegoMD.notificaciones.append(f'{self.jugador.nombre} le da la {i.tipo} {i.nombre} a {jugadorActual.nombre} como dinero')
                else:
                    col = i[0].color
                    for j in i:
                        jugadorActual.tablero[col].append(j)
                        self.jugador.tablero[col].remove(j)
                        Juego.juegoMD.JuegoMD.notificaciones.append(f'{self.jugador.nombre} le da la {j.tipo} {j.nombre} {col} a {jugadorActual.nombre}') 
            self.jugador.AcomodarTablero()
            jugadorActual.AcomodarTablero()     
        else:
            for i in self.jugador.tablero:
                if(i != 'dinero' and i!='comodines' and len(self.jugador.tablero[i])>0 and self.jugador.tablero[i][len(self.jugador.tablero[i]) - 1].tipo != 'propiedad' and self.jugador.tablero[i][len(self.jugador.tablero[i]) - 1].tipo != 'comodin'):
                    for k in self.jugador.tablero[i]:
                        jugadorActual.tablero[i].append(k)
                        self.jugador.tablero[i].remove(k)
                        if self.jugador.tablero[i][0].tipo == 'comodin': #quitar
                            a=5  
                        Juego.juegoMD.JuegoMD.notificaciones.append(f'{self.jugador.nombre} le da la {k.tipo} {k.nombre} a {jugadorActual.nombre}')
                else:
                    for j in self.jugador.tablero[i]:
                        if(j.tipo == 'propiedad'):
                            self.jugador.AnadirPropiedad(jugadorActual, j)
                            Juego.juegoMD.JuegoMD.notificaciones.append(f'{self.jugador.nombre} le da la {j.tipo} {j.nombre} a {jugadorActual.nombre}')
                        elif(j.tipo == 'comodin' and j.enUso != 'dinero'):  #OJOOO revisar este tratamiento de comodin con el de arriba, busca palabra tratamiento
                            self.jugador.AnadirComodin(jugadorActual, j)
                            Juego.juegoMD.JuegoMD.notificaciones.append(f'{self.jugador.nombre} le da la {j.tipo} {j.nombre} a {jugadorActual.nombre} como comodin')            
                        elif(j.tipo == 'accion' and j.subtipo == 'construccion' and j.colorC != None):
                            a = 5
                        else:
                            self.jugador.AnadirDinero(jugadorActual, j)
                            Juego.juegoMD.JuegoMD.notificaciones.append(f'{self.jugador.nombre} le da la {j.tipo} {j.nombre} a {jugadorActual.nombre} como dinero')
                self.jugador.AcomodarTablero()
                jugadorActual.AcomodarTablero()                

class JugadaRandom(Jugada):
    def __init__(self, jugador, mazo, descarte, jugada = None):
        super().__init__(jugador, mazo, descarte, jugada)
    
    def CrearJugada(self):
        a = rd.randint(0, 3)
        cantCartasAJugar = min(a, len(self.jugador.mano))
        cartasAJugar = rd.sample(self.jugador.mano, cantCartasAJugar)
                
        return cartasAJugar
    
    def CartasADescartar(self):
        cantCartasADescartar = len(self.jugador.mano) - 7
        cartasADescartar = []
        usado = []
        manoJugador = self.jugador.mano
        i = 0
        cartasPosiblesADescartar = []
        for k in manoJugador:
            if(k.tipo != 'propiedad'):
                cartasPosiblesADescartar.append(k)
        if(len(cartasPosiblesADescartar) < cantCartasADescartar):
            return self.jugador
        a = rd.sample(cartasPosiblesADescartar, cantCartasADescartar)
        return a
               
    def ComodinesAReponer(self):
        jugadorActual = self.jugador
        result = []
        for i in jugadorActual.tablero['comodines']:
            i.enUso = None
            if(len(i.color) > 0):
                col = rd.sample(i.color, 1)[0]
                result.append([i, col])
            else:
                colores = []
                for k in jugadorActual.tablero:
                    if(k != 'dinero' and k != 'comodines'):
                        colores.append(k)
                col = rd.sample(colores, 1)[0]
                result.append([i, col])
        return result
     
    def UsarDiQNo(self, carta):
        for i in self.jugador.mano:
                if(i.nombre == 'diqno'):
                    usar = rd.randint(0, 1)
                    if(usar == 1):
                        #self.descarte.append(i)
                        #self.jugador.mano.remove(i)
                        #Juego.juegoMD.JuegoMD.notificaciones.append(f'{self.jugador.nombre} usa la {i.tipo} {i.nombre} y niega el efecto de {carta.nombre} contra el')
                        return True, i
        return False, None  
    
    def UsarDoblaRenta(self, carta, cartasAUsar, monto):
        for i in cartasAUsar:
            if(i.nombre == 'doblaRenta'):
                usar = rd.randint(0, 1)
                if(usar == 1):             
                    return 2 * monto, True
        return monto, False                       
    
    def CartasResponder(self, jugadorActual, carta, monto):
        band, diqno = self.UsarDiQNo(carta)
        if(band):
            return [diqno, band]
        elif(carta.subtipo == 'renta' or carta.subtipo == 'robardinero'):
            din, total = DineroPorBilletes(self.jugador)
            dinProp, totalProp = DineroPorPropiedades(self.jugador)
            din[0].extend(dinProp[0])
            din[1].extend(dinProp[1])
            pagar = 0
            cartasADar = []
            indicesUsados = []
            if(total + totalProp >= monto):
                while(pagar < monto):
                    indice = rd.randint(0, len(din[0]) - 1)
                    if(indice not in indicesUsados):
                        cartasADar.append(din[1][indice])
                        pagar += din[0][indice]
                        indicesUsados.append(indice)
                return [carta, jugadorActual, cartasADar]
            else:
                return [carta, jugadorActual]
        elif(carta.subtipo == 'robarprop'):
            if(carta.intercambio == True):
                return [carta, jugadorActual, monto[0], monto[1]]
            else:
                propsADar = monto
                return [carta, jugadorActual,propsADar]

    def ComoUsarCarta(self, carta, paraDoblaRenta):
        jugadorActual = self.jugador
        if(carta.tipo == 'propiedad' or carta.tipo == 'dinero'):
            return [carta]
        elif(carta.tipo == 'comodin'):
            if(len(carta.color) > 0):
                col = rd.sample(carta.color, 1)[0]
            else:
                cols = []
                for i in jugadorActual.tablero:
                    if(i != 'dinero' and i != 'comodines'):
                        cols.append(i)
                col = rd.sample(sorted(cols), 1)[0]
            return [carta, col]
        elif(carta.tipo == 'accion'):
            if(carta.subtipo == 'renta'):
                posiblePago = []
                for i in jugadorActual.tablero:
                    if(len(jugadorActual.tablero[i]) > 0 and len(carta.propiedades) == 0 and i != 'dinero' and i != 'comodines'):
                        posiblePago.append(i)
                    elif(len(jugadorActual.tablero[i]) > 0 and i in carta.propiedades):
                        posiblePago.append(i)
                if(len(posiblePago) > 0):
                    col = rd.sample(posiblePago, 1)
                    monto = CalcularMonto(jugadorActual, col[0]) 
                    monto, bool = self.UsarDoblaRenta(carta, paraDoblaRenta, monto)
                    if(carta.todos):
                        return [carta, col, monto, bool ,self.jugadores]
                    else:
                        jug = self.jugadores[0]
                        while(jug == jugadorActual):
                            jug = rd.sample(self.jugadores, 1)[0]
                        return [carta, col, monto, bool,jug]
                else:
                    rand = rd.randint(0, 1)
                    if(rand == 1):
                        return [carta, 'mano']
                    return [carta, 'dinero']
            elif(carta.subtipo == 'construccion'):
                coloresTablero = sorted(jugadorActual.tablero).copy()
                coloresTablero.remove('dinero')
                coloresTablero.remove('blanco')
                coloresTablero.remove('negro')
                coloresTablero.remove('comodines')
                col = rd.sample(coloresTablero, 1)[0]
                return [carta, col]
            elif(carta.subtipo == 'robarprop'):
                propEnT, jugAsociado = PropiedadesEnTablero(jugadorActual, self.jugadores)
                if(len(propEnT) > 0):
                    if(carta.intercambio):
                        flag = False
                        jugList = []
                        while(not flag):
                            if(len(jugList) == len(jugAsociado)):
                                return
                            jug = rd.randint(0, len(jugAsociado) - 1)
                            if(jugAsociado[jug] != jugadorActual):
                                flag = True
                            else:
                                jugList.append(jug)
                        propsADar = []
                        #indices = []
                        propsInter = []
                        misProps, _ = DineroPorPropiedades(jugadorActual)
                        jugProps, _ = DineroPorPropiedades(jugAsociado[jug])
                        misIndices = []
                        misIndicesJug = []
                        if(len(misProps[1]) >= carta.cuantas and len(jugProps[1]) >= carta.cuantas):
                            if(not((len(misProps[1]) == 1 and type(misProps[1][0]) == list) or (len(jugProps[1]) == 1 and type(jugProps[1][0]) == list))):
                                while(len(propsInter) < carta.cuantas):
                                    ind = rd.randint(0, len(misProps[1]) - 1)
                                    if(ind not in misIndices and type(misProps[1][ind]) != list):
                                        propsInter.append(misProps[1][ind])
                                        misIndices.append(ind)
                                while(len(propsADar) < carta.cuantas):
                                    indice = rd.randint(0, len(jugAsociado) - 1)
                                    if(len(misIndicesJug) == len(jugAsociado)):
                                        return
                                    if(indice not in misIndicesJug and jugAsociado[jug] == jugAsociado[indice] and type(propEnT[indice]) != list):
                                        propsADar.append(propEnT[indice]) 
                                        misIndicesJug.append(indice)
                        return [carta, propsInter, propsADar, jugAsociado[jug]]
                    else:
                        jug = rd.randint(0, len(jugAsociado) - 1)
                        propsADar = []
                        if(carta.cuantas != None):
                            indices = []
                            jugProps, _ = DineroPorPropiedades(jugAsociado[jug])
                            if(len(jugProps[1]) >= carta.cuantas ):
                                if(not(len(jugProps[1]) == 1 and type(jugProps[1][0]) == list)):
                                    while(len(propsADar) < carta.cuantas):
                                        indice = rd.randint(0, len(jugAsociado) - 1)
                                        if(indice not in indices and jugAsociado[jug] == jugAsociado[indice] and type(propEnT[indice]) != list):
                                            propsADar.append(propEnT[indice])
                                            indices.append(indice)
                            return [carta, propsADar, jugAsociado[jug]]
                        else:
                            grupCompl = []
                            jugAs = []
                            for i in range(len(propEnT)):
                                if(type(propEnT[i]) == list and jugAsociado[i] != jugadorActual):
                                    grupCompl.append(propEnT[i])
                                    jugAs.append(jugAsociado[i])
                            if(len(grupCompl) > 0):        
                                indice = rd.randint(0, len(grupCompl) - 1)
                                return [carta, grupCompl[indice], jugAs[indice]]
                            else:
                                rand = rd.randint(0, 1)
                                if(rand == 1):
                                    return [carta, 'mano']
                                return [carta, 'dinero']
                else:
                    rand = rd.randint(0, 1)
                    if(rand == 1):
                        return [carta, 'mano']
                    return [carta, 'dinero']
            elif(carta.subtipo == 'robardinero'):
                if(carta.todos):
                    return [carta, jugadorActual, self.jugadores]
                else:
                    jug = self.jugadores[0]
                    while(jug == jugadorActual):
                        jug = rd.sample(self.jugadores, 1)[0]
                    return [carta, jugadorActual, jug]
            else: #ACCION ROBAR 2 CARTAS
                return [carta]