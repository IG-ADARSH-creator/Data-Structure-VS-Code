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

value = int(input("Enter value to delete: "))

if head is not None and head.data == value:
    head = head.next
else:
    temp = head

    while temp is not None and temp.next is not None:
        if temp.next.data == value:
            temp.next = temp.next.next
            break
        temp = temp.next

print("After deletion:")

temp = head

while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("NULL")