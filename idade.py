import datetime

def idade_do_usuario(data_nascimento, data_atual):
    idade = data_atual.year - data_nascimento.year
    if data_atual.month < data_nascimento.month or (data_atual.month == data_nascimento.month and data_atual.day < data_nascimento.day):
        idade -= 1
    return idade

def main():
    dia = int(input('Informe o dia de nascimento: '))
    mes = int(input('Informe o mês de nascimento: '))
    ano = int(input('Informe o ano de nascimento: '))
    data_nascimento = datetime.date(ano, mes, dia)
    data_atual = datetime.date.today()
    idade = idade_do_usuario(data_nascimento, data_atual)
    print(f'Você tem {idade} anos.')

if __name__== '__main__':
    main()
