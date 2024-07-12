'''

1662. Verificar se Duas Matrizes de Strings são Equivalentes

Dadas duas matrizes de strings word1 e word2, retorne verdadeiro se as duas matrizes representarem a mesma string, e falso caso contrário.
Uma string é representada por uma matriz se os elementos da matriz concatenados em ordem formarem a string.

'''


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # Concatenate all strings in word1 to form a single string
        # Concatenar todas as strings em word1 para formar uma única string
        concatenated_word1 = ''.join(word1)

        # Concatenate all strings in word2 to form a single string
        # Concatenar todas as strings em word2 para formar uma única string
        concatenated_word2 = ''.join(word2)

        # Check if the two concatenated strings are equal
        # Verificar se as duas strings concatenadas são iguais
        return concatenated_word1 == concatenated_word2
