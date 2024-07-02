'''

143. Reordenar Lista
Você recebe a cabeça de uma lista ligada simples. A lista pode ser representada como:

L0 → L1 → … → Ln - 1 → Ln
Reordene a lista para a seguinte forma:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
Você não pode modificar os valores nos nós da lista. Somente os próprios nós podem ser alterados.

'''
# Definition for singly-linked list.
# Definição para lista ligada simples.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        Não retorne nada, modifique o head no lugar.
        """
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the linked list
        # Passo 1: Encontre o meio da lista ligada
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the linked list
        # Passo 2: Inverta a segunda metade da lista ligada
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        # Step 3: Merge the two halves
        # Passo 3: Mescle as duas metades
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2