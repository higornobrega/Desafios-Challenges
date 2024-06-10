'''
1177. Pode fazer palíndromo a partir de substring

Você recebe uma string s e um array queries onde . Podemos reorganizar a substring para cada consulta e então escolher até uma delas para substituir por qualquer letra minúscula do inglês. queries[i] = [lefti, righti, ki]s[lefti...righti]ki

Se for possível que a substring seja uma string de palíndromo após as operações acima, o resultado da consulta será true. Caso contrário, o resultado é false.

Retorna um array booleano answer onde answer[i] está o resultado da consulta .ith queries[i]

Observe que cada letra é contada individualmente para substituição, portanto se, por exemplo e só poderemos substituir duas das letras. Além disso, observe que nenhuma consulta modifica a string inicial .s[lefti...righti] = "aaa"ki = 2s
'''


class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        
        # Prefix sum array for character counts
        # Array de soma prefixada para contagens de caracteres
        prefix_counts = [[0] * 26 for _ in range(n + 1)]
        
        # Populate prefix counts
        # Populando contagens prefixadas
        for i in range(n):
            for j in range(26):
                prefix_counts[i + 1][j] = prefix_counts[i][j]
            prefix_counts[i + 1][ord(s[i]) - ord('a')] += 1
        
        results = []
        
        # Process each query
        # Processar cada consulta
        for left, right, k in queries:
            odd_count = 0
            for j in range(26):
                # Calculate character count for the substring
                # Calcular a contagem de caracteres para a substring
                char_count = prefix_counts[right + 1][j] - prefix_counts[left][j]
                if char_count % 2 != 0:
                    odd_count += 1
            
            # To form a palindrome, odd_count must be <= 2 * k + 1
            # Para formar um palíndromo, odd_count deve ser <= 2 * k + 1
            if odd_count // 2 <= k:
                results.append(True)
            else:
                results.append(False)
        
        return results