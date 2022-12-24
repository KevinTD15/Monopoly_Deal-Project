import nltk

res = [
    'todos', 'casa' , 'hotel', 'cian' , 'magenta', 'mi' , 'otro', 'intercambio', 'cartas',
    'M', 'dsa', 'valor', 'crear','#Valor#', '#Nombre#', '#ColorCo#','jugadores', 'jugador',
    'participante', 'participantes', 'totalidad', ',', 'negro', 'azul', 'marron', 'gris', 'verde', 'naranja',
    'rosa', 'purpura', 'rojo', 'blanco', 'amarillo', 'carta', 'grupo', 'valga', 'intercambiar',
    'conjunto', 'naipe', 'naipes', 'tarjeta', 'tarjetas', 'cada']

coloresEnUso = ['azulClaro', 'carmelita', 'morado', 'anaranjado', 'rojo', 'amarillo', 'verde', 'azul', 'blanco', 'negro']

colores = ['cian', 'magenta', 'negro', 'azul', 'marron', 'gris', 'verde', 'naranja',
           'rosa', 'purpura', 'rojo', 'blanco', 'amarillo','azulClaro', 'carmelita', 'morado', 'anaranjado'
           ]

noTerminales = ['Nombre', 'ColorCo', 'CantGrupo', 'RentaGrupo', 'ValorC', 'M',
                'NombreD', 'Todos', 'Intercambio', 'CartasATomar', 'Turno', 'TipoConstruccion'
                ] #Ver Monto

terminales = ['#Valor#', '#Nombre#', 'todos', 'cada', 'mi', 'otro', 'intercambio', 'intercambiar', 'casa',
              'hotel']

subtipo = ['Renta', 'Construccion', 'Rapida', 'RobarCarta', 'RobarPropiedad', 'RobarDinero']

tipo = ['Propiedad', 'Accion', 'Comodin', 'Dinero']

groucho_grammar = nltk.CFG.fromstring( '''
S -> 'crear' 'carta' Carta | Carta
Carta -> Accion | Propiedad | Dinero | Comodin
Accion -> Renta | Construccion | Rapida | RobarCarta | RobarPropiedad | RobarDinero
Renta -> Nombre ValorC ColorCo Todos | Nombre Todos ColorCo ValorC | Nombre ColorCo Todos ValorC | Nombre Todos ColorCo ValorC
Construccion -> Nombre ValorC TipoConstruccion Monto | TipoConstruccion Monto Nombre ValorC | TipoConstruccion Nombre Monto ValorC
Rapida -> Nombre ValorC Turno | Turno ValorC Nombre | ValorC Turno Nombre | Nombre Turno ValorC
RobarCarta -> Nombre ValorC CartasATomar | Nombre CartasATomar ValorC | CartasATomar Nombre ValorC
RobarPropiedad -> Nombre ValorC Intercambio CartasATomar | CartasATomar Intercambio ValorC Nombre | CartasATomar Intercambio Nombre ValorC | Nombre Intercambio CartasATomar ValorC
RobarDinero -> Nombre Monto Todos ValorC | Nombre Todos Monto ValorC | Todos Monto Nombre ValorC | Monto Todos Nombre ValorC
Propiedad -> Nombre ColorCo CantGrupo RentaGrupo ValorC | Nombre ColorCo ValorC CantGrupo RentaGrupo | ColorCo Nombre ValorC CantGrupo RentaGrupo | ColorCo Nombre CantGrupo RentaGrupo ValorC
Comodin -> Nombre ColorCo ValorC | Nombre ValorC ColorCo
Dinero -> NombreD
Nombre -> '#Nombre#'
NombreD -> Monto
ValorC -> 'valor' Monto | 'valga' Monto
Monto -> Valor 'M' | 'M' Valor
Valor -> '#Valor#'
Todos -> 'todos' | 'cada' | Valor 'jugadores' | Valor 'jugador' | Valor 'participates' | Valor 'participante'
TipoConstruccion -> 'casa' | 'hotel'
Turno -> 'mi' | 'otro'
Intercambio -> 'intercambio' | 'intercambiar'
CantGrupo -> 'grupo' Valor | 'conjunto' Valor
Color -> '#ColorCo#'
ColorCo -> Color | Color Color | Color Color Color | Color Color Color Color |
CartasATomar -> Valor 'cartas' | Valor 'carta' | Valor 'naipe' | Valor 'naipes' | Valor 'tarjeta' | Valor 'tarjetas'
Coma -> ','
RentaGrupo -> Valor | Valor Coma Valor | Valor Coma Valor Coma Valor | Valor Coma Valor Coma Valor Coma Valor
''')

