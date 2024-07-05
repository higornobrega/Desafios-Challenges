'''

1283. Encontre o menor divisor dado um limiar

Dado um array de inteiros numse um inteiro threshold, escolheremos um inteiro positivo divisor, dividiremos todo o array por ele e somaremos o resultado da divisão. Encontre o menor divisor tal que o resultado mencionado acima seja menor ou igual a threshold.

Cada resultado da divisão é arredondado para o inteiro mais próximo maior ou igual àquele elemento. (Por exemplo: 7/3 = 3e 10/2 = 5).

Os casos de teste são gerados para que haja uma resposta.

'''

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def compute_sum(divisor):
            total = 0
            for num in nums:
                total += (num + divisor - 1) // divisor
            return total
        
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if compute_sum(mid) > threshold:
                left = mid + 1
            else:
                right = mid
        return left