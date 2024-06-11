'''
205. Cordas Isomórficas

Dadas duas strings s e t, determine se elas são isomórficas.

Duas strings s e t são isomórficas se os caracteres in s puderem ser substituídos para get t.

Todas as ocorrências de um caractere devem ser substituídas por outro caractere, preservando a ordem dos caracteres. Não há dois personagens que possam mapear para o mesmo personagem, mas um personagem pode mapear para si mesmo.

'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Create two dictionaries to store the mapping of characters
        # Crie dois dicionários para armazenar o mapeamento dos caracteres
        s_to_t = {}
        t_to_s = {}

        # Iterate through characters of both strings
        # Iterar pelos caracteres de ambas as strings
        for char_s, char_t in zip(s, t):
            # If there is already a mapping for char_s
            # Se já houver um mapeamento para char_s
            if char_s in s_to_t:
                # Check if it maps to the correct char_t
                # Verifique se ele mapeia para o char_t correto
                if s_to_t[char_s] != char_t:
                    return False
            else:
                # Create a new mapping from char_s to char_t
                # Crie um novo mapeamento de char_s para char_t
                s_to_t[char_s] = char_t

            # If there is already a mapping for char_t
            # Se já houver um mapeamento para char_t
            if char_t in t_to_s:
                # Check if it maps to the correct char_s
                # Verifique se ele mapeia para o char_s correto
                if t_to_s[char_t] != char_s:
                    return False
            else:
                # Create a new mapping from char_t to char_s
                # Crie um novo mapeamento de char_t para char_s
                t_to_s[char_t] = char_s

        # If all characters were mapped correctly, return True
        # Se todos os caracteres foram mapeados corretamente, retorne True
        return True