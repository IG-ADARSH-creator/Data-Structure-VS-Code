class Node:
    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next = None


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


print("Polynomial:")

temp = head

while temp:
    print(f"{temp.coefficient}x^{temp.exponent}", end="")

    if temp.next:
        print(" + ", end="")

    temp = temp.next

print()