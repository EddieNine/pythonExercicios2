t = int(input('Digite um número para ver sua tabuada: '))
print('-'*10)
for c in range(1, 11):
    soma = t * c
    print(f'{t} x {c} = {soma}')
print('-'*10)
