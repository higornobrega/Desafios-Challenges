'''
2011. Valor Final da Variável Após Realizar Operações
Existe uma linguagem de programação com apenas quatro operações e uma variável X:
++X e X++ incrementam o valor da variável X em 1.
--X e X-- decrementam o valor da variável X em 1.
Inicialmente, o valor de X é 0.
Dada uma lista de strings chamada operations contendo uma lista de operações, retorne o valor final de X após realizar todas as operações.
'''


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for op in operations:
            if '+X' in op or 'X+' in op:
                x += 1
            else:
                x -= 1

        return x
