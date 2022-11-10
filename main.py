from juegoMD import *
from jugador import *
import threading
import time
from colorama import init, Fore
idnotificacion = 0

def main():
    j = JuegoMD()
    j1 = JugadorAleatorio('pepe', True)
    j2 = JugadorAleatorio('jose', True)
    j3 = JugadorAleatorio('cucu', True)
    j4 = JugadorAleatorio('fifi', True)
    j5 = JugadorAleatorio('popo', True)
    j._jugadores.append(j1)
    j._jugadores.append(j2)
    j._jugadores.append(j3)
    #j._jugadores.append(j4)
    #j._jugadores.append(j5)
    #j.notificaciones.append('COMIENZO DEL JUEGO')
    
    init() #para dar color a los cambios de turno
    #evento = threading.Event()8888
    #hilo = threading.Thread(target=mytimer, args=(j,),)
    #hilo.start()

    for i in range(1000):
        j.notificaciones.append('COMIENZO DEL JUEGO')
        j.EjecutarJuego()
        j.notificaciones.append('FIN DEL JUEGO')
        for i in j.notificaciones:
            print(i)
    a = 5
    #evento.clear()

    for i in j.notificaciones:
        print(i)
    
def mytimer(j):
    global idnotificacion
    while (j.notificaciones[idnotificacion] != 'FIN DEL JUEGO'):
        if idnotificacion < len(j.notificaciones):
            color = Fore.WHITE
            if j.notificaciones[idnotificacion][0:5] == 'Turno':
                color = Fore.RED
            print( color + f'{idnotificacion} ' + j.notificaciones[idnotificacion])
            idnotificacion += 1
        else:
            time.sleep(3)
    print(Fore.BLUE + f'{idnotificacion} ' + j.notificaciones[idnotificacion])
    
if __name__ == '__main__':
    main()