'''

560. Soma de Subarray Igual a K
Dado um array de inteiros nums e um inteiro k, retorne o número total de subarrays cuja soma é igual a k.
Um subarray é uma sequência contígua e não vazia de elementos dentro de um array.

'''


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Create a dictionary to store the cumulative sum frequencies
        # Cria um dicionário para armazenar as frequências das somas cumulativas
        # Initialize with 0:1 to handle subarrays starting from the first element
        sum_freq = {0: 1}
        # Inicializa com 0:1 para lidar com subarrays que começam no primeiro elemento
        cumulative_sum = 0  # Initialize the cumulative sum
        # Inicializa a soma cumulativa
        count = 0  # Initialize the count of subarrays that sum to k
        # Inicializa a contagem de subarrays que somam k

        # Iterate through each number in the array
        # Itera por cada número no array
        for num in nums:
            cumulative_sum += num  # Update the cumulative sum
            # Atualiza a soma cumulativa

            # Check if (cumulative_sum - k) exists in the sum_freq dictionary
            # Verifica se (soma_cumulativa - k) existe no dicionário sum_freq
            if (cumulative_sum - k) in sum_freq:
                # If it exists, increment the count by the frequency of (cumulative_sum - k)
                # Se existir, incrementa a contagem pela frequência de (soma_cumulativa - k)
                count += sum_freq[cumulative_sum - k]

            # Update the frequency of the current cumulative_sum in the sum_freq dictionary
            # Atualiza a frequência da soma_cumulativa atual no dicionário sum_freq
            if cumulative_sum in sum_freq:
                sum_freq[cumulative_sum] += 1
            else:
                sum_freq[cumulative_sum] = 1

        return count  # Return the total count of subarrays that sum to k
        # Retorna a contagem total de subarrays que somam k
