import random as rd

class Crupier:    
 
    def FinDeJuegoMD(jugadorActual): #no se si esto pinche
        count = 0
        tableroJugadorActual = jugadorActual.tablero
        for i in tableroJugadorActual:
            if(i == 'dinero'):
                break
            if(len(tableroJugadorActual[i]) >= 1 and len(tableroJugadorActual[i]) == tableroJugadorActual[i][0].cantGrupo):
                count += 1
        fin = count >= 3
        return fin, jugadorActual.nombre
    
    def BarajarMazo(mazo):
        rd.shuffle(mazo)
    
    def RepartirCartas(aTodos : bool, jugadores, mazo, cantCartas, descarte,indice = None): #poner que roba 5 en vez de 8
        if(len(mazo) + len(descarte) < cantCartas):
            raise Exception('Se acabaron todas las cartas del juego')
        if(len(mazo) <= cantCartas):
            mazo.extend(descarte)
            descarte.clear()
            Crupier.BarajarMazo(mazo)
        if(aTodos):
            for j in jugadores:
                for i in range(cantCartas):
                    j.mano.append(mazo.pop(0))
        else:
            for i in range(cantCartas):
                jugadores[indice].mano.append(mazo.pop(0))
        
         
    def VerificarMano(jugadorActual, mazo, descarte):
        cantCartasEnMano = jugadorActual.mano
        if(len(cantCartasEnMano) > 7):
            jugadorActual.DescartarCartas(mazo, descarte)