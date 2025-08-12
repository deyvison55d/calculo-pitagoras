import math
from menu import linha

#Funções para calcular os catetos e a hipotenusa de um triângulo retângulo
def cateto_oposto():
    while True:
        try:
            # Solicita os valores da hipotenusa e do cateto adjacente
            hipotenusa = float(input('Digite o valor da hipotenusa: '))
            cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))

            # Verifica se os valores são válidos
            if hipotenusa <= 0 or cateto_adjacente <= 0:
                print('\033[31mOs valores devem ser maiores que zero. Tente novamente.\033[m')
                linha()
            elif hipotenusa < cateto_adjacente:
                print('\033[31mA hipotenusa deve ser maior que o cateto adjacente. Tente novamente.\033[m')
                linha()
            else:
                break
        except ValueError:
            print('\033[31mEntrada inválida! Por favor, insira um número válido.\033[m')
            linha()

    # Cálculo do cateto oposto      
    num = math.sqrt(hipotenusa ** 2 - cateto_adjacente ** 2)
    return num


def cateto_adjacente():
    while True:
        try:
            # Solicita os valores da hipotenusa e do cateto oposto
            hipotenusa = float(input('Digite o valor da hipotenusa: '))
            cateto_oposto = float(input('Digite o valor do cateto oposto: '))

            # Verifica se os valores são válidos
            if hipotenusa <= 0 or cateto_oposto <= 0:
                print('\033[31mOs valores devem ser maiores que zero. Tente novamente.\033[m')
                linha()
            elif hipotenusa < cateto_oposto:
                print('\033[31mA hipotenusa deve ser maior que o cateto oposto. Tente novamente.\033[m')
                linha()
            else:
                break
        except ValueError:
            print('\033[31mEntrada inválida! Por favor, insira um número válido.\033[m')
            linha()
    
    #Cálculo do cateto adjacente
    num = math.sqrt(hipotenusa ** 2 - cateto_oposto ** 2)
    return num


def hipotenusa():
    while True:
        try:
            # Solicita os valores do cateto oposto e do cateto adjacente
            cateto_oposto = float(input('Digite o valor do cateto oposto: '))
            cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))

            # Verifica se os valores são válidos
            if cateto_oposto <= 0 or cateto_adjacente <= 0:
                print('\033[31mOs valores devem ser maiores que zero. Tente novamente.\033[m')
                linha()
            else:
                break
        except ValueError:
            print('\033[mEntrada inválida! Por favor, insira um número válido.\033[m')
            linha()

    # Cálculo da hipotenusa
    resul = math.sqrt(cateto_oposto** 2 + cateto_adjacente ** 2)
    return resul
