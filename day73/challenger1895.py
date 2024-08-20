'''

1895. Maior Quadrado Mágico

Um quadrado mágico de k x k é uma grade de k x k preenchida com números inteiros de forma que a soma de cada linha, a soma de cada coluna e as somas das duas diagonais sejam todas iguais. Os números inteiros no quadrado mágico não precisam ser distintos. Toda grade de 1 x 1 é trivialmente um quadrado mágico.

Dada uma grade de inteiros de m x n, retorne o tamanho (ou seja, o comprimento do lado k) do maior quadrado mágico que pode ser encontrado dentro dessa grade.

'''


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        # Get the dimensions of the grid
        # Obter as dimensões da grade
        m, n = len(grid), len(grid[0])

        # Function to check if a k x k square starting at (r, c) is a magic square
        # Função para verificar se um quadrado k x k começando em (r, c) é um quadrado mágico
        def is_magic(r, c, k):
            # Initialize sums for comparison
            # Inicializar somas para comparação
            target_sum = sum(grid[r][c:c+k])
            # Row sums / Somas das linhas
            for i in range(r, r + k):
                if sum(grid[i][c:c+k]) != target_sum:
                    return False
            # Column sums / Somas das colunas
            for j in range(c, c + k):
                if sum(grid[i][j] for i in range(r, r + k)) != target_sum:
                    return False
            # Main diagonal sum / Soma da diagonal principal
            if sum(grid[r + i][c + i] for i in range(k)) != target_sum:
                return False
            # Anti-diagonal sum / Soma da anti-diagonal
            if sum(grid[r + i][c + k - 1 - i] for i in range(k)) != target_sum:
                return False
            return True

        # Iterate over all possible square sizes, from largest to smallest
        # Iterar sobre todos os tamanhos possíveis de quadrado, do maior para o menor
        for k in range(min(m, n), 0, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if is_magic(r, c, k):
                        return k
        return 1
