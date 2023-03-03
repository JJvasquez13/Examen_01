volver = True
while volver == True:
    numMax = int(input("Digite un numero mayor que 1 y menor que 9: "))
    if 1 < numMax <= 9:
        for i in range(1, numMax + 1):
            print()
            for j in range(1, i + 1):
                print(j, end=" ")
        for i in range(numMax - 1, 0, -1):
            print()
            for j in range(1, i + 1):
                print(j, end=" ")
        volver = False
    else:
        volver = True
        print("Digito un numero que no se encuentra dentro de los limites establecidos.")