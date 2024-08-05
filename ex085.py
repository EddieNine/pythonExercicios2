listaPares = []
listaImpares = []
for c in range(1, 8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        listaPares.append(valor)
        listaPares.sort()
    else:
        listaImpares.append(valor)
        listaImpares.sort()
print(f'Os valores pares digitados foram: {listaPares}')
print(f'Os valores impares digitados foram: {listaImpares}')