print('De acordo com o teorema de Euler para grafos, um grafo G conexo so possui caminho euleriano se e somente se ele tem exatamente 0 ou 2 vertices de grau impar.')
print('Para os desenhos apresentados na questao temos:')

solution = [[3, 2], [3, 2], [2, 4], [2, 4], [5, 2], [6, 2]]

for i in range(len(solution)):
    print('O Desenho ', i+1, ': conexo com ', solution[i][0],' vertices de grau par e ', solution[i][1], ' vertices de grau impar')
    if solution[i][1] == 0 or solution[i][1] == 2:
        print('Portanto eh possivel de ser desenhado em caminho euleriano')
    else:
        print('Portanto nao eh possivel ser desenhado em caminho euleriano')