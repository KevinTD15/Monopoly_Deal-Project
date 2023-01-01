from dsl.expresiones import *
from dsl.instrucciones import *
from dsl.juego import *

reservadas = {
    'imprimir' : 'IMPRIMIR',
    'mientras' : 'WHILE',
    'si' : 'IF',
    'else' : 'ELSE',
    'func' : 'FUNC',
    'retorno' : 'RETURN',
    'len' : 'LEN',
    'crear' : 'CREAR',
    'comenzar' : 'COMENZAR',
    'juego' : 'JUEGO',
    'agregar' :'AGREGAR',
    'jugador' : 'JUGADOR',
    'aleatorio' : 'ALEATORIO',
    'inteligentebasico' : 'INTELIGENTE1',
    'inteligenteprobabilistico' : 'INTELIGENTE',
    'inteligentemejorado' : 'INTELIGENTE2',
    'ganador' : 'GANADOR',
    'notificaciones' : 'NOTIFICACIONES',
    'jugadores' : 'JUGADORES',
    'reestablecer' : 'REESTABLECER',
    'ejecutarturno' : 'EJECUTARTURNO',
    'carta' : 'CARTA',
    'finaljuego' : 'FINALJUEGO'
}

tokens  = [
    'LLAVIZQ',
    'LLAVDER',
    'PARIZQ',
    'PARDER',
    'CORCHEIZQ',
    'CORCHEDER',
    'IGUAL',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'CONCAT',
    'MENORQUE',
    'MAYORQUE',
    'IGUALQUE',
    'NIGUALQUE',
    'COMA',
    'PUNTO',
    'DECIMAL',
    'ENTERO',
    'CADENA',
    'ID'
] + list(reservadas.values())

# Tokens
t_LLAVIZQ   = r'{'
t_LLAVDER   = r'}'
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_CORCHEIZQ = r'\['
t_CORCHEDER = r'\]'
t_IGUAL     = r'='
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDIDO  = r'/'
t_CONCAT    = r'&'
t_MENORQUE    = r'<'
t_MAYORQUE    = r'>'
t_IGUALQUE  = r'=='
t_NIGUALQUE = r'!='
t_COMA      = r','
t_PUNTO      = r'.'

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
     return t

def t_CADENA(t):
    r'\".*?\"'
    t.value = t.value[1:-1] # remuevo las comillas
    return t 

# Comentario de múltiples líneas /* .. */
def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'//.*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("mpd> Carácter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()

