'''
1991. Encontre o índice médio na matriz

Dado um array inteiro indexado em 0nums , encontre o mais à esquerda middleIndex (ou seja, o menor entre todos os possíveis).

A middleIndexé um índice onde nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].

Se middleIndex == 0, a soma do lado esquerdo é considerada 0. Da mesma forma, se middleIndex == nums.length - 1, a soma do lado direito é considerada 0.

Retorne o mais à esquerda middleIndex que satisfaça a condição ou -1se não existir tal índice .

 

Exemplo 1:

Entrada: nums = [2,3,-1, 8,4 ]
 Saída: 3
 Explicação: A soma dos números antes do índice 3 é: 2 + 3 + -1 = 4
A soma dos números após o índice 3 é: 4 = 4
Exemplo 2:

Entrada: nums = [1,-1, 4 ]
 Saída: 2
 Explicação: A soma dos números antes do índice 2 é: 1 + -1 = 0
A soma dos números após o índice 2 é: 0
Exemplo 3:

Entrada: nums = [2,5]
 Saída: -1
 Explicação: Não há middleIndex válido.
'''

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        size_nums = len(nums)
        for i in range(size_nums):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1