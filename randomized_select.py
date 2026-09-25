import random

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)

    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def randomized_select(arr, low, high, k):
    if low == high:
        return arr[low]

    pivot = randomized_partition(arr, low, high)

    rank = pivot - low + 1

    if k == rank:
        return arr[pivot]

    elif k < rank:
        return randomized_select(arr, low, pivot - 1, k)

    else:
        return randomized_select(arr, pivot + 1, high, k - rank)


arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter i (1 for smallest): "))

if 1 <= k <= len(arr):
    result = randomized_select(arr, 0, len(arr) - 1, k)
    print(f"{k}th smallest element:", result)
else:
    print("Invalid value of i")
