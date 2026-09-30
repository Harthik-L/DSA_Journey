class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_list(head):
    if head is None or head.next is None:
        return head
    new_head = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return new_head

node3 = Node(3)
node2 = Node(2)
node2.next = node3
node1 = Node(1)
node1.next = node2

new_head = reverse_list(node1)

current = new_head
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")