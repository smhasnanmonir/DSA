class Singly_linked_list:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

Head = Singly_linked_list(1)
A = Singly_linked_list(3)
B = Singly_linked_list(4)
C = Singly_linked_list(7)

Head.next = A
A.next = B
B.next = C

# print(Head)

#traverse

curr = Head
while curr:
    print(curr)
    curr = curr.next

#display linked list

def display(head):
    elements = []
    curr = head
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print("-> ".join(elements))

display(Head)


#search for a node

def search(head,value):
    curr = head
    while curr:
        if value == curr.val:
            return True
        curr = curr.next
    return False

search(Head,5)#add a node at the beginning
def add_at_beginning(head,value):
    new_node = Singly_linked_list(value)
    new_node.next = head
    return new_node

Head = add_at_beginning(Head,0)
display(Head)

#add a node at the end
def add_at_end(head,value):
    new_node = Singly_linked_list(value)
    if head is None:
        return new_node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    return head

Head = add_at_end(Head,9)
display(Head)

#add a node at a specific position
def add_at_position(head,value,position):
    new_node = Singly_linked_list(value)
    if position == 0:
        new_node.next = head
        return new_node
    curr = head
    count = 0
    while curr and count < position - 1:
        curr = curr.next
        count += 1
    if curr is None:
        return head
    new_node.next = curr.next
    curr.next = new_node
    return head

Head = add_at_position(Head,2,2)
display(Head)

#delete a node at the beginning
def delete_at_beginning(head):
    if head is None:
        return None
    return head.next

Head = delete_at_beginning(Head)
display(Head)

#delete a node at the end
def delete_at_end(head):
    if head is None:
        return None
    if head.next is None:
        return None
    curr = head
    while curr.next.next:
        curr = curr.next
    curr.next = None
    return head

Head = delete_at_end(Head)
display(Head)

#delete a node at a specific position
def delete_at_position(head,position):
    if head is None:
        return None
    if position == 0:
        return head.next
    curr