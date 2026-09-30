class TreeNode:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

def max_depth_iterative(root):
    if root is None:
        return 0
    queue=[root]
    depth=0
    while queue:
        depth += 1
        next_queue=[]
        for node in queue:
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
        queue = next_queue

    return depth


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

print(max_depth_iterative(root))   # 3