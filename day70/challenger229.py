'''
229. Elemento Majoritário II
Dado um array de inteiros de tamanho n, encontre todos os elementos que aparecem mais de ⌊ n/3 ⌋ vezes.

'''


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Step 1: Initialize two candidate variables and their respective counters
        # Passo 1: Inicializar duas variáveis candidatas e seus respectivos contadores
        candidate1, candidate2, count1, count2 = None, None, 0, 0

        # Step 2: First pass to find potential candidates for majority elements
        # Passo 2: Primeiro percurso para encontrar candidatos potenciais para elementos majoritários
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # Step 3: Reset counters for the second pass
        # Passo 3: Reiniciar contadores para o segundo percurso
        count1, count2 = 0, 0

        # Step 4: Count the actual occurrences of the candidates
        # Passo 4: Contar as ocorrências reais dos candidatos
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        # Step 5: Prepare the result list by checking if the candidates occur more than n/3 times
        # Passo 5: Preparar a lista de resultados verificando se os candidatos ocorrem mais de n/3 vezes
        result = []
        n = len(nums)
        if count1 > n // 3:
            result.append(candidate1)
        if count2 > n // 3:
            result.append(candidate2)

        # Step 6: Return the result list
        # Passo 6: Retornar a lista de resultados
        return result
