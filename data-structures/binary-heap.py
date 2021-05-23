class BinaryHeap:
    def __init__(self, initial_arr=[]):
        self.heap_arr = initial_arr
        self.root = 0
        # self.insertion_index = 0
        self.size = 0

        if initial_arr != []:
            self.size = len(initial_arr)
            self.heapify()

    def get_element_at_index(self, ind):
        if ind < len(self.heap_arr):
            return self.heap_arr[ind]
        else:
            return None

    def add(self, val):
        self.size += 1
        self.heap_arr.append(val)
        self.swim(self.size - 1)

    def peek(self):
        return self.get_element_at_index(self.root)

    def poll(self):
        if self.size == 0:
            return None

        self.size -= 1
        self.swap(self.root, -1)
        polled_element = self.heap_arr.pop(-1)

        if self.size != 0:
            self.sink(self.root)

        print("Polled:", polled_element)
        return polled_element

    def swim(self, ind):
        curr_ind = ind
        parent_ind = self.get_parent_index(curr_ind)

        # print("Before swim:", self.heap_arr)

        while self.heap_arr[curr_ind] < self.heap_arr[parent_ind]:
            self.swap(curr_ind, parent_ind)
            curr_ind = parent_ind
            parent_ind = self.get_parent_index(parent_ind)

        # print("After swim:", self.heap_arr)

    def sink(self, ind):

        # print("Sinking:", self.heap_arr[ind])

        curr_ind = ind
        (left_child_ind, right_child_ind) = self.get_children(ind)
        swap_index = 0

        if self.get_element_at_index(left_child_ind) == None:
            print("No child element for:", self.heap_arr[ind])
            return
        elif self.get_element_at_index(right_child_ind) == None:
            print("Swapping with left child element.")
            swap_index = left_child_ind
        else:
            print(
                "Left child:",
                self.heap_arr[left_child_ind],
                "Right child:",
                self.heap_arr[right_child_ind],
            )
            if self.heap_arr[left_child_ind] < self.heap_arr[right_child_ind]:
                swap_index = left_child_ind
            else:
                swap_index = right_child_ind

        if self.heap_arr[ind] > self.heap_arr[swap_index]:
            self.swap(ind, swap_index)
            self.sink(swap_index)

    def get_parent_index(self, ind):
        return abs(ind - 1) // 2

    def get_children(self, ind):
        return ((2 * ind) + 1, (2 * ind) + 2)

    def swap(self, ind1, ind2):
        print(f"Swapping {self.heap_arr[ind1]} and {self.heap_arr[ind2]}")
        # print("Before swapping:", self.heap_arr)

        self.heap_arr[ind1], self.heap_arr[ind2] = (
            self.heap_arr[ind2],
            self.heap_arr[ind1],
        )

        print("After swapping:", self.heap_arr)

    def heapify(self):
        print("Array for heapification:", self.heap_arr)
        for ind in range((self.size // 2) - 1, -1, -1):
            print("\nIn heapify, sinking index:", ind, "value", self.heap_arr[ind])
            print("Current heap arr:", self.heap_arr)
            self.sink(ind)

    def __str__(self):
        row = curr_ind = 0
        row_element_count = 0
        tab = "\t"

        string_rep = f"SIZE:{self.size} ARR:{self.heap_arr}\n"

        while self.size != 0 and curr_ind < self.size:
            string_rep += f"{tab*((self.size//2)-row)}{self.heap_arr[curr_ind]}\t"
            row_element_count += 1

            if pow(2, row) == row_element_count:
                string_rep += "\n"
                row += 1
                row_element_count = 0

            curr_ind += 1

        return string_rep

    def delete(self, val):
        try:
            ind = self.heap_arr.index(val)
        except:
            return None

        self.swap(ind, -1)
        self.heap_arr.pop(-1)
        self.size -= 1

        self.swim(ind)

        self.sink(ind)


def main():
    heap = BinaryHeap()

    heap.add(2)
    print(heap)

    heap.add(0)
    print(heap)

    heap.add(4)
    print(heap)

    heap.add(1)
    print(heap)

    print(heap.poll())
    print(heap)

    heap.add(-4)
    print(heap)

    heap.add(0)
    print(heap)

    while heap.poll() != None:
        print(heap)

    arr = [2, 0, 4, 3, 3, 1, -4, 0]

    heap2 = BinaryHeap(arr)
    print(heap2)

    print("Deleting")
    heap2.delete(2)
    print(heap2)

    heap3 = BinaryHeap()
    for num in arr:
        heap3.add(num)

    print(heap3)

    while heap2.poll() != None:
        print(heap2)


if __name__ == "__main__":
    main()
