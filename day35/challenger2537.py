'''

2537. Conte o Número de Subarrays Bons

Dado um array de inteiros nums e um inteiro k, retorne o número de subarrays bons de nums.
Um subarray arr é bom se houver pelo menos k pares de índices (i, j) tais que i < j e arr[i] == arr[j].

Um subarray é uma sequência contígua não vazia de elementos dentro de um array.

'''
class Solution:
    def countGood(self, nums, k):
        # Dictionary to keep track of frequency of each number
        # Dicionário para rastrear a frequência de cada número
        count = {}
        
        # Pointers for the sliding window
        # Ponteiros para a janela deslizante
        left = 0
        num_pairs = 0
        good_subarray_count = 0
        
        # Iterate over the array with the right pointer
        # Iterar sobre o array com o ponteiro direito
        for right in range(len(nums)):
            # If the number is not in the dictionary, initialize its count to 0
            # Se o número não está no dicionário, inicializar sua contagem em 0
            if nums[right] not in count:
                count[nums[right]] = 0
            
            # Add the current number to the frequency dictionary
            # Adicionar o número atual ao dicionário de frequência
            num_pairs += count[nums[right]]
            count[nums[right]] += 1
            
            # While the current window has at least k pairs
            # Enquanto a janela atual tiver pelo menos k pares
            while num_pairs >= k:
                # Count subarrays ending at `right` starting from each position up to `left`
                # Contar subarrays terminando em `right` começando de cada posição até `left`
                good_subarray_count += len(nums) - right
                
                # Remove the leftmost number from the window
                # Remover o número mais à esquerda da janela
                count[nums[left]] -= 1
                num_pairs -= count[nums[left]]
                
                # If the count of the number at `left` becomes 0, remove it from the dictionary
                # Se a contagem do número em `left` se tornar 0, removê-lo do dicionário
                if count[nums[left]] == 0:
                    del count[nums[left]]
                
                left += 1
        
        return good_subarray_count