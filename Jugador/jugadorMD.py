from Jugador.jugador import Jugador
from Juego.jugada import JugadaRandom
from utiles import *
from PLN.gramaticaCartas import *

class JugadorAleatorio(Jugador):
    
    def __init__(self, nombre, esBot):
        super().__init__(nombre, esBot)
        self.tablero = {}
        self.colorCantGrupo = {}
        
        for i in range(len(coloresEnUso)):
            self.tablero[coloresEnUso[i]] = []
            self.colorCantGrupo[coloresEnUso[i]] = cantGrupo[i]
        self.tablero['dinero'] = []
        self.tablero['comodines'] = []

        self.mano = []

    def DescartarCartasJ(self,mazo, descarte, jugadores):
        j = JugadaRandom(self, mazo, descarte, jugadores)
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
        jugadsav=jugadores
        j = JugadaRandom(self, mazo, descarte, jugadores)
        for i in jugada:
            if(i == jugada[len(jugada) - 1]):
                break
            if(i != None):
                jugadasav=jugada
                j.UsarCarta(i[0], i, jugada)
                j.ReponerComodin(jugada[len(jugada) - 1])
            
    def Responder(self, jugadorActual, mazo, descarte, carta, monto):
        j = JugadaRandom(self, mazo, descarte)
        resp = j.CartasResponder(jugadorActual, carta, monto)
        j.ResponderAJugada(resp)
        
        
