class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left)+count_nodes(root.right)

root=TreeNode(5)
root.left=TreeNode(3)
root.right=TreeNode(8)
root.left.left=TreeNode(1)
root.left.right=TreeNode(4)
print(count_nodes(root))  #5