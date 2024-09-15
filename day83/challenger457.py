'''
457. Ciclo em Array Circular
Você está jogando um jogo que envolve um array circular de inteiros não nulos, nums. Cada nums[i] denota o número de índices que você deve mover para frente/para trás se estiver localizado no índice i:

Se nums[i] for positivo, mova-se nums[i] passos para frente, e
Se nums[i] for negativo, mova-se nums[i] passos para trás.
Como o array é circular, você pode assumir que mover-se para frente a partir do último elemento leva você ao primeiro elemento, e mover-se para trás a partir do primeiro elemento leva você ao último.

Um ciclo no array consiste em uma sequência de índices seq de comprimento k, onde:

Seguindo as regras de movimento acima, resulta na sequência de índices repetida: seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ....
Todos os nums[seq[j]] são ou todos positivos ou todos negativos.
k > 1.
Retorne true se houver um ciclo em nums, ou false caso contrário.

'''


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        # Helper function to find the next index in a circular array
        # Função auxiliar para encontrar o próximo índice em um array circular
        def next_index(nums, current):
            n = len(nums)
            return (current + nums[current]) % n

        # Iterate over each element in the array to check for possible cycles
        # Itera sobre cada elemento no array para verificar possíveis ciclos
        for i in range(len(nums)):
            # We need to ignore elements that are already visited or form a single element loop
            # Precisamos ignorar elementos que já foram visitados ou formam um ciclo de um único elemento
            if nums[i] == 0:
                continue

            # Initialize slow and fast pointers
            # Inicializa ponteiros lentos e rápidos
            slow, fast = i, next_index(nums, i)

            # Check if both pointers move in the same direction (either both forward or both backward)
            # Verifica se ambos os ponteiros se movem na mesma direção (ambos para frente ou ambos para trás)
            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[next_index(nums, fast)] > 0:
                # If the slow and fast pointers meet, we have found a cycle
                # Se os ponteiros lento e rápido se encontrarem, encontramos um ciclo
                if slow == fast:
                    # Check if the cycle is longer than 1 (to avoid self-loop)
                    # Verifica se o ciclo é maior que 1 (para evitar ciclos de um único elemento)
                    if slow == next_index(nums, slow):
                        break
                    return True

                # Move the slow pointer by 1 step and the fast pointer by 2 steps
                # Move o ponteiro lento 1 passo e o ponteiro rápido 2 passos
                slow = next_index(nums, slow)
                fast = next_index(nums, next_index(nums, fast))

            # Mark all elements in the path as visited by setting them to 0
            # Marca todos os elementos no caminho como visitados, definindo-os como 0
            slow = i
            sign = nums[i]
            while nums[slow] * sign > 0:
                next_slow = next_index(nums, slow)
                nums[slow] = 0  # Mark the current index as visited
                slow = next_slow

        # If no cycle is found, return False
        # Se nenhum ciclo for encontrado, retorna False
        return False
