matriz = [
    [10,20,30,40],
    [50,60,70,80],
    [90,100,110,120],
]

print(matriz[1][2])

#PRIMEIRO INDEX É LINHA
#SEGUNDO INDEX É COLUNA

matriz_aula = [
    ['joao', 8,7,6], ['pedro', 4.5,9,10], ['marcos', 6, 6, 8]
]

for linha in matriz_aula:
    for col in linha:
        print(str(col) + '\t', end = ' ')
    print('')