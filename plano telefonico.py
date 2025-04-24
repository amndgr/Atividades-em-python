import os
from datetime import datetime

tabela = {
    (47, 47): 0.15, (47, 48): 0.25, (47, 49): 0.32,
    (48, 47): 0.28, (48, 48): 0.12, (48, 49): 0.28,
    (49, 47): 0.40, (49, 48): 0.25, (49, 49): 0.09
}
historico = []

def calcular_custo(ddd_origem, ddd_destino, min):
    chave = (ddd_origem, ddd_destino)
    if chave in tabela:
        custo = tabela[chave] * min
    else:
        custo = 0
    return custo

def registrar_consulta(ddd_origem, ddd_destino, min, custo, hora, data):
    consulta = {
        'DDD de origem': ddd_origem,
        'DDD de destino': ddd_destino,
        'Tempo de ligação': min,
        'Custo': custo,
        'Data': data,
        'Horário': hora
    }
    if len(historico)>=5:
        historico.pop(0)
    historico.append(consulta)

def exibir_historico():
    for consulta in historico:
        print(consulta)
    if len(historico) == 0:
        print('Histórico sem ligações!')

def main():
    while True:
        input("")
        os.system('cls')
        print('''-----Bem vindo(a) ao Plano Telefônico-----
          
        0 - Calcular custo da ligação
        1 - Consultar histórico de ligações
        2 - Sair        ''')

        escolha = int(input(''))
        
        os.system('cls')

    
        if escolha == 0:
            ddd_origem = int(input('Digite o DDD de origem: '))
            ddd_destino = int(input('Digite o DDD de destino: '))
            min = float(input('Digite o tempo de ligação em minutos: '))

            agora = datetime.now()
            hora = agora.strftime("%H:%M")
            data = agora.strftime("%Y-%m-%d")
            custo = calcular_custo(ddd_origem, ddd_destino, min)
            registrar_consulta(ddd_origem, ddd_destino, min, custo, hora, data)

            print(f'O custo da ligação é: R${custo:.2f}')

        elif escolha == 1:
            exibir_historico()

        elif escolha == 2:
            print('Programa encerrado.')
            break

        else:
            print('Insira um valor válido!')
            continue
    
        
            
    


if __name__ == '__main__':
    main()