card = 'Faster con valor 5 M el turno mio'.split()# Rapida
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
#card = 'crear carta CHUCHA de color cian grupo de 3 y la renta sea 2, 4, 5 con un valor de 100 M'.split() #Propiedad
#card = 'Rentaaaaa con un valor de 2 M y me tengan que pagar por los colores azul purpura todos'.split() #Renta
#card = 'quiero crear carta que se llame Rentaaaaa contra todos que me tengan que pagar por los colores azul purpura y que valga 3 M'.split() #Renta

def Convertir(card):
    sent = []
    for i in card:
        if i.isdigit():
            sent.append('#Valor#')
        elif i[:len(i)-1].isdigit():
            sent.append('#Valor#')
            sent.append(',')
        else:
            sent.append(i)
            
    sent = ['#Nombre#' if i[0].isupper() and i != 'M' else i for i in sent]
    sent = ['#ColorCo#' if i in colores else i for i in sent]

    numbers = []
    for i in card:
        if i.isdigit():
            numbers.append(i)
        elif i[:len(i)-1].isdigit():
            numbers.append(i[:len(i)-1])
            
    alpha = [i for i in card if i[0].isupper()]
    cols = [i for i in card if i in colores]

    original_sent = []
    for i in sent:
        if(i in res):
            original_sent.append(i)
            
    return original_sent, numbers, alpha, cols

def RecibirValores(original_sent, numbers, alpha, cols):
    parser = nltk.ChartParser(groucho_grammar)
    lista = []
    paramDic = {}
    for tree in parser.parse(original_sent):       
        RecibirValoresRec(tree, paramDic)
        lista.append(paramDic)
        paramDic={}
        #if(type(a) == 'nltk.tree.tree.Tree'):
            #print(type(a) == nltk.Tree)
        #treestr = str(tree)
        #for n in numbers:
        #   treestr = treestr.replace('#Valor#', n, 1)
        #for n in alpha:
        #   treestr = treestr.replace('#Nombre#', n, 1)
        #for n in cols:
        #   treestr = treestr.replace('#ColorCo#', n, 1)
        #print(treestr)
    return lista

def RecibirValoresRec(tree, paramDic, label=None):
    for i in tree:
        # if(i[0] in terminales):
        #     if(label is not None and label in noTerminales):
        #         paramDic[label] = i[0]
        #     else:
        #         paramDic[i._label] = i[0]
        if((type(i) == nltk.Tree and i._label != 'Coma')):
            if(i._label in tipo):
                paramDic['tipo'] = i._label
            elif(i._label in subtipo):
                paramDic['subtipo'] = i._label
            elif(len(i)>1):
                RecibirValoresRec(i, paramDic, i._label)  
            elif(i._label in noTerminales):
                if(len(i) > 0):
                    if (type(i[0]) == nltk.Tree):
                        RecibirValoresRec(i, paramDic, i._label)
                        #label = i._label
                    else:    
                        paramDic[i._label] = i[0]
            elif(label is not None and label in noTerminales):
                if(label in paramDic):
                    paramDic[label].append(i[0])
                else:
                    paramDic[label] = [i[0]]
            RecibirValoresRec(i, paramDic, label)

#def VerfificarCarta(cartasACrear):
#    for i in cartasACrear:
#        if(i['Color'] in coloresEnUso)

def CrearCartas(cartasACrear):
    for i in cartasACrear:
        return

def Ejecutar(card):
    a, b, c, d = Convertir(card)
    cartasACrear = RecibirValores(a,b,c,d)
    #VerfificarCarta(cartasACrear)
    cartasCreadas = CrearCartas(cartasACrear) 
    
Ejecutar(card)