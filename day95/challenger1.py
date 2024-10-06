'''
1. Duas somas

Dado um array de inteiros nums e um inteiro target, retorne os índices dos dois números de modo que a soma deles seja target.
Você pode assumir que cada entrada teria exatamente uma solução e não pode usar o mesmo elemento duas vezes.
Você pode retornar a resposta em qualquer ordem.

'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
