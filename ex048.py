soma = total = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        total += 1
print(f'A soma de todos os {total} valores solicitados é {soma}')