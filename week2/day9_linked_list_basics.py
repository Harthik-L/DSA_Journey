class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
def print_list(head):
    current=head
    while current:
        print(current.value,end=" -> ")
        current=current.next
    print("None")

# Manually building: 1 -> 2 -> 3
node3=Node(3)
node2=Node(2)
node2.next=node3
node1=Node(1)
node1.next=node2

print_list(node1)      # 1 -> 2 -> 3 -> None