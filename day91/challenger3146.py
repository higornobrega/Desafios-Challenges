'''
3146. Diferença de permutação entre duas strings
São fornecidas duas sequências de caracteres s e t tal que cada caractere ocorre no máximo uma vez em s e t é uma permutação de s.

A diferença de permutação entre s e t é definida como a soma da diferença absoluta entre o índice de ocorrência de cada caractere em s e o índice de ocorrência do mesmo caractere em t.

Retorna a diferença de permutação entre s e t.
'''


class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        somatorio = 0
        for i in range(len(s)):
            somatorio += abs(i-t.find(s[i]))
        return somatorio
