def counting_sort(arr, place):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for num in arr:
        digit = (num // place) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        digit = (arr[i] // place) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    if len(arr) == 0:
        return

    max_value = max(arr)

    place = 1

    while max_value // place > 0:
        counting_sort(arr, place)
        place *= 10


arr = list(map(int, input("Enter positive array elements: ").split()))

radix_sort(arr)

print("Sorted array:", arr)