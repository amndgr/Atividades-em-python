import os
import math

#descobrir se é par ou ímpar
def par_impar(a):
    if a % 2 == 0:
        return True
    else:
        return False
    
#ambos par
def potencia(a, b):
   return (a**b)
    
#ambos impar
def soma_fatoriais(a, b):
    fat1 = math.factorial(a)
    fat2 = math.factorial(b)
    return (fat1 + fat2)
    

#1 par e 1 impar
def fatorial_raiz(a, b):
    fatorial1 = math.factorial(a)
    raiz = math.sqrt(b)
    return (fatorial1/raiz)

def main():
    while True:
        input('')
        os.system('cls')
        num1 = int(input('Insira um número: '))
        num2 = int(input('Insira outro número: '))
        if par_impar(num1) and par_impar(num2):
            result = potencia(num1, num2)
            print(f'Dois pares, a potência de um pelo outro é: {result}')

        elif not par_impar(num1) and not par_impar(num2):
            result = soma_fatoriais(num1, num2)
            print(f'Dois ímpares, a soma do fatorial de ambos é {result}')

        else:
            result = fatorial_raiz(num1, num2)
            print(f'1 par e 1 ímpar, o fatorial do 1º dividido pela raiz quadrada do 2º é {result}')

if __name__ == '__main__':
    main()


