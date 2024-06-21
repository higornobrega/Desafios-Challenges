'''

1037. Boomerang Válido
Dado um array de pontos onde points[i] = [xi, yi] representa um ponto no plano X-Y, retorne verdadeiro se esses pontos formarem um boomerang.

Um boomerang é um conjunto de três pontos que são todos distintos e não estão em uma linha reta.

'''

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # Check if all three points are distinct
        # Verifica se todos os três pontos são distintos
        if points[0] == points[1] or points[1] == points[2] or points[0] == points[2]:
            return False
        
        # Function to calculate the slope between two points
        # Função para calcular a inclinação entre dois pontos
        def slope(p1, p2):
            if p1[0] == p2[0]:  # vertical line
                return float('inf')
            return (p2[1] - p1[1]) / (p2[0] - p1[0])
        
        # Calculate slopes between the points
        # Calcula as inclinações entre os pontos
        slope1 = slope(points[0], points[1])
        slope2 = slope(points[1], points[2])
        slope3 = slope(points[0], points[2])
        
        # Check if any two slopes are equal
        # Verifica se alguma das duas inclinações são iguais
        return slope1 != slope2 or slope1 != slope3