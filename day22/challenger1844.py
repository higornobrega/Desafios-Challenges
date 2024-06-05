'''
1844. Substitua todos os dígitos por caracteres

Você recebe uma string indexada em 0s que possui letras minúsculas em inglês em seus índices pares e dígitos em seus índices ímpares .

Existe uma função shift(c, x), onde cé um caractere e xé um dígito, que retorna o caractere depois .xthc

Por exemplo, shift('a', 5) = 'f'e shift('x', 0) = 'x'.
Para cada  índice ímpari , você deseja substituir o dígito s[i]por shift(s[i-1], s[i]).

Retorne sapós substituir todos os dígitos. É garantido que shift(s[i-1], s[i])nunca excederá'z' .

'''

class Solution:
    def replaceDigits(self, s: str) -> str:
        # Alphabet list
        # Lista de alfabeto
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        # Loop through the string
        # Loop através da string
        for i in range(1, len(s), 2):
            # Replace the character with the new character
            # Substitua o caractere pelo novo caractere
            s = s[:i] + alphabet[alphabet.index(s[i-1]) + int(s[i])] + s[i+1:]
            
        return s