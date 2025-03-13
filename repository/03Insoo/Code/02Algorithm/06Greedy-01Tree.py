class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right
    
def greedy_max_path_sum(root):
    path_sum=0
    current_node=root

    while current_node:
        path_sum+=current_node.value
        if current_node.left and current_node.right:
            if current_node.left.value>current_node.right.value:
                current_node=current_node.left
            else:
                current_node=current_node.right
        else:
            current_node=current_node.left if current_node.left else current_node.right

    return path_sum


root=TreeNode(5)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(9)
root.left.right=TreeNode(1)
root.right.left=TreeNode(7)
root.right.right=TreeNode(4)
print("그리드선택의합:", greedy_max_path_sum(root))

        