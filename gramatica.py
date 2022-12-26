import nltk

res = [
    'todos', 'casa' , 'hotel', 'cian' , 'magenta', 'mi' , 'mio', 'otro', 'intercambio', 'cartas',
    'M', 'dsa', 'valor', 'crear','#Valor#', '#Nombre#', '#ColorCo#', 'jugador',
    'participante', 'totalidad', ',', 'negro', 'azul', 'marron', 'gris', 'verde', 'naranja',
    'rosa', 'purpura', 'rojo', 'blanco', 'amarillo', 'carta', 'grupo', 'valga', 'intercambiar',
    'conjunto', 'naipe', 'naipes', 'tarjeta', 'tarjetas', 'cada']

coloresEnUso = ['azulClaro', 'carmelita', 'morado', 'anaranjado', 'rojo', 'amarillo', 'verde', 'azul', 'blanco', 'negro']

cantGrupo = [3,2,3,3,3,3,3,2,2,4]

colores = ['cian', 'magenta', 'negro', 'azul', 'marron', 'gris', 'verde', 'naranja',
           'rosa', 'purpura', 'rojo', 'blanco', 'amarillo','azulClaro', 'carmelita', 'morado', 'anaranjado'
           ]

noTerminales = ['Nombre', 'ColorCo', 'CantGrupo', 'RentaGrupo', 'ValorC', 'M',
                'NombreD', 'Todos', 'Intercambio', 'CartasATomar', 'Turno', 'TipoConstruccion', 'MontoC',
                'MontoD'] #Ver Monto

terminales = ['#Valor#', '#Nombre#', 'todos', 'cada', 'mi', 'otro', 'intercambio', 'intercambiar', 'casa',
              'hotel', 'mio']

subtipo = ['Renta', 'Construccion', 'Rapida', 'RobarCarta', 'RobarPropiedad', 'RobarDinero']

tipo = ['Propiedad', 'Accion', 'Comodin', 'Dinero']

groucho_grammar = nltk.CFG.fromstring( '''
S -> 'crear' 'carta' Carta | Carta
Carta -> Accion | Propiedad | Dinero | Comodin
Accion -> Renta | Construccion | Rapida | RobarCarta | RobarPropiedad | RobarDinero
Renta -> Nombre ValorC ColorCo Todos | Nombre Todos ColorCo ValorC | Nombre ColorCo Todos ValorC | Nombre Todos ColorCo ValorC
Construccion -> Nombre ValorC TipoConstruccion MontoC | TipoConstruccion MontoC Nombre ValorC | TipoConstruccion Nombre MontoC ValorC
Rapida -> Nombre ValorC Turno | Turno ValorC Nombre | ValorC Turno Nombre | Nombre Turno ValorC
RobarCarta -> Nombre ValorC CartasATomar | Nombre CartasATomar ValorC | CartasATomar Nombre ValorC
RobarPropiedad -> Nombre ValorC Intercambio CartasATomar | CartasATomar Intercambio ValorC Nombre | CartasATomar Intercambio Nombre ValorC | Nombre Intercambio CartasATomar ValorC
RobarDinero -> Nombre MontoD Todos ValorC | Nombre Todos MontoD ValorC | Todos MontoD Nombre ValorC | MontoD Todos Nombre ValorC
Propiedad -> Nombre ColorCo CantGrupo RentaGrupo ValorC | Nombre ColorCo ValorC CantGrupo RentaGrupo | ColorCo Nombre ValorC CantGrupo RentaGrupo | ColorCo Nombre CantGrupo RentaGrupo ValorC | Nombre ColorCo RentaGrupo ValorC CantGrupo 
Comodin -> Nombre ColorCo ValorC | Nombre ValorC ColorCo
Dinero -> NombreD
Nombre -> '#Nombre#'
NombreD -> Monto
ValorC -> 'valor' Monto | 'valga' Monto
MontoD -> Valor 'M' | 'M' Valor
MontoC -> Valor 'M' | 'M' Valor
Monto -> Valor 'M' | 'M' Valor
Valor -> '#Valor#'
Todos -> 'todos' | 'cada' | Valor 'jugador' | Valor 'participante'
TipoConstruccion -> 'casa' | 'hotel'
Turno -> 'mi' | 'otro' | 'mio'
Intercambio -> 'intercambio' | 'intercambiar' |
CantGrupo -> 'grupo' Valor | 'conjunto' Valor
Color -> '#ColorCo#'
ColorCo -> Color | Color Color | Color Color Color | Color Color Color Color |
CartasATomar -> Valor 'cartas' | Valor 'carta' | Valor 'naipe' | Valor 'naipes' | Valor 'tarjeta' | Valor 'tarjetas'
Coma -> ','
RentaGrupo -> Valor | Valor Coma Valor | Valor Coma Valor Coma Valor | Valor Coma Valor Coma Valor Coma Valor
''')

def ConvertirV(card):
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

    dicVals = {'#Valor#':[], '#Nombre#': [], '#ColorCo#': []}
    for i in card:
        if i.isdigit():
            dicVals['#Valor#'].append(i)
        elif i[:len(i)-1].isdigit():
            dicVals['#Valor#'].append(i[:len(i)-1])
            
    dicVals['#Nombre#'] = [i for i in card if i[0].isupper() and i != 'M']
    dicVals['#ColorCo#'] = [i for i in card if i in colores]

    original_sent = []
    for i in sent:
        if(i in res):
            original_sent.append(i)
            
    return original_sent, dicVals

def RecibirValores(original_sent, dic):
    parser = nltk.ChartParser(groucho_grammar)
    lista = []
    paramDic = {}
    for tree in parser.parse(original_sent):       
        RecibirValoresRec(tree, paramDic, dic)
        return paramDic

def RecibirValoresRec(tree, paramDic, dic, label=None):
    for i in tree:
        if((type(i) == nltk.Tree and i._label != 'Coma')):
            if(i._label in tipo):
                paramDic['tipo'] = i._label
            elif(i._label in subtipo):
                paramDic['subtipo'] = i._label
            elif(len(i)>1):
                RecibirValoresRec(i, paramDic, dic, i._label)  
            elif(i._label in noTerminales):
                if(len(i) > 0):
                    if (type(i[0]) == nltk.Tree):
                        RecibirValoresRec(i, paramDic, dic, i._label)
                    else:    
                        if(i[0] in dic):
                            paramDic[i._label] = dic[i[0]].pop(0)
                        else:
                            paramDic[i._label] = i[0]
            elif(label is not None and label in noTerminales):
                if(label in paramDic):
                    if(i[0] in dic):
                        paramDic[label].append(dic[i[0]].pop(0))
                    else:
                        paramDic[label].append(i[0])
                else:
                    if(i[0] in dic):
                        paramDic[label] = [dic[i[0]].pop(0)]
                    else:
                        paramDic[label] = [i[0]]
            RecibirValoresRec(i, paramDic, dic, label)

def CrearCartas(cartasACrear):
    for i in cartasACrear:
        return

def Convertir(card):
    arbol, dic = ConvertirV(card)
    return RecibirValores(arbol, dic)
