class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.value,end=" ")
    inorder_traversal(root.right)

#         5
#        / \
#       3   8
#      / \
#     1   4
root=TreeNode(5)
root.left=TreeNode(3)
root.right=TreeNode(8)
root.left.left=TreeNode(1)
root.left.right=TreeNode(4)
inorder_traversal(root)    # 1 3 4 5 8