'''
2278. Percentage of Letter in String

Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent.

Example 1:

Input: s = "foobar", letter = "o"
Output: 33
Explanation:
The percentage of characters in s that equal the letter 'o' is 2 / 6 * 100% = 33% when rounded down, so we return 33.
Example 2:

Input: s = "jjjj", letter = "k"
Output: 0
Explanation:
The percentage of characters in s that equal the letter 'k' is 0%, so we return 0.
 

Constraints:

1 <= s.length <= 100
s consists of lowercase English letters.
letter is a lowercase English letter.
'''

# My Solution
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        
        # Inicialzando variável com tamanho da string
        # Initializing variabel with string size
        size_strint = len(s)
        
        # Contando a quantidade de vezes que a letra ocorre na string
        # Counting the number of times the letter occurs in the string
        count_letter = s.count(letter)
        
        # Calculando a porcentagem
        # Calculating the percentage
        percent_letter = (count_letter * 100) // size_strint
        
        return percent_letter
