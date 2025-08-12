from menu import *
from funções import *

# Exibe o menu e solicita a opção do usuário
res = menu('Calculo de Pitágoras')

if res == 1: # Calcular cateto oposto
    resultado = cateto_oposto()
    print(f'O cateto oposto é: {resultado:.2f}')


elif res == 2: # Calcular cateto adjacente
    resultado = cateto_adjacente()
    print(f'O cateto adjacente é: {resultado:.2f}')


elif res == 3: # Calcular hipotenusa
    resultado = hipotenusa()
    print(f'A hipotenusa é: {resultado:.2f}')


elif res == 4: #Sair
    print('Saindo do programa... Até logo!')