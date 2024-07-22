import random

print('\033[32mSou seu computador...')
computador = random.randint(0, 10)
print('\033[33mAcabei de pensar em um numero entre 0 e 10')
print('Será que você consegue adivinhar qual foi?\033[m')
cont = 0
while True:
    palpite = int(input('\033[34mQual é seu palpite? \033[m'))
    cont += 1
    if palpite < computador:
        print('Mais... Tente mais uma vez.')
    elif palpite > computador:
        print('Menos... Tente mais uma vez.')
    else:
        print(f'Acertou com {cont} tentativas. Parabéns')
        break
