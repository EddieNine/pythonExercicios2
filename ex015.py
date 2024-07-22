dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))
c = (60 * dias) + (0.15 * km)
print(f'O total a pagar é de R${c:.2f}')