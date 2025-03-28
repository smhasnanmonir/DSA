class singlyLinkedList: 
    def __init__(self, val, next=None):
        self.next = next
        self.val = val
    def __str__(self):
        return str(self.val)

Head = singlyLinkedList(1)
A = singlyLinkedList(2)
B = singlyLinkedList(3)

Head.next = A
A.next = B

def insert_at_the_first(head,value):
    new_node = singlyLinkedList(value)
    new_node.next = head
    return new_node

Head = insert_at_the_first(Head,5)

def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print("->".join(elements))
display(Head)

Head = insert_at_the_first(Head, 6)

display(Head)