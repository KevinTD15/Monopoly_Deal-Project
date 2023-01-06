from Juego.juegoMD import *
from Jugador.jugador import *
from PLN.crearCarta import CrearCarta
from dsl.gramatica import parse as Parse
import dsl.ts as TS
from dsl.expresiones import *
from dsl.instrucciones import *
from dsl.juego import *

TSFunciones =  TS.TablaDeSimbolos({})
filaError = -1
#pila = [] #tratamiento de retornos

def procesar_funcionLLam(instr, ts) :
    global filaError
    filaError = instr.fila
    ts_local = TS.TablaDeSimbolos({}) 
    if instr.id in TSFunciones.simbolos :
        p = TSFunciones.simbolos[instr.id].valor[0]
        l1=l2=1
        if(p[0] == None): l1=0
        if (instr.param==None): l2=0
        if(l1 == 0 and l2 == 0):
            pass
        elif (len(p)==len(instr.param)):
            for j in range(len(p)):
                val  = resolver_cadena(instr.param[j], ts)
                simbolo = TS.Simbolo(p[j] , val)
                ts_local.asignar(simbolo, TSFunciones, filaError)
        else:
            error(f'Lista argumentos de la funcion \'{instr.id}\' no coincide con su declaracion')
        instrucciones = TSFunciones.simbolos[instr.id].valor[1]
        val=procesar_instrucciones(instrucciones, ts_local, True)
        if(val != None):
            return val
    elif isinstance(instr.id,IdFuncionJuego): #esta instancia me dice que el id corresponde a una funcion definida en el juego
        juego=ts.obtener('jmpd', filaError).valor
        if  instr.id.id=='reestablecer':
            juego.Reestablecer()         
        elif instr.id.id=='ejecutar' :
            juego.EjecutarTurnoMD()
        elif instr.id.id=='carta' :
            CrearCarta(instr.param)
    else:
        error(f'Funcion \'{instr.id}\' no esta definida')

def procesar_retorno(instr,ts):
    global filaError
    #global pila
    filaError = instr.fila
    return resolver_cadena(instr.exp, ts)
 
def procesar_agregarElem(instr,ts):
    global filaError
    filaError = instr.fila
    val=resolver_cadena(instr.exp, ts)    
    if isinstance(instr.id,IdJuego): #esta instancia me dice que el id corresponde a una lista definida en el juego
        juego=ts.obtener('jmpd', filaError).valor
        if instr.id.id == 'notificaciones':
            ts.agregarElemJuego(instr.id.id, juego.notificaciones,val)
        elif instr.id.id == 'jugadores':
            ts.agregarElemJuego(instr.id.id, juego._jugadores,val)
    else:
        ts.agregarElem(instr.id,val, filaError)
  
def procesar_eliminarElem(instr,ts):
    global filaError
    filaError = instr.fila
    val=resolver_cadena(instr.exp, ts)    
    if isinstance(instr.id,IdJuego): #esta instancia me dice que el id corresponde a una lista definida en el juego
        juego=ts.obtener('jmpd', filaError).valor
        if instr.id.id == 'notificaciones':
            ts.eliminarElemListJuego(instr.id.id,juego.notificaciones,val, filaError)
        elif instr.id.id == 'jugadores':
            ts.eliminarElemListJuego(instr.id.id,juego._jugadores,val, filaError)
    else:
        ts.eliminarElem(instr.id,val, filaError)
  
def procesar_funcionDecl(instr, ts, funcAnidada=False) :
    global filaError
    if(funcAnidada):
        error('No se pueden crear metodos dentro de otros')
    
    filaError = instr.fila
    simbolo = TS.Simbolo(instr.id, (instr.param,instr.instrucciones))
    TSFunciones.asignar(simbolo, ts, filaError)

def procesar_imprimir(instr, ts) :
    global filaError
    filaError = instr.fila
    print('mpd> ', resolver_cadena(instr.cad, ts))

