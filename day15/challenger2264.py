'''
2264. Maior número de 3 mesmos dígitos em string

Você recebe uma string numque representa um número inteiro grande. Um número inteiro é bom se atender às seguintes condições:

É uma substring de numcomprimento 3.
Consiste em apenas um dígito único.
Retorne o número inteiro válido máximo como uma string ou uma string vazia ""se tal número inteiro não existir .

Observação:

Uma substring é uma sequência contígua de caracteres dentro de uma string.
Pode haver zeros à esquerda ou numum bom número inteiro.
'''

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # Loop through digits from 9 to 0
        # Loop de 9 a 0
        for i in range(9, -1, -1):
            # Create a candidate string with three identical digits
            # Cria uma string candidata com três dígitos idênticos
            cdd = str(i) * 3
            # Check if the candidate is in the input string
            # Verifica se a candidata está na string de entrada
            if cdd in num:
                # Return the candidate if found
                # Retorna a candidata se encontrada
                return cdd
        # Return an empty string if no candidate is found
        # Retorna uma string vazia se nenhuma candidata for encontrada
        return ""