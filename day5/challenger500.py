"""
500. Keyboard Row

Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

 

Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Example 2:

Input: words = ["omk"]
Output: []
Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]


500. Linha do teclado

Dado um array de strings words, retorne as palavras que podem ser digitadas usando letras do alfabeto em apenas uma linha do teclado americano como na imagem abaixo .

No teclado americano :

a primeira linha consiste nos caracteres "qwertyuiop",
a segunda linha consiste nos caracteres "asdfghjkl"e
a terceira linha consiste nos caracteres "zxcvbnm".
"""

class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        # Letras da primeira, segunda e terceira linha do teclado convertidas para lista
        # Letters on the first, second and third row of the keyboard converted to list
        line_one = list('qwertyuiop')
        line_two = list("asdfghjkl")
        line_three = list('zxcvbnm')
        
        # Lista para adicionar as palavras que podem ser feitas com as letras de cada linha do teclado
        # List to add the words that can be made with the letters on each line of the keyboard
        words_can_make = []
        
        # Lopping para rodar cada palavra da lista
            # Lopping to rotate each work in the list
        for word in words:
            # Convertendo a palavra em uma lista com todas as letras minúsculas e sem repetilas 
            # Converting the word into a list with all lowercase letters and without repeating them
            character_list = set(list(word.lower()))
            
            # Verificando se todas as letras da palavras estão contidas em alguma linha do teclado 
            # Checking if all the letters of the word are contained in some line of the keyboard
            if all(elemento in line_one for elemento in character_list) or all(elemento in line_two for elemento in character_list) or all(elemento in line_three for elemento in character_list):
                # Adicionando a palavra a lista
                #Adding the word to the list
                words_can_make.append(word)

        # Retornando a lista
        return words_can_make
                    
                    
print(Solution().findWords(["Hello","Alaska","Dad","Peace"]))
print(Solution().findWords(["omk"]))             
print(Solution().findWords(["adsdf","sfd"]))                     