'''

2500. Excluir o Maior Valor em Cada Linha
Você recebe uma matriz de m x n composta por números inteiros positivos.

Realize a seguinte operação até que a matriz se torne vazia:

Exclua o elemento com o maior valor de cada linha. Se existirem vários elementos com o mesmo valor, exclua qualquer um deles. Adicione o maior dos elementos excluídos à resposta. Observe que o número de colunas diminui em um após cada operação.

Retorne a resposta após realizar as operações descritas acima.

'''


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        # Initialize a variable to store the final answer
        # Inicia uma variável para armazenar a resposta final
        answer = 0

        # Perform operations until the grid becomes empty
        # Realiza operações até que a grade se torne vazia
        while grid[0]:
            # Initialize a list to store the greatest value from each row
            # Inicializa uma lista para armazenar o maior valor de cada linha
            max_values = []

            # Iterate through each row in the grid
            # Itera por cada linha na grade
            for row in grid:
                # Find the maximum value in the current row and append it to max_values
                # Encontra o maior valor na linha atual e o adiciona à lista max_values
                max_values.append(max(row))
                # Remove the maximum value from the current row
                # Remove o maior valor da linha atual
                row.remove(max(row))

            # Add the maximum value found in this iteration to the final answer
            # Adiciona o maior valor encontrado nesta iteração à resposta final
            answer += max(max_values)

        # Return the final answer after all operations
        # Retorna a resposta final após todas as operações
        return answer
