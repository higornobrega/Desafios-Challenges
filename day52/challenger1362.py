'''

1362. Divisores Mais Próximos
Dado um número inteiro num, encontre os dois inteiros mais próximos em diferença absoluta cujo produto seja igual a num + 1 ou num + 2.

Retorne os dois inteiros em qualquer ordem.

'''
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        # Defina uma função para encontrar os divisores mais próximos de um determinado número
        def find_closest_divisors(n: int) -> List[int]:
            # Inicialize o melhor par com uma diferença grande
            best_pair = [1, n]
            # Comece a verificar a partir da raiz quadrada de n até 1
            sqrt_n = int(n ** 0.5)  # Calcula a raiz quadrada de n
            for i in range(sqrt_n, 0, -1):
                if n % i == 0:
                    # Se i é um divisor, encontre o par correspondente (i, n // i)
                    pair = [i, n // i]
                    # Verifique se este par é mais próximo do que o par atual melhor
                    if abs(pair[0] - pair[1]) < abs(best_pair[0] - best_pair[1]):
                        best_pair = pair
            return best_pair
        
        # Verifique os divisores mais próximos para num + 1 e num + 2
        closest_for_num_plus_1 = find_closest_divisors(num + 1)
        closest_for_num_plus_2 = find_closest_divisors(num + 2)
        
        # Compare os resultados e retorne o par com a menor diferença
        if abs(closest_for_num_plus_1[0] - closest_for_num_plus_1[1]) < abs(closest_for_num_plus_2[0] - closest_for_num_plus_2[1]):
            return closest_for_num_plus_1
        else:
            return closest_for_num_plus_2