def numeros_repetidos(numeros):
    repetidos = []
    for i in range(len(numeros)):
       vezes = numeros.count(numeros[i]) #aqui a função count verifica quantas vezes cada numero da lista 'numeros'
       if vezes>1 and numeros[i] not in repetidos: #se a quantidade de vezes foi maior q 1 e ainda nao estiver na lista 'repetidos'
           repetidos.append(numeros[i]) #o numero será inserido na lista de numeros repetidos
    return repetidos
            
def qtd_vezes(numeros, repetidos):
    vezes = []
    for i in range(len(repetidos)): #repete o numero de vezes a quantidade de itens da lista repetidos
        vezes.append(numeros.count(repetidos[i])) #adiciona na lista 'vezes' a quantidade de vezes q cada numero em 'repetidos' aparecem na lista 'numeros'
    return vezes

numeros = []

for i in range(10):
    numeros.append(int(input('Digite um número: ')))

repetidos = numeros_repetidos(numeros)
vezes = qtd_vezes(numeros, repetidos)

if len(repetidos)>0:
    for i in range(len(repetidos)):  
        print(f'O número {repetidos[i]} foi repetido {vezes[i]}x')
else:
    print('Nenhum número foi repetido.')



