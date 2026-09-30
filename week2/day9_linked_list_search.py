class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
def contains(head,target):
    current=head
    while current:
        if current.value==target:
          return True
        current=current.next
    return False

node3=Node(3)
node2=Node(2)
node2.next=node3
node1=Node(1)
node1.next=node2

print(contains(node1,2))   #True
print(contains(node1,5))   #False