import ex107

preco = float(input('Digite o preço: R$'))
print(f'A metade de R${preco:.2f} é R${ex107.aumentar(preco):.2f}')
print(f'O dobro de R${preco:.2f} é R${ex107.dobro(preco):.2f}')
print(f'Aumentando 10%, temos R${ex107.aumentar(preco, 10):.2f}')
