'''

2451. Diferença de String Ímpar
Você recebe um array de strings de comprimento igual, words. Suponha que o comprimento de cada string seja n.

Cada string words[i] pode ser convertida em um array de inteiros de diferença difference[i] de comprimento n - 1, onde difference[i][j] = words[i][j+1] - words[i][j], onde 0 <= j <= n - 2. Note que a diferença entre duas letras é a diferença entre suas posições no alfabeto, ou seja, a posição de 'a' é 0, 'b' é 1 e 'z' é 25.

Por exemplo, para a string "acb", o array de inteiros de diferença é [2 - 0, 1 - 2] = [2, -1].
Todas as strings em words têm o mesmo array de inteiros de diferença, exceto uma. Você deve encontrar essa string.

Retorne a string em words que possui um array de inteiros de diferença diferente.
'''


class Solution:
    def oddString(self, words: List[str]) -> str:
        # Calculate the difference integer array for each string in words
        # Calcula a diferença do array de inteiros para cada string em words
        def difference_array(word):
            return [ord(word[i+1]) - ord(word[i]) for i in range(len(word) - 1)]

        # Create a list of difference arrays for all strings in words
        # Cria uma lista de arrays de diferenças para todas as strings em words
        differences = [difference_array(word) for word in words]

        # Identify the unique difference array
        # Identifica o array de diferença único
        for diff in differences:
            if differences.count(diff) == 1:
                # Find the corresponding string with the unique difference array
                # Encontra a string correspondente com o array de diferença único
                return words[differences.index(diff)]

        # Default return in case no unique difference array is found
        # Retorno padrão caso nenhum array de diferença único seja encontrado
        return None
