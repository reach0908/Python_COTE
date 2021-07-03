class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

node1 = Node(1)
node2 = Node(2)
node1.next = node2
head = node1

def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)

node1 = Node(1)
head = node1
for index in range(2,10):
    add(index)

node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)
print("\n")
node3 = Node(1.5)

node = head
search = True
while search:
    if node.data == 1:
        search = False
    else :
        node = node.next

node_next = node.next
node.next = node3
node3.next = node_next

node = head
while node.next:
    print(node.data)
    node = node.next
print (node.data)