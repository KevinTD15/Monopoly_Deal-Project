class CrearJuego:
    '''
        clase que representa la cracion del juego
    '''
    
class CrearJugador:
    '''
        Esta clase representa la creacion del jugador.
        La instrucción imprimir únicamente tiene como parámetro una cadena
    '''

    def __init__(self, fila, tipo,id) :
        self.fila = fila
        self.tipo = tipo
        self.id=id

class IdFuncionJuego() :
    '''
        Esta clase representa el id de las funciones del juego.
        La instrucción mientras recibe como parámetro una expresión lógica y la lista
        de instrucciones a ejecutar si la expresión lógica es verdadera.
    '''
    def __init__(self, id) :
        self.id=id

class IdJuego() :
    '''
        Esta clase representa un identificador del juego
    '''
    def __init__(self, id = "") :
        self.id = id