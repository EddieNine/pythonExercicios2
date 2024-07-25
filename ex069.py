continuar = ''
totMaior18 = totHomem = totMulherMenor20 = 0
while continuar != 'N':
    sexo = ' '
    print('-'*25)
    print('  CADASTRO DE PESSOAS   ')
    print('-' * 25)
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    continuar = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if idade > 18:
        totMaior18 += 1
    if sexo == 'M':
        totHomem += 1
    if sexo == 'F' and idade < 20:
        totMulherMenor20 += 1
    print('-'*25)
print(f'Total de pessoas com mais de 18: {totMaior18}')
print(f'Ao todo temos {totHomem} homens cadastrados')
print(f'E temos {totMulherMenor20} com menos de 20 anos')
