'''
2216. Minimum Deletions to Make Array Beautiful

You are given a 0-indexed integer array nums. The array nums is beautiful if:

nums.length is even.
nums[i] != nums[i + 1] for all i % 2 == 0.
Note that an empty array is considered beautiful.

You can delete any number of elements from nums. When you delete an element, all the elements to the right of the deleted element will be shifted one unit to the left to fill the gap created and all the elements to the left of the deleted element will remain unchanged.

Return the minimum number of elements to delete from nums to make it beautiful.
'''

class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        # Initialize an empty list to keep track of the new sequence
        # Inicializa uma lista vazia para manter a nova sequência
        st = []
        
        # Iterate over each number in the input list
        # Itera sobre cada número na lista de entrada
        for num in nums:
            # If the length of st is odd and the last element is not equal to the current num, append the current num
            # Se o comprimento de st for ímpar e o último elemento não for igual ao número atual, adiciona o número atual
            if len(st) % 2 != 0:
                if st[-1] != num:
                    st.append(num)
            else:
                # Otherwise, just append the current num
                # Caso contrário, apenas adiciona o número atual
                st.append(num)
        
        # If the length of st is odd, remove the last element to make it even
        # Se o comprimento de st for ímpar, remove o último elemento para torná-lo par
        if len(st) % 2 != 0:
            st.pop()
        
        # Return the difference between the original list length and the new list length
        # Retorna a diferença entre o comprimento da lista original e o comprimento da nova lista
        return len(nums) - len(st)