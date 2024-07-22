from time import sleep
import random
print('''Suas opções
        [0] PEDRA
        [1] PAPEL
        [2] TESOURA''')
c = random.randint(0, 2)
itens = ('PEDRA', 'PAPEL', 'TESOURA')
j = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=-' * 10)
print(f'Computador jogou {itens[c]}')
print(f'Jogador jogou {itens[j]}')
print('-=-' * 10)

if c == 0 and j == 2 or c == 2 and j == 1 or c == 1 and j == 0:
    print('PERDEU')
elif j == c:
    print('EMPATE')
else:
    print('GANHOU')
