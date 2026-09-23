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


key = int(input("Enter element to search: "))

temp = head
position = 1
found = False

while temp is not None:
    if temp.data == key:
        print("Element found at position:", position)
        found = True
        break

    temp = temp.next
    position += 1

if not found:
    print("Element not found")