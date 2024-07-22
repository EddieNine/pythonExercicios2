v = float(input('Qual é a distância da sua viagem? '))
if v <= 200:
    p = v * 0.5
elif v > 200:
    p = v * 0.45
print(f'Você está prestes a começar uma viagem de {v}')
print(f'E o preço da sua passagem será de R${p:.2f}')
