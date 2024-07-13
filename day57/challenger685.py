'''

685. Conexão Redundante II
Neste problema, uma árvore enraizada é um grafo direcionado tal que existe exatamente um nó (a raiz) para o qual todos os outros nós são descendentes desse nó, além de que cada nó tem exatamente um pai, exceto o nó raiz, que não tem pais.

A entrada fornecida é um grafo direcionado que começou como uma árvore enraizada com n nós (com valores distintos de 1 a n), com uma aresta direcionada adicional adicionada. A aresta adicionada tem dois vértices diferentes escolhidos de 1 a n e não era uma aresta que já existia.

O grafo resultante é dado como um array 2D de arestas. Cada elemento das arestas é um par [ui, vi] que representa uma aresta direcionada conectando os nós ui e vi, onde ui é pai do filho vi.

Retorne uma aresta que pode ser removida para que o grafo resultante seja uma árvore enraizada de n nós. Se houver múltiplas respostas, retorne a resposta que ocorre por último no array 2D fornecido.

'''


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        # Helper function to find the root parent of a node
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]

        n = len(edges)
        parent = list(range(n + 1))
        candidate1, candidate2 = None, None
        node_parent = {}

        # Step 1: Check for a node with two parents
        for u, v in edges:
            if v in node_parent:
                candidate1 = [node_parent[v], v]
                candidate2 = [u, v]
                break
            node_parent[v] = u

        # Union-Find to detect cycle
        parent = list(range(n + 1))

        def union(x, y):
            rootX = find(parent, x)
            rootY = find(parent, y)
            if rootX != rootY:
                parent[rootX] = rootY
                return True
            return False

        # If there's a node with two parents, ignore candidate2 first
        if candidate2:
            edges.remove(candidate2)

        # Step 2: Detect cycle
        for u, v in edges:
            if not union(u, v):
                if candidate1:
                    return candidate1
                return [u, v]

        # If we ignored candidate2 and no cycle found, return candidate2
        return candidate2