class JugadorInteligente(Jugador):
    def __init__(self, nombre, esBot):
        super().__init__(nombre, esBot)
        self.tablero = {}
        self.colorCantGrupo = {}
        
        for i in range(len(coloresEnUso)):
            self.tablero[coloresEnUso[i]] = []
            self.colorCantGrupo[coloresEnUso[i]] = cantGrupo[i]
        self.tablero['dinero'] = []
        self.tablero['comodines'] = []

        self.mano = []
        
        
    def EvaluarJugada(jugadorActual, jugada, jugadores, descarte, mazo):
        '''HEURISTICA DE PROPIEDADES'''
        valor = 0
        ranking = RankingPropiedades(jugadorActual)

        for i in jugada:
            if (i == jugada[len(jugada) - 1]):
                break
            if(i[0].tipo == 'propiedad'):
                for k in ranking:
                    if(i[0].color in ranking[k] and k != 0):
                        if(k == 1):
                            valor += 1/k - CalcularProbabilidad(True, jugadores, jugadorActual, descarte, mazo)
                        else:
                            valor += 1 / k - CalcularProbabilidad(False, jugadores, jugadorActual, descarte, mazo)
                        ranking[k - 1].append(i[0].color)
                        ranking[k].remove(i[0].color)
                        if(len(ranking[0]) == 3):
                            valor += 1000
                        break
            elif(i[0].tipo == 'comodin'):
                for k in ranking:
                    if(i[1] in ranking[k] and k != 0):
                        if(len(jugadorActual.tablero[i[1]]) > 0 and len(jugadorActual.tablero[i[1]]) < jugadorActual.tablero[i[1]][0].cantGrupo):
                            if(k == 1):
                                valor += 1/k - CalcularProbabilidad(True, jugadores, jugadorActual, descarte, mazo)
                            else:
                                valor += 1 / k - CalcularProbabilidad(False, jugadores, jugadorActual, descarte, mazo)
                            ranking[k - 1].append(i[1])
                            ranking[k].remove(i[1])
                            if(len(ranking[0]) == 3):
                                valor += 1000
                            break
            elif(i[0].tipo == 'dinero'):
                _, dinprop = DineroPorPropiedades(jugadorActual)
                _, dindin = DineroPorBilletes(jugadorActual)
                if(dinprop > dindin):
                    valor += CalcularProbabilidadDin(jugadores, jugadorActual, descarte, mazo)
                else:
                    valor += 1 - CalcularProbabilidadDin(jugadores, jugadorActual, descarte, mazo)
            elif(i[0].tipo == 'accion'):
                if(i[0].nombre == 'diqno'):
                    break
                elif(i[0].tipo == 'robarcarta'):
                    valor += 1/2
                elif(i[0].subtipo == 'robarprop'):
                    if(i[1] == 'mano' or i[1] == 'dinero'):
                        break
                    elif(i[0].intercambio):
                        if(len(i[2]) == 0 or (type[i[1]] == list and len(i[1]) == 0)):
                            break
                        count = 0
                        for j in i[1]:
                            for k in ranking:
                                if(j.color == ranking[k] and k == 0):
                                    break
                                if(j.color == ranking[k] and k != 0):
                                    count += 1 - 1/k
                        for j in i[2]:
                            for k in ranking:
                                if(j.color == ranking[k] and k != 0):
                                    if(k == 1 and len(ranking[0])==2):
                                        count+=100
                                    else:
                                        count += 1/k
                        valor += count
                    else:
                        if(i[0].cuantas != None):
                            count = 0
                            for j in i[1]:
                                for k in ranking:
                                    if(j.color == ranking[k] and k != 0):
                                        if(k == 1 and len(ranking[0])==2):
                                            count+=100
                                        else:
                                            count += 1/k
                                        
                            valor += count
                        else: #FACTOR DECISIVO
                            if(len(ranking[0])==2):
                                valor += 100
                            else:
                                valor += 3                          
                elif(i[0].subtipo == 'construccion'):
                    if(i[0].nombre == 'casa'):
                        if(len(jugadorActual.tablero[i[1]]) > 0 and len(jugadorActual.tablero[i[1]]) == jugadorActual.tablero[i[1]][0].cantGrupo):
                            #if(CantidadDeConstrucciones(jugadorActual.tablero[i[1]]) >= 1):
                            flag = False
                            for k in jugada:
                                if(k == jugada[len(jugada) -1]):
                                    break
                                if(k[0].tipo == 'accion' and k[0].subtipo == 'renta' and (k[0].propiedades == None or i[1] in k[0].propiedades)):
                                    valor += 1
                                    flag = True
                            if(not flag):
                                valor += 1/3
                        else:
                            valor += 1/10
                    elif(i[0].nombre == 'hotel'):
                        if(len(jugadorActual.tablero[i[1]]) > 0 and len(jugadorActual.tablero[i[1]]) == jugadorActual.tablero[i[1]][0].cantGrupo + 1):
                            flag = False
                            for k in jugada:
                                if(k == jugada[len(jugada) -1]):
                                    break
                                if(k[0].tipo == 'accion' and k[0].subtipo == 'renta' and (k[0].propiedades == None or i[1] in k[0].propiedades)):
                                    valor += 1.2
                                    flag = True
                            if(not flag):
                                valor += 1/2
                        else:
                            valor += 1/10
                elif(i[0].subtipo == 'renta'):
                    if(i[1] == 'dinero'):
                        if(len(i[0].propiedades) == 0):
                            for j in jugadorActual.tablero:
                                if(len(jugadorActual.tablero[j]) > 0):
                                    break
                            _, dinprop = DineroPorPropiedades(jugadorActual)
                            _, dindin = DineroPorBilletes(jugadorActual)
                            if(dinprop > dindin):
                                valor += 1/15
                            else:
                                break
                        else:
                            for k in i[0].propiedades:
                                if(len(jugadorActual.tablero[k]) > 0):
                                    break
                            _, dinprop = DineroPorPropiedades(jugadorActual)
                            _, dindin = DineroPorBilletes(jugadorActual)
                            if(dinprop > dindin):
                                valor += 1/15
                            else:
                                break                                   
                    elif(i[1] == 'mano'):
                        break
                    #AKI viene un elif
                elif(i[0].subtipo == 'robardinero'):
                    if(not i[0].todos):
                        jugadorObjetivo = i[2]
                        _, din = DineroPorBilletes(jugadorObjetivo)
                        tieneProp = TieneProp(jugadorObjetivo)
                        if(i[0].monto > din):
                            if(tieneProp):
                                valor += 1/4 #arreglar
                            else:
                                break
                        else:
                            valor += 1/10
                    else:
                        jugadorActual = i[1]
                        count = 0
                        for j in i[2]:
                            if(j != jugadorActual):
                                _, din = DineroPorBilletes(j)
                                tieneProp = TieneProp(j)
                                if(i[0].monto > din):
                                    if(tieneProp):
                                        count += 1
                                else:
                                    valor += 1/10
                        valor += 1/4 * count
           
            #poner aki las cosas!!!!!!!!!!!!
        return valor
    
    def EvaluarJugadaD(self, jugada, jugadores):
        valor = 0
        jugadorActual = self
        ranking = RankingPropiedades(jugadorActual)
        for i in jugada:
            if(i.tipo == 'accion'):
                if(i.subtipo == 'construccion'):
                    for c in self.tablero:
                        if(c != 'dinero' and c != 'comodines'):
                            if(i.nombre == 'casa'):
                                if(len(jugadorActual.tablero[c]) > 0 and len(jugadorActual.tablero[c]) == jugadorActual.tablero[c][0].cantGrupo):
                                    valor += 1/7
                            elif(i.nombre == 'hotel'):
                                if(len(jugadorActual.tablero[c]) > 0 and len(jugadorActual.tablero[c]) == jugadorActual.tablero[c][0].cantGrupo + 1):
                                    valor += 1/9
                elif(i.subtipo == 'robarprop'):
                    if(i.cuantas != None):
                        for j in jugadores:
                            if(j != jugadorActual):
                                for c in j.tablero:
                                    if(c != 'dinero' and c != 'comodines'):
                                        if(len(j.tablero[c]) > 0):
                                            for k in ranking:
                                                if(c in ranking[k]):
                                                    valor += 1/((len(ranking) - k + 1) * 2)
                    else:
                        for j in jugadores:
                            if(j != jugadorActual):
                                for c in j.tablero:
                                    if(c != 'dinero' and c != 'comodines'):
                                        if(len(j.tablero[c]) > 0 and len(j.tablero[c]) >= j.tablero[c][0].cantGrupo):
                                            valor += 1/1000
                        valor += 1/9
                elif(i.subtipo == 'robardinero'):
                    valor += 1/7
                elif(i.subtipo == 'robarcarta'):
                    valor += 1/10
                elif(i.subtipo == 'renta'):
                    valor += 1/5
                elif(i.subtipo == 'rapida'):
                    if(i.nombre == 'diqno'):
                        valor += 1/11
                    else:
                        valor += 1/5
            else: #DINERO
                valor += 1/4
        return valor
                  
    def EvaluarJugadaR(self, jugada, monto):
        valor = 0
        jugadorActual = self
        ranking = RankingPropiedades(jugadorActual)
        if(jugada[0].tipo == 'accion'):
            if(jugada[0].subtipo == 'rapida'):
                valor += 10     
            if(jugada[0].subtipo == 'robardinero' or jugada[0].subtipo == 'renta'):
                if(len(jugada) >= 3):
                    _, dinero = DineroPorBilletes(self)
                    if(dinero >= monto):
                        for i in jugada[2]: 
                            if(type(i) == list):
                                break
                            if(i.tipo == 'propiedad' or (i.tipo == 'comodin' and i.enUso in coloresEnUso)):
                                break
                            else:
                                valor +=1
                        valor += 2
                    else:
                        a, dinprop = DineroPorPropiedades(self)
                        #_, dinGrupComp = DineroPorGrupoCompleto(self)
                        for i in jugada[2]:
                            if(type(i) == list):
                                dinGrupComp = a[0][a[1].index(i)]
                                if(dinprop - dinGrupComp >= monto):
                                    break
                                else:
                                    valor += 0.01
                            elif(i.tipo == 'propiedad' or (i.tipo == 'comodin' and i.enUso in coloresEnUso)):
                                for k in ranking:
                                    if(i.color in ranking[k]):
                                        valor += 1/((len(ranking) - k + 1) * 2)
                            else:
                                valor += 1
                else:
                    valor += 100
        return valor
    
    def PosiblesJugadas(self, mazo, descarte, jugadores):
        listaJugadas = []
        jugadasPosibles = []
        for i in range(1000): #Poner otro numero!!!!!!!!!!!
            j = JugadaRandom(self, mazo, descarte,jugadores)
            jugada = j.CrearJugada()
            if(jugada not in jugadasPosibles):
                cartasConUso = []
                for i in jugada:
                    cartasConUso.append(j.ComoUsarCarta(i, jugada))
                cartasConUso.append(j.ComodinesAReponer())
                listaJugadas.append([self, cartasConUso])
                jugadasPosibles.append(jugada)
        max = -1000 #poner el min value
        result = {}
        for i in range(len(listaJugadas)):
            if(i == len(listaJugadas) - 1):
                break
            ev = listaJugadas[i][0].EvaluarJugada(listaJugadas[i][1], jugadores, descarte, mazo)
            result[ev] = listaJugadas[i]
            if(ev > max):
                max = ev
        if(len(result) == 0):
            return []
        return result[max][1]  
    
    def SeleccionarJugada(self, mazo, descarte, jugadores):
        jugada = self.PosiblesJugadas(mazo, descarte, jugadores)
        return jugada
    
    def EjecutarJugada(self, jugada, mazo, descarte, jugadores):
        j = JugadaRandom(self, mazo, descarte, jugadores)
        for i in jugada:
            if(i == jugada[len(jugada) - 1]):
                break
            if(i != None):
                jugadasav = jugada
                j.UsarCarta(i[0], i, jugada)
                j.ReponerComodin(jugada[len(jugada) - 1])
                
    def DescartarCartasJ(self, mazo, descarte, jugadores):
        j = JugadaRandom(self, mazo, descarte, jugadores)
        cartasADescartar = []
        for i in range(1000):
            cartasADescartar.append(j.CartasADescartar())
        max = -1000 #poner el min value
        result = {}
        for i in cartasADescartar:
            if(type(i) == list):
                ev = j.jugador.EvaluarJugadaD(i, jugadores)
                result[ev] = i
                if(ev > max):
                    max = ev
        if(len(result) == 0):
            j.DescartarCartas(self)
        else:
            j.DescartarCartas(result[max])             
    
    def Responder(self, jugadorActual, mazo, descarte, carta, monto):
        j = JugadaRandom(self, mazo, descarte)
        respuestas = []
        result = {}
        max = -1000
        for i in range(1000):
            respuestas.append(j.CartasResponder(jugadorActual, carta, monto))
        for i in respuestas:    
            ev = j.jugador.EvaluarJugadaR(i, monto)
            result[ev] = i
            if(ev > max):
                max = ev
        j.ResponderAJugada(result[max])
        

