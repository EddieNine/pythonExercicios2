from time import sleep


def valores(*args):
    print('\nAnalisando os valores passado')
    for c in args:
        print(f'{c} ', end='', flush=True)
        sleep(0.3)
    print(f'Foram informados {len(args)} valores ao todo')
    print(f'O maior valor informado foi {max(args)}')


valores(1, 2, 3, 5, 6, 8)
