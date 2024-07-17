'''

455. Distribuição de Cookies
Assuma que você é um pai incrível e quer dar alguns cookies aos seus filhos. Mas, você deve dar a cada criança no máximo um cookie.

Cada criança i tem um fator de ganância g[i], que é o tamanho mínimo de um cookie com o qual a criança ficará satisfeita; e cada cookie j tem um tamanho s[j]. Se s[j] >= g[i], podemos atribuir o cookie j à criança i, e a criança i ficará satisfeita. Seu objetivo é maximizar o número de crianças satisfeitas e retornar o número máximo.
'''


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort the greed factors of the children
        # Ordenar os fatores de ganância das crianças
        g.sort()
        # Sort the sizes of the cookies
        # Ordenar os tamanhos dos cookies
        s.sort()

        # Initialize pointers for children and cookies
        # Inicializar ponteiros para crianças e cookies
        child_i = 0
        cookie_j = 0
        # Initialize count of content children
        # Inicializar contador de crianças contentes
        content_children = 0

        # Iterate while there are children and cookies left to check
        # Iterar enquanto houver crianças e cookies restantes para verificar
        while child_i < len(g) and cookie_j < len(s):
            # If the current cookie can satisfy the current child's greed
            # Se o cookie atual puder satisfazer a ganância da criança atual
            if s[cookie_j] >= g[child_i]:
                # Increase the count of content children
                # Aumentar o contador de crianças contentes
                content_children += 1
                # Move to the next child
                # Passar para a próxima criança
                child_i += 1
            # Move to the next cookie
            # Passar para o próximo cookie
            cookie_j += 1

        # Return the number of content children
        # Retornar o número de crianças contentes
        return content_children
