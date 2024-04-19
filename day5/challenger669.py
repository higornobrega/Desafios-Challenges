# 669. Corte uma árvore de pesquisa binária
# Dado o rootvalor de uma árvore de pesquisa binária e os limites mais baixos e mais altos como lowe high, corte a árvore para que todos os seus elementos fiquem em [low, high]. Cortar a árvore não deve alterar a estrutura relativa dos elementos que permanecerão na árvore (ou seja, o descendente de qualquer nó deve permanecer descendente). Pode-se provar que existe uma resposta única .

# Retorne a raiz da árvore de pesquisa binária aparada . Observe que a raiz pode mudar dependendo dos limites fornecidos.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # O(n) time,
    # O(h) space,
    # Approach: dfs, divide and conquer
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if root.val < low:
            return self.trimBST(root.right, low, high)
        
        if root.val > high:
            return self.trimBST(root.left, low, high)
        
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root