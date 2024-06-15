'''
2899. Últimos Inteiros Visitados
Dado um array de inteiros nums, onde nums[i] é um inteiro positivo ou -1. Precisamos encontrar, para cada -1, o respectivo inteiro positivo, que chamamos de último inteiro visitado.

Para alcançar esse objetivo, vamos definir dois arrays vazios: seen e ans.

Comece iterando desde o início do array nums.

Se um inteiro positivo for encontrado, adicione-o à frente de seen.
Se um -1 for encontrado, deixe k ser o número de -1s consecutivos vistos até agora (incluindo o -1 atual).
Se k for menor ou igual ao comprimento de seen, adicione o k-ésimo elemento de seen a ans.
Se k for estritamente maior que o comprimento de seen, adicione -1 a ans.
Retorne o array ans.
'''


class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        # Initialize the seen list to keep track of positive integers
        seen = []
        # Initialize the ans list to keep track of the result
        ans = []
        # Counter for consecutive -1s
        k = 0
        
        # Iterate through each number in the input list
        for num in nums:
            if num != -1:
                # If the number is a positive integer, prepend it to the seen list
                seen.insert(0, num)
                # Reset the counter for consecutive -1s
                k = 0
            else:
                # If the number is -1, increment the counter for consecutive -1s
                k += 1
                # Check if the current count of consecutive -1s is less than or equal to the length of the seen list
                if k <= len(seen):
                    # If yes, append the k-th element from the seen list to ans
                    ans.append(seen[k - 1])
                else:
                    # If no, append -1 to ans
                    ans.append(-1)
        
        # Return the resulting list
        return ans