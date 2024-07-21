'''

1254. Número de Ilhas Fechadas

Dado uma grade 2D que consiste em 0s (terra) e 1s (água). Uma ilha é um grupo maximamente conectado de 0s nas quatro direções e uma ilha fechada é uma ilha totalmente (em todas as direções: esquerda, cima, direita, baixo) cercada por 1s.

Retorne o número de ilhas fechadas.
'''


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # Function to perform DFS and mark visited cells
        # Função para realizar DFS e marcar células visitadas
        def dfs(x, y):
            # Check if the current cell is out of bounds or already visited (1)
            # Verifica se a célula atual está fora dos limites ou já foi visitada (1)
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 1:
                return
            # Mark the current cell as visited
            # Marca a célula atual como visitada
            grid[x][y] = 1
            # Perform DFS in all four possible directions
            # Realiza DFS em todas as quatro direções possíveis
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        # Eliminate islands connected to the border
        # Elimina ilhas conectadas à borda
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1) and grid[i][j] == 0:
                    dfs(i, j)

        closed_islands = 0

        # Count and eliminate closed islands
        # Conta e elimina ilhas fechadas
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j] == 0:
                    closed_islands += 1
                    dfs(i, j)

        return closed_islands
