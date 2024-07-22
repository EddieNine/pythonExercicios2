print('Gerador de PA')
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
t = p
cont = 1
while cont <= 10:
    print(f'{t} > ', end='')
    t += r
    cont += 1
print('fim')