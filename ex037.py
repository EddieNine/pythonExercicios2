from time import sleep
numero = int(input('\033[33mDigite um número inteiro: \033[m'))
print('''\033[34mEscolha uma das bases para conversão:\033[m
        \033[35m[1] Converter para BINARIO
        [2] Converter para OCTAL
        [3] Converter para HEXADECIMAL\033[m''')
try:
    opcao = int(input('Sua opção: '))
    print(f'Você escolheu a opção {opcao}. Estamos convertendo seu numero. Aguarde ...')
    sleep(2)
    if opcao == 1:
        print(f'O numero \033[32m{numero}\033[m convertido para BINARIO é igual a {bin(numero)[2:]}')
    elif opcao == 2:
        print(f'O numero \033[32m{numero}\033[m convertido para OCTAL é igual a {oct(numero)[2:]}')
    elif opcao == 3:
        print(f'O numero \033[32m{numero}\033[m convertido para HEXADECIMAL é igual a {hex(numero)[2:]}')
    else:
        print('Opção invalida!')
except ValueError:
    print(f'Erro! {ValueError}')

