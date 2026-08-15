
# numero = int(input("Digite um número : "))
# tabuada = []
# for x in range (1,11):
#     print("tabuada do número", x)
#     for y in range (1,11):
#         print(x, " X ", y, " = ", x*y)
#         tabuada = [x][y]




matriz = []
i=0
cont = "a"

while cont:
    matriz.append([])
    SKU = input("Digite o SKU:")
    matriz[i].append(SKU)

    codigo = input("Digite o codigo:")
    matriz[i].append(codigo)
    
    produto = input("Digite o seu produto:")
    matriz[i].append(produto)
    i+=1

    cont = input("Deseja continuar?")

for i in range(len(matriz)):
        
        print("")
        for x in range (0,3):
            print(matriz [i][x], end= " - "),

        
    

# print(matriz)

