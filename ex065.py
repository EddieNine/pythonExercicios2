soma = maior = menor = cont = 0
while True:
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp in 'Nn':
        break
    elif resp in 'Ss':
        continue
    else:
        print('Digite apenas "S" ou "N", O numero foi contado.')
        continue
media = soma / cont
print(f'Você digitou {cont} numeros e a media foi de {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')