#anadido
def test(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print (tok)

# Asociación de operadores y precedencia
precedence = (
    ('left','CONCAT'),
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO'),
    )

# Definición de la gramática

def p_inicio(t) :
    'inicio           : instrucciones'
    t[0] = t[1]

def p_instrucciones_lista(t) :
    'instrucciones    : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
    t[0] = [t[1]]

def p_instruccion(t) :
    '''instruccion      : instrImprimir
                        | instrAsignacion
                        | instrWhile
                        | instrIf
                        | instrIfElse
                        | declFuncion
                        | llamaFuncion
                        | instrRetorno
                        | instrAgregar
                        | instrLen
                        | instrCrear
                        | instrComenzar'''
    t[0] = t[1]

def p_variable(t):
    ''' variable : ID 
                | ID CORCHEIZQ expresion_cadena CORCHEDER
                | idjuego  
                | idjuego CORCHEIZQ expresion_cadena CORCHEDER atributo
    '''
    if len(t)==2:
        t[0]=t[1]
    elif len(t)==5:
        t[0]=ExpresionLista(t[1],t[3],None)  
    elif len(t)==6:
        t[0]=ExpresionLista(t[1],t[3],t[5])  

def p_id_juego(t):
    ''' idjuego : JUGADORES
                | NOTIFICACIONES
                | GANADOR
                | FINALJUEGO
    '''
    t[0]=ExpresionIdentificadorJuego(t[1])

def p_id_juego_atrib(t): 
    ''' atributo : PUNTO ID
                | vacio'''
    if len(t)==3:
        t[0] = t[2]
    else:
        t[0] = t[1]
    

def p_decl_funcion(t) :
    'declFuncion  : FUNC ID PARIZQ argument_list_decl PARDER LLAVIZQ instrucciones LLAVDER' 
    t[0] = FuncionDecl(t[2],t[4],t[7])

def p_argument_list_decl(t):
    '''argument_list_decl : argument_list_decl COMA argument_decl 
                        | argument_decl
                        | vacio'''
    if len(t)==4:
        t[1].append(t[3])
        t[0] = t[1]
    elif len(t)==2:
        t[0] = [t[1]]

def p_argument_decl(t):
    'argument_decl :  variable'
    t[0]= t[1]

def p_argument_list(t):
    '''argument_list : argument_list COMA argument 
                    | argument
                    | vacio'''
    if len(t)==4:    
        t[1].append(t[3])
        t[0] = t[1]
    elif len(t)==2 and t[1]!=None:
        t[0] = [t[1]]
    else:   
        t[0] = t[1]

def p_argument(t):
    'argument :  expresion_cadena'
    t[0]= t[1]

def p_llama_funcion(t):
    ''' llamaFuncion : ID PARIZQ argument_list PARDER
                    | idfuncjuego PARIZQ argument_list PARDER'''
    t[0] = Funcion(t[1],t[3])

def p_idfuncjuego(t):
    ''' idfuncjuego : REESTABLECER
            | EJECUTARTURNO
            | CARTA
            '''
    t[0] = IdFuncionJuego(t[1])

def p_return(t):
    'instrRetorno : RETURN expresion_cadena'
    t[0]=Retorno(t[2])

def p_instruccion_imprimir(t) :
    'instrImprimir   : IMPRIMIR PARIZQ expresion_cadena PARDER'
    t[0] =Imprimir(t[3])

def p_instruccion_len(t) :
    'instrLen   : LEN PARIZQ expresion_cadena PARDER'
    t[0] =Len(t[3])

def p_asignacion_instr(t) :
    '''instrAsignacion   : variable IGUAL expresion_cadena
                        | variable IGUAL llamaFuncion'''
    t[0] =Asignacion(t[1], t[3])

def p_asignacion_corchetes(t) :
    'instrAsignacion   : variable IGUAL CORCHEIZQ CORCHEDER'
    t[0] =Asignacion(t[1], ExpresionListaVacia())

def p_while_instr(t) :
    'instrWhile     : WHILE PARIZQ expresion_logica PARDER LLAVIZQ instrucciones LLAVDER'
    t[0] =While(t[3], t[6])

def p_if_instr(t) :
    'instrIf           : IF PARIZQ expresion_logica PARDER LLAVIZQ instrucciones LLAVDER'
    t[0] =If(t[3], t[6])

def p_if_else_instr(t) :
    'instrIfElse      : IF PARIZQ expresion_logica PARDER LLAVIZQ instrucciones LLAVDER ELSE LLAVIZQ instrucciones LLAVDER'
    t[0] =IfElse(t[3], t[6], t[10])

def p_agregar(t):
    ''' instrAgregar : AGREGAR  expresion_cadena ID
                    | AGREGAR  expresion_cadena idjuego'''
    t[0]=AgregarElemLista(t[3],t[2])

def p_crear(t):
    ''' instrCrear : CREAR JUEGO
                    | CREAR CARTA CADENA
                    | CREAR JUGADOR tipo ID'''
    if len(t)==3:
        t[0]=CrearJuego()
    elif len(t)==4:
        t[0]=Funcion(IdFuncionJuego(t[2]),t[3])
    elif len(t)==5:
        t[0]=CrearJugador(t[3],t[4])

def p_tipo_jugador(t):
    ''' tipo : ALEATORIO
            | INTELIGENTE
            | INTELIGENTE1
            | INTELIGENTE2'''
    t[0] = t[1]

def p_comenzar_juego(t):
    ''' instrComenzar : COMENZAR JUEGO'''
    t[0] = ComenzarJuego()

def p_expresion_binaria(t):
    '''expresion_numerica : expresion_numerica MAS expresion_numerica
                        | expresion_numerica MENOS expresion_numerica
                        | expresion_numerica POR expresion_numerica
                        | expresion_numerica DIVIDIDO expresion_numerica'''
    if t[2] == '+'  : t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MAS)
    elif t[2] == '-': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.MENOS)
    elif t[2] == '*': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.POR)
    elif t[2] == '/': t[0] = ExpresionBinaria(t[1], t[3], OPERACION_ARITMETICA.DIVIDIDO)

def p_expresion_agrupacion(t):
    '''expresion_numerica : PARIZQ expresion_numerica PARDER '''
    if len(t)==4:
        t[0] = t[2]

def p_expresion_simple(t):
    '''expresion_numerica : ENTERO
                          | DECIMAL 
                          '''
    t[0] = ExpresionNumero(t[1])

def p_expresion_numerica_id(t):
    'expresion_numerica   : variable'
    t[0] = ExpresionIdentificador(t[1])

def p_expresion_numerica_len(t):
    'expresion_numerica   : instrLen'
    t[0]=t[1]

def p_expresion_concatenacion(t) :
    'expresion_cadena     : expresion_cadena CONCAT expresion_cadena'
    t[0] = ExpresionConcatenar(t[1], t[3])

def p_expresion_cadena(t) :
    'expresion_cadena     : CADENA'
    t[0] = ExpresionDobleComilla(t[1])

def p_expresion_cadena_numerico(t) :
    'expresion_cadena     : expresion_numerica'
    t[0] = ExpresionCadenaNumerica(t[1])

def p_expresion_logica(t) :
    '''expresion_logica : expresion_numerica MAYORQUE expresion_numerica
                        | expresion_numerica MENORQUE expresion_numerica
                        | expresion_numerica IGUALQUE expresion_numerica
                        | expresion_numerica NIGUALQUE expresion_numerica'''
    if t[2] == '>'    : t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MAYOR_QUE)
    elif t[2] == '<'  : t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.MENOR_QUE)
    elif t[2] == '==' : t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.IGUAL)
    elif t[2] == '!=' : t[0] = ExpresionLogica(t[1], t[3], OPERACION_LOGICA.DIFERENTE)

def p_vacio(t):
    'vacio :'
    pass

def p_error(t):
    print(f'Error sintáctico en: \'{t.value}\' en línea: {t.lineno} columna: {t.lexpos}')
    exit()

import ply.yacc as yacc
parser = yacc.yacc()


def parse(input) :
    #test(input)
    return parser.parse(input)