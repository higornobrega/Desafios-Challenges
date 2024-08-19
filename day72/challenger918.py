'''

918. Soma Máxima de Subarray Circular
Dado um array circular de inteiros chamado nums com comprimento n, retorne a soma máxima possível de um subarray não vazio de nums.

Um array circular significa que o final do array se conecta ao início do array. Formalmente, o próximo elemento de nums[i] é nums[(i + 1) % n] e o elemento anterior de nums[i] é nums[(i - 1 + n) % n].

Um subarray pode incluir cada elemento do buffer fixo nums no máximo uma vez. Formalmente, para um subarray nums[i], nums[i + 1], ..., nums[j], não existe i <= k1, k2 <= j com k1 % n == k2 % n.

'''


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Function to find the maximum sum of a non-circular subarray
        # Função para encontrar a soma máxima de um subarray não circular
        def kadane(nums):
            max_ending_here = max_so_far = nums[0]
            # Iterate over the array, starting from the second element
            # Iterar sobre o array, começando pelo segundo elemento
            for num in nums[1:]:
                # Update the maximum sum ending at the current position
                # Atualizar a soma máxima terminando na posição atual
                max_ending_here = max(num, max_ending_here + num)
                # Update the global maximum sum found so far
                # Atualizar a soma máxima global encontrada até agora
                max_so_far = max(max_so_far, max_ending_here)
            return max_so_far

        # Case 1: Find the maximum sum of a non-circular subarray
        # Caso 1: Encontrar a soma máxima de um subarray não circular
        max_kadane = kadane(nums)

        # Case 2: Find the maximum sum of a circular subarray
        # Caso 2: Encontrar a soma máxima de um subarray circular
        total_sum = sum(nums)
        # Invert the signs of the elements to find the minimum subarray sum
        # Inverter os sinais dos elementos para encontrar a soma mínima do subarray
        for i in range(len(nums)):
            nums[i] = -nums[i]

        # If the maximum sum of the inverted array is equal to the negative of the total sum,
        # it means all elements are negative, so we should return the result of Case 1.
        # Se a soma máxima do array invertido for igual ao negativo da soma total,
        # isso significa que todos os elementos são negativos, então devemos retornar o resultado do Caso 1.
        max_circular = total_sum + kadane(nums)

        # Return the maximum value between Case 1 and Case 2, unless all elements are negative
        # Retornar o valor máximo entre Caso 1 e Caso 2, a menos que todos os elementos sejam negativos
        if max_circular == 0:
            return max_kadane
        else:
            return max(max_kadane, max_circular)
