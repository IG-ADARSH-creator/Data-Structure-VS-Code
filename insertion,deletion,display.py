class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = None


def insert(data):
    global head

    new_node = Node(data)

    if head is None:
        head = new_node
    else:
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node


def delete(data):
    global head

    if head is None:
        print("List is empty")
        return

    if head.data == data:
        head = head.next
        print("Node deleted")
        return

    temp = head

    while temp.next is not None:
        if temp.next.data == data:
            temp.next = temp.next.next
            print("Node deleted")
            return
        temp = temp.next

    print("Element not found")


def display():
    if head is None:
        print("List is empty")
        return

    temp = head

    while temp is not None:
        print(temp.data, end=" -> ")
        temp = temp.next

    print("NULL")


while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        insert(value)

    elif choice == 2:
        value = int(input("Enter value to delete: "))
        delete(value)

    elif choice == 3:
        display()

    elif choice == 4:
        break

    else:
        print("Invalid choice")