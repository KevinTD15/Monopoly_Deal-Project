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
    def AcomodarTablero():
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
                
    def UsarDiQNo(self, carta):
        for i in self.jugador.mano:
                if(i.nombre == 'diqno'):
                    usar = rd.randint(0, 1)
                    if(usar == 1):
                        self.descarte.append(i)
                        self.jugador.mano.remove(i)
                        juegoMD.JuegoMD.notificaciones.append(f'{self.jugador.nombre} usa la {i.tipo} {i.nombre} y niega el efecto de {carta.nombre} contra el')
                        return True
        return False
    
    
    
    def AnadirPropiedadMano(self,carta):
        jugadorActual = self.jugador
        if(len(jugadorActual.tablero[carta.color]) < carta.cantGrupo):
            jugadorActual.tablero[carta.color].append(carta)
            juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} pone la {carta.tipo} {carta.color} {carta.nombre} en su tablero') 
        elif(len(jugadorActual.tablero[carta.color]) > 0 and len(jugadorActual.tablero[carta.color]) >= jugadorActual.tablero[carta.color][0].cantGrupo):
            for k in jugadorActual.tablero[carta.color]:
                if(k.tipo == 'comodin'):
                    jugadorActual.tablero[carta.color].insert(0, carta)
                    jugadorActual.tablero['comodines'].append(k)
                    k.enUso = None
                    jugadorActual.tablero[carta.color].remove(k)
        jugadorActual.mano.remove(carta)

            
    def AnadirPropiedad(self, jugadorActual,carta ):
        if(len(jugadorActual.tablero[carta.color]) > 0 and len(jugadorActual.tablero[carta.color]) >= jugadorActual.tablero[carta.color][0].cantGrupo):
            for k in jugadorActual.tablero[carta.color]:
                if(k.tipo == 'comodin'):
                    jugadorActual.tablero[carta.color].insert(0, carta)
                    self.jugador.tablero[carta.color].remove(carta)
                    jugadorActual.tablero['comodines'].append(k)
                    k.enUso = None
                    jugadorActual.tablero[carta.color].remove(k)                   
        else:
            jugadorActual.tablero[carta.color].append(carta)
            self.jugador.tablero[carta.color].remove(carta)
 
    def AnadirComodin(self, jugadorActual,carta):
        if (carta.enUso != None and carta.enUso != 'dinero'): #OJOOO revisar este tratamiento de comodin con el de abajo
            jugadorActual.tablero['comodines'].append(carta)
            self.jugador.tablero[carta.enUso].remove(carta) 
            carta.enUso = None   
        elif (carta.tipo == 'comodin' and carta.enUso == None):
            jugadorActual.tablero['comodines'].append(carta)
            self.jugador.tablero['comodines'].remove(carta)    
            
    def AnadirSimple(self, jugadorActual,carta):
        jugadorActual.tablero[carta.tipo].append(carta)
        self.jugador.tablero[carta.tipo].remove(carta)
    
    def AnadirDinero(self, jugadorActual,carta):
        jugadorActual.tablero['dinero'].append(carta)
        self.jugador.tablero['dinero'].remove(carta)
                        
                            
    def DarCartas(self, jugadorActual, cartasADar = None):
        if(cartasADar != None):
            for i in cartasADar:
                if(type(i) != list):
                    if(i.tipo == 'propiedad'):
                        self.AnadirPropiedad(jugadorActual,i )
                        juegoMD.JuegoMD.notificaciones.append(f'{self.jugador.nombre} le da la {i.tipo} {i.nombre} a {jugadorActual.nombre}')
                    elif(i.tipo == 'comodin' ):
                        self.AnadirComodin(jugadorActual,i)
                        juegoMD.JuegoMD.notificaciones.append(f'{self.jugador.nombre} le da la {i.tipo} {i.nombre} a {jugadorActual.nombre} como comodin')             
                    else:
                        self.AnadirDinero(jugadorActual,i)
                        juegoMD.JuegoMD.notificaciones.append(f'{self.jugador.nombre} le da la {i.tipo} {i.nombre} a {jugadorActual.nombre} como dinero')
                else:
                    col = i[0].color
                    for j in i:
                        jugadorActual.tablero[col].append(j)
                        self.jugador.tablero[col].remove(j)
                        #OJOOO anadi notificacion
                        juegoMD.JuegoMD.notificaciones.append(f'{self.jugador.nombre} le da la {j.tipo} {j.nombre} a {jugadorActual.nombre}')
 
        else:
            for i in self.jugador.tablero:
                if(i != 'dinero' and i!='comodines' and len(self.jugador.tablero[i])>0 and self.jugador.tablero[i][len(self.jugador.tablero[i]) - 1].tipo != 'propiedad' and self.jugador.tablero[i][len(self.jugador.tablero[i]) - 1].tipo != 'comodin'):
                    for k in self.jugador.tablero[i]:
                       jugadorActual.tablero[i].append(k)
                       self.jugador.tablero[i].remove(k)
                       juegoMD.JuegoMD.notificaciones.append(f'{self.jugador.nombre} le da la {k.tipo} {k.nombre} a {jugadorActual.nombre}')
                for j in self.jugador.tablero[i]:
                    if(j.tipo == 'propiedad'):
                        self.AnadirPropiedad(jugadorActual, j)
                        juegoMD.JuegoMD.notificaciones.append(f'{self.jugador.nombre} le da la {j.tipo} {j.nombre} a {jugadorActual.nombre}')
                    elif(j.tipo == 'comodin'):  #OJOOO revisar este tratamiento de comodin con el de arriba, busca palabra tratamiento
                        self.AnadirComodin(jugadorActual, j)
                        juegoMD.JuegoMD.notificaciones.append(f'{self.jugador.nombre} le da la {j.tipo} {j.nombre} a {jugadorActual.nombre} como comodin')            
                    else:
                        self.AnadirDinero(jugadorActual, j)
                        juegoMD.JuegoMD.notificaciones.append(f'{self.jugador.nombre} le da la {j.tipo} {j.nombre} a {jugadorActual.nombre} como dinero')
                            
    def ResponderAJugada(self, jugadorActual, carta, monto):
        band = self.UsarDiQNo(carta)
        if(not band):
            if(carta.subtipo == 'renta' or carta.subtipo == 'robardinero'):
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
                    self.DarCartas(jugadorActual, cartasADar)
                else:
                    self.DarCartas(jugadorActual)
            elif(carta.subtipo == 'robarprop'):
                if(carta.intercambio == True):
                    propsADar = monto[0]
                    for i in monto[1]:
                        if(i.tipo == 'propiedad'):
                            self.jugador.tablero[i.color].append(i)
                            jugadorActual.tablero[i.color].remove(i)
                        elif(i.tipo == 'comodin'):
                            self.jugador.tablero['comodines'].append(i)
                            if(i.enUso != None):
                                jugadorActual.tablero[i.enUso].remove(i)
                            else:
                                jugadorActual.tablero['comodines'].remove(i)
                        juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} le da la {i.tipo} {i.nombre} a {self.jugador.nombre}')
                else:
                    propsADar = monto
                if(carta.cuantas != None):
                    for i in propsADar:
                        if(i.tipo == 'propiedad'):
                            self.AnadirPropiedad(jugadorActual, i)
                        else:
                            self.AnadirComodin(jugadorActual, i)
                        juegoMD.JuegoMD.notificaciones.append(f'{self.jugador.nombre} le da la {i.tipo} {i.nombre} a {jugadorActual.nombre}')
                else:
                    jugadorActual.tablero[propsADar[0].color].extend(propsADar)
                    self.jugador.tablero[propsADar[0].color].clear()
            else:
                pass
    
    def AcomodarTablero(self): #####COMPLETAR ESTOOOOOOOOOOOOOOOOOOOO
        for i in self.jugador.tablero:
            if(i != 'dinero' and i != 'comodines'):
                if(len(self.jugador.tablero[i]) == 1 and self.jugador.tablero[i][0].tipo == 'comodin'):
                    self.jugador.tablero[i][0].enUso = None
                    self.jugador.tablero['comodines'].append(self.jugador.tablero[i][0])
                    self.jugador.tablero[i].remove(self.jugador.tablero[i][0])
                else:
                    if(len(self.jugador.tablero[i]) > 1 and self.jugador.tablero[i][0].tipo == 'comodin'):
                        band = False
                        for k in range(len(self.jugador.tablero[i])):
                            if(self.jugador.tablero[i][k].tipo == 'propiedad'):
                                tmp = self.jugador.tablero[i][0]
                                prop = self.jugador.tablero[i][k]
                                self.jugador.tablero[i].remove(prop)
                                self.jugador.tablero[i].remove(tmp)
                                self.jugador.tablero[i].insert(0, prop)
                                self.jugador.tablero[i].insert(k, tmp)
                                band = True
                        if(not band):
                            for k in self.jugador.tablero[i]:
                                self.jugador.tablero['comodines'].append(k)
                                k.enUso = None
                            self.jugador.tablero[i].clear()    
    
    def UsarCarta(self, carta, jugada):
        jugadorActual = self.jugador  #OJOOO duda jugador ahi quien es
        
        if(carta.tipo == 'propiedad'):
            self.AnadirPropiedadMano(carta)
            pass
        elif(carta.tipo == 'dinero'):
            jugadorActual.tablero[carta.tipo].append(carta)
            jugadorActual.mano.remove(carta)
            juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} pone la carta de {carta.tipo} de $ {carta.nombre} en su tablero')        
        
        elif(carta.tipo == 'comodin'):
            if (len(carta.color) > 0):
                col = rd.sample(carta.color, 1)
                if(len(jugadorActual.tablero[col[0]]) > 0 and jugadorActual.tablero[col[0]][0].cantGrupo > len(jugadorActual.tablero[col[0]])):
                    jugadorActual.tablero[col[0]].append(carta)
                    carta.enUso = col[0]
                    juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} pone el {carta.tipo} {carta.nombre} en el grupo {col[0]}') 
                else:
                    jugadorActual.tablero['dinero'].append(carta)
                    carta.enUso = 'dinero'
                    juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} pone el {carta.tipo} {carta.nombre} como dinero') 
            else:
                cols = []
                for i in jugadorActual.tablero:
                    if(i != 'dinero' and i != 'comodines'):
                        cols.append(i)
                col = rd.sample(sorted(cols), 1)
                if(len(jugadorActual.tablero[col[0]]) > 0 and col[0] != 'dinero' and jugadorActual.tablero[col[0]][0].cantGrupo > len(jugadorActual.tablero[col[0]])):                    
                    jugadorActual.tablero[col[0]].append(carta)
                    carta.enUso = col[0]
                    juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} pone el {carta.tipo} {carta.nombre} en el grupo {col[0]}') 
                else:
                    juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} no hace nada con el {carta.tipo} {carta.nombre}')                
            jugadorActual.mano.remove(carta)
        
        else:
            
            if(carta.subtipo == 'renta'):
                posiblePago = []
                for i in jugadorActual.tablero:
                    if(len(jugadorActual.tablero[i]) > 0 and len(carta.propiedades) == 0 and i != 'dinero' and i != 'comodines'):
                        posiblePago.append(i)
                    elif(len(jugadorActual.tablero[i]) > 0 and i in carta.propiedades):
                        posiblePago.append(i)
                if(len(posiblePago) == 0):
                    jugadorActual.tablero['dinero'].append(carta)
                    juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} usa la carta {carta.tipo} {carta.nombre} como dinero')
                    jugadorActual.mano.remove(carta)
                else:
                    col = rd.sample(posiblePago, 1)
                    monto = CalcularMonto(jugadorActual, col[0])
                    monto = UsarDoblaRenta(jugadorActual, self.descarte, carta, jugada, monto)
                    if(carta.todos):
                        juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} usa la carta {carta.tipo} {carta.nombre} contra todos')
                        for j in self.jugadores:
                            if (j != jugadorActual):
                                j.Responder(jugadorActual, self.mazo, self.descarte, carta, monto)
                                #self.AcomodarTablero()
                    else:
                        jug = self.jugadores[0]
                        while(jug == jugadorActual):
                            jug = rd.sample(self.jugadores, 1)[0]
                        #jugs = self.jugadores.copy()
                        #jugs.remove(jugadorActual)
                        #jug = rd.sample(jugs, 1)
                        jug.Responder(jugadorActual, self.mazo, self.descarte, carta, monto)
                        juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} usa la carta {carta.tipo} {carta.nombre} contra {jug.nombre}')
                        
                    self.descarte.append(carta)
                    jugadorActual.mano.remove(carta)
            
            elif(carta.subtipo == 'construccion'):
                coloresTablero = sorted(jugadorActual.tablero).copy()
                coloresTablero.remove('dinero')
                coloresTablero.remove('blanco')
                coloresTablero.remove('negro')
                coloresTablero.remove('comodines')
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
                propEnT, jugAsociado = PropiedadesEnTablero(jugadorActual, self.jugadores)
                if(len(propEnT) > 0):
                    if(carta.intercambio):
                        jug = rd.randint(0, len(jugAsociado) - 1)
                        propsADar = []
                        indices = []
                        propsInter = []
                        misProps, _ = DineroPorPropiedades(jugadorActual)
                        misIndices = []
                        if(len(misProps[1]) > carta.cuantas):
                            while(len(propsInter) < carta.cuantas):
                                ind = rd.randint(0, len(misProps[1]) - 1)
                                if(ind not in misIndices and type(misProps[1][ind]) != list):
                                    propsInter.append(misProps[1][ind])
                            while(len(propsADar) < carta.cuantas):
                                indice = rd.randint(0, len(jugAsociado) - 1)
                                if(indice not in indices and jugAsociado[jug] == jugAsociado[indice] and type(propEnT[indice]) != list):
                                    propsADar.append(propEnT[indice])                                                              
                            jugAsociado[jug].Responder(jugadorActual, self.mazo, self.descarte, carta, (propsADar, propsInter))
                    else:                                  
                        jug = rd.randint(0, len(jugAsociado) - 1)
                        propsADar = []
                        if(carta.cuantas != None):
                            indices = []
                            while(len(propsADar) < carta.cuantas):
                                indice = rd.randint(0, len(jugAsociado) - 1)
                                if(indice not in indices and jugAsociado[jug] == jugAsociado[indice] and type(propEnT[indice]) != list):
                                    propsADar.append(propEnT[indice])                                                              
                            jugAsociado[jug].Responder(jugadorActual, self.mazo, self.descarte, carta, propsADar)
                        else:
                            #FACTOR DECISIVO
                            grupCompl = []
                            jugAs = []
                            for i in range(len(propEnT)):
                                if(type(propEnT[i]) == list and jugAsociado[i] != jugadorActual):
                                    grupCompl.append(propEnT[i])
                                    jugAs.append(jugAsociado[i])
                            if(len(grupCompl) > 0):        
                                indice = rd.randint(0, len(grupCompl) - 1)
                                jugAs[indice].Responder(jugadorActual, self.mazo, self.descarte, carta, grupCompl[indice])
                            
            elif(carta.subtipo == 'robardinero'):
                if(carta.todos):
                    juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} usa la carta {carta.tipo} {carta.nombre} contra todos')
                    for i in self.jugadores:
                        if (i != jugadorActual):
                            i.Responder(jugadorActual, self.mazo, self.descarte, carta, carta.monto)
                else:
                    jug = self.jugadores[0]
                    while(jug == jugadorActual):
                        jug = rd.sample(self.jugadores, 1)[0]
                    juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} usa la carta {carta.tipo} {carta.nombre} contra {jug.nombre}')
                    jug.Responder(jugadorActual, self.mazo, self.descarte, carta, carta.monto)
            
            else: #robar carta
                Crupier.RepartirCartas(False, jugadorActual, self.mazo, int(carta.cantCartasATomar), self.descarte)
                juegoMD.JuegoMD.notificaciones.append(f'{jugadorActual.nombre} usa la {carta.tipo} {carta.nombre} y toma {carta.cantCartasATomar} del mazo')                
    
