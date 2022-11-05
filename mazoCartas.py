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
    #casa
    casa            = AccionConstruccion('casa', 'accion', 'construccion', 3, 'casa', 3)
    casa2           = AccionConstruccion('casa', 'accion', 'construccion', 3, 'casa', 3)
    casa3           = AccionConstruccion('casa', 'accion', 'construccion', 3, 'casa', 3)
    #hotel
    hotel          = AccionConstruccion ('hotel', 'accion', 'construccion', 4, 'hotel', 4)
    hotel2         = AccionConstruccion ('hotel', 'accion', 'construccion', 4, 'hotel', 4)
    #renta
    renta0         = AccionRenta('rentaVA', 'accion', 'renta', 1,['verde', 'azul'], True)
    renta00        = AccionRenta('rentaVA', 'accion', 'renta', 1,['verde', 'azul'], True)
    renta1         = AccionRenta('rentaVN', 'accion', 'renta', 1,['verde', 'negro'], True)
    renta11         = AccionRenta('rentaVN', 'accion', 'renta', 1,['verde', 'negro'], True)
    renta2         = AccionRenta('rentaAM', 'accion', 'renta', 1,['anaranjado', 'morado'], True)
    renta22         = AccionRenta('rentaAM', 'accion', 'renta', 1,['anaranjado', 'morado'], True)
    renta3         = AccionRenta('rentaAR', 'accion', 'renta', 1,['amarillo', 'rojo'], True)
    renta33         = AccionRenta('rentaAR', 'accion', 'renta', 1,['amarillo', 'rojo'], True)
    renta4         = AccionRenta('rentaAcC', 'accion', 'renta', 1,['azulClaro', 'carmelita'], True)
    renta44         = AccionRenta('rentaAcC', 'accion', 'renta', 1,['azulClaro', 'carmelita'], True)
    rentaT1         = AccionRenta('rentaT', 'accion', 'renta', 3, [], False)
    rentaT2         = AccionRenta('rentaT', 'accion', 'renta', 3, [], False)
    rentaT3         = AccionRenta('rentaT', 'accion', 'renta', 3, [], False)
    #robarCarta
    robar1          = AccionRobarCarta('go', 'accion', 'robarcarta', 1, 2)
    robar2          = AccionRobarCarta('go', 'accion', 'robarcarta', 1, 2)
    robar3          = AccionRobarCarta('go', 'accion', 'robarcarta', 1, 2)
    robar4          = AccionRobarCarta('go', 'accion', 'robarcarta', 1, 2)
    robar5          = AccionRobarCarta('go', 'accion', 'robarcarta', 1, 2)
    robar6          = AccionRobarCarta('go', 'accion', 'robarcarta', 1, 2)
    robar7          = AccionRobarCarta('go', 'accion', 'robarcarta', 1, 2)
    robar8          = AccionRobarCarta('go', 'accion', 'robarcarta', 1, 2)
    robar9          = AccionRobarCarta('go', 'accion', 'robarcarta', 1, 2)
    robar0          = AccionRobarCarta('go', 'accion', 'robarcarta', 1, 2)
    #rapida
    diqno1          = AccionRapida('diqno', 'accion', 'rapida', 4, -1)
    diqno2          = AccionRapida('diqno', 'accion', 'rapida', 4, -1)
    diqno3          = AccionRapida('diqno', 'accion', 'rapida', 4, -1)
    doblaR1         = AccionRapida ('doblaRenta', 'accion', 'rapida', 1, 1)
    doblaR2         = AccionRapida ('doblaRenta', 'accion', 'rapida', 1, 1)
    #robarprop
    factordecisivo1 = AccionRobarPropiedad('factorDesicivo', 'accion', 'robarprop',  5, False)
    factordecisivo2 = AccionRobarPropiedad('factorDesicivo', 'accion', 'robarprop',  5, False)
    tratoA1         = AccionRobarPropiedad('tratoAstuto', 'accion', 'robarprop', 3, False, 1)
    tratoA2         = AccionRobarPropiedad('tratoAstuto', 'accion', 'robarprop', 3, False, 1)
    tratoA3         = AccionRobarPropiedad('tratoAstuto', 'accion', 'robarprop', 3, False, 1)
    tratoF1         = AccionRobarPropiedad('tratoForzado', 'accion', 'robarprop', 3, True, 1)
    tratoF2         = AccionRobarPropiedad('tratoForzado', 'accion', 'robarprop', 3, True, 1)
    tratoF3         = AccionRobarPropiedad('tratoForzado', 'accion', 'robarprop', 3, True, 1)
    #robardinero
    cumpleano1      = AccionRobarDinero('cumpleano', 'accion', 'robardinero', 2, True, 2)
    cumpleano2      = AccionRobarDinero('cumpleano', 'accion', 'robardinero', 2, True, 2)
    cumpleano3      = AccionRobarDinero('cumpleano', 'accion', 'robardinero', 2, True, 2)
    deuda1          = AccionRobarDinero('cobradeuda', 'accion', 'robardinero', 3, False, 5)
    deuda2          = AccionRobarDinero('cobradeuda', 'accion', 'robardinero', 3, False, 5)
    deuda3          = AccionRobarDinero('cobradeuda', 'accion', 'robardinero', 3, False, 5)   
     
    #DINERO
    dinero5        = Dinero('5', 'dinero')
    dinero51        = Dinero('5', 'dinero')
    dinero41        = Dinero('4', 'dinero')
    dinero42        = Dinero('4', 'dinero')
    dinero43        = Dinero('4', 'dinero')
    dinero31        = Dinero('3', 'dinero')
    dinero32        = Dinero('3', 'dinero')
    dinero33        = Dinero('3', 'dinero')
    dinero21        = Dinero ('2', 'dinero')
    dinero22        = Dinero ('2', 'dinero')
    dinero23        = Dinero ('2', 'dinero')
    dinero24        = Dinero ('2', 'dinero')
    dinero25        = Dinero ('2', 'dinero')
    dinero11        = Dinero ('1', 'dinero')
    dinero12        = Dinero ('1', 'dinero')
    dinero13        = Dinero ('1', 'dinero')
    dinero14        = Dinero ('1', 'dinero')
    dinero15        = Dinero ('1', 'dinero')
    dinero16        = Dinero ('1', 'dinero')
    dinero10       = Dinero ('10', 'dinero')
    
    #COMODIN
    comodinM       = Comodin('Maestro', 'comodin', [])
    comodinM1       = Comodin('Maestro', 'comodin', [])
    comodin        = Comodin('AnM', 'comodin', ['anaranjado', 'morado'], 2)
    comodina        = Comodin('AnM', 'comodin', ['anaranjado', 'morado'], 2)
    comodin2       = Comodin('NV', 'comodin', ['negro', 'verde'], 4)
    comodin3       = Comodin('BN', 'comodin', ['blanco', 'negro'], 2)
    comodin4       = Comodin('AcN', 'comodin', ['azulClaro', 'negro'], 4)
    comodin5       = Comodin('AmR', 'comodin', ['amarillo', 'rojo'], 3)
    comodin51       = Comodin('AmR', 'comodin', ['amarillo', 'rojo'], 3)
    comodin6       = Comodin('AzV', 'comodin', ['azul', 'verde'], 4 )
    comodin7       = Comodin('AcC', 'comodin', ['azulClaro', 'carmelita'], 1)
    


    cartas : Cartas = [ventnor, atlantico, jardinesM ,vermont ,oriental, connecticut  ,tenese,
                    ny, stjames, reading, vr, pennsylvania ,bio,muelle, park, mediterraneo ,
                    baltica, agua, electricidad , virginia, sanCarlos, estados, pennsylvaniaV,
                    pacifico, carolinaNorte, ilinois, indiana, kentucky, casa, casa2, casa3, hotel, 
                    hotel2, renta0, renta00, renta1, renta11, renta22, renta33, renta44, 
                    renta2, renta3, renta4, rentaT1, rentaT2, rentaT3, robar1, robar2, robar3, 
                    robar4, robar5, robar6, robar7, robar8, robar9, robar0, diqno1, diqno2,
                    diqno3, doblaR1, doblaR2, factordecisivo1, factordecisivo2, tratoA1, tratoA2, tratoA3,           
                    tratoF1, tratoF2, tratoF3, dinero5, dinero41, dinero42, dinero31, dinero21, dinero11, dinero10, comodinM, 
                    comodin, dinero51, dinero43, dinero32, dinero33, dinero22, dinero23, dinero24, dinero25,
                    dinero12, dinero13 ,dinero14 ,dinero15 , dinero16, comodinM1,
                    comodin2, comodin3, comodin4, comodin5, comodin6, comodin7, cumpleano1, cumpleano2,
                    cumpleano3, deuda1, deuda2, deuda3, comodina, comodin51]