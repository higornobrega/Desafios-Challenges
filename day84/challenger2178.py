'''
2178. Divisão Máxima de Inteiros Pares Positivos
Você recebe um número inteiro finalSum. Divida-o em uma soma do maior número possível de inteiros pares positivos únicos.

Por exemplo, dado finalSum = 12, as seguintes divisões são válidas (inteiros pares positivos únicos que somam finalSum): (12), (2 + 10), (2 + 4 + 6) e (4 + 8). Entre elas, (2 + 4 + 6) contém o maior número de inteiros. Note que finalSum não pode ser dividido em (2 + 2 + 4 + 4), pois todos os números devem ser únicos.

Retorne uma lista de inteiros que representem uma divisão válida contendo o maior número de inteiros. Se não existir uma divisão válida para finalSum, retorne uma lista vazia. Você pode retornar os inteiros em qualquer ordem.

'''


class Solution:
    def maximumEvenSplit(self, finalSum: int):
        # Primeiro, verificamos se finalSum é ímpar, pois não podemos dividi-lo em números pares.
        # Se finalSum for ímpar, retornamos uma lista vazia.
        if finalSum % 2 != 0:
            return []

        # Inicializamos uma lista vazia para armazenar os números pares únicos.
        result = []
        current_even = 2  # O menor número par possível é 2.

        # Continuamos somando números pares até que finalSum não possa mais ser dividido.
        while finalSum >= current_even:
            # Adicionamos o número par atual à lista.
            result.append(current_even)
            # Subtraímos o número par atual de finalSum.
            finalSum -= current_even
            current_even += 2  # Passamos para o próximo número par.

        # Se sobrar algum valor em finalSum (o que pode acontecer no último loop),
        # adicionamos o valor restante ao último número da lista.
        if finalSum > 0:
            result[-1] += finalSum

        return result
