import random as rd

class Crupier:    
 
    def FinDeJuegoMD(jugadorActual): #no se si esto pinche
        count = 0
        tableroJugadorActual = jugadorActual.tablero
        for i in tableroJugadorActual:
            if(i == 'dinero' or i == 'comodines'):
                break
            if(len(tableroJugadorActual[i]) >= 1 and len(tableroJugadorActual[i]) >= jugadorActual.colorCantGrupo[i]):
                count += 1
        fin = count >= 3
        return fin, jugadorActual.nombre
    
    def BarajarMazo(mazo):
        rd.shuffle(mazo)
    
    def RepartirCartas(aTodos : bool, jugadores, mazo, cantCartas, descarte,indice = None): 
        if(len(mazo) + len(descarte) < cantCartas):
            return True
        if(len(mazo) <= cantCartas):
            mazo.extend(descarte)
            descarte.clear()
            Crupier.BarajarMazo(mazo)
        if(aTodos):
            for j in jugadores:
                for i in range(cantCartas):
                    h = mazo.pop(0)
                    j.mano.append(h)
        else:
            for i in range(cantCartas):
                h = mazo.pop(0)
                jugadores.mano.append(h)
        
    def VerificarMano(jugadorActual, mazo, descarte, jugadores):
        cantCartasEnMano = jugadorActual.mano
        if(len(cantCartasEnMano) > 7):
            jugadorActual.DescartarCartasJ(mazo, descarte, jugadores)
            