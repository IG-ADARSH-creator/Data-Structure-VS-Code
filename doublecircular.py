class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CircularLinkedList:
    def __init__(self):
        self.tail = None

    def insert(self, data):
        node = Node(data)
        if self.tail is None:
            node.next = node
            self.tail = node
        else:
            node.next = self.tail.next
            self.tail.next = node
            self.tail = node

    def delete(self, data):
        if self.tail is None:
            return False

        previous = self.tail
        current = self.tail.next

        while True:
            if current.data == data:
                if current == previous:  # Only one node
                    self.tail = None
                else:
                    previous.next = current.next
                    if current == self.tail:
                        self.tail = previous
                return True

            previous, current = current, current.next
            if current == self.tail.next:
                break

        return False

    def display(self):
        if self.tail is None:
            print("Empty")
            return

        values = []
        current = self.tail.next
        while True:
            values.append(str(current.data))
            current = current.next
            if current == self.tail.next:
                break
        print(" -> ".join(values) + " -> (back to start)")


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        node = Node(data)
        if self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def delete(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return True
            current = current.next

        return False

    def display_forward(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        print(" <-> ".join(values) if values else "Empty")

    def display_backward(self):
        values = []
        current = self.tail
        while current:
            values.append(str(current.data))
            current = current.prev
        print(" <-> ".join(values) if values else "Empty")


# Example
circular = CircularLinkedList()
circular.insert(10)
circular.insert(20)
circular.insert(30)
circular.display()
circular.delete(20)
circular.display()

doubly = DoublyLinkedList()
doubly.insert(10)
doubly.insert(20)
doubly.insert(30)
doubly.display_forward()
doubly.delete(20)
doubly.display_forward()
doubly.display_backward()