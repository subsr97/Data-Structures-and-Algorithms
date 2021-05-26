def merge(arr, left, mid, right):

    # print("Merging:", arr[left : mid + 1], arr[mid + 1 : right + 1])

    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    for ind in range(n1):
        L[ind] = arr[left + ind]

    for ind in range(n2):
        R[ind] = arr[mid + 1 + ind]

    i = 0
    j = 0
    ind = left

    while i < n1 and j < n2:
        if L[i] < R[j]:
            arr[ind] = L[i]
            i += 1
        else:
            arr[ind] = R[j]
            j += 1

        ind += 1

    while i < n1:
        arr[ind] = L[i]
        ind += 1
        i += 1

    while j < n2:
        arr[ind] = R[j]
        ind += 1
        j += 1

    # print("Merge result:", arr[left : right + 1])


def merge_sort_helper(arr, left, right):

    if left < right:
        mid = left + ((right - left) // 2)
        # mid = (left + (right - 1)) // 2

        merge_sort_helper(arr, left, mid)
        merge_sort_helper(arr, mid + 1, right)
        merge(arr, left, mid, right)


def merge_sort(arr, reverse=False):
    if arr == []:
        return []

    n = len(arr)

    merge_sort_helper(arr, 0, n - 1)

    if reverse:
        arr.reverse()


def main():
    arr = [64, 56, 23, 0, 79, -3, 8]
    print("Original arr:\n", arr)

    merge_sort(arr)
    print("Sorted arr:\n", arr)

    merge_sort(arr, reverse=True)
    print("Sorted arr in descending:\n", arr)


if __name__ == "__main__":
    main()
