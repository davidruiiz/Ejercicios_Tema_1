from ast import main

def separar(lista):
    lista.sort()
    pares=[]
    impares=[]
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    return pares,impares
        
(pares,impares)=separar([1,3,2,4,5,7,9,8,6])
print("pares: {}\t impares: {}".format(pares,impares))

if __name__ == '__main__':
    main()