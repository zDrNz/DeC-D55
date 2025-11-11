class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        if not inorder or not preorder:
            return None

        root = TreeNode(preorder.pop(0))

        mid = inorder.index(root.val)

        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])

        return root