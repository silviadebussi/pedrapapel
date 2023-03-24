from random import *

jogada = int(input('Insira sua jogada sendo pedra = 0, papel = 1 e tesoura = 2: '))

maquina = randint(0,2)
if maquina == 0:
    print('O computador escolheu pedra')
else:
    if maquina == 1:
        print('O computador escolheu Papel')
    else:
        if maquina == 2:
         print('O computador escolheu Tesoura')


if jogada == 0 and maquina == 2 or jogada == 1 and maquina == 0 or jogada == 2 and maquina == 1:
        print('Jogador venceu')
else:
        if jogada == maquina:
            print('Empate')
        else:
             if jogada == 1 and maquina == 2 or jogada == 2 and maquina == 0 or jogada == 0 and maquina == 1:
                print('Máquina venceu')
             else:
                 print('Inválido')
