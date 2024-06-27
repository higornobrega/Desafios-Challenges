'''

852. Índice do Pico em um Array de Montanha

Você recebe um array de montanha arr de comprimento n, onde os valores aumentam até um elemento de pico e depois diminuem.

Retorne o índice do elemento de pico.

Sua tarefa é resolver isso com uma complexidade de tempo de O(log(n)).

'''

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # Set initial left and right pointers
        # Define os ponteiros iniciais à esquerda e à direita
        left, right = 0, len(arr) - 1
        
        # Perform binary search
        # Realiza a busca binária
        while left < right:
            # Find the middle index
            # Encontra o índice do meio
            mid = (left + right) // 2
            
            # If the middle element is less than the next element,
            # the peak must be on the right half
            # Se o elemento do meio for menor que o próximo elemento,
            # o pico deve estar na metade direita
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                # If the middle element is greater than or equal to the next element,
                # the peak must be on the left half or it is the mid element
                # Se o elemento do meio for maior ou igual ao próximo elemento,
                # o pico deve estar na metade esquerda ou é o próprio elemento do meio
                right = mid
        
        # Left will be pointing to the peak element index
        # 'Left' estará apontando para o índice do elemento de pico
        return left
