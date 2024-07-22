import random

p = str(input('Primeiro aluno: '))
s = str(input('Segundo aluno: '))
t = str(input('Terceiro aluno: '))
q = str(input('Quarto aluno: '))
lista = [p, s, t, q]
random.shuffle(lista)
print(f'A Ordem de apresentação será\n{lista}')