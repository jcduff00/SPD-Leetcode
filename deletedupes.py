class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Step 1: Create a deleteDuplicates function and set it equal to the head of the linked list
def deleteDuplicates(head):
    current = head

#Step 2: Create a while loop to iterate through the linked list with a conditional that checks if the current iterated value is equal to the corresponding value
    while current is not None and current.next is not None:
        if current.val == current.next.val:
            current.next = current.next.next
        #Step 3: If the current value is not equal to the successive value, move to the next iteration in the list
        else:
            current = current.next

    return head

# Step 4: Implementation
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)

#Call the deleteDuplicates function
result = deleteDuplicates(head)

#Print the values of the resultant linked list
while result is not None:
    print(result.val)
    result = result.next