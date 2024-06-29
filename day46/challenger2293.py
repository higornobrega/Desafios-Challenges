'''

2293. Jogo Min Max
Você recebe um array de inteiros nums indexado em 0, cujo comprimento é uma potência de 2.

Aplique o seguinte algoritmo em nums:

Deixe n ser o comprimento de nums. Se n == 1, termine o processo. Caso contrário, crie um novo array de inteiros indexado em 0 newNums de comprimento n / 2.
Para cada índice par i, onde 0 <= i < n / 2, atribua o valor de newNums[i] como min(nums[2 * i], nums[2 * i + 1]).
Para cada índice ímpar i, onde 0 <= i < n / 2, atribua o valor de newNums[i] como max(nums[2 * i], nums[2 * i + 1]).
Substitua o array nums por newNums.
Repita todo o processo começando do passo 1.
Retorne o último número que permanece em nums após aplicar o algoritmo.

'''

class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        # While the length of nums is greater than 1, keep processing
        # Enquanto o comprimento de nums for maior que 1, continue processando
        while len(nums) > 1:
            new_nums = []
            # Iterate over half the length of the current nums array
            # Iterar sobre metade do comprimento do array atual nums
            for i in range(len(nums) // 2):
                if i % 2 == 0:
                    # For even indices, take the minimum of the two corresponding elements
                    # Para índices pares, pegue o mínimo dos dois elementos correspondentes
                    new_nums.append(min(nums[2 * i], nums[2 * i + 1]))
                else:
                    # For odd indices, take the maximum of the two corresponding elements
                    # Para índices ímpares, pegue o máximo dos dois elementos correspondentes
                    new_nums.append(max(nums[2 * i], nums[2 * i + 1]))
            # Replace nums with the new_nums array
            # Substitua nums pelo array new_nums
            nums = new_nums
        # Return the last remaining number
        # Retorne o último número restante
        return nums[0]