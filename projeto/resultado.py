from tabela import *
from funções import *


res = menu()
if res == 1: #Calcular cateto oposto
    resultado = cateto_oposto()
    print(f'O cateto oposto é: {resultado:.2f}')


elif res == 2: #Calcular cateto adjacente
    hipotenusa = float(input('Digite o valor da hipotenusa: '))
    oposto = float(input('Digite o valor do cateto oposto: '))
    resultado = cateto_adjacente(hipotenusa, oposto)
    print(f'O cateto adjacente é: {resultado:.2f}')


elif res == 3: #Calcular hipotenusa
    oposto = float(input('Digite o valor do cateto oposto: '))
    adjacente = float(input('Digite o valor do cateto adjacente: '))
    resultado = hipotenusa(oposto, adjacente)
    print(f'A hipotenusa é: {resultado:.2f}')