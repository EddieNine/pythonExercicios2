s = float(input('Qual é o salário do funcionário?  R$'))
if s > 1250:
    a = (s * 0.1) + s
else:
    a = (s * 0.15) + s
print(f'Quem ganhava R${s:.2f} passa a ganhar R${a:.2f} agora.')