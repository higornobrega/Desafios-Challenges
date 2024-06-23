'''
3101. Contar Subarrays Alternantes

Você recebe um array binário nums.

Chamamos um subarray de alternante se nenhum dois elementos adjacentes no subarray tiverem o mesmo valor.

Retorne o número de subarrays alternantes em nums.

'''

class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        # Variable to store the total number of alternating subarrays
        # Variável para armazenar o número total de subarrays alternantes
        total_count = 0
        
        # Variable to store the length of the current alternating subarray
        # Variável para armazenar o comprimento do subarray alternante atual
        current_length = 1
        
        # Iterate over the array starting from the second element
        # Iterar sobre o array começando do segundo elemento
        for i in range(1, len(nums)):
            # Check if the current element is different from the previous one
            # Verificar se o elemento atual é diferente do anterior
            if nums[i] != nums[i - 1]:
                # Increment the length of the current alternating subarray
                # Incrementar o comprimento do subarray alternante atual
                current_length += 1
            else:
                # Calculate the number of alternating subarrays that end at the previous element
                # Calcular o número de subarrays alternantes que terminam no elemento anterior
                total_count += (current_length * (current_length + 1)) // 2
                
                # Reset the length of the current alternating subarray to 1
                # Redefinir o comprimento do subarray alternante atual para 1
                current_length = 1
        
        # Add the count of the last alternating subarray
        # Adicionar a contagem do último subarray alternante
        total_count += (current_length * (current_length + 1)) // 2
        
        return total_count