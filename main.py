from juegoMD import *
from jugador import *
import threading

idnotificacion = 0

def mytimer(j):
    global idnotificacion
    if (idnotificacion < len(j.notificaciones)):
        print(j.notificaciones[idnotificacion])
        idnotificacion += 1

def main():
    j = JuegoMD()
    j1 = JugadorAleatorio('pepe', True)
    j2 = JugadorAleatorio('jose', True)
    j._jugadores.append(j1)
    j._jugadores.append(j2)
    j.notificaciones.append('COMIENZO DEL JUEGO')
    j.EjecutarJuego()
    j.notificaciones.append('FIN DEL JUEGO')
    for i in j.notificaciones:
        print(i)
    
if __name__ == '__main__':
    main()