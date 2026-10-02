
# 1. Stack using an array (Python list)
class ArrayStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


# 2. Stack using a linked list
class LinkedStack:
    class Node:
        def __init__(self, value, next_node=None):
            self.value = value
            self.next = next_node

    def __init__(self):
        self.top = None

    def push(self, item):
        self.top = self.Node(item, self.top)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.value

    def is_empty(self):
        return self.top is None


# 3. Infix to postfix
# Supports numbers/variables, parentheses, +, -, *, /, and ^
def infix_to_postfix(expression):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    output = []
    operators = []

    # Split expressions such as "12 + x * (3 - 1)" into tokens.
    tokens = []
    i = 0
    while i < len(expression):
        char = expression[i]
        if char.isspace():
            i += 1
        elif char.isalnum() or char == ".":
            start = i
            while i < len(expression) and (
                expression[i].isalnum() or expression[i] == "."
            ):
                i += 1
            tokens.append(expression[start:i])
        elif char in "+-*/^()":
            tokens.append(char)
            i += 1
        else:
            raise ValueError(f"Invalid character: {char}")

    for token in tokens:
        if token not in precedence and token not in ("(", ")"):
            output.append(token)
        elif token == "(":
            operators.append(token)
        elif token == ")":
            while operators and operators[-1] != "(":
                output.append(operators.pop())
            if not operators:
                raise ValueError("Mismatched parentheses")
            operators.pop()
        else:
            while (
                operators
                and operators[-1] in precedence
                and (
                    precedence[operators[-1]] > precedence[token]
                    or (
                        precedence[operators[-1]] == precedence[token]
                        and token != "^"  # ^ is right-associative
                    )
                )
            ):
                output.append(operators.pop())
            operators.append(token)

    while operators:
        operator = operators.pop()
        if operator == "(":
            raise ValueError("Mismatched parentheses")
        output.append(operator)

    return " ".join(output)


# 4. Postfix evaluation
def evaluate_postfix(expression):
    stack = []

    for token in expression.split():
        if token in {"+", "-", "*", "/", "^"}:
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression")
            right = stack.pop()
            left = stack.pop()

            if token == "+":
                result = left + right
            elif token == "-":
                result = left - right
            elif token == "*":
                result = left * right
            elif token == "/":
                result = left / right
            else:
                result = left ** right

            stack.append(result)
        else:
            stack.append(float(token))

    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")

    result = stack.pop()
    return int(result) if result.is_integer() else result


# 5. Balanced parentheses
def has_balanced_parentheses(expression):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []

    for char in expression:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack.pop() != pairs[char]:
                return False

    return not stack


# 6. Tower of Hanoi (recursion)
def tower_of_hanoi(disks, source, auxiliary, destination):
    if disks < 1:
        return
    if disks == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    tower_of_hanoi(disks - 1, source, destination, auxiliary)
    print(f"Move disk {disks} from {source} to {destination}")
    tower_of_hanoi(disks - 1, auxiliary, source, destination)


# Examples
if __name__ == "__main__":
    print("Infix to postfix:", infix_to_postfix("(3 + 4) * 2"))
    print("Postfix result:", evaluate_postfix("3 4 + 2 *"))
    print("Balanced:", has_balanced_parentheses("{[()]}"))

    print("Tower of Hanoi:")
    tower_of_hanoi(3, "A", "B", "C")
