'''

1192. Conexões Críticas em uma Rede

Existem n servidores numerados de 0 a n - 1 conectados por conexões não direcionadas de servidor para servidor, formando uma rede onde connections[i] = [ai, bi] representa uma conexão entre os servidores ai e bi. Qualquer servidor pode alcançar outros servidores direta ou indiretamente através da rede.
Uma conexão crítica é uma conexão que, se removida, fará com que alguns servidores não consigam alcançar outros servidores.

Retorne todas as conexões críticas na rede em qualquer ordem.

'''
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # Create an adjacency list to represent the graph
        # Cria uma lista de adjacência para representar o grafo
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        # Initialize variables to store discovery times and the lowest discovery times reachable
        # Inicializa variáveis para armazenar tempos de descoberta e os menores tempos de descoberta alcançáveis
        discovery = [-1] * n
        low = [-1] * n
        self.time = 0
        result = []
        
        # Helper function for DFS traversal
        # Função auxiliar para travessia DFS
        def dfs(node, parent):
            if discovery[node] != -1:
                return
            discovery[node] = low[node] = self.time
            self.time += 1
            
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if discovery[neighbor] == -1:
                    dfs(neighbor, node)
                    # Update low-link values
                    # Atualiza valores de low-link
                    low[node] = min(low[node], low[neighbor])
                    # Check if the current edge is a bridge
                    # Verifica se a aresta atual é uma ponte
                    if low[neighbor] > discovery[node]:
                        result.append([node, neighbor])
                else:
                    low[node] = min(low[node], discovery[neighbor])
        
        # Start DFS from the first node
        # Inicia DFS a partir do primeiro nó
        dfs(0, -1)
        return result