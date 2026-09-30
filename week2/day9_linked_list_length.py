class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def list_length(head):
    count=0
    current=head
    while current:
        count+=1
        current=current.next
    return count

# Creating linked list: 1 -> 2 -> 3
node3 = Node(3)
node2 = Node(2)
node2.next = node3
node1 = Node(1)
node1.next = node2

print(list_length(node1))   # 3