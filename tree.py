# Example of binary tree implementation
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Creating a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
