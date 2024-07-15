'''

2748. Número de Pares Bonitos
Você recebe um array de inteiros nums indexado a partir de 0. Um par de índices i, j onde 0 <= i < j < nums.length é chamado de bonito se o primeiro dígito de nums[i] e o último dígito de nums[j] forem coprimos.

Retorne o número total de pares bonitos em nums.

Dois inteiros x e y são coprimos se não houver nenhum inteiro maior que 1 que divida ambos. Em outras palavras, x e y são coprimos se gcd(x, y) == 1, onde gcd(x, y) é o máximo divisor comum de x e y.

'''


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        # Function to find the first digit of a number
        # Função para encontrar o primeiro dígito de um número
        def first_digit(n: int) -> int:
            while n >= 10:
                n //= 10
            return n

        # Function to find the last digit of a number
        # Função para encontrar o último dígito de um número
        def last_digit(n: int) -> int:
            return n % 10

        # Function to calculate gcd without importing
        # Função para calcular o mdc sem importar
        def gcd(x: int, y: int) -> int:
            while y:
                x, y = y, x % y
            return x

        beautiful_pairs = 0  # Initialize count of beautiful pairs
        # Inicializa a contagem de pares bonitos

        n = len(nums)
        # Loop through all pairs (i, j) with 0 <= i < j < n
        # Percorre todos os pares (i, j) com 0 <= i < j < n
        for i in range(n):
            for j in range(i + 1, n):
                # Get the first digit of nums[i] and last digit of nums[j]
                # Obtém o primeiro dígito de nums[i] e o último dígito de nums[j]
                first_d = first_digit(nums[i])
                last_d = last_digit(nums[j])

                # Check if first_d and last_d are coprime
                # Verifica se first_d e last_d são coprimos
                if gcd(first_d, last_d) == 1:
                    beautiful_pairs += 1

        return beautiful_pairs
