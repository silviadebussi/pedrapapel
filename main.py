from random import *

jogada = int(input('Insira sua jogada sendo pedra = 0, papel = 1 e tesoura = 2: '))

maquina = randint(0,2)

print(maquina)

if jogada == 0 and maquina == 1:
    print('Maquina venceu')
else:
    if jogada == 0 and maquina == 2:
        print('Jogador venceu')
    else:
        if jogada == 0 and maquina == 0:
            print('Empate')
        else:
            if jogada == 1 and maquina == 1:
                print('Empate')
            else:
                if jogada == 1 and maquina == 0:
                    print('jogador Venceu')
                else:
                    if jogada == 1 and maquina == 2:
                     print('Máquina venceu')
                    else:
                        if jogada == 2 and maquina == 0:
                            print('Máquina venceu')
                        else:
                            if jogada == 2 and maquina == 1:
                                print('Jogador venceu')
                            else:
                                if jogada == 2 and maquina == 2:
                                    print('Empate')
                                else:
                                    print('Inválido')
