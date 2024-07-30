palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar',
            'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
vogais = ('a', 'e', 'i', 'o', 'u')
for palavra in palavras:
    print(f'\nNa palavra {palavra} temos ', end='')
    for letra in palavra:
        if letra.lower() in vogais:
            print(letra, end=' ')