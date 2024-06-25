'''

1929. Concatenação de Array

Dado um array de inteiros nums de comprimento n, você quer criar um array ans de comprimento 2n onde ans[i] == nums[i] e ans[i + n] == nums[i] para 0 <= i < n (indexado a partir de 0).
Especificamente, ans é a concatenação de dois arrays nums.

Retorne o array ans.

'''
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Juntando as listas
        # Putting the lists together
        return nums+nums
    