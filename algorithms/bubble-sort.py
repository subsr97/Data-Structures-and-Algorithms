def bubble_sort(arr, reverse=False):
    if arr == []:
        return arr

    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    if not reverse:
        return arr
    else:
        return arr[::-1]


def main():
    arr = [64, 56, 23, 0, 79, -3, 8]
    print("Original array:\n", arr)

    print("Sorted array:\n", bubble_sort(arr))
    print("Sorted array in descending order:\n", bubble_sort(arr, reverse=True))


if __name__ == "__main__":
    main()
