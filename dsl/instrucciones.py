class Imprimir:
    '''
        Esta clase representa la instrucción imprimir.
        Recibe como parámetro una cadena
    '''
    def __init__(self, fila, cad ) :
        self.fila = fila
        self.cad = cad

class While :
    '''
        Esta clase representa la instrucción mientras.
        La instrucción mientras recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''

    def __init__(self, fila, expLogica, instrucciones = []) :
        self.fila = fila
        self.expLogica = expLogica
        self.instrucciones = instrucciones

class Asignacion:
    '''
        Esta clase representa la instrucción de asignación de variables
        Recibe como parámetro el identificador a asignar y el valor que será asignado.
    '''

    def __init__(self, fila, id,  exp) :
        self.fila = fila
        self.id = id
        self.exp = exp

class If : 
    '''
        Esta clase representa la instrucción if.
        La instrucción if recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''

    def __init__(self, fila, expLogica, instrucciones = []) :
        self.fila = fila
        self.expLogica = expLogica
        self.instrucciones = instrucciones

class IfElse : 
    '''
        Esta clase representa la instrucción if-else.
        La instrucción if-else recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera y otro lista de instrucciones
        a ejecutar si la expresión lógica es falsa.
    '''

    def __init__(self, fila, expLogica, instrIfVerdadero = [], instrIfFalso = []) :
        self.fila = fila
        self.expLogica = expLogica
        self.instrIfVerdadero = instrIfVerdadero
        self.instrIfFalso = instrIfFalso


class FuncionDecl :
    '''
        Esta clase representa la instruccion de declaracion de funcion.
        Recibe como parámetro el identificador, lista de parametros (puede estar vacia) y
        la lista de instrucciones.
    '''

    def __init__(self, fila, id, param = [], instrucciones = []) :
        self.id = id
        self.fila = fila
        self.param = param
        self.instrucciones = instrucciones

class Funcion :
    '''
        Esta clase representa la instruccion de llamado a funcion.
        Recibe como parámetro el identificador y lista de parametros (puede estar vacia).
    '''

    def __init__(self, fila, id, param = []) :
        self.id = id
        self.param = param
        self.fila = fila

class Retorno :
    '''
        Esta clase representa la instrucción Retorno de una funcion.
        Recibe como parámetro expresion a retornar.
    '''

    def __init__(self, fila, exp) :
        self.exp = exp
        self.fila = fila
                
class AgregarElemLista :
    '''
        Esta clase representa la instruccion de agregar elementos a una lista.
        Recibe como parámetro el identificador de la lista y el elemento a añadir.
    '''
    def __init__(self, fila, id, exp) :
        self.id=id
        self.exp = exp
        self.fila = fila
        
class EliminarElemLista :
    '''
        Esta clase representa la instruccion de eliminar elementos a una lista.
        Recibe como parámetro el identificador de la lista y indice del elemento a eliminar.
    '''
    def __init__(self, fila, id, exp) :
        self.id=id
        self.exp = exp
        self.fila = fila
        
class Len :
    '''
        Esta clase representa la funcion len que calcula la longitud del parametro recibido
        Recibe como parámetro una cadena o lista.
    '''

    def __init__(self,  cad) :
        self.cad = cad
