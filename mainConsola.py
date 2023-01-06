from Juego.juegoMD import *
from Jugador.jugadorMD import *
from PLN.crearCarta import CrearCarta

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

        dic = CrearTabla(j)
        resumen = EjecutarSimulacion(j, dic, int(cp))
        ImprimirResumen(resumen)
        
        print('''Teclee
              1- Salir
              2- Volver a ejecutar''')
        fin = input()

if __name__ == '__main__':
    main()