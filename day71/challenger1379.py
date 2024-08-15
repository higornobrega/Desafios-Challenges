'''
1379.Encontre um Nó Correspondente de uma Árvore Binária em um Clone Dessa Árvore
Dadas duas árvores binárias, original e clonada, e uma referência a um nó alvo na árvore original.

A árvore clonada é uma cópia da árvore original.

Retorne uma referência para o mesmo nó na árvore clonada.

Observe que você não tem permissão para alterar nenhuma das duas árvores ou o nó alvo, e a resposta deve ser uma referência a um nó na árvore clonada.

'''

# Definition for a binary tree node.
# Definição para um nó de árvore binária.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # Base case: if the current node in the cloned tree is None, return None
        # Caso base: se o nó atual na árvore clonada é None, retorne None
        if not cloned:
            return None

        # If the current node in the cloned tree has the same value as the target node, return it
        # Se o nó atual na árvore clonada tem o mesmo valor que o nó alvo, retorne-o
        if cloned.val == target.val:
            return cloned

        # Recur on the left subtree
        # Recursão na subárvore esquerda
        left_result = self.getTargetCopy(original.left, cloned.left, target)
        if left_result:  # If we found the target in the left subtree, return it
            # Se encontramos o alvo na subárvore esquerda, retorne-o
            return left_result

        # Recur on the right subtree
        # Recursão na subárvore direita
        return self.getTargetCopy(original.right, cloned.right, target)
