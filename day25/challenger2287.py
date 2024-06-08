'''
2287. Reorganize os caracteres para formar a string alvo

Você recebe duas strings indexadas em 0 s e target. Você pode pegar algumas letras s e reorganizá-las para formar novas strings.

Retorne o número máximo de cópias target que podem ser formadas retirando cartas se reorganizando-as.
'''
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        from collections import Counter

        # Count the frequency of each character in s
        # Contar a frequência de cada caractere em s
        count_s = Counter(s)
        
        # Count the frequency of each character in target
        # Contar a frequência de cada caractere em target
        count_target = Counter(target)
        
        # Initialize the maximum number of copies as infinity
        # Inicializar a quantidade máxima de cópias como infinita
        max_copies = float('inf')
        
        # Calculate the maximum number of copies of target that can be formed
        # Calcular o número máximo de cópias de target que podem ser formadas
        for char in count_target:
            if char in count_s:
                # Update max_copies with the minimum value found
                # Atualizar max_copies com o menor valor encontrado
                max_copies = min(max_copies, count_s[char] // count_target[char])
            else:
                # If a character in target is not found in s, return 0
                # Se um caractere em target não for encontrado em s, retornar 0
                return 0
        
        # Return the maximum number of copies of target that can be formed
        # Retornar o número máximo de cópias de target que podem ser formadas
        return max_copies