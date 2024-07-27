times = ('Grêmio', 'Cruzeiro', 'Flamengo', 'Fortaleza', 'Bahia',
         'Palmeiras', 'Vasco da Gama', 'Atlético Mineiro',
         'Cuiabá', 'Coritiba', 'Internacional', 'Corinthians',
         'Botafogo', 'Fluminense', 'Red Bull, Bragantino')
print(f'Lista de times do Brasileiro: {times}')
print(f'Os 5 primeiros são: {times[:5]}')
print(f'os 4 ultimos são: {times[-4:]}')
print(f'Times em ordem alfabetica: {sorted(times)}')
print(f'O Cruzeiro está na {times.index('Cruzeiro')} posição')