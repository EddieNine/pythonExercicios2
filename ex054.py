from datetime import datetime
atual = datetime.today().year
menor = maior = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}° pessoa nasceu? '))
    idade = atual - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'Ao todo tivemos {menor} pessoas menores de idade')