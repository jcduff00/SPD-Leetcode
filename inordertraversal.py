class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    #Step 1
    traversal = []

    #Step 2
    def inorderTraversalRecursive(node):
        #Step 3
        if node is not None:
            inorderTraversalRecursive(node.left)
            traversal.append(node.val)
            inorderTraversalRecursive(node.right)

    #Step 4
    inorderTraversalRecursive(root)

    #Step 5
    return traversal

#Step 6: Implementation
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
result = inorderTraversal(root)
print(result)  # Output: [1, 3, 2]