def ficha(nome='<desconhecido>', number=0):
    print(f'O jogador {nome} fez {numero} gol(s) na partida.')


nome = str(input('Nome do Jogador: '))
numero = str(input('Número de Gols: '))
if numero.isnumeric():
    numero = int(numero)
else:
    numero = 0
if nome.strip() == '':
    ficha(number=numero)
else:
    ficha(nome, numero)


