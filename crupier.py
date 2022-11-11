import random as rd

class Crupier:    
 
    def FinDeJuegoMD(jugadorActual): #no se si esto pinche
        count = 0
        tableroJugadorActual = jugadorActual.tablero
        for i in tableroJugadorActual:
            if(i == 'dinero'):
                break
            if(len(tableroJugadorActual[i]) >= 1 and len(tableroJugadorActual[i]) >= tableroJugadorActual[i][0].cantGrupo):
                count += 1
        fin = count >= 3
        return fin, jugadorActual.nombre
    
    def BarajarMazo(mazo):
        rd.shuffle(mazo)
    
    def RepartirCartas(aTodos : bool, jugadores, mazo, cantCartas, descarte,indice = None): 
        if(len(mazo) + len(descarte) < cantCartas):
            raise Exception('Se acabaron todas las cartas del juego')
        if(len(mazo) <= cantCartas):
            mazo.extend(descarte)
            descarte.clear()
            Crupier.BarajarMazo(mazo)
        if(aTodos):
            for j in jugadores:
                for i in range(cantCartas):
                    h = mazo.pop(0)
                    if(h in j.mano):
                        a = 5
                    #j.mano.append(mazo.pop(0)) OJOOO
                    j.mano.append(h)
        else:
            for i in range(cantCartas):
                h = mazo.pop(0)
                if(h in jugadores.mano):
                    a = 5
                #jugadores.mano.append(mazo.pop(0)) OJOOO
                jugadores.mano.append(h)
        
    def VerificarMano(jugadorActual, mazo, descarte):
        cantCartasEnMano = jugadorActual.mano
        if(len(cantCartasEnMano) > 7):
            jugadorActual.DescartarCartasJ(mazo, descarte)
            