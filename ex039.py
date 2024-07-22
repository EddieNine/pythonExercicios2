from datetime import datetime
ano = int(input('Ano de nascimento: '))
atual = datetime.today().year
idade = atual - ano
print(f'Quem nasceu em {ano} tem {idade} em {atual}')
if idade < 18:
    faltaAno = 18 - idade
    seraAno = ano + 18
    print(f'Ainda faltam {faltaAno} anos para o alistamento')
    print(f'Seu alistamento será em {seraAno}')
elif idade > 18:
    foiAno = (atual - idade) + 18
    passouAno = atual - foiAno
    print(f'Você ja deveria ter se alistado há {passouAno} anos')
    print(f'Seu alistamento foi em {foiAno}')
else:
    print('Você tem que se alistar IMEDIATAMENTE!')