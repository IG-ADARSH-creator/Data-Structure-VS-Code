class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = None

n = int(input("Enter number of nodes: "))

for i in range(n):
    data = int(input("Enter data: "))

    new_node = Node(data)

    if head is None:
        head = new_node
    else:
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = new_node


print("Original list:")

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("NULL")


previous = None
current = head

while current is not None:
    next_node = current.next
    current.next = previous
    previous = current
    current = next_node

head = previous


print("Reversed list:")

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("NULL")