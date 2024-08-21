import ex107

preco = float(input('Digite o preço: R$'))
print(f'A metade de R${preco} é R${ex107.aumentar(preco)}')
print(f'O dobro de R${preco} é R${ex107.dobro(preco)}')
print(f'Aumentando 10%, temos R${ex107.aumentar(preco, 10)}')
