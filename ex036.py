print('-='*30)
print('Analisador de Trinângulos')
print('-='*30)
p = float(input('Primeiro segmento: '))
s = float(input('Segundo segmento: '))
t = float(input('Terceiro segmento: '))
if p < s + t and s < p + t and t < s + p:
    print('Os angulos podem formar um triângulo')
    if p == s == t:
        print('Podem formar um triãngulo equilatero')
else:
    print('Os angulos não podem formar um triângulo')
