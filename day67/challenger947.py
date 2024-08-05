'''

947.A Maioria das Pedras Removidas com a Mesma Linha ou Coluna

Em um plano 2D, colocamos n pedras em alguns pontos de coordenadas inteiras. Cada ponto de coordenada pode ter no máximo uma pedra.

Uma pedra pode ser removida se compartilhar a mesma linha ou a mesma coluna com outra pedra que não foi removida.

Dado um array stones de comprimento n onde stones[i] = [xi, yi] representa a localização da i-ésima pedra, retorne o maior número possível de pedras que podem ser removidas.


'''


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # Define a helper function to find the root of a node with path compression
        # Define uma função auxiliar para encontrar a raiz de um nó com compressão de caminho
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # Define a helper function to union two nodes
        # Define uma função auxiliar para unir dois nós
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY

        parent = {}

        # Initialize the parent for each stone's row and column
        # Inicializa o pai para cada linha e coluna das pedras
        for x, y in stones:
            if x not in parent:
                parent[x] = x
            if ~y not in parent:
                parent[~y] = ~y
            union(x, ~y)

        # Count the number of unique roots
        # Conta o número de raízes únicas
        unique_roots = len({find(x) for x in parent})

        # The number of stones that can be removed is total stones minus the number of unique roots
        # O número de pedras que podem ser removidas é o total de pedras menos o número de raízes únicas
        return len(stones) - unique_roots
