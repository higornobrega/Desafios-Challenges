'''

930. Subarrays Binários com Soma
Dado um array binário nums e um inteiro goal, retorne o número de subarrays não vazios com soma igual a goal.

Um subarray é uma parte contígua do array.

'''


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # Dictionary to store the count of prefix sums
        # Dicionário para armazenar a contagem das somas prefixas
        prefix_sum_count = {0: 1}  # Initialize with zero sum having count 1
        count = 0  # Initialize the count of subarrays with sum equal to goal
        current_sum = 0  # Initialize the current sum of the subarray

        for num in nums:
            current_sum += num  # Update the current sum with the current element

            # Check how many times (current_sum - goal) has appeared
            # Verificar quantas vezes (current_sum - goal) apareceu
            if current_sum - goal in prefix_sum_count:
                count += prefix_sum_count[current_sum - goal]

            # Add the current sum to the prefix sum count dictionary
            # Adicionar a soma atual ao dicionário de contagem de somas prefixas
            if current_sum in prefix_sum_count:
                prefix_sum_count[current_sum] += 1
            else:
                prefix_sum_count[current_sum] = 1

        return count
