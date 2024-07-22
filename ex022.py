from time import sleep
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
sleep(1)
sep = nome.split()
print(f'Seu nome em maiúsculas é {nome.upper()}\n'
      f'seu nome em minúsculas é {nome.lower()}\n'
      f'seu nome tem ao todo {len(nome) - nome.count(' ')} letras\n'
      f'seu primeiro nome é {sep[0]} e ele tem {len(sep[0])} letras')
