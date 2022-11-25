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
    j6 = JugadorInteligente('kevin', True)
    j7 = JugadorInteligente('mapa', True)
    j8 = JugadorInteligente('mama', True)
    j9 = JugadorInteligente('aya', True)
    j0 = JugadorInteligente('tala', True)
    j._jugadores.append(j6)
    j._jugadores.append(j7)
    j._jugadores.append(j8)
    j._jugadores.append(j9)
    j._jugadores.append(j0)
    #j._jugadores.append(j5)
    j._jugadores.append(j2)
    #j.notificaciones.append('COMIENZO DEL JUEGO')
    
    init() #para dar color a los cambios de turno
    #evento = threading.Event()
    #hilo = threading.Thread(target=mytimer, args=(j,),)
    #hilo.start()
    dic = {}
    total = 0
    for i in j._jugadores:
        dic[i.nombre] = 0
    dic['Nadie'] = 0
    
    for i in range(400):
        j.notificaciones.append('COMIENZO DEL JUEGO')
        j.EjecutarJuego()       
        dic[j.ganador] += 1
        total += 1
        j.notificaciones.append(f'Gano: {j.ganador} en {j.count} turnos')
        j.notificaciones.append('FIN DEL JUEGO')
        for i in j.notificaciones:
            print(i)
            
    print('\nRESUMEN DE PARTIDAS')
    for i in dic:
        if(i != 'Nadie'):
            print(f'{i} tiene {dic[i]} victorias')
    #evento.clear()

    #for i in j.notificaciones:
    #    print(i)
    
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