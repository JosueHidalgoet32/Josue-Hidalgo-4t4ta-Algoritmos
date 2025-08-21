def ej1():
 numeros = []
 for x in range(5):
     num = int(input(f"ingrese 5 numeros {x+1}:"))
     numeros.append(num)
 print("los numeros que ingresaste son:")
 for n in numeros:
     print(n)
def ej2():
    frutas = ["manzana","pera","frutilla","kiwi","durian","Parchita"]

    buscar = input("Ingrese el nombre de una fruta: ")

    if buscar in frutas:
        indice = frutas.index(buscar)
        print(f"La fruta que usted eligio se encuentra en la posicion numero {indice}")
    else:
        print("Fruta not found")
def ej3():
    notas = [7, 8, 5, 9, 10, 6, 4, 8, 9, 7]
    suma = 0
    for x in notas:
        suma += x

    promedio = suma / len(notas)

    print(f"Suma total: {suma}")
    print(f"Promedio: {promedio}")
def ej4():
    temperaturas = [22,18,30,25,19,28,80]

    temperatura_max = temperaturas[0]
    temperatura_min = temperaturas[0]

    for x in temperaturas:
        if x > temperatura_max:
            temperatura_max = x
        if x < temperatura_min:
            temperatura_min = x
    print(f"la temperatura maxima es: {temperatura_max}")
    print(f"la temperatura minima es: {temperatura_min}")
def ej5():
    numeros = [1,8,7,2,3,4,6,5,9,10]

    for n in range(len(numeros)):
        for x in range(len(numeros)-1):
            if numeros[x] > numeros[x+1]:
                 numeros[x],numeros[x+1] = numeros[x+1],numeros[x]
    print(f"la lista queda asi {numeros}")
def ej6():
    numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

    pares = 0

    impares = 0

    for x in numeros:
        if x % 2 == 0:
            pares +=1
        else:
            impares += 1
    print(f"la cantidad de pares son {pares}")
    print(f"lacantidad de impares son {impares}")
ej1()
ej2()
ej3()
ej4()
ej5()
ej6()