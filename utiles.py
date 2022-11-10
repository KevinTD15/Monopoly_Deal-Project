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

def CantidadDeConstrucciones(listaDeUnColor):
    cont = 0
    for i in listaDeUnColor:
        if(i.tipo == 'accion'):
            cont += 1
    return cont
        
