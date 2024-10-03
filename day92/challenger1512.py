'''
1512. Número de Pares Bons
Dado um array de números inteiros nums, retorne o número de pares bons.
Um par (i, j) é chamado de bom se nums[i] == nums[j] e i < j.
'''


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cont = 0
        for i in range(len(nums)):

            if nums[i+1:].count(nums[i]) > 0:
                cont += nums[i+1:].count(nums[i])
        return cont
