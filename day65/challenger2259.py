'''

2259. Remova o Dígito do Número para Maximizar o Resultado
Você recebe uma string "number" que representa um número inteiro positivo e um caractere "digit".

Retorne a string resultante após remover exatamente uma ocorrência de "digit" de "number" de modo que o valor da string resultante em forma decimal seja maximizado. Os casos de teste são gerados de forma que "digit" ocorra pelo menos uma vez em "number".
'''


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        # Initialize a variable to store the maximum result
        # Inicializa uma variável para armazenar o resultado máximo
        max_result = ""

        # Loop through each character in the number string
        # Itera sobre cada caractere na string number
        for i in range(len(number)):
            # Check if the current character is the digit we want to remove
            # Verifica se o caractere atual é o dígito que queremos remover
            if number[i] == digit:
                # Create a new string by removing the current digit
                # Cria uma nova string removendo o dígito atual
                new_number = number[:i] + number[i+1:]

                # Update max_result if the new number is greater
                # Atualiza max_result se o novo número for maior
                if new_number > max_result:
                    max_result = new_number

        # Return the maximum result after removing one occurrence of the digit
        # Retorna o resultado máximo após remover uma ocorrência do dígito
        return max_result
