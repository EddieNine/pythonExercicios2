import random
from time import sleep
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {jogos} JOGOS -=-=-=')
sleep(1)
for c in range(1, jogos + 1):
    lista = [random.randint(0, 50), random.randint(0, 50), random.randint(0, 50),
             random.randint(0, 50), random.randint(0, 50), random.randint(0, 50)]
    print(f'Jogo {c}: {lista}')
    sleep(1)
print('-=-=-= < BOA SORTE > -=-=-=')
