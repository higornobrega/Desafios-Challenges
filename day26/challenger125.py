'''
125. Palíndromo válido

Uma frase é um palíndromo se, depois de converter todas as letras maiúsculas em minúsculas e remover todos os caracteres não alfanuméricos, for lida da mesma forma para frente e para trás. Os caracteres alfanuméricos incluem letras e números.

Dada uma string s, retorne true se for um palíndromo ou false caso contrário .
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert the string to lowercase and filter out non-alphanumeric characters
        # Converta a string para minúsculas e filtre caracteres não alfanuméricos
        filtered_s = ''.join(char.lower() for char in s if char.isalnum())
        
        # Check if the filtered string is equal to its reverse
        # Verifique se a string filtrada é igual ao seu reverso
        return filtered_s == filtered_s[::-1]