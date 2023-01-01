from Juego.juegoMD import *
from Jugador.jugadorMD import *
from PLN.crearCarta import CrearCarta
import threading
import time
from colorama import init, Fore
idnotificacion = 0

def CrearJugador(nombre, tipo):
    if(tipo == 'Inteligente'):
        return JugadorInteligente(nombre, True)
    elif(tipo == 'Inteligente1'):
        return JugadorInteligente1(nombre, True)
    elif(tipo == 'Inteligente2'):
        return JugadorInteligente2(nombre, True)
    elif(tipo == 'Aleatorio'):
        return JugadorAleatorio(nombre, True)

def CrearTabla(j):
    dic = {}
    for i in j._jugadores:
        dic[i.nombre] = 0
    dic['Nadie'] = 0
    return dic
    
def ImprimirResumen(resumen):
    print('\nRESUMEN DE PARTIDAS')
    for i in resumen:
        if(i != 'Nadie'):
            print(f'{i} tiene {resumen[i]} victorias')

def EjecutarSimulacion(j, dic, cp):
    total = 0
    for i in range(cp):
        j.notificaciones.append('COMIENZO DEL JUEGO')
        j.EjecutarJuego()       
        dic[j.ganador] += 1
        total += 1
        j.notificaciones.append(f'Gano: {j.ganador} en {j.count} turnos')
        j.notificaciones.append('FIN DEL JUEGO')
        for i in j.notificaciones:
            print(i)
    return dic

def main():
    fin = '2'
   
    while(fin == '2'):
        j = JuegoMD()
        lj = []
        tj = []
        inp = '0'
        inp1 = '0'
        inp2 = 'a'
        cj = '0'
        cp = 'a'
        while(not(inp == '1' or inp == '2')):
            print('''Desea añadir cartas nuevas al juego
                  1- Si
                  2- No''')
            inp = input()
        if(inp == '1'):
            while(not(inp1 == '1' or inp1 == '2')):
                print('''De donde desea añadirlas
                      1- Consola
                      2- txt''')
                inp1 = input()
            if(inp1 == '1'):
                while(not inp2.isdigit()):
                    print('Cuantas desea añadir')
                    inp2 = input()
                for i in range(int(inp2)):
                    print('Teclee la carta que desee')
                    carta = input()
                    sms = CrearCarta(carta)
                    print(sms)
            # elif(inp1 == 2):
            #     print('Teclee ubicacion del .txt')
            #     path = input()
        while(not (cj.isdigit() and int(cj) >= 2 and int(cj) <= 5)):       
            print('Teclee cantidad de jugadores entre 2 y 5')
            cj = input()
        for i in range(int(cj)):
            t=''
            while t != 'Aleatorio' or t != 'Inteligente' or t != 'Inteligente1' or t!= 'Inteligente2':
                print(f'Teclee el nombre y tipo del jugador {i}')
                n = input().split(' ')
                if(len(n)>1 and (n[1] == 'Aleatorio' or n[1] == 'Inteligente' or n[1] == 'Inteligente1' or n[1] == 'Inteligente2')):
                    t = n[1]
                    j._jugadores.append(CrearJugador(n[0], t)) 
                    break
                    
        while(not cp.isdigit()):        
            print('Telcee cantidad de partidas a ejecutar')
            cp = input()    

        init() #para dar color a los cambios de turno
        #evento = threading.Event()
        #hilo = threading.Thread(target=mytimer, args=(j,),)
        #hilo.start()

        dic = CrearTabla(j)
        resumen = EjecutarSimulacion(j, dic, int(cp))
        ImprimirResumen(resumen)
        
        print('''Teclee
              1- Salir
              2- Volver a ejecutar''')
        fin = input()

    #evento.clear()

    #for i in j.notificaciones:
    #    print(i)
    
# def mytimer(j):
#     global idnotificacion
#     while (j.notificaciones[idnotificacion] != 'FIN DEL JUEGO'):
#         if idnotificacion < len(j.notificaciones):
#             color = Fore.WHITE
#             if j.notificaciones[idnotificacion][0:5] == 'Turno':
#                 color = Fore.RED
#             print( color + f'{idnotificacion} ' + j.notificaciones[idnotificacion])
#             idnotificacion += 1
#         else:
#             time.sleep(3)
#     print(Fore.BLUE + f'{idnotificacion} ' + j.notificaciones[idnotificacion])
 
# j1 = JugadorAleatorio('pepe', True)
    # j2 = JugadorAleatorio('jose', True)
    # j3 = JugadorAleatorio('cucu', True)
    # j4 = JugadorAleatorio('fifi', True)
    # j5 = JugadorAleatorio('popo', True)
    # j6 = JugadorInteligente('kevin', True)
    # j7 = JugadorInteligente('mapa', True)
    # j8 = JugadorInteligente('mama', True)
    # j9 = JugadorInteligente('aya', True)
    # j0 = JugadorInteligente('tala', True)
    # j._jugadores.append(j6)
    # j._jugadores.append(j7)
    # j._jugadores.append(j8)
    # j._jugadores.append(j9)
    # j._jugadores.append(j0)
    # #j._jugadores.append(j5)
    # j._jugadores.append(j2) 
    
if __name__ == '__main__':
    main()