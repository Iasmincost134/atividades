# Listas = ["Maria", 23,[ "Porto Alegre","Sao Paulo"]]
# # Tuplas = (";aria", 23, "Porto Alegre")

# Lista1 = [1,2,3,4]
# Lista2 = [5,7,3,4]

# soma = Lista1 + Lista2

# # print (max(soma))
# # print (sum(soma));
# # print(Listas[0]) 

# Listas.append([3][0])
# # adiciona
# # Lista1.insert((1, "Pedro" ))
# print(Listas)

# construa uma lista de tarefas
# Exclua a Tarefa

tarefas = []
cont = 1

while cont:

    tarefa = input("Informe a sua tarefa : ")
    tarefas.append(tarefa)


    cont = input("Deseja continuar? (Sim/Não) : ")

    if cont == 'Sim':
        tarefa = input("Tem certeza? :")
    else:
        break

# for i in range(len(tarefas)):
#     print(i)

for i in (tarefas):
    # tarefa = input('Deseja remover alguma tarefa?')
    # tarefas.append(tarefa)
    # tarefas[1]

    print(i)

print ("vc tem", len(tarefas),"para fazer")
print (tarefas)


for i in range (len(tarefas)):
    print("Ordem", i+1, "Tarefas", tarefas[1] )


