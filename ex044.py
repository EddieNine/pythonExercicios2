print('\033[32m========= LOJAS GUANABARA =========')
p = float(input('Preço das compras: R$'))
print('''\033[33mFORMAS DE PAGAMENTO
        [1] À vista dinheiro/cheque
        [2] Á vista no cartão
        [3] 2x no cartão
        [4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    d = p - (p * 0.1)
    print(f'O valor total de R${p:.2f} com 10% de desconto ficou R${d:.2f}')
elif opcao == 2:
    d = p - (p * 0.05)
    print(f'O valor total de R${p:.2f} com 5% de desconto ficou R${d:.2f}')
elif opcao == 3:
    d = p / 2
    print(f'O Produto com valor de R${p:.2f} \n2x de R${d:.2f} no cartão sem desconto')
elif opcao == 4:
    opcaoExtra = int(input('Quantas parcelas? '))
    j = p + (p * 0.2)
    vezes = j / opcaoExtra
    print(f'O Produto com valor de R${p:.2f} \n{opcaoExtra}x de R${vezes:.2f} no cartão com Juros de 20%\n'
          f'TOTAL: R${j:.2f}')
else:
    print('Opção invalida!')