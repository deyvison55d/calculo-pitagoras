import math


#Funções para calcular os catetos e a hipotenusa de um triângulo retângulo
def cateto_oposto():
    while True:
        try:
            hipotenusa = float(input('Digite o valor da hipotenusa: '))
            cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
            if hipotenusa <= 0 or cateto_adjacente <= 0:
                print('Os valores devem ser maiores que zero. Tente novamente.')
            elif hipotenusa < cateto_adjacente:
                print('A hipotenusa deve ser maior que o cateto adjacente. Tente novamente.')
            else:
                break
        except ValueError:
            print('Entrada inválida! Por favor, insira um número válido.')
    num = math.sqrt(hipotenusa ** 2 - cateto_adjacente ** 2)
    return num


def cateto_adjacente(hipotenusa, cateto_oposto):
    num = math.sqrt(hipotenusa ** 2 - cateto_oposto ** 2)
    return num


def hipotenusa(cateto_oposto, cateto_adjacente):
    resul = math.sqrt(cateto_oposto** 2 + cateto_adjacente ** 2)
    return resul
