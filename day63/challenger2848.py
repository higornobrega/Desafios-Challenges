'''

2848. Pontos que Intersectam com Carros
Você recebe uma matriz de inteiros 2D indexada a partir de 0, chamada nums, que representa as coordenadas dos carros estacionados em uma linha numérica. Para qualquer índice i, nums[i] = [starti, endi] onde starti é o ponto de início do i-ésimo carro e endi é o ponto de término do i-ésimo carro.
'''


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        # Create a set to keep track of all unique points that are covered by any car
        # Cria um conjunto para rastrear todos os pontos únicos cobertos por qualquer carro
        covered_points = set()

        # Iterate through each car's start and end points
        # Itera através dos pontos de início e fim de cada carro
        for start, end in nums:
            # Add all points from start to end (inclusive) to the set
            # Adiciona todos os pontos do início ao fim (inclusive) ao conjunto
            for point in range(start, end + 1):
                covered_points.add(point)

        # The number of unique points covered by any car is the length of the set
        # O número de pontos únicos cobertos por qualquer carro é o tamanho do conjunto
        return len(covered_points)
