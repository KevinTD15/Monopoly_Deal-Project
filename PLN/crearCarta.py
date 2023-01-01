from PLN.gramaticaCartas import *
from Mazo.cartasMD import *
from Mazo.mazoCartas import *

#card = 'Faster con valor 5 M el turno mio'.split()# Rapida
#card = 'quiero crear carta Robaraaa con valor 5 M para poder robar del mazo 3 cartas'.split() #Robar Carta
#card = 'necesito crear carta Facho para robar propiedad con valor 10 M de intercambio de 3 cartas'.split() #Robar Propiedad
#card = 'necesito crear carta Facho con valor 10 M para robar de 3 cartas'.split() #Robar Propiedad
#card = 'Fachodinero para robar 10 M a 1 jugador con valor 6 M'.split() #Robar dinero
#card = 'crear carta RRentass con valor 2 M con colores cian rojo contra 1 jugador'.split() #Renta ver estooo la pila de #Color#
#card = 'Casosona con valor 2 M la cual es una casa y me tienen q dar 3 M mas'.split()
#card = 'crear carta de 10 M'.split()
#card = 'Comdindin cian magenta con valor 3 M'.split() #Comodin
#card = 'Comdindin maestro con valor 3 M'.split() #Comodin
#card = 'crear carta Propi de color cian para un grupo de tamaño 3 donde las rentas son 2, 3, 5 con valor 2 M'.split()
#card = 'quiero crear una carta que se llame PEPR que sea propiedad de color verde de cuyo grupo es de tamaño 3 cuya renta tenga los valores 2, 3, 5 el valor es de 10 M'.split()
#card = 'crear carta CHUCHA de color cian grupo de 3 y la renta sea 2, 4, 5 con un valor de 100 M'.split() #Propiedad
#card = 'Rentaaaaa con un valor de 2 M y me tengan que pagar por los colores azul purpura todos'.split() #Renta
#card = 'quiero crear carta que se llame Rentaaaaa contra todos que me tengan que pagar por los colores azul purpura y que valga 3 M'.split() #Renta

def Crear(carta):
    if(carta['tipo'] == 'Propiedad'):
        carta['RentaGrupo'] = [int(i) for i in carta['RentaGrupo']]
        return Propiedades(carta['Nombre'], 'propiedad', carta['ColorCo'][0], int(carta['CantGrupo'][0]), carta['RentaGrupo'], int(carta['ValorC'][0]))
    elif(carta['tipo'] == 'Dinero'):
        return Dinero(carta['NombreD'][0], 'dinero')
    elif(carta['tipo'] == 'Comodin'):
        return Comodin(carta['Nombre'], 'comodin', carta['ColorCo'], int(carta['ValorC'][0]))
    elif(carta['tipo'] == 'Accion'):
        if(carta['subtipo'] == 'Renta'):
            if(carta['Todos'] != 'todos'):
                return AccionRenta(carta['Nombre'], 'accion', 'renta', int(carta['ValorC'][0]), carta['ColorCo'], False)
            return AccionRenta(carta['Nombre'], 'accion', 'renta', int(carta['ValorC'][0]), carta['ColorCo'], True)
        elif(carta['subtipo'] == 'Construccion'):
            return AccionConstruccion(carta['Nombre'], 'accion', 'construccion', int(carta['ValorC'][0]), carta['TipoConstruccion'], int(carta['MontoC'][0]))
        elif(carta['subtipo'] == 'RobarCarta'):
            return AccionRobarCarta(carta['Nombre'], 'accion', 'robarcarta', int(carta['ValorC'][0]), int(carta['CartasATomar'][0]))
        elif(carta['subtipo'] == 'Rapida'):
            return AccionRapida(carta['Nombre'], 'accion', 'rapida', int(carta['ValorC'][0]), carta['Turno'])
        elif(carta['subtipo'] == 'RobarPropiedad'):
            if('Intercambio' in carta):
                return AccionRobarPropiedad(carta['Nombre'], 'accion', 'robarprop', int(carta['ValorC'][0]), True, int(carta['CartasATomar'][0]))
            return AccionRobarPropiedad(carta['Nombre'], 'accion', 'robarprop', int(carta['ValorC'][0]), False, int(carta['CartasATomar'][0]))
        elif(carta['subtipo'] == 'RobarDinero'):
            if(carta['Todos'] != 'todos'):
                return AccionRobarDinero(carta['Nombre'], 'accion', 'robardinero', int(carta['ValorC'][0]), False, int(carta['MontoD'][0]))
            return AccionRobarDinero(carta['Nombre'], 'accion', 'robardinero', int(carta['ValorC'][0]), True, int(carta['MontoD'][0]))

def EsCartaValida(carta):
    if(carta is None):
        return False, 'carta inválida o faltan parámetros'
    if(carta['tipo'] == 'Propiedad'):
        if(int(carta['CantGrupo'][0]) != len(carta['RentaGrupo'])):
            nombr = carta['Nombre']
            return False, f'En la carta {nombr} CantGrupo es diferente de la cantidad de elementos en RentaGrupo'
        if('ColorCo' not in carta):
            return False, 'color invalido'
        if(carta['ColorCo'][0] in coloresEnUso):
            a =carta['ColorCo'][0]
            return False, f'El grupo de color {a} ya esta completo'
        count = 0
        for i in Mazo.cartas:
            if(i.tipo == 'propiedad' and i.color == carta['ColorCo'][0]):
                count += 1
        if(count == int(carta['CantGrupo'][0])):
            coloresEnUso.append(carta['ColorCo'][0])
            cantGrupo.append(int(carta['CantGrupo'][0]))
    if(carta['tipo'] == 'Comodin'):
       for i in carta['ColorCo']:
           if(i not in coloresEnUso):
               return False, f'el color {i} no esta en uso'
    elif(carta['tipo'] == 'Accion'):
        if(carta['subtipo'] == 'Renta'):
            for i in carta['ColorCo']:
                if(i not in coloresEnUso):
                    return False, f'el color {i} no esta en uso'
    return True, 'ok'
                

def CrearCarta(card):
    carta = Convertir(card.split())
    flag, sms = EsCartaValida(carta)
    if(flag):
        cartaCreada = Crear(carta)
        Mazo.cartas.append(cartaCreada)
        return sms
    else:
        return sms
    
#CrearCarta(card)
    