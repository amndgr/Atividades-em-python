i_nome = ''
i_sabor = ''
i_peso = ''
menu = 0
fruta = []

class Frutas:
    def __init__(self, nome, sabor, peso):
        self.nome = nome
        self.sabor = sabor
        self.peso = peso
        print("Cadastro realizado com sucesso!")
    
    def descascar(self):
        print("A fruta está pronta para consumo")

    def exibir(self):
        print("""
                Nome:   %10s
                Sabor:  %10s
                Peso:   %10s
              """%(self.nome, self.sabor, self.peso))

while menu != 3:
    print('Insira a opcão desejada: \n1- Cadastrar\n2- Vizualizar\n3- Encerrar')
    menu = int(input('-> '))
    match menu:
        case 1:
            i_nome = input('Insira o nome da fruta que será cadastrada: ')
            i_sabor = input('insira o sabor da fruta: ')
            i_peso = float(input('Insira o peso unitário da fruta: '))
            fruta.append(Frutas(i_nome, i_sabor, i_peso))

        case 2:
            for x in range(len(fruta)):
                print(fruta[x].nome)
                print(fruta[x].sabor)
                print(fruta[x].peso)

                print('Dados da função:')
                fruta[x].exibir()

        case 3:
            break

