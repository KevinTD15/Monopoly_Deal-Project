from cartasMD import *

class Mazo(Cartas):
    ventnor = Propiedades('ventnor', 'propiedad', ['amarillo'], 3, [2, 4, 6], 3)
    comodin = Comodin('comodin1', 'comodin', [])
    vermont = Propiedades('vermont', 'propiedad', ['azulClaro'], 3, [1,2,3], 1)
    tenese = Propiedades('tenese', 'propiedad', ['anaranjado'], 3, [1,3,5], 2)
    casa = AccionConstruccion('casa1', 'accion', 'construccion', 3, 'casa', 3)
    renta = AccionRenta('renta1', 'accion', 'renta', 4,['verde', 'azul'], True)
    robar = AccionRobarCarta('go', 'accion', 'robarcarta', 3, 2)
    diqno = AccionRapida('diqno', 'accion', 'rapida', 5, -1)
    factordecisivo = AccionRobarPropiedad('fd', 'accion', 'robarprop',  5, False)
    dinero = Dinero('5', 'dinero')
    dinero1 = Dinero('4', 'dinero')
    comodin = Comodin('comodin2', 'comodin', ['amarillo, morado'], 2)
    reading = Propiedades('reading', 'propiedad', ['negro'], 4, [1,2,3,4], 2)
    renta1 = AccionRenta('renta2', 'accion', 'renta', 3, [], False)

    cartas : Cartas = [tenese, casa, renta, robar, diqno, factordecisivo, ventnor, comodin, vermont,
                       dinero1, comodin, reading, renta1]

for i in Mazo.cartas:
    print (i)