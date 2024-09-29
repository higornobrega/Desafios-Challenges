'''
2894. Diferença entre Somas Divisíveis e Não Divisíveis Resolvido
Fácil
Tópicos
Empresas
Dica

Você tem dois inteiros positivos n e m.

Defina dois inteiros da seguinte forma:

num1: A soma de todos os inteiros no intervalo [1, n] (incluindo ambos os limites) que não são divisíveis por m.
num2: A soma de todos os inteiros no intervalo [1, n] (incluindo ambos os limites) que são divisíveis por m.
Retorne o valor de num1 - num2.
'''


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divisible = 0
        not_divisible = 0
        for i in range(1, n+1):
            if i % m == 0:
                divisible += i
            else:
                not_divisible += i
        return not_divisible - divisible
