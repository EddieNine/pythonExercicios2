import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
soma = math.pow(co, 2) + math.pow(ca, 2)
soma1 = math.hypot(co, ca)
print(f'A hipotenusa vai medir {math.sqrt(soma):.2f}')
print(f'Hipotenusa {soma1:.2f}')
