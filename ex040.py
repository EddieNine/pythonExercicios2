p = float(input('Primeiro nota: '))
s = float(input('Segunda nota: '))
media = (p + s) / 2
print(f'Tirando {p} e {s}, a média do aluno é {media:.1f}')
if media < 5:
    print('REPROVADO')
elif 5 <= media <= 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')