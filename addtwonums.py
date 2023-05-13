
#Step 1: Define ListNode 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    #Step 2: Create an example node to hold ListNode and thereby the result
    example_node = ListNode()
    current = example_node
    
    #Step 3: Create a basic carry value for addition and set equal to zero. This allows the value to always point to the newly created node after calculation
    carry = 0 
    
    while l1 or l2 or carry:
        #Step 4: Calculate the sum of the current digits and the carry variable
        sum = carry
        
        if l1:
            sum += l1.val
            l1 = l1.next
        
        if l2:
            sum += l2.val
            l2 = l2.next
        
        #Step 5: Calculate the carry value and update the sum
        carry = sum // 10
        sum %= 10
        
        #Step 6: Create a new node with the resulting sum 
        current.next = ListNode(sum)
        current = current.next
    
    #Step 7: Implementation
    return example_node.next