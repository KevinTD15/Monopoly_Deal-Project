from math import factorial

def TieneProp(jugador):
    for i in jugador.tablero:
        if(len(jugador.tablero[i]) > 0):
            return True
    return False

def CalcularMonto(jugador, color):
    if(color == 'comodines'):
        acum = 0
        for i in jugador.tablero[color]:
            acum += i.valor
        return acum
    elif(len(jugador.tablero[color]) <= jugador.tablero[color][0].cantGrupo):
        return jugador.tablero[color][0].renta[len(jugador.tablero[color]) - 1]
    else:
        i = 0
        cantPorGrupoColorI = jugador.tablero[color][0].cantGrupo
        acum = jugador.tablero[color][0].renta[len(jugador.tablero[color][0].renta) - 1]
        while i + cantPorGrupoColorI < len(jugador.tablero[color]):
            if jugador.tablero[color][len(jugador.tablero[color]) - 1 - i].tipo=='propiedad':
                acum += jugador.tablero[color][len(jugador.tablero[color]) - 1 - i].valor
            else:
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

def CantidadDeConstrucciones(listaDeUnColor):
    cont = 0
    for i in listaDeUnColor:
        if(i.tipo == 'accion'):
            cont += 1
    return cont

def RankingPropiedades(jugadorActual):
    rank = {}
    valUsados = []
    for i in jugadorActual.colorCantGrupo:
        if(len(jugadorActual.tablero[i]) < jugadorActual.colorCantGrupo[i]):
            val = jugadorActual.colorCantGrupo[i] - len(jugadorActual.tablero[i])
            if(val < 0):
                val = 0
            if(val in valUsados):
                rank[val].append(i)
            else:
                rank[val] = []
                rank[val].append(i)
                valUsados.append(val)
    for i in range(5):
        if(i not in rank):
            rank[i] = []
    return rank

def CalcularProbabilidad(flag, jugadores, jugadorActual, descarte, mazo):
    prob = 0
    total = 0
    cartasDesconocidas = 0
    cartasDesconocidasEnMano = 0
    cond = None
    if(flag): #si es carta que roba grupo completo
        for i in descarte:
            if(i.tipo == 'accion' and i.subtipo == 'robarprop' and i.cuantas == None):
                    prob += 1
                    total += 1
        for i in jugadores:
            if(i == jugadorActual):
                for h in jugadorActual.mano:
                    if(h.tipo == 'accion' and h.subtipo == 'robarprop' and h.cuantas == None):
                        prob += 1
                        total += 1
            else:
                cartasDesconocidasEnMano += len(i.mano)
                cartasDesconocidas += len(i.mano)
                for h in i.mano:
                    if(h.tipo == 'accion' and h.subtipo == 'robarprop' and h.cuantas == None):
                        total += 1
            for j in i.tablero['dinero']:
                    if(j.tipo == 'accion' and j.subtipo == 'robarprop' and j.cuantas == None):
                        prob += 1
                        total += 1
        cartasDesconocidas += len(mazo)
        for z in mazo:
            if(z.tipo == 'accion' and z.subtipo == 'robarprop' and z.cuantas == None):
                total += 1
    else:
        for i in descarte:
            if(i.tipo == 'accion' and i.subtipo == 'robarprop' and i.cuantas != None):
                prob += 1
                total += 1
        for i in jugadores:
            if(i == jugadorActual):
                for h in jugadorActual.mano:
                    if(h.tipo == 'accion' and h.subtipo == 'robarprop' and h.cuantas != None):
                        prob += 1
                        total += 1
            else:
                cartasDesconocidasEnMano += len(i.mano)
                cartasDesconocidas += len(i.mano)
                for h in i.mano:
                    if(h.tipo == 'accion' and h.subtipo == 'robarprop' and h.cuantas != None):
                        total += 1
            for j in i.tablero['dinero']:
                if(j.tipo == 'accion' and j.subtipo == 'robarprop' and j.cuantas != None):
                    prob += 1
                    total += 1
        cartasDesconocidas += len(mazo)
        for z in mazo:
            if(z.tipo == 'accion' and z.subtipo == 'robarprop' and z.cuantas != None):
                total += 1
                
    x = cartasDesconocidas - (total - prob) - cartasDesconocidasEnMano
    if(x <= 0):
        return 0
    numer = (factorial(cartasDesconocidas - (total - prob)) / (factorial(cartasDesconocidasEnMano) * factorial(x)))
    den = factorial(cartasDesconocidas) / (factorial(cartasDesconocidasEnMano) * factorial(cartasDesconocidas - cartasDesconocidasEnMano)) #combinatoria
    a= 1 - (numer / den)
    return a

def CalcularProbabilidadDin (jugadores, jugadorActual, descarte, mazo):
    prob = 0
    total = 0
    cartasDesconocidas = 0
    cartasDesconocidasEnMano = 0
    for i in descarte:
        if(i.tipo == 'accion' and (i.subtipo == 'robardinero' or i.subtipo == 'renta')):
            prob += 1
            total += 1
    for i in jugadores:
        if(i == jugadorActual):
            for h in jugadorActual.mano:
                if(h.tipo == 'accion' and (h.subtipo == 'robardinero' or h.subtipo == 'renta')):
                    prob += 1
                    total += 1
        else:
            cartasDesconocidasEnMano += len(i.mano)
            cartasDesconocidas += len(i.mano)
            for h in i.mano:
                if(h.tipo == 'accion' and (h.subtipo == 'robardinero' or h.subtipo == 'renta')):
                    total += 1
        for j in i.tablero['dinero']:
            if(j.tipo == 'accion' and (j.subtipo == 'robardinero' or j.subtipo == 'renta')):
                prob += 1
                total += 1
    cartasDesconocidas += len(mazo)
    for z in mazo:
        if(z.tipo == 'accion' and (z.subtipo == 'robardinero' or z.subtipo == 'renta')):
            total += 1
                
    x = cartasDesconocidas - (total - prob) - cartasDesconocidasEnMano
    if(x <= 0):
        return 0
    numer = (factorial(cartasDesconocidas - (total - prob)) / (factorial(cartasDesconocidasEnMano) * factorial(x)))
    den = factorial(cartasDesconocidas) / (factorial(cartasDesconocidasEnMano) * factorial(cartasDesconocidas - cartasDesconocidasEnMano)) #combinatoria
    a= 1 - (numer / den)
    return a