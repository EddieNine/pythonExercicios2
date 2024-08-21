import ex108 as m

preco = float(input('Digite o preço: R$'))
print(f'A metade de {m.moeda(preco)} é {m.moeda(m.aumentar(preco))}')
print(f'O dobro de {m.moeda(preco)} é {m.moeda(m.dobro(preco))}')
print(f'Aumentando 10%, temos {m.aumentar(preco, 10)}')
