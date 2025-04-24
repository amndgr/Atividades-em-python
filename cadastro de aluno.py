import os

class Cadastro:
    def __init__(self, nome, matricula, notas, situacao):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas
        self.situacao = situacao
        print('Cadastro realizado com sucesso.')

    @staticmethod
    def calcular_media(notas):
        media = sum(notas) / len(notas)
        return media
    
    @staticmethod
    def visualizar(alunos):
        for aluno in alunos:
            print(f'''
                Aluno: {aluno.nome}
                Matrícula: {aluno.matricula}
                Notas: {aluno.notas}
                Situação: {aluno.situacao}''')

def main():  
    alunos = []
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Insira a opção desejada: \n1- Cadastrar aluno \n2- Visualizar \n3- Encerrar')
        menu = int(input('-> '))
        match menu:
            case 1:
                nome = input('Nome do aluno: ')
                matricula = int(input('Matrícula: '))
                notas = []
                qtd = int(input('Quantidade de notas do aluno: '))
                for i in range(qtd):
                    nota = float(input(f'{i+1}º Nota: '))
                    if nota > 10:
                        print('Nota inválida.')
                        input('Pressione ENTER para recomeçar.')
                        break
                    notas.append(nota)
                else:
                    media = Cadastro.calcular_media(notas)
                    if len(notas) < 3:
                        situacao = 'Cursando'
                    elif len(notas) == 3 and media >= 7:
                        situacao = 'Aprovado'
                    elif len(notas) == 3 and media < 7:
                        situacao = 'Reprovado'
                    else:
                        print('Erro: quantidade de notas inesperada.')
                        input('Pressione ENTER para recomeçar.')
                        continue

                    aluno = Cadastro(nome, matricula, notas, situacao)
                    alunos.append(aluno)
                          
            case 2:
                Cadastro.visualizar(alunos)
                input('Pressione ENTER para voltar ao menu.')
                continue
            case 3:
                break

if __name__ == '__main__':
    main()
