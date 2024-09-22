'''
2269. Encontre a Beleza-K de um Número

A beleza-K de um número inteiro num é definida como o número de substrings de num quando ele é lido como uma string que atendem às seguintes condições:

Ela tem um comprimento de k.
Ela é um divisor de num.
Dado os inteiros num e k, retorne a beleza-K de num.

Nota:

Zeros à esquerda são permitidos.
0 não é divisor de nenhum valor.
Uma substring é uma sequência contínua de caracteres em uma string.
'''


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        # Convert the number to a string to facilitate extracting substrings
        # Converta o número para uma string para facilitar a extração de substrings
        num_str = str(num)

        # Initialize a counter for the number of valid divisors
        # Inicialize um contador para o número de divisores válidos
        count = 0

        # Iterate through the string and extract all substrings of length k
        # Itere através da string e extraia todas as substrings de comprimento k
        for i in range(len(num_str) - k + 1):
            # Get the substring of length k
            # Pegue a substring de comprimento k
            sub_str = num_str[i:i + k]

            # Convert the substring back to an integer
            # Converta a substring de volta para um inteiro
            sub_num = int(sub_str)

            # Check if the substring is a valid divisor (not zero and divides num)
            # Verifique se a substring é um divisor válido (não é zero e divide num)
            if sub_num != 0 and num % sub_num == 0:
                # If valid, increment the count
                # Se for válido, incremente o contador
                count += 1

        # Return the total count of valid divisors
        # Retorne o total de divisores válidos
        return count
