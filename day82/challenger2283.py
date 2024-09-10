'''
2283. Verifique se o Número Tem Contagem de Dígitos Igual ao Valor do Dígito
Você recebe uma string num indexada em 0 de comprimento n, consistindo de dígitos. Retorne true se, para cada índice i no intervalo 0 <= i < n, o dígito i ocorrer num[i] vezes em num, caso contrário, retorne false.

'''


class Solution:
    def digitCount(self, num: str) -> bool:
        # Create a frequency array to store the count of each digit (0-9)
        # Crie um array de frequência para armazenar a contagem de cada dígito (0-9)
        digit_count = [0] * 10

        # Count the occurrences of each digit in the string num
        # Conte as ocorrências de cada dígito na string num
        for digit in num:
            digit_count[int(digit)] += 1

        # Check if the digit count matches the value at each index in num
        # Verifique se a contagem de dígitos corresponde ao valor em cada índice de num
        for i in range(len(num)):
            if digit_count[i] != int(num[i]):
                # If any digit count does not match, return False
                # Se qualquer contagem de dígitos não corresponder, retorne False
                return False

        # If all checks pass, return True
        # Se todas as verificações forem satisfeitas, retorne True
        return True
