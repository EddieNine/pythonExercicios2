import random
from time import sleep
print('\033[33m-=-'*30)
print('\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[33m-=-'*30)
c = random.randint(0, 5)
j = int(input('Em que número eu pensei? '))
print('\033[35mPROCESSANDO...')
sleep(1)
if c != j:
    print(f'Ganhei! Eu pensei no número {c} e não no {j}!')
else:
    print('Você ganhou!!!!')

