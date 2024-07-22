
numero = cont = soma = 0
while numero != 999:
    numero = int(input('Digite um número [999 para parar]: '))
    cont += 1
    soma += numero
print(f'Você digitou {cont} numeros e a soma entre eles foi {soma}')