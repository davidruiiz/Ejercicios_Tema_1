
def Nombre_Apellido():
    cadena = "zeréP nauJ,01"
    legible=cadena[::-1]
    frase = legible.split(",")
    Nota_de_nota=frase[0]
    Nombre_Apellido=frase[1]
    return "{} ha sacado un {}".format(Nombre_Apellido, Nota_de_nota)



if __name__=="__main__":
    print(Nombre_Apellido())
    
