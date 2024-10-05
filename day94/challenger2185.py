'''
2185. Contando Palavras com um Prefixo Dado

Você recebe um array de strings, chamado words, e uma string pref.

Retorne o número de strings em words que contêm pref como prefixo.

Um prefixo de uma string s é qualquer substring contínua no início de s.
'''


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cont = 0
        for word in words:
            if word.startswith(pref):
                cont += 1

        return cont
