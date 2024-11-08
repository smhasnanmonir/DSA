#doubley linked list

class doubly_linked2:
  def __init__(self,val,next=None,prev=None):
    self.val = val
    self.next = next
    self.prev = prev
  
  def __str__(self):
    return str(self.val)
  
Head = Tail = doubly_linked2(5)

def display1(head):
  elements1 = []
  curr = head
  while curr:
    elements1.append(str(curr.val))
    curr = curr.next
  print("<->".join(elements1))

display1(Head)

def insert_at_first(head,tail,val):
  new_node = doubly_linked2(val,next=head)
  head.prev = new_node
  return new_node, tail

head1,tail = insert_at_first(Head,Tail,3)

display1(head1)