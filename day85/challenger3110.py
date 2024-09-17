'''
3110. Pontuação de uma String Resolvido

Você recebe uma string s. A pontuação de uma string é definida como a soma da diferença absoluta entre os valores ASCII de caracteres adjacentes.

Retorne a pontuação de s.

'''


class Solution:
    def scoreOfString(self, s: str) -> int:
        # Pontuação
        # Score
        score = 0

        # Incrementar a string
        # Increase a string
        for i in range(len(s)-1):
            score = score + abs(ord(s[i]) - ord(s[i+1]))
        return score
