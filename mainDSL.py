from dsl.interprete import inicia
import os

def main():
    print('Teclee direccion de archivo \'.mpd\'')
    pathInput = input()
    if(pathInput != ''):
        path = pathInput
    else:
        path = "dsl/Ejemplos/juegoMD.mpd"
        
    if not os.path.isfile(path) :
        print('Archivo no existe')
    elif not path.endswith('.mpd'):
        print('Archivo no es \'mpd\'')
    else:
        f = open(path, "r")
        texto = f.read()
        inicia(texto)
    
if __name__ == '__main__':
    main()