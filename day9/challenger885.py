'''
885. Matriz Espiral III

Você começa na célula (rStart, cStart)de uma rows x colsgrade voltada para o leste. O canto noroeste está na primeira linha e coluna da grade, e o canto sudeste está na última linha e coluna.

Você caminhará em espiral no sentido horário para visitar todas as posições desta grade. Sempre que você sair do limite da grade, continuaremos nossa caminhada fora da grade (mas poderemos retornar ao limite da grade mais tarde). Eventualmente, alcançamos todos rows * colsos espaços da grade.

Retorne uma matriz de coordenadas representando as posições da grade na ordem em que você as visitou .

 

Exemplo 1:


Entrada: linhas = 1, colunas = 4, rStart = 0, cStart = 0
 Saída: [[0,0],[0,1],[0,2],[0,3]]
Exemplo 2:


Entrada: linhas = 5, colunas = 6, rStart = 1, cStart = 4
 Saída: [[1,4],[1,5],[2,5],[2,4],[2,3], [1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2 ,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1 ],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
 

Restrições:

1 <= rows, cols <= 100
0 <= rStart < rows
0 <= cStart < cols
'''

class Solution:  
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
    
        directions = [[0,1], [1,0], [0, -1], [-1,0]]
        result = [[r0, c0]]
        index = 0 
        increment = 1
        steps = 0
        while len(result) < R*C:
            for i in range(increment):
                r0, c0 = r0 + directions[index][0], c0 + directions[index][1]
                if 0 <= r0 < R and 0 <= c0 < C:
                    result.append([r0, c0])
            
            steps += 1
            if steps % 2 == 0:
                steps = 0
                increment += 1
            index = (index + 1) %4


        return result