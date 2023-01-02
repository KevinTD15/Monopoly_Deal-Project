from enum import Enum

class Simbolo() :
    'Esta clase representa un simbolo dentro de nuestra tabla de simbolos'

    def __init__(self, id, valor) :
        self.id = id
        self.valor = valor

class TablaDeSimbolos() :
    'Esta clase representa la tabla de simbolos (TS)'
    
    filaError = -1

    def __init__(self, simbolos = {}) :
        self.simbolos = simbolos

    def chequeaIDenTS(self,id, filaError):
        'chequea si id existe en la TS, en ese caso muestra error e interrumpe la ejecucion'
        if not id in self.simbolos :
            self.error(f'Variable \'{id}\' no definida', filaError)

    def obtener(self, id, filaError) :
        self.chequeaIDenTS(id, filaError)
        return self.simbolos[id]

    def asignar(self, simbolo, filaError) :
        if id in self.simbolos :
            if type(self.simbolos.valor)!=type(simbolo.valor):
                self.error(f'Variable \'{id}\' inconsistente' , filaError)   
        self.simbolos[simbolo.id] = simbolo

    def eliminar(self, id, filaError): 
        'Solo se utiliza para eliminar entrada en la TS de id=\'retorno\' una vez terminada ejecucion de la funcion (simulando pop de pila)'
        self.chequeaIDenTS(id, filaError)
        del self.simbolos[id]

    #region Tratamiento de listas
    def agregarElem(self, id, val, filaError) :
        self.chequeaIDenTS(id, filaError)
        if (type(self.simbolos[id].valor) != list):
            self.error(f'Variable \'{id}\' no es una lista', filaError)
        self.simbolos[id].valor.append(val)

    def eliminarElem(self, id, indice, filaError) :
        self.chequeaIDenTS(id, filaError)
        self.simbolos[id].valor[indice]

    def asignarElemList(self, id, indice,val, filaError) :
        self.chequeaIDenTS(id, filaError) 
        if indice>= len(self.simbolos[id].valor):
            self.error(f'Lista \'{id}\' indice \'{indice}\' fuera de rango', filaError)                 
        self.simbolos[id].valor[indice]=val

    def obtenerElemList(self, id, indice, filaError) :
        self.chequeaIDenTS(id, filaError) 
        if indice>= len(self.simbolos[id].valor):
            self.error(f'Lista \'{id}\' indice \'{indice}\' fuera de rango', filaError)                  
        return self.simbolos[id].valor[indice]
    #endregion
    #region Tratamiento de las listas que estan definidas en el juego, no en el DSL
    def agregarElemJuego(self, id, val) :
        'Agregar elemento a una lista definida en el juego'
        id.append(val)

    def obtenerElemListJuego(self, id, indice, filaError) :
        'Obtener elemento de una lista definida en el juego'
        if indice>= len(id):
            self.error(f'Lista \'{id}\' indice \'{indice}\' fuera de rango', filaError)          
        return id[indice]

    def asignarElemListJuego(self, id, indice,val, filaError) :
        'Asignar un valor a una posicion de una lista definida en el juego'
        if indice>= len(id):
            self.error(f'Lista \'{id}\' indice \'{indice}\' fuera de rango', filaError)  
        id[indice]=val
    #endregion            
    def error(self, cad, fila):
        print(f'mpd> Error en línea {fila}: {cad}')  
        exit()
        
