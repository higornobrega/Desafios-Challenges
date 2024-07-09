'''

1046. Você recebe um array de inteiros chamado "stones", onde stones[i] é o peso da i-ésima pedra.

Estamos jogando um jogo com as pedras. A cada turno, escolhemos as duas pedras mais pesadas e as esmagamos juntas. Suponha que as duas pedras mais pesadas tenham pesos x e y, com x <= y. O resultado desse esmagamento é:

Se x == y, ambas as pedras são destruídas, e
Se x != y, a pedra de peso x é destruída, e a pedra de peso y tem um novo peso de y - x.
No final do jogo, resta no máximo uma pedra.

Retorne o peso da última pedra restante. Se não houver pedras restantes, retorne 0.

'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            # Ordenar as pedras em ordem decrescente
            stones.sort(reverse=True)
            
            # Pegar as duas maiores pedras
            first = stones.pop(0)
            second = stones.pop(0)
            
            if first != second:
                # Se não forem iguais, a diferença volta para a lista
                stones.append(first - second)
        
        # Retorne a última pedra restante ou 0 se não houver pedras
        return stones[0] if stones else 0