def procesar_asignacion(instr, ts) :
    global filaError
    filaError = instr.fila
    val = resolver_cadena(instr.exp, ts)
    if isinstance(instr.id, ExpresionLista):
        elemList= instr.id
        indice = resolver_cadena(elemList.exp, ts)
        ts.asignarElemList(elemList.id, indice, val, filaError) #asignar valor a un elemento de la lista
    else:
        simbolo = TS.Simbolo(instr.id, val)
        ts.asignar(simbolo, TSFunciones, filaError)    

def procesar_while(instr, ts) :
    global filaError
    filaError = instr.fila
    while resolver_expresion_logica(instr.expLogica, ts) :
        val = procesar_instrucciones(instr.instrucciones, ts)
        if val!= None:
            return val

def procesar_if(instr, ts) :
    global filaError
    filaError = instr.fila
    val = resolver_expresion_logica(instr.expLogica, ts)
    if val :
        val=procesar_instrucciones(instr.instrucciones, ts)
        if val!=None:
            return val
        
def procesar_if_else(instr, ts) :
    global filaError
    filaError = instr.fila
    val = resolver_expresion_logica(instr.expLogica, ts)
    if val :
        val = procesar_instrucciones(instr.instrIfVerdadero, ts)
    else :
         val = procesar_instrucciones(instr.instrIfFalso, ts)
    if val!= None:
        return val

def procesar_crearjuego(instr, ts):
    simbolo = TS.Simbolo('jmpd' , JuegoMD())
    ts.asignar(simbolo, TSFunciones, filaError)

def procesar_comenzarjuego(instr, ts):
    juego=ts.obtener('jmpd', filaError).valor
    juego.EjecutarJuego()

def procesar_crearjugador(instr, ts):
    global filaError
    filaError = instr.fila
    tip = instr.tipo
    id = instr.id
    if(tip == 'aleatorio'):
        simbolo = TS.Simbolo(id , JugadorAleatorio(id, True) )
        ts.asignar(simbolo, TSFunciones, filaError)
    elif(tip == 'inteligenteBasico'):
        simbolo = TS.Simbolo(id , JugadorInteligente1(id, True) )
        ts.asignar(simbolo, TSFunciones, filaError)
    elif(tip == 'inteligenteProbabilistico'):
        simbolo = TS.Simbolo(id , JugadorInteligente(id, True)  )
        ts.asignar(simbolo, TSFunciones, filaError)
    elif(tip == 'inteligenteMejorado'):
        simbolo = TS.Simbolo(id , JugadorInteligente2(id, True)  )
        ts.asignar(simbolo, TSFunciones, filaError)

def resolver_cadena(expCad, ts) :
    if isinstance(expCad, ExpresionConcatenar) :
        exp1 = resolver_cadena(expCad.exp1, ts)
        exp2 = resolver_cadena(expCad.exp2, ts)
        if type(exp1)!=str: exp1=str(exp1)
        if type(exp2)!=str: exp2=str(exp2)
        return exp1 + exp2
    elif isinstance(expCad, ExpresionDobleComilla) :
        return expCad.exp
    elif isinstance(expCad, ExpresionCadenaNumerica) :
        if type(expCad.exp) == str:
            return expCad.exp
        return resolver_expresion_aritmetica(expCad.exp, ts)
    else :
        return resolver_expresion_aritmetica(expCad, ts)

def resolver_expresion_logica(expLog, ts) :
    exp1 = resolver_cadena(expLog.exp1, ts)
    exp2 = resolver_cadena(expLog.exp2, ts)
    if expLog.operador == OPERACION_LOGICA.MAYOR_QUE : return exp1 > exp2
    if expLog.operador == OPERACION_LOGICA.MENOR_QUE : return exp1 < exp2
    if expLog.operador == OPERACION_LOGICA.IGUAL : return exp1 == exp2
    if expLog.operador == OPERACION_LOGICA.DIFERENTE : return exp1 != exp2