def CalcularMonto(jugador, color):
    if(len(jugador.tablero[color]) <= jugador.tablero[color][0].cantGrupo):
        return jugador.tablero[color][0].renta[len(jugador.tablero[color]) - 1]
    else:
        i = 0
        cantPorGrupoColorI = jugador.tablero[color][0].cantGrupo
        acum = jugador.tablero[color][0].renta[len(jugador.tablero[color][0].renta) - 1]
        while i + cantPorGrupoColorI < len(jugador.tablero[color]):
            acum += jugador.tablero[color][len(jugador.tablero[color]) - 1 - i].monto
            i += 1
        return acum

def DineroPorBilletes(jugador):
    sum = 0
    dinero = ([],[])
    for i in jugador.tablero['dinero']:
        if (i.tipo == 'dinero'):
            sum += int(i.nombre)
            dinero[0].append(int(i.nombre))
            dinero[1].append(i)
        else:
            sum += i.valor
            dinero[0].append(i.valor)
            dinero[1].append(i)
    return dinero, sum

def DineroPorPropiedades(jugador):
    sum = 0
    dinero = ([],[])
    for i in jugador.tablero:
        if(i != 'dinero'):
            if(len(jugador.tablero[i])>0 and jugador.tablero[i][len(jugador.tablero[i]) - 1].tipo != 'propiedad' and jugador.tablero[i][len(jugador.tablero[i]) - 1].tipo != 'comodin'):
                m = CalcularMonto(jugador, i)
                sum += m
                dinero[0].append(m)
                grupoEntero = []
                for k in jugador.tablero[i]:
                    grupoEntero.append(k)
                dinero[1].append(grupoEntero)
            else:
                for j in jugador.tablero[i]:
                    if(j.nombre != 'Maestro'):
                        sum += j.valor
                        dinero[0].append(j.valor)
                        dinero[1].append(j)
    return dinero, sum
    
