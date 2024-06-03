'''
203. Remover elementos da lista vinculada

Dado o head valor de uma lista vinculada e um número inteiro val, remova todos os nós da lista vinculada que possui Node.val == val e retorne o novo cabeçalho.
'''



# Definition for singly-linked list.
# Definição para lista encadeada simples.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution class
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases such as removing the head node
        # Crie um nó dummy para lidar com casos especiais, como remover o nó cabeça
        dummy = ListNode(next=head)
        # Initialize current and previous pointers
        # Inicialize os ponteiros current e previous
        current = head
        previous = dummy
        
        # Iterate through the list
        # Itere pela lista
        while current:
            # If the current node's value is the target value
            # Se o valor do nó atual for o valor alvo
            if current.val == val:
                # Skip the current node by linking previous node to the next node
                # Pule o nó atual ligando o nó anterior ao próximo nó
                previous.next = current.next
            else:
                # Move the previous pointer to the current node
                # Mova o ponteiro anterior para o nó atual
                previous = current
            # Move the current pointer to the next node
            # Mova o ponteiro atual para o próximo nó
            current = current.next
        
        # Return the new head of the list, which is next of dummy node
        # Retorne a nova cabeça da lista, que é o próximo do nó dummy
        return dummy.next