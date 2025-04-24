livros = []
class Livro:
    def __init__(self, titulo, autor, editora, ano):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.ano = ano

    
    def __str__(self):
        return f'{self.titulo} de {self.autor}, {self.editora}, {self.ano}'
    
class Biblioteca:
    def __init__(self, titulo, autor, editora, ano):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.ano = ano

def cadastrar():
        x = int(input('Quantos livros deseja cadastrar?: '))
        for i in range(x):
            titulo = input(f'Informe o título do {i+1}º livro: ')
            autor = input(f'Autor do {i+1}º livro: ')
            editora = input(f'Editora: ')
            ano = int(input(f'Ano de lançamento: '))
            livros.append(Livro(titulo, autor, editora, ano))

def main():
    
    cadastrar()

if __name__ == '__main__':
    main()
    
            

            
            

        