import random

comparisons = 0

def randomized_quicksort(arr, low, high):
    global comparisons

    if low < high:
        pivot_index = random.randint(low, high)

        # Move pivot to the end
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            comparisons += 1

            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        p = i + 1

        randomized_quicksort(arr, low, p - 1)
        randomized_quicksort(arr, p + 1, high)


arr = list(map(int, input("Enter array elements: ").split()))

randomized_quicksort(arr, 0, len(arr) - 1)

print("Sorted array:", arr)
print("Number of comparisons:", comparisons)
