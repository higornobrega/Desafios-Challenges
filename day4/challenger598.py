'''
598. Adição de Gama II

Você recebe uma m x nmatriz Minicializada com todos 0e um array de operações ops, onde as médias devem ser incrementadas em um para todos e .ops[i] = [ai, bi]M[x][y]0 <= x < ai0 <= y < bi

Conte e retorne o número máximo de inteiros na matriz após realizar todas as operações .

 

Exemplo 1:


Entrada: m = 3, n = 3, ops = [[2,2],[3,3]]
 Saída: 4
 Explicação: O número inteiro máximo em M é 2, e há quatro dele em M. Então retorne 4 .
Exemplo 2:

Entrada: m = 3, n = 3, operações = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[ 3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
 Saída: 4
Exemplo 3:

Entrada: m = 3, n = 3, ops = []
 Saída: 9
 

Restrições:

1 <= m, n <= 4 * 104
0 <= ops.length <= 104
ops[i].length == 2
1 <= ai <= m
1 <= bi <= n
'''


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # Se não houver operações, a matriz inteira será incrementada
        # If there are no operations, the entire matrix will be incremented
        if len(ops) == 0:
            return m * n
        # Caso contrário, a matriz será incrementada até o menor valor de x e y
        # Otherwise, the matrix will be incremented to the smallest value of x and y
        x = min(op[0] for op in ops)
        y = min(op[1] for op in ops)

        return x * y