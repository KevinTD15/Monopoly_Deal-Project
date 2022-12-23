class Cartas:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    
class Propiedades(Cartas):
    def __init__(self, nombre, tipo, color, cantGrupo : int = None, renta : list = [], valor : int = None):
        Cartas.__init__(self, nombre, tipo)
        self.color = color
        self.valor = valor
        self.cantGrupo = cantGrupo
        self.renta = renta

    def __str__(self):
        return f'tipo: {self.tipo}, nom: {self.nombre}, col: {self.color}, val: {self.valor}, rent: {self.renta}, cantGrup: {self.cantGrupo}'

class Comodin(Cartas):
    def __init__(self, nombre, tipo, color : list, valor : int, enUso = None):
        super().__init__(nombre, tipo)
        self.color = color
        self.valor = valor
        self.enUso = enUso
    
    def __str__(self):
        return f'tipo: {self.tipo}, nom: {self.nombre}, col: {self.color}, val: {self.valor}'

class Dinero(Cartas):
    def __init__(self, nombre, tipo):
        Cartas.__init__(self, nombre, tipo)

    def __str__(self):
        return f'tipo: {self.tipo}, val: {self.nombre}'
    
class Accion(Cartas):
    def __init__(self, nombre, tipo, subtipo, valor):
        Cartas.__init__(self, nombre, tipo)
        self.subtipo = subtipo
        self.valor = valor
        
class AccionRenta(Accion):
    def __init__(self, nombre, tipo, subtipo, valor, propiedades : list, todos : bool):
        super().__init__(nombre, tipo, subtipo, valor)
        self.todos = todos
        self.propiedades = propiedades
        
    def __str__(self):
        return f'tipo: {self.tipo}, subt: {self.subtipo}, nom: {self.nombre}, val: {self.valor}, props: {self.propiedades}, todos: {self.todos}'
    
class AccionConstruccion(Accion):
    def __init__(self, nombre, tipo, subtipo, valor, construccion, monto, colorC = None): #monto es cuanto da la casa
        super().__init__(nombre, tipo, subtipo, valor)
        self.construccion = construccion
        self.monto = monto
        self.colorC = colorC
    
    def __str__(self):
        return f'tipo: {self.tipo}, subt: {self.subtipo}, nom: {self.nombre}, val: {self.valor}, const: {self.construccion}, monto: {self.monto}'

class AccionRapida(Accion):
    def __init__(self, nombre, tipo, subtipo, valor, turno): #turno 1 si es en mi turno, 0 si no y -1 en ambos
        super().__init__(nombre, tipo, subtipo, valor)
        self.turno = turno
    
    def __str__(self):
        return f'tipo: {self.tipo}, subt: {self.subtipo}, nom: {self.nombre}, val: {self.valor}, turno: {self.turno}'

class AccionRobarCarta(Accion):
    def __init__(self, nombre, tipo, subtipo, valor, cantCartasATomar):
        super().__init__(nombre, tipo, subtipo, valor)
        self.cantCartasATomar = cantCartasATomar
    
    def __str__(self):
        return f'tipo: {self.tipo}, subt: {self.subtipo}, nom: {self.nombre}, val: {self.valor}, cant: {self.cantCartasATomar}'
        
class AccionRobarPropiedad(Accion):
    def __init__(self, nombre, tipo, subtipo, valor, intercambio : bool, cuantas = None):
        super().__init__(nombre, tipo, subtipo, valor)
        self.intercambio = intercambio
        self.cuantas = cuantas #si cuantas es none es que lo roba todo
    
    def __str__(self):
        return f'tipo: {self.tipo}, subt: {self.subtipo}, nom: {self.nombre}, val: {self.valor}, inter: {self.intercambio}, cant: {self.cuantas}'
    
class AccionRobarDinero(Accion):
    def __init__(self, nombre, tipo, subtipo, valor, todos : bool, monto : int):
        super().__init__(nombre, tipo, subtipo, valor)
        self.todos = todos
        self.monto = monto
        
    def __str__(self):
        return f'tipo: {self.tipo}, subt: {self.subtipo}, nom: {self.nombre}, val: {self.valor}, cant: {self.todos}, monto: {self.monto}'