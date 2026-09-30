class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def tree_height(root):
    if root is None:
        return -1
    return 1+max(tree_height(root.left),tree_height(root.right))

root=TreeNode(5)
root.left=TreeNode(3)
root.right=TreeNode(8)
root.left.left=TreeNode(1)
root.left.right=TreeNode(4)

print(tree_height(root))  #2
