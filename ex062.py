print('Gerador de PA')
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
t = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{t} > ', end='')
        t += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quer quantos termos a mais? Digite 0 para parar: '))
print(f'Você obteve um total de {total} termos')