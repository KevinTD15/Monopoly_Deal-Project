from dsl.interprete import inicia
def main():
    f = open("dsl/Ejemplos/juegoMD.mpd", "r")
    input = f.read()
    inicia(input)
    
if __name__ == '__main__':
    main()