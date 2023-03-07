from ast import main
import sys

def num():
    while True:
        numeros=input("Valor: ")
        try:
            numeros=int(numeros)
        except:
            print("valor no aceptado", file=sys.stderr)
        else:
            break
            sys.exit()
    return str(numeros)

def descomponer():
    numeros=num()
    numero=numeros[::-1]
    ceros_izquierda=0
    while True:
        for i in str(numero):
            ceros_izquierda+=1
            print((i.ljust(int(ceros_izquierda),'0')).zfill(len(numero)), "\n")
        if ceros_izquierda >= len(numero):
            break

(descomponer())

if __name__=="__main__":
    main()