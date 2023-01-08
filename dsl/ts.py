class Simbolo() :
    'Esta clase representa un simbolo dentro de nuestra tabla de simbolos'

    def __init__(self, id, valor, tipo=0) :
        self.id = id
        self.valor = valor
        self.tipo = tipo 

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

    def asignar(self, simbolo, tsFunciones, filaError) :
        if simbolo.id in tsFunciones.simbolos :
                self.error(f'\'{simbolo.id}\' definido como funcion y variable' , filaError)   
        self.simbolos[simbolo.id] = simbolo

    def eliminar(self, id, filaError): 
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
        self.simbolos[id].valor.pop(indice)

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
    def agregarElemJuego(self, id, lista,  val) :
        'Agregar elemento a una lista definida en el juego'
        lista.append(val)

    def obtenerElemListJuego(self, id, lista, indice, filaError) :
        'Obtener elemento de una lista definida en el juego'
        if indice>= len(lista):
            self.error(f'Lista \'{id}\' indice \'{indice}\' fuera de rango', filaError)          
        return lista[indice]

    def asignarElemListJuego(self, id, lista, indice,val, filaError) :
        'Asignar un valor a una posicion de una lista definida en el juego'
        if indice>= len(lista):
            self.error(f'Lista \'{id}\' indice \'{indice}\' fuera de rango', filaError)  
        lista[indice]=val
        
    def eliminarElemListJuego(self, id, lista, indice, filaError) :
        'Elemento de una lista definida en el juego'
        if indice>= len(lista):
            self.error(f'Lista \'{id}\' indice \'{indice}\' fuera de rango', filaError)          
        return lista.pop(indice)
        
    
    #endregion            
    def error(self, cad, fila):
        print(f'mpd> Error en línea {fila}: {cad}')  
        exit()
        
