'''
414. Terceiro Número Máximo

Dado um array inteiro nums, retorne o terceiro número máximo distinto neste array. Se o terceiro máximo não existir, retorne o número máximo .

Exemplo 1:

Entrada: nums = [3,2,1]
 Saída: 1
 Explicação:
O primeiro máximo distinto é 3.
O segundo máximo distinto é 2.
O terceiro máximo distinto é 1.
Exemplo 2:

Entrada: nums = [1,2]
 Saída: 2
 Explicação:
O primeiro máximo distinto é 2.
O segundo máximo distinto é 1.
O terceiro máximo distinto não existe, então o máximo (2) é retornado.
Exemplo 3:

Entrada: nums = [2,2,3,1]
 Saída: 1
 Explicação:
O primeiro máximo distinto é 3.
O segundo máximo distinto é 2 (ambos os 2 são contados juntos, pois têm o mesmo valor).
O terceiro máximo distinto é 1.
 
Restrições:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
'''

# My Solution
# Miinha Solução
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Remover os números repetidos
        # Remove the repeated numbers
        nums_set_list=list(set(nums))
        
        # Ordena a lista
        # Sort the list
        nums_set_list.sort()
        
        # Verifica o tamanho da lista
        # Check the list size
        len_nums = len(nums_set_list)
        
        # Verifica se a lista tem menos de 3 elementos
        # Check if the list has less than 3 elements
        if len_nums<3:
            # Retorna o maior número
            # Return the largest number
            return(max(nums_set_list))
        else:    
            # Retorna o terceiro maior número
            # Return the third largest number
            return(nums_set_list[-3])