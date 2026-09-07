def vectores(datos):
    for dato in datos:
        print(datos)

def media(datos):
    suma = sum(datos)
    return suma/len(datos) if datos else 0

def main():
    pares=[2,4,6,8,10]
    impares=[1,3,5,7,9]
    vectores(pares)
    print(F" media {media(pares)}")
    vectores(impares)
    print(F" media {media(impares)}")

main()