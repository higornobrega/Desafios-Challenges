'''

2611. Ratos e Queijo

Há dois ratos e n diferentes tipos de queijo, cada tipo de queijo deve ser comido por exatamente um rato.
Um ponto do queijo com índice i (indexado a partir de 0) é:

reward1[i] se o primeiro rato comê-lo.
reward2[i] se o segundo rato comê-lo.
Você recebe um array de inteiros positivos reward1, um array de inteiros positivos reward2 e um inteiro não negativo k.

Retorne o máximo de pontos que os ratos podem alcançar se o primeiro rato comer exatamente k tipos de queijo.
'''
class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        # Calculate the initial total points if all cheeses were eaten by the second mouse
        # Calcular os pontos totais iniciais se todos os queijos fossem comidos pelo segundo rato
        total_points = sum(reward2)
        
        # Calculate the difference in points if the first mouse eats the cheese instead of the second mouse
        # Calcular a diferença nos pontos se o primeiro rato comer o queijo em vez do segundo rato
        diff = [reward1[i] - reward2[i] for i in range(len(reward1))]
        
        # Sort the differences in descending order
        # Ordenar as diferenças em ordem decrescente
        diff.sort(reverse=True)
        
        # Add the top k differences to the total points
        # Adicionar as k maiores diferenças aos pontos totais
        total_points += sum(diff[:k])
        
        return total_points  # Return the maximum total points / Retornar os pontos totais máximos