from datetime import datetime
pessoa = dict()
pessoa['Nome'] = str(input('Nome: '))
pessoa['Idade'] = int(input('Ano de nascimento: '))
pessoa['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
pessoa['Idade'] = datetime.now().year - pessoa['Idade']
if pessoa['CTPS'] != 0:
    pessoa['Contratação'] = int(input('Ano de Contratação: '))
    pessoa['Salário'] = float(input('Salário: R$'))
    pessoa['Aposentadoria'] = pessoa['Idade'] + ((pessoa['Contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in pessoa.items():
    print(f'{k}: {v}')