class JugadorInteligente1(Jugador):
    def __init__(self, nombre, esBot):
        super().__init__(nombre, esBot)
        self.tablero = {}
        self.colorCantGrupo = {}
        
        for i in range(len(coloresEnUso)):
            self.tablero[coloresEnUso[i]] = []
            self.colorCantGrupo[coloresEnUso[i]] = cantGrupo[i]
        self.tablero['dinero'] = []
        self.tablero['comodines'] = []

        self.mano = []
        
        
    def EvaluarJugada(jugadorActual, jugada, jugadores, descarte, mazo):
        '''HEURISTICA DE PROPIEDADES'''
        valor = 0
        ranking = RankingPropiedades(jugadorActual)

        for i in jugada:
            if (i == jugada[len(jugada) - 1]):
                break
            if(i[0].tipo == 'propiedad'):
                for k in ranking:
                    if(i[0].color in ranking[k] and k != 0):
                        if(k == 1):
                            valor += 1/k# - CalcularProbabilidad(True, jugadores, jugadorActual, descarte, mazo)
                        else:
                            valor += 1 / k #- CalcularProbabilidad(False, jugadores, jugadorActual, descarte, mazo)
                        ranking[k - 1].append(i[0].color)
                        ranking[k].remove(i[0].color)
                        if(len(ranking[0]) == 3):
                            valor += 1000
                        break
            elif(i[0].tipo == 'comodin'):
                for k in ranking:
                    if(i[1] in ranking[k] and k != 0):
                        if(len(jugadorActual.tablero[i[1]]) > 0 and len(jugadorActual.tablero[i[1]]) < jugadorActual.tablero[i[1]][0].cantGrupo):
                            valor += 1 / k
                            ranking[k - 1].append(i[1])
                            ranking[k].remove(i[1])
                            if(len(ranking[0]) == 3):
                                valor += 1000
                            break
            elif(i[0].tipo == 'dinero'):
                _, dinprop = DineroPorPropiedades(jugadorActual)
                _, dindin = DineroPorBilletes(jugadorActual)
                if(dinprop > dindin):
                    valor += 1/12
            elif(i[0].tipo == 'accion'):
                if(i[0].nombre == 'diqno'):
                    break
                elif(i[0].tipo == 'robarcarta'):
                    valor += 1/2
                elif(i[0].subtipo == 'robarprop'):
                    if(i[1] == 'mano' or i[1] == 'dinero'):
                        break
                    elif(i[0].intercambio):
                        if(len(i[2]) == 0 or (type[i[1]] == list and len(i[1]) == 0)):
                            break
                        count = 0
                        for j in i[1]:
                            for k in ranking:
                                if(j.color == ranking[k] and k == 0):
                                    break
                                if(j.color == ranking[k] and k != 0):
                                    count += 1 - 1/k
                        for j in i[2]:
                            for k in ranking:
                                if(j.color == ranking[k] and k != 0):
                                    count += 1/k
                        valor += count
                    else:
                        if(i[0].cuantas != None):
                            count = 0
                            for j in i[1]:
                                for k in ranking:
                                    if(j.color == ranking[k] and k != 0):
                                        count += 1/k
                            valor += count
                        else: #FACTOR DECISIVO
                            valor += 3                      
                elif(i[0].subtipo == 'construccion'):
                    if(i[0].nombre == 'casa'):
                        if(len(jugadorActual.tablero[i[1]]) > 0 and len(jugadorActual.tablero[i[1]]) == jugadorActual.tablero[i[1]][0].cantGrupo):
                            valor += 1/3
                        else:
                            break
                    elif(i[0].nombre == 'hotel'):
                        if(len(jugadorActual.tablero[i[1]]) > 0 and len(jugadorActual.tablero[i[1]]) == jugadorActual.tablero[i[1]][0].cantGrupo + 1):
                            valor += 1/2
                        else:
                            break
                elif(i[0].subtipo == 'renta'):
                    if(i[1] == 'dinero'):
                        if(len(i[0].propiedades) == 0):
                            for j in jugadorActual.tablero:
                                if(len(jugadorActual.tablero[j]) > 0):
                                    break
                            _, dinprop = DineroPorPropiedades(jugadorActual)
                            _, dindin = DineroPorBilletes(jugadorActual)
                            if(dinprop > dindin):
                                valor += 1/15
                            else:
                                break
                        else:
                            for k in i[0].propiedades:
                                if(len(jugadorActual.tablero[k]) > 0):
                                    break
                            _, dinprop = DineroPorPropiedades(jugadorActual)
                            _, dindin = DineroPorBilletes(jugadorActual)
                            if(dinprop > dindin):
                                valor += 1/15
                            else:
                                break                                   
                    elif(i[1] == 'mano'):
                        break
                    #AKI viene un elif
                elif(i[0].subtipo == 'robardinero'):
                    if(not i[0].todos):
                        jugadorObjetivo = i[2]
                        _, din = DineroPorBilletes(jugadorObjetivo)
                        tieneProp = TieneProp(jugadorObjetivo)
                        if(i[0].monto > din):
                            if(tieneProp):
                                valor += 1/4 #arreglar
                            else:
                                break
                        else:
                            valor += 1/10
                    else:
                        jugadorActual = i[1]
                        count = 0
                        for j in i[2]:
                            if(j != jugadorActual):
                                _, din = DineroPorBilletes(j)
                                tieneProp = TieneProp(j)
                                if(i[0].monto > din):
                                    if(tieneProp):
                                        count += 1
                                else:
                                    valor += 1/10
                        valor += 1/4 * count
           
            #poner aki las cosas!!!!!!!!!!!!
        return valor
    
    def EvaluarJugadaD(self, jugada, jugadores):
        valor = 0
        jugadorActual = self
        ranking = RankingPropiedades(jugadorActual)
        for i in jugada:
            if(i.tipo == 'accion'):
                if(i.subtipo == 'construccion'):
                    for c in self.tablero:
                        if(c != 'dinero' and c != 'comodines'):
                            if(i.nombre == 'casa'):
                                if(len(jugadorActual.tablero[c]) > 0 and len(jugadorActual.tablero[c]) == jugadorActual.tablero[c][0].cantGrupo):
                                    valor += 1/7
                            elif(i.nombre == 'hotel'):
                                if(len(jugadorActual.tablero[c]) > 0 and len(jugadorActual.tablero[c]) == jugadorActual.tablero[c][0].cantGrupo + 1):
                                    valor += 1/9
                elif(i.subtipo == 'robarprop'):
                    if(i.cuantas != None):
                        for j in jugadores:
                            if(j != jugadorActual):
                                for c in j.tablero:
                                    if(c != 'dinero' and c != 'comodines'):
                                        if(len(j.tablero[c]) > 0):
                                            for k in ranking:
                                                if(c in ranking[k]):
                                                    valor += 1/((len(ranking) - k + 1) * 2)
                    else:
                        for j in jugadores:
                            if(j != jugadorActual):
                                for c in j.tablero:
                                    if(c != 'dinero' and c != 'comodines'):
                                        if(len(j.tablero[c]) > 0 and len(j.tablero[c]) >= j.tablero[c][0].cantGrupo):
                                            valor += 1/1000
                        valor += 1/9
                elif(i.subtipo == 'robardinero'):
                    valor += 1/5
                elif(i.subtipo == 'robarcarta'):
                    valor += 1/10
                elif(i.subtipo == 'renta'):
                    valor += 1/7
                elif(i.subtipo == 'rapida'):
                    if(i.nombre == 'diqno'):
                        valor += 1/11
                    else:
                        valor += 1/7
            else: #DINERO
                valor += 1/4
        return valor
                  
    def EvaluarJugadaR(self, jugada, monto):
        valor = 0
        jugadorActual = self
        ranking = RankingPropiedades(jugadorActual)
        if(jugada[0].tipo == 'accion'):
            if(jugada[0].subtipo == 'rapida'):
                valor += 10     
            if(jugada[0].subtipo == 'robardinero' or jugada[0].subtipo == 'renta'):
                if(len(jugada) >= 3):
                    _, dinero = DineroPorBilletes(self)
                    if(dinero >= monto):
                        for i in jugada[2]:
                            if(type(i) == list):
                                break
                            if(i.tipo == 'propiedad' or (i.tipo == 'comodin' and i.enUso in coloresEnUso)):
                                break
                            else:
                                valor +=1
                        valor += 2
                    else:
                        a, dinprop = DineroPorPropiedades(self)
                        #_, dinGrupComp = DineroPorGrupoCompleto(self)
                        for i in jugada[2]:
                            if(type(i) == list):
                                dinGrupComp = a[0][a[1].index(i)]
                                if(dinprop - dinGrupComp >= monto):
                                    break
                                else:
                                    valor += 0.01
                            elif(i.tipo == 'propiedad' or (i.tipo == 'comodin' and i.enUso in coloresEnUso)):
                                for k in ranking:
                                    if(i.color in ranking[k]):
                                        valor += 1/((len(ranking) - k + 1) * 2)
                            else:
                                valor += 1
                else:
                    valor += 100
        return valor
    
    def PosiblesJugadas(self, mazo, descarte, jugadores):
        listaJugadas = []
        jugadasPosibles = []
        for i in range(1000): #Poner otro numero!!!!!!!!!!!
            j = JugadaRandom(self, mazo, descarte,jugadores)
            jugada = j.CrearJugada()
            if(jugada not in jugadasPosibles):
                cartasConUso = []
                for i in jugada:
                    cartasConUso.append(j.ComoUsarCarta(i, jugada))
                cartasConUso.append(j.ComodinesAReponer())
                listaJugadas.append([self, cartasConUso])
                jugadasPosibles.append(jugada)
        max = -1000 #poner el min value
        result = {}
        for i in range(len(listaJugadas)):
            if(i == len(listaJugadas) - 1):
                break
            ev = listaJugadas[i][0].EvaluarJugada(listaJugadas[i][1], jugadores, descarte, mazo)
            result[ev] = listaJugadas[i]
            if(ev > max):
                max = ev
        if(len(result)==0):
            return []
        return result[max][1]  
    
    def SeleccionarJugada(self, mazo, descarte, jugadores):
        jugada = self.PosiblesJugadas(mazo, descarte, jugadores)
        return jugada
    
    def EjecutarJugada(self, jugada, mazo, descarte, jugadores):
        j = JugadaRandom(self, mazo, descarte, jugadores)
        for i in jugada:
            if(i == jugada[len(jugada) - 1]):
                break
            if(i != None):
                jugadasav = jugada
                j.UsarCarta(i[0], i, jugada)
                j.ReponerComodin(jugada[len(jugada) - 1])
                
    def DescartarCartasJ(self, mazo, descarte, jugadores):
        j = JugadaRandom(self, mazo, descarte, jugadores)
        cartasADescartar = []
        for i in range(1000):
            cartasADescartar.append(j.CartasADescartar())
        max = -1000 #poner el min value
        result = {}
        for i in cartasADescartar:
            if(type(i) == list):
                ev = j.jugador.EvaluarJugadaD(i, jugadores)
                result[ev] = i
                if(ev > max):
                    max = ev
        if(len(result) == 0):
            j.DescartarCartas(self)
        else:
            j.DescartarCartas(result[max])             
    
    def Responder(self, jugadorActual, mazo, descarte, carta, monto):
        j = JugadaRandom(self, mazo, descarte)
        respuestas = []
        result = {}
        max = -1000
        for i in range(1000):
            respuestas.append(j.CartasResponder(jugadorActual, carta, monto))
        for i in respuestas:    
            ev = j.jugador.EvaluarJugadaR(i, monto)
            result[ev] = i
            if(ev > max):
                max = ev
        j.ResponderAJugada(result[max])
        
