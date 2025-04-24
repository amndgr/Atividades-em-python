class Veiculos:
    def __init__(self, marca, modelo, capacidade, desempenho):
        self.marca = marca
        self.modelo = modelo
        self.capacidade = capacidade
        self.desempenho = desempenho

    def cadastro_de_veiculo(carros):
        marca = input('Marca: ')
        modelo = input('Modelo: ')
        capacidade = int(input('Capacidade: '))
        desempenho = int(input('Desempenho (Km/l): '))
        carros.append(Veiculos(marca, modelo, capacidade, desempenho))
        print('Cadastro realizado com sucesso!')
    

    def calcular_autonomia(self, desempenho, combustivel):
        autonomia = desempenho*combustivel
        return autonomia
    
    def calcular_combustivel(self, distancia, desempenho):
        combustivel = distancia/desempenho 
        return combustivel  
    
    def calcular_paradas(self, combustivel, capacidade):
        if combustivel > self.capacidade:
            paradas = combustivel/self.capacidade
            return print(f'Serão necessárias {int(paradas)} de abastecimento')
        if combustivel <= self.capacidade:
            print('Paradas de abastecimentos não serão necessárias.')
            return 
carros = []
menu = 0

def main():
    while menu != 4:
        print('1. Cadastro de veículo\n2. Calcular autonomia\n3. Calcular combustível\n4. Encerrar')
        menu = int(input('Selecione uma opção para continuar: '))
        match menu:
            case 1:
                Veiculos.cadastro_de_veiculo(carros)
                
                

if __name__ == '__main__':
    main()
        

    


