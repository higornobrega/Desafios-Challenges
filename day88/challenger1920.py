'''
1920. Construir Array a partir de Permutação
Dada uma permutação nums com índice começando do zero (0-indexado), construa um array ans do mesmo tamanho, onde ans[i] = nums[nums[i]] para cada 0 <= i < nums.length e retorne-o.
Uma permutação nums com índice começando do zero é um array de inteiros distintos que vai de 0 até nums.length - 1 (inclusive).
'''


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            ans.append(nums[n])
        return ans
