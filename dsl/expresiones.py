from enum import Enum

class OPERACION_ARITMETICA(Enum) :
    MAS = 1
    MENOS = 2
    POR = 3
    DIVIDIDO = 4

class OPERACION_LOGICA(Enum) :
    MAYOR_QUE = 1
    MENOR_QUE = 2
    IGUAL = 3
    DIFERENTE = 4

class ExpresionNumerica:
    '''
        Esta clase representa una expresión numérica
    '''

class ExpresionIdentificador() :
    '''
        Esta clase representa un identificador.
    '''

    def __init__(self, id = "") :
        self.id = id

class ExpresionIdentificadorJuego() :
    '''
        Esta clase representa un identificador.
    '''
    def __init__(self, id = "") :
        self.id = id

class ExpresionConcatenar() :
    '''
        Esta clase representa una Expresión de tipo cadena.
        Recibe como parámetros las 2 expresiones a concatenar
    '''

    def __init__(self, exp1, exp2) :
        self.exp1 = exp1
        self.exp2 = exp2

class ExpresionDobleComilla() :
    '''
        Esta clase representa una cadena entre comillas doble.
        Recibe como parámetro el valor del token procesado por el analizador léxico
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionCadenaNumerica() :
    '''
        Esta clase representa una expresión numérica tratada como cadena.
        Recibe como parámetro la expresión numérica
    '''
    def __init__(self, exp) :
        self.exp = exp

class ExpresionNumero() :
    '''
        Esta clase representa una expresión numérica entera o decimal.
    '''

    def __init__(self, exp = 0) :
        self.exp = exp

class ExpresionLogica() :
    '''
        Esta clase representa la expresión lógica.
        Esta clase recibe los operandos y el operador
    '''

    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

class ExpresionBinaria(ExpresionNumerica) :
    '''
        Esta clase representa la Expresión Aritmética Binaria.
        Esta clase recibe los operandos y el operador
    '''

    def __init__(self, exp1, exp2, operador) :
        self.exp1 = exp1
        self.exp2 = exp2
        self.operador = operador

class ExpresionLista() :
    '''
        Esta clase representa un identificador de tipo arreglo.
        Recibe el identificador y la expresion dentro del corchete
    '''
    def __init__(self, id , exp, atributo) :
        self.id = id
        self.exp = exp
        self.atributo = atributo

class ExpresionListaVacia() :
    '''
        Esta clase representa lista vacia.
    '''