def resolver_expresion_aritmetica(expNum, ts) :
    if isinstance(expNum, ExpresionBinaria) :
        exp1 = resolver_expresion_aritmetica(expNum.exp1, ts)
        exp2 = resolver_expresion_aritmetica(expNum.exp2, ts)
        if type(exp1)==str or type(exp2)==str:
            error('Operacion aritmetica, inconsistencia de datos')
        if expNum.operador == OPERACION_ARITMETICA.MAS : return exp1 + exp2
        if expNum.operador == OPERACION_ARITMETICA.MENOS : return exp1 - exp2
        if expNum.operador == OPERACION_ARITMETICA.POR : return exp1 * exp2
        if expNum.operador == OPERACION_ARITMETICA.DIVIDIDO : return exp1 / exp2
    elif isinstance(expNum, ExpresionNumero) :
        return expNum.exp
    elif isinstance(expNum, ExpresionIdentificador) : #aqui ver en el expNum si es de tipo ExpresionLista ent
        if isinstance(expNum.id, ExpresionLista):
            elemList= expNum.id
            indice = resolver_cadena(elemList.exp, ts)
            if  isinstance(elemList.id,IdJuego):
                juego=ts.obtener('jmpd', filaError).valor
                if elemList.id.id == 'notificaciones':
                    if expNum.id.atributo!=None:
                        error('Nofiticaciones no tiene atributo')
                    return ts.obtenerElemListJuego(elemList.id.id, juego.notificaciones, indice, filaError)
                elif elemList.id.id == 'jugadores':
                    if expNum.id.atributo==None:
                        return ts.obtenerElemListJuego(elemList.id.id, juego._jugadores, indice, filaError)
                    elif expNum.id.atributo == 'nombre':
                        ts.obtenerElemListJuego(elemList.id.id, juego._jugadores, indice, filaError)
                        return juego._jugadores[indice].nombre
            return ts.obtenerElemList(elemList.id,indice, filaError)
        elif  isinstance(expNum.id,IdJuego): #el identificador esta definido en el juego
            juego=ts.obtener('jmpd', filaError).valor
            if expNum.id.id == 'ganador':
                return juego.ganador
            elif expNum.id.id == 'notificaciones':  #cuando el trabajo no es con lista es porque se le esta haciendo len()
                return juego.notificaciones
            elif expNum.id.id == 'jugadores':
                return juego._jugadores
            elif expNum.id.id == 'finalJuego':
                return juego.final
        return ts.obtener(expNum.id, filaError).valor

    elif isinstance(expNum, Funcion) :
        return procesar_funcionLLam(expNum, ts)
    elif isinstance(expNum, ExpresionListaVacia) :
        return []
    elif isinstance(expNum, Len) :
        exp = resolver_cadena(expNum.cad, ts) # expresionCadenaNum
        return len(exp)
    else:   
        error('Cadena no válida')
    
def error(cad):
    global filaError
    print(f'mpd> Error en línea {filaError}:  {cad}')  
    exit()
    
def procesar_instrucciones(instrucciones, ts, funcAnidada=False) :
    if instrucciones==None: 
        error('No existen instrucciones definidas en el bloque')
    else:
        val_retorno=None
        for instr in instrucciones :
            if isinstance(instr, Imprimir) : procesar_imprimir(instr, ts)
            elif isinstance(instr, Asignacion) : procesar_asignacion(instr, ts)
            elif isinstance(instr, While) : val_retorno= procesar_while(instr, ts)
            elif isinstance(instr, If) :  val_retorno=procesar_if(instr, ts)
            elif isinstance(instr, IfElse) : val_retorno= procesar_if_else(instr, ts)
            
            elif isinstance(instr, FuncionDecl) : procesar_funcionDecl(instr, ts, funcAnidada)
            elif isinstance(instr, Funcion) : procesar_funcionLLam(instr, ts)
            elif isinstance(instr, Retorno) : return procesar_retorno(instr, ts)
            elif isinstance(instr, AgregarElemLista) : procesar_agregarElem(instr, ts)
            
            elif isinstance(instr, EliminarElemLista) : procesar_eliminarElem(instr, ts)
            elif isinstance(instr, CrearJuego) : procesar_crearjuego(instr, ts) 
            elif isinstance(instr, CrearJugador) : procesar_crearjugador(instr, ts)       
            else :  
                error('Instrucción no válida')
            if val_retorno!=None:
                return val_retorno

def inicia(input):
    instrucciones = Parse(input)
    ts_global = TS.TablaDeSimbolos()
    procesar_instrucciones(instrucciones, ts_global)