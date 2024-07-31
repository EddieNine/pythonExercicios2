continuar = ' '
lista = []
while continuar != 'N':
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
print('-=-' * 30)
lista.sort()
print(f'Você digitou os valores {lista}')