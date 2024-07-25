print('-' * 30)
print('      LOJA SUPER BARATÃO     ')
print('-' * 30)
total = totmil = menor = cont = 0
barato = ' '
lista = list()
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    resp = ' '
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper()[0].strip()
    if resp == 'N':
        break
print('------ FIM DO PROGRAMA ------')
print(f'O total da compra foi de R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
