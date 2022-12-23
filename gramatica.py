import nltk
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

res = [
    'todos', 'casa' , 'hotel', 'cian' , 'magenta', 'mio' , 'otro', 'intercambio', 'cartas',
    'M', 'dsa', 'valor', 'crear','#Valor#', '#Nombre#', '#ColorCo#','jugadores', 'jugador',
    'participante', 'participantes', 'totalidad', ',', 'negro', 'azul', 'marron', 'gris', 'verde', 'naranja',
    'rosa', 'purpura', 'rojo', 'blanco', 'amarillo', 'carta', 'grupo']

colores = ['cian', 'magenta', 'negro', 'azul', 'marron', 'gris', 'verde', 'naranja',
           'rosa', 'purpura', 'rojo', 'blanco', 'amarillo']

groucho_grammar = nltk.CFG.fromstring( '''
S -> 'crear' 'carta' Carta | Carta
Carta -> Accion | Propiedad | Dinero | Comodin
Accion -> Renta | Construccion | Rapida | RobarCarta | RobarPropiedad | RobarDinero
Renta -> Nombre ValorC ColorCo Todos
Construccion -> Nombre ValorC TipoConstruccion Monto
Rapida -> Nombre ValorC Turno
RobarCarta -> Nombre ValorC CartasATomar
RobarPropiedad -> Nombre ValorC Intercambio CartasATomar
RobarDinero -> Nombre Monto Todos ValorC
Propiedad -> Nombre ColorCo CantGrupo RentaGrupo ValorC
Comodin -> Nombre ColorCo ValorC
Dinero -> NombreD
Nombre -> '#Nombre#'
ValorC -> 'valor' Valor
Valor -> '#Valor#'
Todos -> 'todos' | Valor 'jugadores' | Valor 'jugador' | Valor 'participates' | Valor 'participante'
TipoConstruccion -> 'casa' | 'hotel'
Turno -> 'mio' | 'otro'
Intercambio -> 'intercambio'
Monto -> Valor 'M' | 'M' Valor
CantGrupo -> 'grupo' Valor
ColorCo -> '#ColorCo#' | '#ColorCo#' '#ColorCo#' |
NombreD -> Monto
CartasATomar -> Valor 'cartas' | Valor 'carta'
Coma -> ','
RentaGrupo -> '#Valor#' | '#Valor#' Coma '#Valor#' | '#Valor#' Coma '#Valor#' Coma '#Valor#'
''')

#|'#Valor#' Coma '#Valor#' Coma '#Valor#' Coma '#Valor#' | '#Valor#' Coma '#Valor#' Coma '#Valor#' Coma '#Valor#' Coma '#Valor#'

def NormalizeDoc(s):
    '''Funcion que normaliza cada documento. Ej: si el doc tiene -á- sera sustituida por -a-'''
    replacements = (
        ("á","a"), ("é","e"), ("í","i"), ("ó","o"), ("ú","u"), ("-", " "), (".", " "), ("_", " "), ("/", " ")
    )
    for a,b in replacements:
        s = s.replace(a,b)
    return s

def CleanToken(text):
    '''Funcion que elimina las palabras que -no aportan significado-, preposiciones, articulos, etc'''
    tokenize = nltk.word_tokenize(NormalizeDoc(text))
    cleanToken = []
    stop = set(stopwords.words('english'))
    stop1 = set(stopwords.words('spanish'))
    stop = stop.union(stop1)
    lemmatizer  = WordNetLemmatizer()
    for i in tokenize:
        i = lemmatizer.lemmatize(i)
        if not i.lower() in stop and "'" not in i:
            if (len(i) > 1):
                cleanToken.append(i.lower())
    return cleanToken

#card = 'Faster con valor 5 el turno mio'.split()# Rapida
#card = 'quiero crear carta Robaraaa con valor 5 para poder robar del mazo 3 cartas'.split() #Robar Carta
#card = 'necesito crear carta Facho para robar propiedad con valor 10 de intercambio de 3 cartas'.split() #Robar Propiedad
#card = 'necesito crear carta Facho con valor 10 de intercambio de 3 cartas'.split() #Robar Propiedad
#card = 'Fachodinero para robar 10 M a 2 jugadores con valor 6'.split() #Robar dinero
#card = 'crear carta RRentass con valor 2 con colores cian rojo contra 1 jugador'.split() #Renta ver estooo la pila de #Color#
#card = 'Casosona con valor 2 la cual es una casa y me tienen q dar 3 M mas'.split()
#card = 'crear carta de 10 M'.split()
#card = 'Comdindin cian magenta con valor 3'.split() #Comodin
#card = 'Comdindin maestro con valor 3'.split() #Comodin
#card = 'crear carta Propi de color cian para un grupo de tamaño 3 donde las rentas son 2, 3, 5 con valor 2'.split()
#card = 'quiero crear una carta que se llame PEPR que sea propiedad de color verde de cuyo grupo es de tamaño 3 cuya renta tenga los valores 2, 3, 5 el valor es de 10 '.split()
#card = 'crear carta CHUCHA de color cian grupo de 3 y la renta sea 2, 4, 5 de valor 100'.split()
card = 'Rentaaaaa con un valor de 2 y me tengan que pagar por los colores azul purpura todos'.split()

#a = CleanToken(card)

sent = []
for i in card:
    if i.isdigit():
        sent.append('#Valor#')
    elif i[:len(i)-1].isdigit():
        sent.append('#Valor#')
        sent.append(',')
    else:
        sent.append(i)
        
#sent = ['#Valor#' if i.isdigit() else i for i in card]
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

parser = nltk.ChartParser(groucho_grammar)
for tree in parser.parse(original_sent):
    treestr = str(tree)
    for n in numbers:
        treestr = treestr.replace('#Valor#', n, 1)
    for n in alpha:
        treestr = treestr.replace('#Nombre#', n, 1)
    for n in cols:
        treestr = treestr.replace('#ColorCo#', n, 1)
    print(treestr)