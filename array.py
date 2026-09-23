arr = list(map(int, input("Enter array elements: ").split()))

while True:
    print("\n1. Traversal")
    print("2. Insertion")
    print("3. Deletion")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Array:", arr)

    elif choice == 2:
        pos = int(input("Enter position (0-based index): "))
        value = int(input("Enter value: "))

        if 0 <= pos <= len(arr):
            arr.insert(pos, value)
            print("After insertion:", arr)
        else:
            print("Invalid position!")

    elif choice == 3:
        pos = int(input("Enter position (0-based index): "))

        if 0 <= pos < len(arr):
            arr.pop(pos)
            print("After deletion:", arr)
        else:
            print("Invalid position!")

    elif choice == 4:
        print("Program ended.")
        break

    else:
        print("Invalid choice!")