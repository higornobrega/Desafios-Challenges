'''

910. Menor Intervalo II
Você recebe um array de inteiros nums e um inteiro k.

Para cada índice i, onde 0 <= i < nums.length, altere nums[i] para ser nums[i] + k ou nums[i] - k.

A pontuação de nums é a diferença entre os elementos máximo e mínimo em nums.

Retorne a pontuação mínima de nums após alterar os valores em cada índice.

'''

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        # Sort the array to make it easier to find the minimum and maximum values
        # Ordena o array para facilitar a localização dos valores mínimo e máximo
        nums.sort()
        
        # Calculate the initial score, which is the difference between the max and min of the sorted array
        # Calcula a pontuação inicial, que é a diferença entre o máximo e o mínimo do array ordenado
        initial_score = nums[-1] - nums[0]
        
        # Initialize the result with the initial score
        # Inicializa o resultado com a pontuação inicial
        result = initial_score
        
        # Iterate through the array and try to minimize the difference
        # Itera através do array e tenta minimizar a diferença
        for i in range(len(nums) - 1):
            # Get the current max and min after adding/subtracting k
            # Obtém o máximo e o mínimo atuais após adicionar/subtrair k
            high = max(nums[i] + k, nums[-1] - k)
            low = min(nums[0] + k, nums[i + 1] - k)
            
            # Update the result with the minimum difference found
            # Atualiza o resultado com a menor diferença encontrada
            result = min(result, high - low)
        
        return result