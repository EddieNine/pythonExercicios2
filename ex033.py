p = int(input('Primeiro valor: '))
s = int(input('Segundo valor: '))
t = int(input('Terceiro valor: '))
menor = p
if s < p and s < t:
    menor = s
if t < p and t < s:
    menor = t
maior = p
if s > p and s > t:
    maior = s
if t > p and t > s:
    maior = t
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')