'''

3033. Modifique a Matriz

Dada uma matriz inteira m x n indexada a partir de 0 chamada matrix, crie uma nova matriz indexada a partir de 0 chamada answer. Faça answer igual a matrix, depois substitua cada elemento com o valor -1 pelo maior elemento em sua respectiva coluna.
Retorne a matriz answer.

'''


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # Number of rows in the matrix
        # Número de linhas na matriz
        m = len(matrix)
        
        # Number of columns in the matrix
        # Número de colunas na matriz
        n = len(matrix[0])
        
        # Create a list to store the maximum value of each column
        # Cria uma lista para armazenar o valor máximo de cada coluna
        max_in_col = [-1] * n
        
        # Find the maximum value in each column
        # Encontra o valor máximo em cada coluna
        for j in range(n):
            for i in range(m):
                if matrix[i][j] != -1:
                    if max_in_col[j] == -1 or matrix[i][j] > max_in_col[j]:
                        max_in_col[j] = matrix[i][j]
        
        # Create the answer matrix as a copy of the input matrix
        # Cria a matriz de resposta como uma cópia da matriz de entrada
        answer = [row[:] for row in matrix]
        
        # Replace each -1 with the maximum value of its respective column
        # Substitui cada -1 pelo valor máximo da respectiva coluna
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == -1:
                    answer[i][j] = max_in_col[j]
        
        return answer