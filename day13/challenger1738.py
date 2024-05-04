'''
1738. Encontre o K-ésimo maior valor da coordenada XOR

Você recebe um 2D matrixde tamanho m x n, consistindo em números inteiros não negativos. Você também recebe um número inteiro k.

O valor da coordenada (a, b)da matriz é o XOR de todos matrix[i][j]os where 0 <= i <= a < me 0 <= j <= b < n (indexados em 0) .

Encontre o maior valor (indexado 1) de todas as coordenadas de .kthmatrix

Exemplo 1:

Entrada: matriz = [[5,2],[1,6]], k = 1
 Saída: 7
 Explicação: O valor da coordenada (0,1) é 5 XOR 2 = 7, que é o maior valor.
Exemplo 2:

Entrada: matriz = [[5,2],[1,6]], k = 2
 Saída: 5
 Explicação: O valor da coordenada (0,0) é 5 = 5, que é o segundo maior valor.
Exemplo 3:

Entrada: matriz = [[5,2],[1,6]], k = 3
 Saída: 4
 Explicação: O valor da coordenada (1,0) é 5 XOR 1 = 4, que é o terceiro maior valor.
'''

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        
        res = []                                                                
        prefix_sum = [[0]*(len(matrix[0])+1) for _ in range(0,len(matrix)+1)]   
        size_matrix = len(matrix)
        for i in range(1,size_matrix+1):
            XOR_value = 0
            size_matrix_initial =  len(matrix[0])                                                    
            for j in range(1,size_matrix_initial+1):
                XOR_value ^= matrix[i-1][j-1]                                 
                prefix_sum[i][j] = XOR_value^prefix_sum[i-1][j]                
                res.append(prefix_sum[i][j])                              
                    
        return sorted(res)[-k]       