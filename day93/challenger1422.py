'''
1422. Pontuação Máxima Após Dividir uma String
Dada uma string s composta de zeros e uns, retorne a pontuação máxima possível após dividir a string em duas substrings não vazias (ou seja, uma substring à esquerda e outra à direita).

A pontuação após dividir a string é definida como o número de zeros na substring esquerda somado ao número de uns na substring direita..
'''


class Solution:
    def maxScore(self, s: str) -> int:
        cont = 0
        for i in range(1, len(s)):
            init = s[0:i]
            final = s[i:len(s)]
            count_zero = init.count('0')
            count_one = final.count('1')
            score = count_zero+count_one
            if score > cont:
                cont = score
        return cont
