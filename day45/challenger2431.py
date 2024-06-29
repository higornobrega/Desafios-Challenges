'''

2341. Número Máximo de Pares em um Array
Você recebe um array de inteiros nums indexado em 0. Em uma operação, você pode fazer o seguinte:

Escolha dois inteiros em nums que sejam iguais.
Remova ambos os inteiros de nums, formando um par.
A operação é realizada em nums tantas vezes quanto possível.

Retorne um array de inteiros answer indexado em 0 de tamanho 2, onde answer[0] é o número de pares que foram formados e answer[1] é o número de inteiros restantes em nums após realizar a operação o máximo de vezes possível.

'''

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        # Create a dictionary to count occurrences of each number
        # Cria um dicionário para contar as ocorrências de cada número
        count = {}
        
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        pairs = 0
        leftovers = 0
        
        # Count pairs and leftovers
        # Conta os pares e os restos
        for value in count.values():
            pairs += value // 2
            leftovers += value % 2
        
        return [pairs, leftovers]