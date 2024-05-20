'''
2654. Minimum Number of Operations to Make All Array Elements Equal to 1

You are given a 0-indexed array nums consisiting of positive integers. You can do the following operation on the array any number of times:

Select an index i such that 0 <= i < n - 1 and replace either of nums[i] or nums[i+1] with their gcd value.
Return the minimum number of operations to make all elements of nums equal to 1. If it is impossible, return -1.

The gcd of two integers is the greatest common divisor of the two integers.

 

Example 1:

Input: nums = [2,6,3,4]
Output: 4
Explanation: We can do the following operations:
- Choose index i = 2 and replace nums[2] with gcd(3,4) = 1. Now we have nums = [2,6,1,4].
- Choose index i = 1 and replace nums[1] with gcd(6,1) = 1. Now we have nums = [2,1,1,4].
- Choose index i = 0 and replace nums[0] with gcd(2,1) = 1. Now we have nums = [1,1,1,4].
- Choose index i = 2 and replace nums[3] with gcd(1,4) = 1. Now we have nums = [1,1,1,1].
Example 2:

Input: nums = [2,10,6,14]
Output: -1
Explanation: It can be shown that it is impossible to make all the elements equal to 1.
 
'''

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Helper function to calculate the GCD (Greatest Common Divisor)
        # Função auxiliar para calcular o MDC (Máximo Divisor Comum)
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # If there's a 1 in the list, return the number of non-1 elements
        # Se houver um 1 na lista, retorna o número de elementos diferentes de 1
        if 1 in nums:
            return len(nums) - nums.count(1)
        
        # Initialize get to a high value representing an impossible scenario
        # Inicializa 'get' com um valor alto representando um cenário impossível
        get = 100
        
        # Iterate over the list to find the minimum subarray whose GCD is 1
        # Itera sobre a lista para encontrar o subarray mínimo cujo MDC é 1
        for i in range(len(nums) - 1):
            s = nums[i]
            for j in range(i + 1, len(nums)):
                s = gcd(s, nums[j])
                if s == 1:
                    get = min(get, j - i - 1)
                    break
        
        # If get remains 100, no such subarray was found, return -1
        # Se 'get' permanecer 100, nenhum subarray foi encontrado, retorna -1
        if get == 100:
            get = -1
        else:
            # Otherwise, adjust get to include the full array length
            # Caso contrário, ajusta 'get' para incluir o comprimento total do array
            get += len(nums)
        
        return get
