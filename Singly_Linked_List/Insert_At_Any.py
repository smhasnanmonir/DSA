class singly_linked_list():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)

def list_to_linked_list(lst):
    if not lst:  # If the list is empty, return None
        return None
    
    head = singly_linked_list(lst[0])  # Create the head node
    current = head  # Keep track of the current node
    
    for value in lst[1:]:  # Iterate through the rest of the list
        current.next = singly_linked_list(value)  # Create a new node and link it
        current = current.next  # Move to the new node
    
    return head  # Return the head of the linked list

# Example usage:
my_list = [1, 2, 3, 4, 5]
Head = list_to_linked_list(my_list)

def visual_link(head):
    elements = []
    curr = head
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print("->".join(elements))

visual_link(Head)

def insert_at_anywhere(head,val,position):
    curr = head
    count = 0
    new_node = singly_linked_list(val)
    if position == 0:
        new_node.next = head
        return new_node
    while curr and count < position - 1:
        curr = curr.next
        count+=1
    if curr == None:
        return
    temp = curr.next  # Store the original next node
    curr.next = new_node  # Insert the new node
    new_node.next = temp  # Link the new node to the original next node
    return head

# Head = insert_at_anywhere(Head,5,0)

# visual_link(Head)

Head = insert_at_anywhere(Head,2,2)    

visual_link(Head)
        

