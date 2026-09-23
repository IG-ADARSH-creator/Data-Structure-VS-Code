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


print("Linked List:")

temp = head

while temp is not None:
    print(temp.data, end=" -> ")
    temp = temp.next

print("NULL")