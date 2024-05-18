'''
2215. Encontre a diferença de duas matrizes

Dadas duas matrizes inteiras indexadas em 0nums1 e nums2, retorne uma lista answer de tamanho 2 onde:

answer[0] é uma lista de todos os números inteiros distintos nos quais nãonums1 estão presentes nums2.
answer[1] é uma lista de todos os números inteiros distintos nos quais nãonums2 estão presentes nums1.
Observe que os inteiros nas listas podem ser retornados em qualquer ordem.


Exemplo 1:

Entrada: nums1 = [1,2,3], nums2 = [2,4,6]
 Saída: [[1,3],[4,6]]
 Explicação:
 Para nums1, nums1[1] = 2 está presente em índice 0 de nums2, enquanto nums1[0] = 1 e nums1[2] = 3 não estão presentes em nums2. Portanto, resposta[0] = [1,3].
Para nums2, nums2[0] = 2 está presente no índice 1 de nums1, enquanto nums2[1] = 4 e nums2[2] = 6 não estão presentes em nums2. Portanto, resposta[1] = [4,6].
Exemplo 2:

Entrada: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
 Saída: [[3],[]]
 Explicação:
 Para nums1, nums1[2] e nums1[3] são não presente em nums2. Como nums1[2] == nums1[3], seu valor é incluído apenas uma vez e resposta[0] = [3].
Cada número inteiro em nums2 está presente em nums1. Portanto, resposta[1] = [].
 

Restrições:

1 <= nums1.length, nums2.length <= 1000
-1000 <= nums1[i], nums2[i] <= 1000
'''

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Convert the lists to sets and find the differences
        # Converte as listas em conjuntos e encontra as diferenças
        difference1 = set(nums1) - set(nums2)  
        # Elements in nums1 but not in nums2
        # Elementos em nums1, mas não em nums2
        difference2 = set(nums2) - set(nums1)  
        # Elements in nums2 but not in nums1
        # Elementos em nums2, mas não em nums1
        # Return the differences as a list of lists
        # Retorna as diferenças como uma lista de listas
        return [list(difference1), list(difference2)]