numero = int(input('Digite um numero: '))
cont = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        cont += 1
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(c, end='')
print(f'\nO numero {numero} foi divisivel {cont} vezes')
if cont == 2:
    print('E por isso ele é primo')
else:
    print('E por isso não é primo')