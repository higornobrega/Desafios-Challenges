'''
628. Produto Máximo de Três Números
Dado um array de inteiros nums, encontre três números cujo produto seja o máximo e retorne o produto máximo.

'''


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Sort the array in ascending order
        # Ordena o array em ordem crescente
        nums.sort()

        # Option 1: Product of the three largest numbers
        # Opção 1: Produto dos três maiores números
        max_product_option_1 = nums[-1] * nums[-2] * nums[-3]

        # Option 2: Product of the two smallest numbers (which could be negative)
        # and the largest number
        # Opção 2: Produto dos dois menores números (que podem ser negativos)
        # e o maior número
        max_product_option_2 = nums[0] * nums[1] * nums[-1]

        # Return the maximum of the two options
        # Retorna o maior valor entre as duas opções
        return max(max_product_option_1, max_product_option_2)
