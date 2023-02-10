#Escreva um algorítimo para ler o número total de municípios, o número de votos branco, nulos e válidos.
#Calcule e escreva o percentual que cada representa em relação ao total de eleitores.

total = int(input('Digite o número total de eleitores do município: '))
brancos = int(input('Digite o número total de votos brancos: '))
nulos = int(input('Digite o número total de votos nulos: '))
validos = int(input('Digite o número total de votos válidos: '))

percentual_brancos = (100 * brancos) / total
percentual_nulos = (100 * nulos) / total
percentual_validos = (100 * validos) / total

print(f'''
    O percentual de votos foi de: \n 
    Brancos: {percentual_brancos:.2f}%,\n
    Nulos: {percentual_nulos:.2f}%,\n
    Válidos: {percentual_validos:.2f}%.
    ''')