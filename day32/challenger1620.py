'''
1620. Coordenada Com Máxima Qualidade de Rede

Você recebeu um array de torres de rede towers, onde towers[i] = [xi, yi, qi] denota a i-ésima torre de rede com localização (xi, yi) e fator de qualidade qi. Todas as coordenadas são coordenadas inteiras no plano X-Y, e a distância entre duas coordenadas é a distância Euclidiana.

Você também recebeu um inteiro radius onde uma torre é alcançável se a distância for menor ou igual a radius. Fora dessa distância, o sinal fica distorcido, e a torre não é alcançável.

A qualidade do sinal da i-ésima torre em uma coordenada (x, y) é calculada com a fórmula ⌊qi / (1 + d)⌋, onde d é a distância entre a torre e a coordenada. A qualidade da rede em uma coordenada é a soma das qualidades do sinal de todas as torres alcançáveis.

Retorne o array [cx, cy] representando a coordenada inteira (cx, cy) onde a qualidade da rede é máxima. Se houver várias coordenadas com a mesma qualidade de rede, retorne a coordenada não negativa lexicograficamente mínima.

Nota:

Uma coordenada (x1, y1) é lexicograficamente menor que (x2, y2) se:

x1 < x2, ou
x1 == x2 e y1 < y2.
⌊val⌋ é o maior inteiro menor ou igual a val (a função floor).

'''

class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        # Function to calculate the squared distance between two points (x1, y1) and (x2, y2)
        # Função para calcular a distância ao quadrado entre dois pontos (x1, y1) e (x2, y2)
        def squared_distance(x1, y1, x2, y2):
            return (x1 - x2) ** 2 + (y1 - y2) ** 2
        
        # Determine the range of coordinates to check
        # Determinar a faixa de coordenadas a verificar
        min_x = min(tower[0] for tower in towers)
        max_x = max(tower[0] for tower in towers)
        min_y = min(tower[1] for tower in towers)
        max_y = max(tower[1] for tower in towers)
        
        best_quality = -1
        best_coordinate = [0, 0]
        
        # Iterate over all possible integral coordinates in the given range
        # Iterar sobre todas as coordenadas inteiras possíveis na faixa dada
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                total_quality = 0
                for tx, ty, tq in towers:
                    sq_dist = squared_distance(x, y, tx, ty)
                    if sq_dist <= radius * radius:
                        d = sq_dist ** 0.5
                        total_quality += tq // (1 + d)
                
                # Update the best coordinate if the current total quality is higher
                # Atualizar a melhor coordenada se a qualidade total atual for maior
                if total_quality > best_quality or (total_quality == best_quality and (x < best_coordinate[0] or (x == best_coordinate[0] and y < best_coordinate[1]))):
                    best_quality = total_quality
                    best_coordinate = [x, y]
        
        return best_coordinate