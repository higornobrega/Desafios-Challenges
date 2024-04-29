'''
2294. Matriz de partição tal que a diferença máxima seja K

Você recebe uma matriz inteira numse um inteiro k. Você pode particionar numsem uma ou mais subsequências de modo que cada elemento numsapareça em exatamente uma das subsequências.

Retorne o número mínimo de subsequências necessárias para que a diferença entre os valores máximo e mínimo em cada subsequência seja no máximo k .

Uma subsequência é uma sequência que pode ser derivada de outra sequência excluindo alguns ou nenhum elemento sem alterar a ordem dos elementos restantes.

 

Exemplo 1:

Entrada: nums = [3,6,1,2,5], k = 2
 Saída: 2
 Explicação:
Podemos particionar nums nas duas subsequências [3,1,2] e [6,5].
A diferença entre o valor máximo e mínimo na primeira subsequência é 3 - 1 = 2.
A diferença entre o valor máximo e mínimo na segunda subsequência é 6 - 5 = 1.
Como foram criadas duas subsequências, retornamos 2. Pode-se mostrar que 2 é o número mínimo de subsequências necessárias.
Exemplo 2:

Entrada: nums = [1,2,3], k = 1
 Saída: 2
 Explicação:
Podemos particionar nums nas duas subsequências [1,2] e [3].
A diferença entre o valor máximo e mínimo na primeira subsequência é 2 - 1 = 1.
A diferença entre o valor máximo e mínimo na segunda subsequência é 3 - 3 = 0.
Como duas subsequências foram criadas, retornamos 2. Observe que outra solução ideal é particionar nums nas duas subsequências [1] e [2,3].
Exemplo 3:

Entrada: nums = [2,2,4,5], k = 0
 Saída: 3
 Explicação:
Podemos particionar nums nas três subsequências [2,2], [4] e [5].
A diferença entre o valor máximo e mínimo nas primeiras subsequências é 2 - 2 = 0.
A diferença entre o valor máximo e mínimo nas segundas subsequências é 4 - 4 = 0.
A diferença entre o valor máximo e mínimo nas terceiras subsequências é 5 - 5 = 0.
Como foram criadas três subsequências, retornamos 3. Pode-se mostrar que 3 é o número mínimo de subsequências necessárias.
'''

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        if not k: 
            return len(Counter(nums).keys())
        
        ck=sorted(list(Counter(nums).keys()))
        cnt=0
        i=0
        
        while i < len(ck):
            ridx = bisect.bisect_right(ck,ck[i]+k)
            if ridx == len(ck): 
                ridx -= 1
            if ck[ridx] > ck[i] + k:
                while ck[ridx] > ck[i] + k:
                    ridx -= 1
            cnt += 1
            i = ridx + 1
        return cnt