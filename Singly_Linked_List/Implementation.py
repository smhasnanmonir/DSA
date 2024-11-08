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

search(Head,5)