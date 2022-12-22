import nltk
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

res = ['propiedad', 'accion', 'dinero','construccion' , 'renta' , 'robar' ,'carta' , 'rapida',
    'todos', 'casa' , 'hotel', 'cian' , 'magenta', 'mio' , 'otro', 'intercambio', 'cartas',
    'M', 'grupo', 'tomar', 'asd', 'dsa', 'valor', 'crear','#Valor#', '#Nombre#', '#ColorCo#','jugadores', 'jugador']
colores = ['cian', 'magenta']

groucho_grammar = nltk.CFG.fromstring( '''
S -> 'crear' 'carta' Carta | Carta
Carta -> Accion | Propiedad | Dinero | Comodin
Accion -> Renta | Construccion | Rapida | RobarCarta | RobarPropiedad | RobarDinero
Renta -> Nombre Tipo Subtipo ValorC ColorCo Todos | Nombre Subtipo ValorC ColorCo Todos
Construccion -> Nombre Tipo Subtipo ValorC TipoConstruccion Monto | Nombre Subtipo ValorC TipoConstruccion Monto
Rapida -> Nombre Tipo Subtipo ValorC Turno | Nombre Subtipo ValorC Turno
RobarCarta -> Nombre Tipo Subtipo ValorC CartasATomar | Nombre Subtipo ValorC CartasATomar
RobarPropiedad -> Nombre Tipo Subtipo ValorC Intercambio Cuantas | Nombre Subtipo ValorC Intercambio Cuantas
RobarDinero -> Nombre Tipo Subtipo Monto Todos ValorC | Nombre Subtipo Monto Todos ValorC
Propiedad -> Nombre Tipo ColorC CantGrupo RentaGrupo Valor
Comodin -> Nombre Tipo ColorCo Valor
Dinero -> NombreD Tipo | Tipo NombreD
Nombre -> '#Nombre#'
Tipo -> 'propiedad' | 'accion' | 'dinero'
Subtipo -> 'construccion' | 'renta' | 'robar' 'carta' | 'rapida' | 'robar' 'propiedad' | 'robar'
ValorC -> 'valor' Valor
Valor -> '#Valor#'
Todos -> 'todos' | Valor 'jugadores' | Valor 'jugador'
TipoConstruccion -> 'casa' | 'hotel'
ColorC -> 'cian' | 'magenta'
Turno -> 'mio' | 'otro'
Intercambio -> 'intercambio'
Cuantas -> Valor 'cartas'
Monto -> Valor 'M' | 'M' Valor
CantGrupo -> 'grupo' Valor | 'grupo' Valor
ColorCo -> '#ColorCo#' | '#ColorCo#' '#ColorCo#' |
NombreD -> Valor
CartasATomar -> 'tomar' Valor 'cartas'
Props -> 'asd'
RentaGrupo -> 'dsa'
''')

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

#card = 'Faster accion rapida con valor 5 mio'.split()# Rapida
#card = 'quiero crear carta Robaraaa de tipo robar carta con valor 5 tomar 3 cartas'.split() #Robar Carta
#card = 'necesito crear carta Facho para robar propiedad con valor 10 de intercambio de 3 cartas'.split() #Robar Propiedad
#card = 'Fachodinero de tipo accion para robar 10 M a 2 jugadores con valor 6'.split() #Robar dinero
#card = 'crear carta RRentass de tipo renta con valor 2 con colores cian magenta contra todos'.split() #Renta ver estooo la pila de #Color#
card = 'Casosona de tipo construccion con valor 2 la cual es una casa y me tienen q dar 3 M mas'.split()


#a = CleanToken(card)
sent = ['#Valor#' if i.isdigit() else i for i in card]
sent = ['#Nombre#' if i[0].isupper() and i != 'M' else i for i in sent]
sent = ['#ColorCo#' if i in colores else i for i in sent]
numbers = [i for i in card if i.isdigit()]
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