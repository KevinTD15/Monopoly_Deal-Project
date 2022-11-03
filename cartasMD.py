import enum
from abc import ABC, abstractclassmethod

class Cartas:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    
class Propiedades(Cartas):
    def __init__(self, nombre, tipo, color : list, cantGrupo, renta : list, valor = None):
        Cartas.__init__(self, nombre, tipo)
        self.color = color
        self.valor = valor
        self.cantGrupo = cantGrupo
        self.renta = renta
    
    def print(self):
        print(f'''El nombre es: {self.nombre} \n
              El tipo es {self.tipo} \n
              el color es: {self.color[0]} \n''')

class Dinero(Cartas):
    def __init__(self, nombre, tipo):
        Cartas.__init__(self, nombre, tipo)

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
        
class AccionConstruccion(Accion):
    def __init__(self, nombre, tipo, subtipo, valor, construccion, monto): #monto es cuanto da la casa
        super().__init__(nombre, tipo, subtipo, valor)
        self.construccion = construccion
        self.monto = monto

class AccionRapida(Accion):
    def __init__(self, nombre, tipo, subtipo, valor, turno : bool): #turno es si se juega la carta en tu turno o en el del contrario 
        super().__init__(nombre, tipo, subtipo, valor)
        self.turno = turno

class AccionRobarCarta(Accion):
    def __init__(self, nombre, tipo, subtipo, valor, cantCartasATomar):
        super().__init__(nombre, tipo, subtipo, valor)
        self.cantCartasATomar = cantCartasATomar
        
class AccionRobarPropiedad(Accion):
    def __init__(self, nombre, tipo, subtipo, valor, intercambio : bool, cuantas = None):
        super().__init__(nombre, tipo, subtipo, valor)
        self.intercambio = intercambio
        self.cuantas = cuantas #si cuantas es none es que lo roba todo
        

#test
tenese = Propiedades('tenese', 'propiedad', ['anaranjado'], 3, [1,3,5], 2)
casa = AccionConstruccion('casa1', 'accion', 'construccion', 3, 'casa', 3)
renta = AccionRenta('renta1', 'accion', 'renta', 4,['verde', 'azul'], True)
robar = AccionRobarCarta('go', 'accion', 'robarcarta', 3, 2)
diqno = AccionRapida('diqno', 'accion', 'rapida', 5, True)
factordecisivo = AccionRobarPropiedad('fd', 'accion', 'robarprop',  5, False)

cartas : Cartas = [tenese, casa, renta, robar, diqno, factordecisivo]
print(cartas)


