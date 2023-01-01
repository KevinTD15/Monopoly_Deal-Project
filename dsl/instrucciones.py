class Instruccion:
    '''This is an abstract class'''

class Imprimir(Instruccion) :
    '''
        Esta clase representa la instrucción imprimir.
        La instrucción imprimir únicamente tiene como parámetro una cadena
    '''

    def __init__(self,  cad) :
        self.cad = cad

class Len(Instruccion) :
    '''
        Esta clase representa la instrucción imprimir.
        La instrucción imprimir únicamente tiene como parámetro una cadena
    '''

    def __init__(self,  cad) :
        self.cad = cad

class While(Instruccion) :
    '''
        Esta clase representa la instrucción mientras.
        La instrucción mientras recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''

    def __init__(self, expLogica, instrucciones = []) :
        self.expLogica = expLogica
        self.instrucciones = instrucciones

class Asignacion(Instruccion) :
    '''
        Esta clase representa la instrucción de asignación de variables
        Recibe como parámetro el identificador a asignar y el valor que será asignado.
    '''

    def __init__(self, id, exp) :
        self.id = id
        self.exp = exp

class AgregarElemLista(Instruccion) :
    '''
        Esta clase instancia nombre lista y el id a anadir.
        Recibe como parámetro el valor del token procesado por el analizador léxico
    '''
    def __init__(self, id, exp) :
        self.id=id
        self.exp = exp

class If(Instruccion) : 
    '''
        Esta clase representa la instrucción if.
        La instrucción if recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''

    def __init__(self, expLogica, instrucciones = []) :
        self.expLogica = expLogica
        self.instrucciones = instrucciones

class IfElse(Instruccion) : 
    '''
        Esta clase representa la instrucción if-else.
        La instrucción if-else recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera y otro lista de instrucciones
        a ejecutar si la expresión lógica es falsa.
    '''

    def __init__(self, expLogica, instrIfVerdadero = [], instrIfFalso = []) :
        self.expLogica = expLogica
        self.instrIfVerdadero = instrIfVerdadero
        self.instrIfFalso = instrIfFalso


class FuncionDecl(Instruccion) :
    '''
        Esta clase representa declaracion de funcion.
        La instrucción mientras recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''

    def __init__(self, id, param = [], instrucciones = []) :
        self.id = id
        self.param = param
        self.instrucciones = instrucciones

class Funcion(Instruccion) :
    '''
        Esta clase representa declaracion de funcion.
        La instrucción mientras recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''

    def __init__(self, id, param = []) :
        self.id = id
        self.param = param

class Retorno(Instruccion) :
    '''
        Esta clase representa declaracion de funcion.
        La instrucción mientras recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''

    def __init__(self,exp) :
        self.exp = exp