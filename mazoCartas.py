from cartasMD import *

class Mazo(Cartas):
    tenese = Propiedades('tenese', 'propiedad', ['anaranjado'], 3, [1,3,5], 2)
    casa = AccionConstruccion('casa1', 'accion', 'construccion', 3, 'casa', 3)
    renta = AccionRenta('renta1', 'accion', 'renta', 4,['verde', 'azul'], True)
    robar = AccionRobarCarta('go', 'accion', 'robarcarta', 3, 2)
    diqno = AccionRapida('diqno', 'accion', 'rapida', 5, True)
    factordecisivo = AccionRobarPropiedad('fd', 'accion', 'robarprop',  5, False)

    cartas : Cartas = [tenese, casa, renta, robar, diqno, factordecisivo]
    
print(Mazo.cartas)