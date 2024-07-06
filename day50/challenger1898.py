'''

1898. Número Máximo de Caracteres Removíveis

Você recebe duas strings s e p, onde p é uma subsequência de s. Você também recebe um array de inteiros distintos removable indexado em 0, contendo um subconjunto de índices de s (s também é indexado em 0).

Você quer escolher um inteiro k (0 <= k <= removable.length) de forma que, após remover k caracteres de s usando os primeiros k índices em removable, p ainda seja uma subsequência de s. Mais formalmente, você marcará o caractere em s[removable[i]] para cada 0 <= i < k, depois removerá todos os caracteres marcados e verificará se p ainda é uma subsequência.

Retorne o máximo k que você pode escolher de forma que p ainda seja uma subsequência de s após as remoções.

Uma subsequência de uma string é uma nova string gerada a partir da string original com alguns caracteres (pode ser nenhum) deletados sem alterar a ordem relativa dos caracteres restantes.

'''
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def is_subsequence(s, p):
            # Check if p is a subsequence of s
            iter_s = iter(s)
            return all(char in iter_s for char in p)
        
        def can_remove_k(k):
            # Create a modified version of s with the first k removable characters removed
            modified_s = list(s)
            for i in range(k):
                modified_s[removable[i]] = ''
            modified_s = ''.join(modified_s)
            return is_subsequence(modified_s, p)
        
        left, right = 0, len(removable)
        while left < right:
            mid = (left + right + 1) // 2
            if can_remove_k(mid):
                left = mid
            else:
                right = mid - 1
        return left