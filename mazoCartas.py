from cartasMD import *

class Mazo(Cartas):
    #PROPIEDADES
    ventnor        = Propiedades('ventnor', 'propiedad', 'amarillo', 3, [2, 4, 6], 3)
    atlantico      = Propiedades('atlantico', 'propiedad', 'amarillo', 3, [2, 4, 6], 3)
    jardinesM      = Propiedades('jardinesMarvin', 'propiedad', 'amarillo', 3, [2, 4, 6], 3)
    vermont        = Propiedades('vermont', 'propiedad', 'azulClaro', 3, [1,2,3], 1)
    oriental       = Propiedades('oriental', 'propiedad', 'azulClaro', 3, [1,2,3], 1)
    connecticut    = Propiedades('connecticut', 'propiedad', 'azulClaro', 3, [1,2,3], 1)
    tenese         = Propiedades('tenese', 'propiedad', 'anaranjado', 3, [1,3,5], 2)
    ny             = Propiedades('nuevaYork', 'propiedad', 'anaranjado', 3, [1,3,5], 2)
    stjames        = Propiedades('stJames', 'propiedad', 'anaranjado', 3, [1,3,5], 2)
    reading        = Propiedades('reading', 'propiedad', 'negro', 4, [1,2,3,4], 2)
    vr             = Propiedades('viaRapida', 'propiedad', 'negro', 4, [1,2,3,4], 2)
    pennsylvania   = Propiedades('pennsylvania', 'propiedad', 'negro', 4, [1,2,3,4], 2)
    bio            = Propiedades('b&o', 'propiedad', 'negro', 4, [1,2,3,4], 2)
    muelle         = Propiedades('elMuelle', 'propiedad', 'azul', 2, [3,8], 4) 
    park           = Propiedades('plazaPark', 'propiedad', 'azul', 2, [3,8], 4)
    mediterraneo   = Propiedades('mediterraneo', 'propiedad', 'carmelita', 2, [1,2], 1)
    baltica        = Propiedades('baltica', 'propiedad', 'carmelita', 2, [1,2], 1)
    agua           = Propiedades('agua', 'propiedad', 'blanco', 2, [1,2], 2)
    electricidad   = Propiedades('electricidad', 'propiedad', 'blanco', 2, [1,2], 2)
    virginia       = Propiedades('virginia', 'propiedad', 'morado', 3, [1,2,4], 2)
    sanCarlos      = Propiedades('sanCarlos', 'propiedad', 'morado', 3, [1,2,4], 2)
    estados        = Propiedades('estados', 'propiedad', 'morado', 3, [1,2,4], 2)
    pennsylvaniaV  = Propiedades('pennsylvania', 'propiedad', 'verde', 3, [2,4,7], 4)
    pacifico       = Propiedades('pacifico', 'propiedad', 'verde', 3, [2,4,7], 4)
    carolinaNorte  = Propiedades('carolinaNorte', 'propiedad', 'verde', 3, [2,4,7], 4)
    ilinois        = Propiedades('ilinois', 'propiedad', 'rojo', 3, [2,3,6], 3)
    indiana        = Propiedades('indiana', 'propiedad', 'rojo', 3, [2,3,6], 3)
    kentucky       = Propiedades('kentucky', 'propiedad', 'rojo', 3, [2,3,6], 3) 
    
    #ACCION   
    casa           = AccionConstruccion('casa1', 'accion', 'construccion', 3, 'casa', 3) #3
    hotel          = AccionConstruccion ('hotel1', 'accion', 'construccion', 4, 'hotel', 4) #2
    renta          = AccionRenta('renta1', 'accion', 'renta', 1,['verde', 'azul'], True) #2
    renta1         = AccionRenta('renta2', 'accion', 'renta', 1,['verde', 'negro'], True) #2
    renta2         = AccionRenta('renta3', 'accion', 'renta', 1,['anaranjado', 'morado'], True) #2
    renta3         = AccionRenta('renta4', 'accion', 'renta', 1,['amarillo', 'rojo'], True) #2
    renta4         = AccionRenta('renta5', 'accion', 'renta', 1,['azulClaro', 'carmelita'], True) #2
    rentaT         = AccionRenta('rentaT', 'accion', 'renta', 3, [], False) #3
    robar          = AccionRobarCarta('go', 'accion', 'robarcarta', 1, 2) #10
    diqno          = AccionRapida('diqno', 'accion', 'rapida', 4, -1) #3
    doblaR         = AccionRapida ('doblaRenta', 'accion', 'rapida', 1, 1) #2
    factordecisivo = AccionRobarPropiedad('factorDesicivo', 'accion', 'robarprop',  5, False) #2
    tratoA         = AccionRobarPropiedad('tratoAstuto', 'accion', 'robarprop', 3, False, 1) #3
    tratoF         = AccionRobarPropiedad('tratoForzado', 'accion', 'robarprop', 3, True, 1) #3
    cumpleano      = AccionRobarDinero('cumpleano', 'accion', 'robardinero', 2, True, 2) #3
    deuda          = AccionRobarDinero('cobradeuda', 'accion', 'robardinero', 3, False, 5) #3
    
    #DINERO
    dinero5        = Dinero('5', 'dinero') #2
    dinero4        = Dinero('4', 'dinero') #3
    dinero3        = Dinero('3', 'dinero') #3
    dinero2        = Dinero ('2', 'dinero') #5
    dinero1        = Dinero ('1', 'dinero') #6
    dinero10       = Dinero ('10', 'dinero') #1
    
    #COMODIN
    comodinM       = Comodin('comodinM', 'comodin', []) #2
    comodin        = Comodin('comodin2', 'comodin', ['anaranjado', 'morado'], 2) #2
    comodin2       = Comodin('comodin3', 'comodin', ['negro', 'verde'], 4)
    comodin3       = Comodin('comodin4', 'comodin', ['blanco', 'negro'], 2)
    comodin4       = Comodin('comodin5', 'comodin', ['azulClaro', 'negro'], 4)
    comodin5       = Comodin('comodin6', 'comodin', ['amarillo', 'rojo'], 3) #2
    comodin6       = Comodin('comodin7', 'comodin', ['azul', 'verde'], 4 )
    comodin7       = Comodin('comodin8', 'comodin', ['azulClaro', 'carmelita'], 1)
    


    cartas : Cartas = [ventnor, atlantico, jardinesM ,vermont ,oriental, connecticut  ,tenese,
                    ny, stjames, reading, vr, pennsylvania ,bio,muelle, park, mediterraneo ,
                    baltica, agua, electricidad , virginia, sanCarlos, estados, pennsylvaniaV,
                    pacifico, carolinaNorte, ilinois, indiana, kentucky, casa, hotel, renta, renta1,
                    renta2, renta3, renta4, rentaT, robar, diqno, doblaR,factordecisivo, tratoA, 
                    tratoF, dinero5, dinero4, dinero3, dinero2, dinero1, dinero10, comodinM, comodin, 
                    comodin2, comodin3, comodin4, comodin5, comodin6, comodin7, cumpleano, deuda,]

for i in Mazo.cartas:
    print (i)