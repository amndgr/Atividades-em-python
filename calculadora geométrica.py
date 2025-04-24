import math
import os
import time

def area_quadrado():
    l = float(input('Informe a medida de um dos lados: '))
    print(f'Área do quadrado: {l**2:.2f}cm²/m²')

def perimetro_quadrado():
    l = float(input('Informe a medida de um dos lados: '))
    print(f'Perímetro do quadrado: {l*4:.2f}cm/m')

def area_retangulo():
    b = float(input('Informe a base: '))
    h = float(input('Informe a altura: '))
    print(f'Área do retângulo: {b*h:.2f}cm²/m²')

def perimetro_retangulo():
    b = float(input('Informe a base: '))
    h = float(input('Informe a altura: '))
    print(f'Perímetro do retângulo: {(2*b) + (2*h):.2f}cm/m')

def area_circulo():
    r = float(input('Informe o raio: '))
    print(f'Área do círculo: {math.pi*(r**2):.2f}cm²/m²')

def perimetro_circulo():
    r = float(input('Informe o raio: '))
    print(f'Perímetro do círculo: {2*math.pi*r:.2f}cm/m')

def area_cilindro():
    r = float(input('Informe o raio do cilindro: '))
    h = float(input('Informe a altura do cilindro: '))
    ab = math.pi*(r**2)
    al = 2*math.pi*r*h
    area = 2*ab+al
    print(f'Área do cilindro: {area:.2f}cm²/m²')

def volume_cilindro():
    r = float(input('Informe o raio do cilindro: '))
    h = float(input('Informe a altura do cilindro: '))
    v = math.pi*(r**2)*h
    print(f'Volume do cilindro: {v:.2f}cm³/m³')


def __main__():
    while True:
        os.system('cls')
        print('''
                 _____________________
                |  _________________  |
                | |   Calculadora   | |
                | |_ _Geométrica____| |
                |  ___ ___ ___   ___  |
                | | 7 | 8 | 9 | | + | |
                | |___|___|___| |___| |
                | | 4 | 5 | 6 | | - | |
                | |___|___|___| |___| |
                | | 1 | 2 | 3 | | x | |
                | |___|___|___| |___| |
                | | . | 0 | = | | / | |
                | |___|___|___| |___| |
                |_____________________|
              ''')
        print('1.Calcular área\n2.Calcular perímetro\n3.Calcular volume\n4.Sair')
        menu = int(input('Escolha uma opção: '))
        match menu:
            case 1:
                menuarea = 0
                while menuarea != 5:
                    os.system('cls')
                    print('1.Quadrado\n2.Retângulo\n3.Círculo\n4.Cilindro\n5.Voltar')
                    menuarea = int(input('Escolha uma opção: '))
                    match menuarea:
                        case 1:
                            os.system('cls')
                            area_quadrado()
                            input('Pressione ENTER para voltar.')
                        case 2:
                            os.system('cls')
                            area_retangulo()
                            input('Pressione ENTER para voltar.')
                        case 3:
                            os.system('cls')
                            area_circulo()
                            input('Pressione ENTER para voltar.')
                        case 4:
                            os.system('cls')
                            area_cilindro()
                            input('Pressione ENTER para voltar.')
                        case ValueError:
                            continue
            case 2:
                menuperimetro = 0
                while menuperimetro != 4:
                    os.system('cls')
                    print('1.Quadrado\n2.Retângulo\n3.Círculo\n4.Voltar')
                    menuperimetro = int(input('Escolha uma opção: '))
                    match menuperimetro:
                        case 1: 
                            os.system('cls')
                            perimetro_quadrado()
                            input('Pressione ENTER para voltar.')
                        case 2:
                            os.system('cls')
                            perimetro_retangulo()
                            input('Pressione ENTER para voltar.')
                        case 3:
                            os.system('cls')
                            perimetro_circulo()
                            input('Pressione ENTER para voltar.')
                        case ValueError:
                            continue
            case 3:
                menuvolume = 0
                while menuvolume != 2:
                    os.system('cls')
                    print('1.Cilindro\n2.Voltar')
                    match menuvolume:
                        case 1:
                            os.system('cls')
                            volume_cilindro()
                            input('Pressione ENTER para voltar.')
                        case ValueError:
                            continue
            case 4:
                os.system('cls')
                print('''
                 _____________________
                |  _________________  |
                | |  Desligando     | |
                | |_________________| |
                |  ___ ___ ___   ___  |
                | | 7 | 8 | 9 | | + | |
                | |___|___|___| |___| |
                | | 4 | 5 | 6 | | - | |
                | |___|___|___| |___| |
                | | 1 | 2 | 3 | | x | |
                | |___|___|___| |___| |
                | | . | 0 | = | | / | |
                | |___|___|___| |___| |
                |_____________________|
              ''')
                time.sleep(0.5)
                os.system('cls')
                print('''
                 _____________________
                |  _________________  |
                | |  Desligando.    | |
                | |_________________| |
                |  ___ ___ ___   ___  |
                | | 7 | 8 | 9 | | + | |
                | |___|___|___| |___| |
                | | 4 | 5 | 6 | | - | |
                | |___|___|___| |___| |
                | | 1 | 2 | 3 | | x | |
                | |___|___|___| |___| |
                | | . | 0 | = | | / | |
                | |___|___|___| |___| |
                |_____________________|
              ''')
                time.sleep(0.5)
                os.system('cls')
                print('''
                 _____________________
                |  _________________  |
                | |  Desligando..   | |
                | |_________________| |
                |  ___ ___ ___   ___  |
                | | 7 | 8 | 9 | | + | |
                | |___|___|___| |___| |
                | | 4 | 5 | 6 | | - | |
                | |___|___|___| |___| |
                | | 1 | 2 | 3 | | x | |
                | |___|___|___| |___| |
                | | . | 0 | = | | / | |
                | |___|___|___| |___| |
                |_____________________|
              ''')
                time.sleep(0.5)
                os.system('cls')
                print('''
                 _____________________
                |  _________________  |
                | |  Desligando...  | |
                | |_________________| |
                |  ___ ___ ___   ___  |
                | | 7 | 8 | 9 | | + | |
                | |___|___|___| |___| |
                | | 4 | 5 | 6 | | - | |
                | |___|___|___| |___| |
                | | 1 | 2 | 3 | | x | |
                | |___|___|___| |___| |
                | | . | 0 | = | | / | |
                | |___|___|___| |___| |
                |_____________________|
              ''')
                time.sleep(0.5)
                os.system('cls')
                print('''
                 _____________________
                |  _________________  |
                | |     tchau :)    | |
                | |_________________| |
                |  ___ ___ ___   ___  |
                | | 7 | 8 | 9 | | + | |
                | |___|___|___| |___| |
                | | 4 | 5 | 6 | | - | |
                | |___|___|___| |___| |
                | | 1 | 2 | 3 | | x | |
                | |___|___|___| |___| |
                | | . | 0 | = | | / | |
                | |___|___|___| |___| |
                |_____________________|
              ''')
                time.sleep(0.3)
                os.system('cls')


                break           
            case ValueError:
                continue         


if __name__ == '__main__':
    __main__()
