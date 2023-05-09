class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
    #Step 1
    if p is None and q is None:
        return True

    #Step 2
    if p is None or q is None:
        return False

    #Step 3
    if p.val != q.val:
        return False

    #Step 4 and 5
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

#Step 6: Implementation
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

result = isSameTree(p, q)
print(result)  # Output: True