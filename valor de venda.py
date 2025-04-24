import os

def registrar_produto(produto, valor_compra, valor_venda, lucro):
    produtos = {
        'Produto': produto,
        'Valor de compra': valor_compra,
        'Valor de venda': valor_venda,
        'Lucro': lucro
    }
    tabela_de_produtos.append(produtos)
    print('Produto registrado com sucesso!')
    print(produtos)
tabela_de_produtos = []

def lista_de_produtos(produto, valor_venda):
    estoque = {
        'Produto': produto,
        'Preço': valor_venda
    }
    lista_produtos.append(estoque)
lista_produtos = []

def calcular_valor_venda(valor_compra, per_lucro):
    lucro = valor_compra * (per_lucro/100) 
    return valor_compra + lucro

def calcular_lucro(valor_compra, per_lucro):
    lucro = valor_compra * (per_lucro/100) 
    return lucro

def exibir_estoque():
    for estoque in lista_produtos:
        print(estoque)
        input('Pressione ENTER para voltar ao menu')
    if len(lista_produtos) == 0:
        print('Sem produtos no estoque.')
        input('Pressione ENTER para voltar ao menu')

def encontrar_indice_matriz_strings(lista_produtos, produto):
    for i, linha in enumerate(lista_produtos):
        for j, valor in enumerate(linha):
            if valor == produto:
                return (i)

    return None

def calcular_valor_total(valor_produto):
    total = 0
    total = total + valor_produto
    return total

def calcular_lucro_produto(lucro_produto):
    total = 0
    total = total + lucro_produto
    return total

def adicionar_carrinho(produto, valor_venda):
    carrinho_lista = {
        'Produto': produto,
        'Preço': valor_venda
    }
    carrinho.append(carrinho_lista)
carrinho = []

def main():
    while True:
        os.system('cls')
        print('==========Menu==========\n1. Registrar produto\n2. Consultar estoque \n3. Fazer compras \n4. Sair')
        escolha = input('Selecione uma das opções acima: ')
        os.system('cls')
        if escolha == '1':
            while True:
                produto = input('Nome do produto: ')
                valor_compra = float(input('Valor de compra: R$'))
                per_lucro = float(input('Margem de lucro (em %): '))
                valor_venda = calcular_valor_venda(valor_compra, per_lucro)
                valor_venda = round(valor_venda, 2)
                lucro = calcular_lucro(valor_compra, per_lucro)
                lucro = round(lucro, 2)
                print(f'Valor de venda do produto: R${valor_venda}')
                print(f'Lucro: R${lucro}')
                registrar_produto(produto, valor_compra, valor_venda, lucro)
                lista_de_produtos(produto, valor_venda)
                sair = input('Pressione ENTER para sair ou qualquer tecla para continuar: ')
                if sair == "":
                    break
        elif escolha == '2':
            exibir_estoque()

        elif escolha == '3':
            while True:
                exibir_estoque()
                produt = input('Informe o nome do produto que deseja adicionar ao carrinho: ')
                valor_produto = tabela_de_produtos[encontrar_indice_matriz_strings(tabela_de_produtos, produt), 2]
                lucro_produto = tabela_de_produtos[encontrar_indice_matriz_strings(tabela_de_produtos), 3]
                adicionar_carrinho(produt, valor_produto)
                lucro_total = calcular_lucro_produto(lucro_produto)
                total = calcular_valor_total(valor_produto)
                sair = input('Pressione ENTER para sair ou qualquer tecla para continuar: ')
                if sair == "":
                    break
            print(f'Carrinho: {carrinho}\nValor total: R${total}\nLucro: R${lucro_total:.2f}')



        elif escolha == '4':
            break
        else:
            continue
                
if __name__ == '__main__':
    main()
        
