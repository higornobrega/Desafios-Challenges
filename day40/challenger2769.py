'''
2769. Encontre o Número Máximo Atingível

Dado dois inteiros, num e t. Um número é atingível se ele puder se tornar igual a num após aplicar a seguinte operação:
Aumente ou diminua o número em 1, e simultaneamente aumente ou diminua num em 1.
Retorne o número máximo atingível após aplicar a operação no máximo t vezes.

'''

class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        # Calculation to get the right number
        # cálculo para conseguir o número certo
        return (num + t) + t
        
    