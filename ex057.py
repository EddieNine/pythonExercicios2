sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while True:
    if sexo in 'MmFf':
        print(f'Sexo {sexo} registrado com sucesso')
        break
    else:
        sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper()[0]