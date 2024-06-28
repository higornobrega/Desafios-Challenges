'''

2070. Item Mais Bonito para Cada Consulta
Você recebe um array bidimensional de inteiros items onde items[i] = [pricei, beautyi] denota o preço e a beleza de um item, respectivamente.

Você também recebe um array de inteiros queries indexado em 0. Para cada queries[j], você deseja determinar a beleza máxima de um item cujo preço seja menor ou igual a queries[j]. Se nenhum item desse tipo existir, a resposta para essa consulta é 0.

Retorne um array answer do mesmo comprimento que queries, onde answer[j] é a resposta para a j-ésima consulta.

'''


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Sort items by price
        # Ordenar itens por preço
        items.sort()
        
        # Create a list to store the maximum beauty for each query
        # Criar uma lista para armazenar a beleza máxima para cada consulta
        results = []
        
        # Sort the queries while keeping track of their original indices
        # Ordenar as consultas enquanto rastreia seus índices originais
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        
        max_beauty = 0
        j = 0
        n = len(items)
        
        # Iterate through the sorted queries
        # Iterar através das consultas ordenadas
        for query, original_index in sorted_queries:
            # While there are items with price <= query, update max_beauty
            # Enquanto houver itens com preço <= consulta, atualizar max_beauty
            while j < n and items[j][0] <= query:
                max_beauty = max(max_beauty, items[j][1])
                j += 1
            
            # Store the result in the original query's index
            # Armazenar o resultado no índice original da consulta
            results.append((original_index, max_beauty))
        
        # Sort results by original index to restore the order
        # Ordenar os resultados pelo índice original para restaurar a ordem
        results.sort()
        
        # Extract the answers in the correct order
        # Extrair as respostas na ordem correta
        return [res[1] for res in results]