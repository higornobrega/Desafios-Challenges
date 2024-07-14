'''

2644. Encontre a Pontuação Máxima de Divisibilidade
Você recebe dois arrays de inteiros, nums e divisors.

A pontuação de divisibilidade de divisors[i] é o número de índices j tais que nums[j] é divisível por divisors[i].

Retorne o inteiro divisors[i] com a maior pontuação de divisibilidade. Se vários inteiros tiverem a pontuação máxima, retorne o menor deles.

'''


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        # Initialize variables to keep track of the maximum score and the corresponding divisor
        # Inicializa variáveis para manter o controle da pontuação máxima e o divisor correspondente
        max_score = 0
        best_divisor = float('inf')

        # Iterate over each divisor to calculate its divisibility score
        # Itera sobre cada divisor para calcular sua pontuação de divisibilidade
        for divisor in divisors:
            score = 0
            # Calculate how many elements in nums are divisible by the current divisor
            # Calcula quantos elementos em nums são divisíveis pelo divisor atual
            for num in nums:
                if num % divisor == 0:
                    score += 1

            # Update the maximum score and the best divisor if a higher score is found
            # Atualiza a pontuação máxima e o melhor divisor se uma pontuação maior for encontrada
            if score > max_score or (score == max_score and divisor < best_divisor):
                max_score = score
                best_divisor = divisor

        # Return the divisor with the maximum divisibility score
        # Retorna o divisor com a pontuação máxima de divisibilidade
        return best_divisor
