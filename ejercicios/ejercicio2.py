import sys

def num():
    numero_magico=12345679
    while True:
        numero=(input("Nº entre 1 y 9: "))
        try:
            numero=int(numero)
        except:
            print("El caracter ni válido", file=sys.stderr)
            pass
        else:
            if 1<=int(numero)<=9:
                break
                sys.exit()
            else:
                pass
    n1=numero*9
    print("{} multiplicado por 9 es {}".format(numero, n1))
    valor_magico=numero_magico*n1
    return "{} multiplicado por {} es {}".format(n1, numero_magico, valor_magico)



if __name__=="__main__":
    print(num())
    