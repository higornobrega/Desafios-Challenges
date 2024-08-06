'''
1376. Tempo Necessário para Informar Todos os Funcionários
Uma empresa tem n funcionários, cada um com um ID único que varia de 0 a n - 1. O chefe da empresa é aquele com o headID.

Cada funcionário tem um gerente direto fornecido no array manager, onde manager[i] é o gerente direto do i-ésimo funcionário, manager[headID] = -1. Além disso, é garantido que as relações de subordinação têm uma estrutura de árvore.

O chefe da empresa quer informar todos os funcionários da empresa sobre uma notícia urgente. Ele informará seus subordinados diretos, e eles informarão seus subordinados, e assim por diante até que todos os funcionários saibam da notícia urgente.

O i-ésimo funcionário precisa de informTime[i] minutos para informar todos os seus subordinados diretos (ou seja, após informTime[i] minutos, todos os seus subordinados diretos podem começar a espalhar a notícia).

Retorne o número de minutos necessários para informar todos os funcionários sobre a notícia urgente.

'''


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Create an adjacency list to represent the tree structure of employees
        # Cria uma lista de adjacência para representar a estrutura em árvore dos funcionários
        tree = [[] for _ in range(n)]
        for i in range(n):
            if manager[i] != -1:
                tree[manager[i]].append(i)

        # Depth-First Search to calculate the total time needed
        # Busca em Profundidade para calcular o tempo total necessário
        def dfs(employee_id):
            max_time = 0
            for subordinate in tree[employee_id]:
                max_time = max(max_time, dfs(subordinate))
            return max_time + informTime[employee_id]

        # Start DFS from the head of the company
        # Inicia a Busca em Profundidade a partir do chefe da empresa
        return dfs(headID)
