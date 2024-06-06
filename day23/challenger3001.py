'''
3001. Movimentos Mínimos para Capturar a Rainha

Existe um tabuleiro de xadrez com 1 índice 8 x 8 contendo 3peças.

Você recebe 6números inteiros a, b, c, d, ee fonde:

(a, b)denota a posição da torre branca.
(c, d)denota a posição do bispo branco.
(e, f)denota a posição da rainha preta.
Dado que você só pode mover as peças brancas, retorne o número mínimo de movimentos necessários para capturar a rainha preta .

Observe que:

As torres podem mover qualquer número de casas na vertical ou na horizontal, mas não podem saltar sobre outras peças.
Os bispos podem mover qualquer número de casas na diagonal, mas não podem saltar sobre outras peças.
Uma torre ou um bispo podem capturar a rainha se ela estiver localizada em uma casa para onde eles possam se mover.
A rainha não se move.

'''
class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # 1) Check if the Queen is in the same positive diagonal as the bishop
        # 1) Verifique se a rainha está na mesma diagonal positiva que o bispo
        if (c + d) == (e + f):
            # Check if the rook is in the bishop's way of reaching the Queen 
            # Verifique se a torre está no caminho do bispo para alcançar a rainha
            if (a + b) == (c + d):
                if not ((e > a > c) or (e < a < c)):
                    return 1
            else:
                return 1

        # 2) Check if the Queen is in the same negative diagonal as the bishop
        # 2) Verifique se a rainha está na mesma diagonal negativa que o bispo
        elif (c - d) == (e - f):
            # Check if the rook is in the bishop's way of reaching the Queen 
            # Verifique se a torre está no caminho do bispo para alcançar a rainha
            if (a - b) == (c - d):
                if not ((e > a > c) or (e < a < c)):
                    return 1
            else:
                return 1

        # 3) Check if the Queen is in the same row as the rook
        # 3) Verifique se a rainha está na mesma linha que a torre
        if a == e:
            # Check if the Bishop is blocking the rook
            # Verifique se o bispo está bloqueando a torre
            if not ((c == a) and ((b < d < f) or (f < d < b))):
                return 1
        # 4) Check if the Queen is in the same column as the rook
        # 4) Verifique se a rainha está na mesma coluna que a torre
        elif b == f:
            # Check if the Bishop is blocking the rook
            # Verifique se o bispo está bloqueando a torre
            if not ((d == b) and ((a < c < e) or (e < c < a))):
                return 1

        # The rook will always be able to reach the queen in at most 2 moves
        # A torre sempre poderá alcançar a rainha em no máximo 2 movimentos
        return 2