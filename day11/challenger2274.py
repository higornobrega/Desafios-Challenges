'''
2274. Máximo de Pisos Consecutivos Sem Pisos Especiais

Alice administra uma empresa e alugou alguns andares de um prédio para escritórios. Alice decidiu que alguns desses pisos deveriam ser pisos especiais , usados ​​apenas para relaxamento.

Você recebe dois inteiros bottome top, que indicam que Alice alugou todos os andares de bottomaté top( inclusive ). Você também recebe o array inteiro special, onde special[i]denota um piso especial que Alice designou para relaxamento.

Retorna o número máximo de andares consecutivos sem piso especial .

Exemplo 1:

Entrada: inferior = 2, superior = 9, especial = [4,6]
 Saída: 3
 Explicação: A seguir estão os intervalos (inclusive) de andares consecutivos sem piso especial:
- (2, 3) com um total de 2 pisos.
- (5, 5) com valor total de 1 piso.
- (7, 9) com um total de 3 pisos.
Portanto, retornamos o número máximo que é de 3 andares.
Exemplo 2:

Entrada: inferior = 6, superior = 8, especial = [7,6,8]
 Saída: 0
 Explicação: Cada andar alugado é um andar especial, então retornamos 0.
 

Restrições:

1 <= special.length <= 105
1 <= bottom <= special[i] <= top <= 109
Todos os valores de specialsão únicos.
'''


class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        
        special.sort()
        maxfloor=0
        
        for i in range(len(special)-1):
            maxfloor=max(maxfloor,special[i+1]-special[i])
        
        return max(special[0]-bottom,maxfloor-1,top-special[len(special)-1])