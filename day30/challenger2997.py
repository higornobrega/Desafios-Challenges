'''
1239. Comprimento Máximo de uma String Concatenada com Caracteres Únicos
Você recebe um array de strings arr. Uma string s é formada pela concatenação de uma subsequência de arr que possui caracteres únicos.

Retorne o comprimento máximo possível de s.

Uma subsequência é um array que pode ser derivado de outro array excluindo alguns ou nenhum elemento sem alterar a ordem dos elementos restantes.
'''

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # Helper function to check if a string has all unique characters
        # Função auxiliar para verificar se uma string tem todos os caracteres únicos
        def is_unique(s: str) -> bool:
            return len(s) == len(set(s))
        
        # Function to perform backtracking
        # Função para realizar backtracking
        def backtrack(index: int, current: str) -> int:
            # If the current string does not have unique characters, return 0
            # Se a string atual não tiver caracteres únicos, retorna 0
            if not is_unique(current):
                return 0
            
            # The maximum length is initially the length of the current string
            # O comprimento máximo é inicialmente o comprimento da string atual
            max_length = len(current)