soma = cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}° numero: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} valores pares e a soma vale {soma}')
