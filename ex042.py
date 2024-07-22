p1 = int(input('Primeiro segmento: '))
p2 = int(input('Segundo segmento: '))
p3 = int(input('Terceiro segmento: '))
if p1 < p2 + p3 and p2 < p1 + p3 and p3 < p1 + p2:
    print('Os segmentos acima PODEM formar um triangulo ', end='')
    if p1 == p2 == p3:
        print('EQUILATERO')
    if p1 != p2 != p3 != p1:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('Os segmentos acima NÂO PODEM formar um triangulo')