class JugadorInteligente2(Jugador):
    def __init__(self, nombre, esBot):
        super().__init__(nombre, esBot)
        self.tablero = {}
        self.colorCantGrupo = {}
        
        for i in range(len(coloresEnUso)):
            self.tablero[coloresEnUso[i]] = []
            self.colorCantGrupo[coloresEnUso[i]] = cantGrupo[i]
        self.tablero['dinero'] = []
        self.tablero['comodines'] = []

        self.mano = []
        
        
    def EvaluarJugada(jugadorActual, jugada, jugadores, descarte, mazo):
        '''HEURISTICA DE PROPIEDADES'''
        valor = 0
        ranking = RankingPropiedades(jugadorActual)

        for i in jugada:
            if (i == jugada[len(jugada) - 1]):
                break
            if(i[0].tipo == 'propiedad'):
                for k in ranking:
                    if(i[0].color in ranking[k] and k != 0):
                        if(k == 1):
                            valor += 1/k# - CalcularProbabilidad(True, jugadores, jugadorActual, descarte, mazo)
                        else:
                            valor += 1 / k #- CalcularProbabilidad(False, jugadores, jugadorActual, descarte, mazo)
                        ranking[k - 1].append(i[0].color)
                        ranking[k].remove(i[0].color)
                        if(len(ranking[0]) == 3):
                            valor += 1000
                        break
            elif(i[0].tipo == 'comodin'):
                for k in ranking:
                    if(i[1] in ranking[k] and k != 0):
                        if(len(jugadorActual.tablero[i[1]]) > 0 and len(jugadorActual.tablero[i[1]]) < jugadorActual.tablero[i[1]][0].cantGrupo):
                            valor += 1 / k
                            ranking[k - 1].append(i[1])
                            ranking[k].remove(i[1])
                            if(len(ranking[0]) == 3):
                                valor += 1000
                            break
            elif(i[0].tipo == 'dinero'):
                _, dinprop = DineroPorPropiedades(jugadorActual)
                _, dindin = DineroPorBilletes(jugadorActual)
                if(dinprop > dindin):
                    valor += 1/12
            elif(i[0].tipo == 'accion'):
                if(i[0].nombre == 'diqno'):
                    break
                elif(i[0].tipo == 'robarcarta'):
                    valor += 1/2
                elif(i[0].subtipo == 'robarprop'):
                    if(i[1] == 'mano' or i[1] == 'dinero'):
                        break
                    elif(i[0].intercambio):
                        if(len(i[2]) == 0 or (type[i[1]] == list and len(i[1]) == 0)):
                            break
                        count = 0
                        for j in i[1]:
                            for k in ranking:
                                if(j.color == ranking[k] and k == 0):
                                    break
                                if(j.color == ranking[k] and k != 0):
                                    count += 1 - 1/k
                        for j in i[2]:
                            for k in ranking:
                                if(j.color == ranking[k] and k != 0):
                                    count += 1/k
                        valor += count
                    else:
                        if(i[0].cuantas != None):
                            count = 0
                            for j in i[1]:
                                for k in ranking:
                                    if(j.color == ranking[k] and k != 0):
                                        count += 1/k
                            valor += count
                        else: #FACTOR DECISIVO
                            valor += 3                      
                elif(i[0].subtipo == 'construccion'):
                    if(i[0].nombre == 'casa'):
                        if(len(jugadorActual.tablero[i[1]]) > 0 and len(jugadorActual.tablero[i[1]]) == jugadorActual.tablero[i[1]][0].cantGrupo):
                            flag = False
                            for k in jugada:
                                if(k == jugada[len(jugada) -1]):
                                    break
                                if(k[0].tipo == 'accion' and k[0].subtipo == 'renta' and (k[0].propiedades == None or i[1] in k[0].propiedades)):
                                    valor += 1
                                    flag = True
                            if(not flag):
                                valor += 1/3
                        else:
                            valor += 1/10
                    elif(i[0].nombre == 'hotel'):
                        if(len(jugadorActual.tablero[i[1]]) > 0 and len(jugadorActual.tablero[i[1]]) == jugadorActual.tablero[i[1]][0].cantGrupo + 1):
                            flag = False
                            for k in jugada:
                                if(k == jugada[len(jugada) -1]):
                                    break
                                if(k[0].tipo == 'accion' and k[0].subtipo == 'renta' and (k[0].propiedades == None or i[1] in k[0].propiedades)):
                                    valor += 1.2
                                    flag = True
                            if(not flag):
                                valor += 1/2
                        else:
                            valor += 1/10
                elif(i[0].subtipo == 'renta'):
                    if(i[1] == 'dinero'):
                        if(len(i[0].propiedades) == 0):
                            for j in jugadorActual.tablero:
                                if(len(jugadorActual.tablero[j]) > 0):
                                    break
                            _, dinprop = DineroPorPropiedades(jugadorActual)
                            _, dindin = DineroPorBilletes(jugadorActual)
                            if(dinprop > dindin):
                                valor += 1/15
                            else:
                                break
                        else:
                            for k in i[0].propiedades:
                                if(len(jugadorActual.tablero[k]) > 0):
                                    break
                            _, dinprop = DineroPorPropiedades(jugadorActual)
                            _, dindin = DineroPorBilletes(jugadorActual)
                            if(dinprop > dindin):
                                valor += 1/15
                            else:
                                break                                   
                    elif(i[1] == 'mano'):
                        break
                    else:
                        if(type(i[4]) == list):
                            for k in i[4]:
                                if(k != jugadorActual):
                                    #_, dinprop = DineroPorPropiedades(k)
                                    b = TieneProp(k)
                                    _, dindin = DineroPorBilletes(k)
                                    if(i[2] > dindin and b):
                                        valor += 1 + i[2]/10
                                    elif(i[2] > dindin and not b):
                                        valor += 1/5 + i[2]/10
                                    elif(i[2] <= dindin):
                                        valor += 1/3 +i[2]/10
                        else:
                            #_, dinprop = DineroPorPropiedades(i[4])
                            _, dindin = DineroPorBilletes(i[4])
                            b = TieneProp(i[4])
                            if(i[2] > dindin and b):
                                valor += 1 + i[2]/10
                            elif(i[2] > dindin and not b):
                                valor += 1/5 +i[2]/10
                            elif(i[2] <= dindin):
                                valor += 1/3 +i[2]/10
                elif(i[0].subtipo == 'robardinero'):
                    if(not i[0].todos):
                        jugadorObjetivo = i[2]
                        _, din = DineroPorBilletes(jugadorObjetivo)
                        tieneProp = TieneProp(jugadorObjetivo)
                        if(i[0].monto > din):
                            if(tieneProp):
                                valor += 1 #arreglar
                            else:
                                valor += 1/7
                        else:
                            valor += 1/4
                    else:
                        jugadorActual = i[1]
                        #count = 0
                        for j in i[2]:
                            if(j != jugadorActual):
                                _, din = DineroPorBilletes(j)
                                tieneProp = TieneProp(j)
                                if(i[0].monto > din):
                                    if(tieneProp):
                                        valor += 1
                                    else:
                                        valor += 1/7
                                else:
                                    valor += 1/4
                        #valor += 1/4 * count
           
            #poner aki las cosas!!!!!!!!!!!!
        return valor
    
    def EvaluarJugadaD(self, jugada, jugadores):
        valor = 0
        jugadorActual = self
        ranking = RankingPropiedades(jugadorActual)
        for i in jugada:
            if(i.tipo == 'accion'):
                if(i.subtipo == 'construccion'):
                    for c in self.tablero:
                        if(c != 'dinero' and c != 'comodines'):
                            if(i.nombre == 'casa'):
                                if(len(jugadorActual.tablero[c]) > 0 and len(jugadorActual.tablero[c]) == jugadorActual.tablero[c][0].cantGrupo):
                                    valor += 1/7
                            elif(i.nombre == 'hotel'):
                                if(len(jugadorActual.tablero[c]) > 0 and len(jugadorActual.tablero[c]) == jugadorActual.tablero[c][0].cantGrupo + 1):
                                    valor += 1/9
                elif(i.subtipo == 'robarprop'):
                    if(i.cuantas != None):
                        for j in jugadores:
                            if(j != jugadorActual):
                                for c in j.tablero:
                                    if(c != 'dinero' and c != 'comodines'):
                                        if(len(j.tablero[c]) > 0):
                                            for k in ranking:
                                                if(c in ranking[k]):
                                                    valor += 1/((len(ranking) - k + 1) * 2)
                    else:
                        for j in jugadores:
                            if(j != jugadorActual):
                                for c in j.tablero:
                                    if(c != 'dinero' and c != 'comodines'):
                                        if(len(j.tablero[c]) > 0 and len(j.tablero[c]) >= j.tablero[c][0].cantGrupo):
                                            valor += 1/1000
                        valor += 1/9
                elif(i.subtipo == 'robardinero'):
                    valor += 1/5
                elif(i.subtipo == 'robarcarta'):
                    valor += 1/10
                elif(i.subtipo == 'renta'):
                    valor += 1/7
                elif(i.subtipo == 'rapida'):
                    if(i.nombre == 'diqno'):
                        valor += 1/11
                    else:
                        valor += 1/7
            else: #DINERO
                valor += 1/4
        return valor
                  
    def EvaluarJugadaR(self, jugada, monto):
        valor = 0
        jugadorActual = self
        ranking = RankingPropiedades(jugadorActual)
        if(jugada[0].tipo == 'accion'):
            if(jugada[0].subtipo == 'rapida'):
                valor += 10     
            if(jugada[0].subtipo == 'robardinero' or jugada[0].subtipo == 'renta'):
                if(len(jugada) >= 3):
                    _, dinero = DineroPorBilletes(self)
                    if(dinero >= monto):
                        for i in jugada[2]:
                            if(type(i) == list):
                                break
                            if(i.tipo == 'propiedad' or (i.tipo == 'comodin' and i.enUso in coloresEnUso)):
                                break
                            else:
                                valor +=1
                        valor += 2
                    else:
                        a, dinprop = DineroPorPropiedades(self)
                        #_, dinGrupComp = DineroPorGrupoCompleto(self)
                        for i in jugada[2]:
                            if(type(i) == list):
                                dinGrupComp = a[0][a[1].index(i)]
                                if(dinprop - dinGrupComp >= monto):
                                    break
                                else:
                                    valor += 0.01
                            elif(i.tipo == 'propiedad' or (i.tipo == 'comodin' and i.enUso in coloresEnUso)):
                                for k in ranking:
                                    if(i.color in ranking[k]):
                                        valor += 1/((len(ranking) - k + 1) * 2)
                            else:
                                valor += 1
                else:
                    valor += 100
        return valor
    
    def PosiblesJugadas(self, mazo, descarte, jugadores):
        listaJugadas = []
        jugadasPosibles = []
        for i in range(1000): #Poner otro numero!!!!!!!!!!!
            j = JugadaRandom(self, mazo, descarte,jugadores)
            jugada = j.CrearJugada()
            if(jugada not in jugadasPosibles):
                cartasConUso = []
                for i in jugada:
                    cartasConUso.append(j.ComoUsarCarta(i, jugada))
                cartasConUso.append(j.ComodinesAReponer())
                listaJugadas.append([self, cartasConUso])
                jugadasPosibles.append(jugada)
        max = -1000 #poner el min value
        result = {}
        for i in range(len(listaJugadas)):
            if(i == len(listaJugadas) - 1):
                break
            ev = listaJugadas[i][0].EvaluarJugada(listaJugadas[i][1], jugadores, descarte, mazo)
            result[ev] = listaJugadas[i]
            if(ev > max):
                max = ev
        if(len(result)==0):
            return []
        return result[max][1]  
    
    def SeleccionarJugada(self, mazo, descarte, jugadores):
        jugada = self.PosiblesJugadas(mazo, descarte, jugadores)
        return jugada
    
    def EjecutarJugada(self, jugada, mazo, descarte, jugadores):
        j = JugadaRandom(self, mazo, descarte, jugadores)
        for i in jugada:
            if(i == jugada[len(jugada) - 1]):
                break
            if(i != None):
                jugadasav = jugada
                j.UsarCarta(i[0], i, jugada)
                j.ReponerComodin(jugada[len(jugada) - 1])
                
    def DescartarCartasJ(self, mazo, descarte, jugadores):
        j = JugadaRandom(self, mazo, descarte, jugadores)
        cartasADescartar = []
        for i in range(1000):
            cartasADescartar.append(j.CartasADescartar())
        max = -1000 #poner el min value
        result = {}
        for i in cartasADescartar:
            if(type(i) == list):
                ev = j.jugador.EvaluarJugadaD(i, jugadores)
                result[ev] = i
                if(ev > max):
                    max = ev
        if(len(result) == 0):
            j.DescartarCartas(self)
        else:
            j.DescartarCartas(result[max])             
    
    def Responder(self, jugadorActual, mazo, descarte, carta, monto):
        j = JugadaRandom(self, mazo, descarte)
        respuestas = []
        result = {}
        max = -1000
        for i in range(1000):
            respuestas.append(j.CartasResponder(jugadorActual, carta, monto))
        for i in respuestas:    
            ev = j.jugador.EvaluarJugadaR(i, monto)
            result[ev] = i
            if(ev > max):
                max = ev
        j.ResponderAJugada(result[max])