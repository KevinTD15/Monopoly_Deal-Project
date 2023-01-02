from Juego.juegoMD import *
from Jugador.jugador import *
from PLN.crearCarta import CrearCarta
import dsl.gramatica as g
import dsl.ts as TS
from dsl.expresiones import *
from dsl.instrucciones import *
from dsl.juego import *

TSFunciones =  TS.TablaDeSimbolos({})
filaError = -1

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
                ts_local.asignar(simbolo, filaError)
        else:
            error(f'Lista argumentos de la funcion \'{instr.id}\' no coincide con su declaracion')
        instrucciones = TSFunciones.simbolos[instr.id].valor[1]
        procesar_instrucciones(instrucciones, ts_local)
        if 'retorno' in ts_local.simbolos:          
            val = ts_local.obtener('retorno', filaError).valor
            ts_local.eliminar('retorno', filaError)
            return val
    elif isinstance(instr.id,IdFuncionJuego): #esta instancia me dice que el id corresponde a una funcion definida en el juego
        juego=ts.obtener('jmpd', filaError).valor
        if  instr.id.id=='Reestablecer':
            juego.Reestablecer()         
        elif instr.id.id=='EjecutarTurno' :
            juego.EjecutarTurnoMD()
        elif instr.id.id=='carta' :
            CrearCarta(instr.param)
    else:
        error(f'Funcion \'{instr.id}\' no esta definida')

def procesar_retorno(instr,ts):
    global filaError
    filaError = instr.fila
    val=resolver_cadena(instr.exp, ts)
    simbolo = TS.Simbolo('retorno' , val )
    ts.asignar(simbolo, filaError)

def procesar_agregarElem(instr,ts):
    global filaError
    filaError = instr.fila
    val=resolver_cadena(instr.exp, ts)    
    if isinstance(instr.id,IdJuego): #esta instancia me dice que el id corresponde a una lista definida en el juego
        juego=ts.obtener('jmpd', filaError).valor
        if instr.id.id == 'notificaciones':
            ts.agregarElemJuego(juego.notificaciones,val)
        elif instr.id.id == 'jugadores':
            ts.agregarElemJuego(juego._jugadores,val)
    else:
        ts.agregarElem(instr.id,val, filaError)
  
def procesar_funcionDecl(instr, ts) :
    global filaError
    filaError = instr.fila
    simbolo = TS.Simbolo(instr.id, (instr.param,instr.instrucciones))
    TSFunciones.asignar(simbolo, filaError)

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
        ts.asignar(simbolo, filaError)    

def procesar_while(instr, ts) :
    global filaError
    filaError = instr.fila
    while resolver_expresion_logica(instr.expLogica, ts) :
        procesar_instrucciones(instr.instrucciones, ts)

def procesar_if(instr, ts) :
    global filaError
    filaError = instr.fila
    val = resolver_expresion_logica(instr.expLogica, ts)
    if val :
        procesar_instrucciones(instr.instrucciones, ts)

def procesar_if_else(instr, ts) :
    global filaError
    filaError = instr.fila
    val = resolver_expresion_logica(instr.expLogica, ts)
    if val :
        procesar_instrucciones(instr.instrIfVerdadero, ts)
    else :
        procesar_instrucciones(instr.instrIfFalso, ts)

def procesar_crearjuego(instr, ts):
    simbolo = TS.Simbolo('jmpd' , JuegoMD())
    ts.asignar(simbolo, filaError)

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
        ts.asignar(simbolo, filaError)
    elif(tip == 'inteligenteBasico'):
        simbolo = TS.Simbolo(id , JugadorInteligente1(id, True) )
        ts.asignar(simbolo, filaError)
    elif(tip == 'inteligenteProbabilistico'):
        simbolo = TS.Simbolo(id , JugadorInteligente(id, True)  )
        ts.asignar(simbolo, filaError)
    elif(tip == 'inteligenteMejorado'):
        simbolo = TS.Simbolo(id , JugadorInteligente2(id, True)  )
        ts.asignar(simbolo, filaError)

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
    exp1 = resolver_expresion_aritmetica(expLog.exp1, ts)
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
                    return juego.notificaciones[indice]
                elif elemList.id.id == 'jugadores':
                    if expNum.id.atributo==None:
                        return juego._jugadores[indice]
                    elif expNum.id.atributo == 'nombre':
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
    
def procesar_instrucciones(instrucciones, ts) :
    if instrucciones==None: 
        error('No existen instrucciones definidas en el bloque')
    else:
        for instr in instrucciones :
            if isinstance(instr, Imprimir) : procesar_imprimir(instr, ts)
            elif isinstance(instr, Asignacion) : procesar_asignacion(instr, ts)
            elif isinstance(instr, While) : procesar_while(instr, ts)
            elif isinstance(instr, If) : procesar_if(instr, ts)
            elif isinstance(instr, IfElse) : procesar_if_else(instr, ts)
            
            elif isinstance(instr, FuncionDecl) : procesar_funcionDecl(instr, ts)
            elif isinstance(instr, Funcion) : procesar_funcionLLam(instr, ts)
            elif isinstance(instr, Retorno) : procesar_retorno(instr, ts)
            elif isinstance(instr, AgregarElemLista) : procesar_agregarElem(instr, ts)
            elif isinstance(instr, CrearJuego) : procesar_crearjuego(instr, ts) 
            elif isinstance(instr, CrearJugador) : procesar_crearjugador(instr, ts)       
            else :  
                error('Instrucción no válida')

def inicia(input):
    instrucciones = g.parse(input)
    ts_global = TS.TablaDeSimbolos()
    procesar_instrucciones(instrucciones, ts_global)