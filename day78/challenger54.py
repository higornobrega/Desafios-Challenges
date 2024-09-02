'''

54.Matriz Espiral
Dada uma matriz m x n, retorne todos os elementos da matriz na ordem espiral.

'''


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Initialize an empty list to store the spiral order of elements
        # Inicializa uma lista vazia para armazenar a ordem espiral dos elementos
        result = []

        # Define the boundaries of the spiral (top, bottom, left, right)
        # Define os limites da espiral (superior, inferior, esquerdo, direito)
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        # Continue looping until the boundaries overlap
        # Continue o loop até que os limites se sobreponham
        while top <= bottom and left <= right:
            # Traverse from left to right along the top boundary
            # Percorra da esquerda para a direita ao longo do limite superior
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            # Move the top boundary down
            # Mova o limite superior para baixo
            top += 1

            # Traverse from top to bottom along the right boundary
            # Percorra de cima para baixo ao longo do limite direito
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            # Move the right boundary to the left
            # Mova o limite direito para a esquerda
            right -= 1

            # Check if there are rows left to traverse
            # Verifique se ainda há linhas para percorrer
            if top <= bottom:
                # Traverse from right to left along the bottom boundary
                # Percorra da direita para a esquerda ao longo do limite inferior
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                # Move the bottom boundary up
                # Mova o limite inferior para cima
                bottom -= 1

            # Check if there are columns left to traverse
            # Verifique se ainda há colunas para percorrer
            if left <= right:
                # Traverse from bottom to top along the left boundary
                # Percorra de baixo para cima ao longo do limite esquerdo
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                # Move the left boundary to the right
                # Mova o limite esquerdo para a direita
                left += 1

        # Return the result containing the elements in spiral order
        # Retorna o resultado contendo os elementos em ordem espiral
        return result
