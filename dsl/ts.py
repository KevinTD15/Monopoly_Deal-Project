from enum import Enum

class Simbolo() :
    'Esta clase representa un simbolo dentro de nuestra tabla de simbolos'

    def __init__(self, id, valor) :
        self.id = id
        self.valor = valor

class TablaDeSimbolos() :
    'Esta clase representa la tabla de simbolos'

    def __init__(self, simbolos = {}) :
        self.simbolos = simbolos

    def siIDenTS(self,id):
        if not id in self.simbolos :
            print('mpd> Error: variable ', id, ' no definida')
            exit() 
        return True

    def obtener(self, id) :
        if self.siIDenTS(id):
            return self.simbolos[id]
        return

    def asignar(self, simbolo) :
        if id in self.simbolos :
            if type(self.simbolos.valor)!=type(simbolo.valor):
                print('mpd> Error: variable ', id, ' inconsistente' )
                exit()     
        self.simbolos[simbolo.id] = simbolo

    def eliminar(self, id):
        if self.siIDenTS(id):
            del self.simbolos[id]

    def agregarElem(self, id, val) :
        if self.siIDenTS(id):
            self.simbolos[id].valor.append(val)

    def eliminarElem(self, id, indice) :
        if self.siIDenTS(id):
            self.simbolos[id].valor[indice]

    def asignarElemList(self, id, indice,val) :
        if self.siIDenTS(id): 
            if indice>= len(self.simbolos[id].valor):
                print('mpd> Error: lista ', id, ' indice ',indice, 'fuera de rango')  
                exit() 
            else:
                self.simbolos[id].valor[indice]=val

    def obtenerElemList(self, id, indice) :
        if self.siIDenTS(id): 
            if indice>= len(self.simbolos[id].valor):
                print('mpd> Error: lista ', id, ' indice ',indice, 'fuera de rango')  
                exit() 
            else:
                return self.simbolos[id].valor[indice]

    def agregarElemJuego(self, id, val) :
            id.append(val)

    def obtenerElemListJuego(self, id, indice) :
        if indice>= len(id):
            print('mpd> Error: lista ', id, ' indice ',indice, 'fuera de rango')  
            exit() 
        return id[indice]

    def asignarElemListJuego(self, id, indice,val) :
        if indice>= len(id):
                print('mpd> Error: lista ', id, ' indice ',indice, 'fuera de rango')  
                exit() 
        else:
            id[indice]=val
