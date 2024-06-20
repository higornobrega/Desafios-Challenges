'''
138. Copiar Lista com Ponteiro Aleatório
É dada uma lista ligada de comprimento n, onde cada nó contém um ponteiro aleatório adicional, que pode apontar para qualquer nó na lista ou ser nulo.

Construa uma cópia profunda da lista. A cópia profunda deve consistir exatamente em n novos nós, onde cada novo nó tem seu valor definido para o valor do nó original correspondente. Tanto o ponteiro next quanto o ponteiro aleatório dos novos nós devem apontar para novos nós na lista copiada, de modo que os ponteiros na lista original e na lista copiada representem o mesmo estado da lista. Nenhum dos ponteiros na nova lista deve apontar para nós na lista original.

Por exemplo, se houver dois nós X e Y na lista original, onde X.random --> Y, então para os dois nós correspondentes x e y na lista copiada, x.random --> y.

Retorne o nó head da lista ligada copiada.

A lista ligada é representada na entrada/saída como uma lista de n nós. Cada nó é representado como um par de [val, random_index], onde:

val: um inteiro representando Node.val
random_index: o índice do nó (intervalo de 0 a n-1) para o qual o ponteiro aleatório aponta, ou nulo se não apontar para nenhum nó.
Seu código receberá apenas o nó head da lista ligada original.
'''

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Create a mapping from original nodes to their copies
        # Criar um mapeamento dos nós originais para suas cópias
        old_to_new = {}

        # Step 1: Create a copy of each node and store it in the hashmap
        # Passo 1: Criar uma cópia de cada nó e armazená-la no hashmap
        current = head
        while current:
            copy = Node(current.val)
            old_to_new[current] = copy
            current = current.next

        # Step 2: Assign next and random pointers for the copied nodes
        # Passo 2: Atribuir ponteiros next e random para os nós copiados
        current = head
        while current:
            copy = old_to_new[current]
            if current.next:
                copy.next = old_to_new[current.next]
            if current.random:
                copy.random = old_to_new[current.random]
            current = current.next
        
        # Return the head node of the copied list
        # Retornar o nó head da lista copiada
        return old_to_new[head]