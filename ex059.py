def somar(a, b):
    return a + b


def multiplicar(a, b):
    return a * b


while True:
    p = int(input('Primeiro valor: '))
    s = int(input('Segundo valor: '))
    print(''' 
            [1] Somar
            [2] Multiplicar
            [3] Maior
            [4] Novos números
            [5] Sair do programa''')
    opcao = int(input('>>>> Qual é a sua opção? '))
    if opcao == 1:
        print(f'A soma entre {p} + {s} é {somar(p, s)}')
    elif opcao == 2:
        print(f'A multiplicação entre {p} * {s} é {multiplicar(p, s)}')
    elif opcao == 3:
        if p > s:
            maior = p
        else:
            maior = s
        print(f'O maior entre {p} e {s} é {maior}')
    elif opcao == 4:
        continue
    elif opcao == 5:
        break
    else:
        print('Opção invalida. Tente novamente')
    print('=-='*10)
