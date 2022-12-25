from gramatica import Convertir
from cartasMD import *

#card = 'Faster con valor 5 M el turno mio'.split()# Rapida
#card = 'quiero crear carta Robaraaa con valor 5 M para poder robar del mazo 3 cartas'.split() #Robar Carta
#card = 'necesito crear carta Facho para robar propiedad con valor 10 M de intercambio de 3 cartas'.split() #Robar Propiedad
#card = 'necesito crear carta Facho con valor 10 M de intercambio de 3 cartas'.split() #Robar Propiedad
#card = 'Fachodinero para robar 10 M a 2 jugadores con valor 6 M'.split() #Robar dinero
#card = 'crear carta RRentass con valor 2 M con colores cian rojo contra 1 jugador'.split() #Renta ver estooo la pila de #Color#
#card = 'Casosona con valor 2 M la cual es una casa y me tienen q dar 3 M mas'.split()
#card = 'crear carta de 10 M'.split()
#card = 'Comdindin cian magenta con valor 3 M'.split() #Comodin
#card = 'Comdindin maestro con valor 3 M'.split() #Comodin
#card = 'crear carta Propi de color cian para un grupo de tamaño 3 donde las rentas son 2, 3, 5 con valor 2 M'.split()
#card = 'quiero crear una carta que se llame PEPR que sea propiedad de color verde de cuyo grupo es de tamaño 3 cuya renta tenga los valores 2, 3, 5 el valor es de 10 M'.split()
card = 'crear carta CHUCHA de color cian grupo de 3 y la renta sea 2, 4, 5 con un valor de 100 M'.split() #Propiedad
#card = 'Rentaaaaa con un valor de 2 M y me tengan que pagar por los colores azul purpura todos'.split() #Renta
#card = 'quiero crear carta que se llame Rentaaaaa contra todos que me tengan que pagar por los colores azul purpura y que valga 3 M'.split() #Renta

def Crear(carta):
    if(carta['tipo'] == 'Propiedad'):
        carta['RentaGrupo'] = [int(i) for i in carta['RentaGrupo']]
        cartaCreada = Propiedades(carta['Nombre'], 'propiedad', carta['ColorCo'][0], int(carta['CantGrupo'][0]), carta['RentaGrupo'], int(carta['ValorC'][0]))
        a = 5

def CrearCarta(card):
    carta = Convertir(card)
    cartaCreada = Crear(carta)
    
CrearCarta(card)
    