def PropiedadesEnTablero(jugadorActual, jugadores):
    cartas = []
    jug = []
    for i in jugadores:
        if(i != jugadorActual):
            for j in i.tablero:
                if(j != 'dinero' and len(i.tablero[j])>0 and i.tablero[j][len(i.tablero[j]) - 1].tipo != 'propiedad' and i.tablero[j][len(i.tablero[j]) - 1].tipo != 'comodin'):
                    grupoEntero = []
                    for h in i.tablero[j]:
                        grupoEntero.append(h)
                    cartas.append(grupoEntero)
                    jug.append(i)
                else :
                    for k in i.tablero[j]:
                        if(k.tipo == 'propiedad' or (k.tipo == 'comodin' and k.enUso != 'dinero')):
                            cartas.append(k)
                            jug.append(i)
    return cartas, jug

def UsarDoblaRenta(self, descarte,carta, cartasAUsar, monto): #PONER ESTO DONDE VA!!!!
        for i in cartasAUsar:
            if(i.nombre == 'doblaRenta'):
                usar = rd.randint(0, 1)
                if(usar == 1):
                    descarte.append(i)
                    self.mano.remove(i)
                    cartasAUsar.remove(i)
                    juegoMD.JuegoMD.notificaciones.append(f'{self.nombre} usa la {i.tipo} {i.nombre} y duplica el monto a pagar de {carta.nombre}')
                    return 2 * monto
        return monto