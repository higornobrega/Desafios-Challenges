'''
2844. Operações Mínimas para Fazer um Número Especial

Você recebe uma string indexada em 0num representando um número inteiro não negativo.

Em uma operação, você pode escolher qualquer dígito nume excluí-lo. Observe que se você excluir todos os dígitos de num, numtorna-se 0.

Retorne o número mínimo de operações necessárias para tornar num especial .

Um número inteiro xé considerado especial se for divisível por 25.
'''

class Solution:
    def minimumOperations(self, num: str) -> int:
        """
        Calculate the minimum number of operations needed to make the number end with 00, 25, 50, or 75.
        Calcular o número mínimo de operações necessárias para que o número termine em 00, 25, 50 ou 75.
        
        :param num: A string representing a large number / Uma string representando um número grande
        :return: Minimum number of operations / Número mínimo de operações
        """
        
        # Helper function to find the position of character 'c' starting from index 'start'
        # Função auxiliar para encontrar a posição do caractere 'c' começando do índice 'start'
        def find(c, start):
            for i in range(start, -1, -1):
                if num[i] == c:
                    return i
            return -1

        N = len(num)  # Length of the input number string / Comprimento da string do número de entrada
        ans = float('inf')  # Initialize the answer to infinity / Inicializar a resposta com infinito

        # Check patterns "00", "25", "50", "75"
        # Verificar os padrões "00", "25", "50", "75"
        for pat in ["00", "25", "50", "75"]:
            j = find(pat[1], N-1)  # Find position of the second character of the pattern / Encontrar a posição do segundo caractere do padrão
            i = find(pat[0], j-1)  # Find position of the first character of the pattern / Encontrar a posição do primeiro caractere do padrão
            if 0 <= i < j:
                # Calculate the number of operations and update the minimum answer
                # Calcular o número de operações e atualizar a resposta mínima
                ans = min(ans, j-i-1 + N-1-j)

        # If no valid pattern is found, handle the special case where we need to remove all but one zero
        # Se nenhum padrão válido for encontrado, tratar o caso especial onde precisamos remover todos os zeros exceto um
        if ans == float('inf'):
            return N - num.count('0')  # Return the length of the number minus the count of '0' / Retornar o comprimento do número menos a contagem de '0'
        else:
            return ans  # Return the minimum number of operations found / Retornar o número mínimo de operações encontrado
