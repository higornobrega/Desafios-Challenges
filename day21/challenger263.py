'''
263. Número feio
Um número feio é um número inteiro positivo cujos fatores primos são limitados a 2, 3 e 5.

Dado um número inteiro n, retorne verdadeiro se n for um número feio.
'''

class Solution:
    def isUgly(self, n: int) -> bool:
        # Base case: if n is less than or equal to 0, it is not an ugly number
        # Caso base: se n for menor ou igual a 0, não é um número feio
        if n <= 0:
            return False
        
        # Prime factors to check
        # Fatores primos para verificar
        prime_factors = [2, 3, 5]
        
        # Divide n by 2, 3, and 5 as long as it is divisible by them
        # Divida n por 2, 3 e 5 enquanto for divisível por eles
        for factor in prime_factors:
            while n % factor == 0:
                n //= factor
        
        # If after division, n becomes 1, it is an ugly number
        # Se após a divisão, n se tornar 1, é um número feio
        return n == 1