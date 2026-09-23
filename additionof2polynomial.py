class Node:
    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next = None


def create_polynomial():
    head = None

    n = int(input("Enter number of terms: "))

    for i in range(n):
        coefficient = int(input("Enter coefficient: "))
        exponent = int(input("Enter exponent: "))

        new_node = Node(coefficient, exponent)

        if head is None:
            head = new_node
        else:
            temp = head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    return head


def display(head):
    temp = head

    while temp:
        print(f"{temp.coefficient}x^{temp.exponent}", end="")

        if temp.next:
            print(" + ", end="")

        temp = temp.next

    print()


def add_polynomials(p1, p2):
    result = None
    tail = None

    while p1 is not None and p2 is not None:

        if p1.exponent == p2.exponent:
            coefficient = p1.coefficient + p2.coefficient
            exponent = p1.exponent

            p1 = p1.next
            p2 = p2.next

        elif p1.exponent > p2.exponent:
            coefficient = p1.coefficient
            exponent = p1.exponent

            p1 = p1.next

        else:
            coefficient = p2.coefficient
            exponent = p2.exponent

            p2 = p2.next

        new_node = Node(coefficient, exponent)

        if result is None:
            result = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    while p1 is not None:
        new_node = Node(p1.coefficient, p1.exponent)
        tail.next = new_node
        tail = new_node
        p1 = p1.next

    while p2 is not None:
        new_node = Node(p2.coefficient, p2.exponent)
        tail.next = new_node
        tail = new_node
        p2 = p2.next

    return result


print("Enter First Polynomial")
poly1 = create_polynomial()

print("\nEnter Second Polynomial")
poly2 = create_polynomial()

print("\nFirst Polynomial:")
display(poly1)

print("Second Polynomial:")
display(poly2)

result = add_polynomials(poly1, poly2)

print("Addition of Two Polynomials:")
display(result)