from datetime import datetime
ano = int(input('Ano de nascimento: '))
atual = datetime.today().year
anos = atual - ano
print(f'O atleta tem {anos} anos.')
if anos <= 9:
    print('Mirim')
elif anos <= 14:
    print('Infantil')
elif anos <= 19:
    print('Junior')
elif anos <= 25:
    print('Sênior')
else:
    print('Master')