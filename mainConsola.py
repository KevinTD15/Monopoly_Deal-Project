from Juego.juegoMD import *
from Jugador.jugadorMD import *
from PLN.crearCarta import CrearCarta
import threading
import time

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
    elif(tipo == 'Montecarlo'):
        return JugadorMontecarlo(nombre, True)
    
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
    mc = juego.turnosJugadorMC * 3 * 30
    print (f'Jugador Montecarlo jugo {juego.turnosJugadorMC} veces por tanto se ejecutaron {mc} juegos extra al aplicar algoritmo Montecarlo.')
    

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
        while(not (cj.isdigit() and int(cj) >= 2 and int(cj) <= 5)):       
            print('Teclee cantidad de jugadores entre 2 y 5')
            cj = input()

        for i in range(int(cj)):
            t=''
            while t != 'Aleatorio' and t != 'Inteligente' and t != 'Inteligente1' and t!= 'Inteligente2' and t!= 'Montecarlo':
                print(f'Teclee el nombre y tipo del jugador {i}')
                n = input().split(' ')
                if(len(n)>1 and (n[1] == 'Aleatorio' or n[1] == 'Inteligente' or n[1] == 'Inteligente1' or n[1] == 'Inteligente2' or n[1] == 'Montecarlo')):
                    t = n[1]
                    j._jugadores.append(CrearJugador(n[0], t)) 
                    break
                    
        while(not cp.isdigit()):        
            print('Teclee cantidad de partidas a ejecutar')
            cp = input()   
             
        #evento = threading.Event()
        #hilo = threading.Thread(target=mytimer, args=(j,),)
        #hilo.start()

        dic = CrearTabla(j)
        resumen = j.EjecutarSimulacion(dic, int(cp))
        ImprimirResumen(resumen)
        
        print('''Teclee
              1- Salir
              2- Volver a ejecutar''')
        fin = input()

def mytimer(j):
    global idnotificacion
    if idnotificacion < len(j.notificaciones):
        while (j.notificaciones[idnotificacion] != 'FIN DEL JUEGO'):
            if idnotificacion < len(j.notificaciones):
                if j.notificaciones[idnotificacion][0:5] == 'Turno':
                    print( f'{idnotificacion} ' + j.notificaciones[idnotificacion])
                idnotificacion += 1
            else:
                time.sleep(3)
        print(f'{idnotificacion} ' + j.notificaciones[idnotificacion])
    

if __name__ == '__main__':
    main()