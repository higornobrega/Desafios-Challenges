'''

168. Título de Coluna de Planilha do Excel

Dado um número inteiro columnNumber, retorne o título correspondente da coluna conforme aparece em uma planilha do Excel.
Por exemplo:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...

'''

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # Initialize an empty string to store the resulting column title
        # Inicializa uma string vazia para armazenar o título da coluna resultante
        result = ""
        
        # Loop until the columnNumber is greater than 0
        # Loop até que o columnNumber seja maior que 0
        while columnNumber > 0:
            # Decrement columnNumber by 1 to handle 0-based indexing
            # Decrementa columnNumber em 1 para lidar com indexação baseada em 0
            columnNumber -= 1
            
            # Find the remainder when columnNumber is divided by 26
            # Encontra o resto quando columnNumber é dividido por 26
            remainder = columnNumber % 26
            
            # Convert the remainder to the corresponding letter and prepend to result
            # Converte o resto para a letra correspondente e adiciona ao início de result
            result = chr(65 + remainder) + result
            
            # Update columnNumber for the next iteration by integer division by 26
            # Atualiza columnNumber para a próxima iteração pela divisão inteira por 26
            columnNumber //= 26
        
        # Return the final column title
        # Retorna o título da coluna final
        return result