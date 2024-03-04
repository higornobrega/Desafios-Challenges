'''
2085. Count Common Words With One Occurrence
Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.

Example 1:

Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
Output: 2
Explanation:
- "leetcode" appears exactly once in each of the two arrays. We count this string.
- "amazing" appears exactly once in each of the two arrays. We count this string.
- "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not count this string.
- "as" appears once in words1, but does not appear in words2. We do not count this string.
Thus, there are 2 strings that appear exactly once in each of the two arrays.
Example 2:

Input: words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]
Output: 0
Explanation: There are no strings that appear in each of the two arrays.
Example 3:

Input: words1 = ["a","ab"], words2 = ["a","a","a","ab"]
Output: 1
Explanation: The only string that appears exactly once in each of the two arrays is "ab".
 
Constraints:

1 <= words1.length, words2.length <= 1000
1 <= words1[i].length, words2[j].length <= 30
words1[i] and words2[j] consists only of lowercase English letters.
'''

# Solution 1 - No help from the internet
# Solução 1 - Sem Ajuda da internet

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        # Initialize the variables
        # Inicializa as variáveis
        cont = 0
        repet = []
        cont_word = 0
        
        # Checking for repeated words
        # Verificando se existe palavras repetidas
        for word11 in set(words1):
            for word12 in words1:
                if word11 == word12:
                    cont_word = cont_word + 1
            if cont_word > 1:
                repet.append(word11)
            cont_word = 0

        for word21 in set(words2):
            for word22 in words2:
                if word21 == word22:
                    cont_word = cont_word + 1
            if cont_word > 1:
                repet.append(word21)
            cont_word = 0

        # Checking if the word is repeated in the 2 lists but not repeated in the list list itself
        # Verificando se a palavra se repete nas 2 listas mas não se repete na própria lista
        for word1 in words1:
            for word2 in words2:
                if word1 == word2 and word1 not in set(repet):
                    cont = cont + 1
         
        return cont
        
