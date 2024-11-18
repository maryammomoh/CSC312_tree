	class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def copy_tree(node):
    # Base case: if the node is null, return null
    if node is None:
        return None
    
    # Create a new node with the same value
    new_node = TreeNode(node.value)
    
    # Recursively copy the left and right subtrees
    new_node.left = copy_tree(node.left)
    new_node.right = copy_tree(node.right)
    
    return new_node


