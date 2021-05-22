class Stack:
    """
    Stack implementation using Python's inbuilt list.
    """

    def __init__(self, initial_arr=[]):
        """
        Initialize the stack with an optional initial array.
        """
        self.arr = initial_arr
        self.size = len(self.arr)

    def push(self, new_element):
        """
        Push an element to the stack.
        """
        self.arr.append(new_element)
        self.size += 1

    def pop(self):
        """
        Pop an element from the stack.
        Raises an exception if the stack is empty.
        """
        if self.is_empty():
            raise Exception("Stack is empty.")

        self.size -= 1
        return self.arr.pop()

    def get_size(self):
        """
        Returns the size of the stack.
        """
        return self.size

    def is_empty(self):
        """
        Returns whether the stack is empty.
        """
        return self.size == 0

    def top(self):
        """
        Returns the top of the stack, without popping it.
        """
        return self.arr[-1]

    def __str__(self):
        """
        Returns a string representation of the stack.
        """
        return str(self.arr)


class SizedStack(Stack):
    """
    Sized Stack implementation. Inherits Stack, adds the functionality of limiting the capacity of the stack.
    """

    def __init__(self, capacity=0, initial_arr=[]):

        if capacity <= 0:
            self.capacity = 0
        else:
            self.capacity = capacity

        if self.is_capacity_set() and len(initial_arr) > self.capacity:
            raise Exception("Invalid capacity/initial stack.")

        super().__init__(initial_arr)

    def get_capacity(self):
        return self.capacity

    def is_capacity_set(self):
        return self.capacity != 0

    def push(self, new_element):
        if self.is_capacity_set() and self.get_size() == self.get_capacity():
            raise Exception("Stack is full.")

        super().push(new_element)


def main():

    print("STACK EXAMPLE:")
    s1 = Stack()
    s1.push(1)
    s1.push(2)
    print(s1.pop())
    s1.push(3)
    print(s1.top())

    print(s1)

    s2 = Stack([1, 2, 3])
    s2.push(4)
    s2.push(5)

    try:
        for _ in range(6):
            print(s2.pop())
            print("Current stack:", s2, "Current size:", s2.get_size())
    except Exception as e:
        print("Got exception:", e)

    print("\nSIZED STACK EXAMPLE:")

    ss1 = SizedStack(3)
    ss1.push(1)
    ss1.push(2)
    print(ss1.pop())
    ss1.push(3)
    print(ss1.pop())

    try:
        ss2 = SizedStack(2, [1, 2, 3])
    except Exception as e:
        print("Got exception:", e)

    ss2 = SizedStack()
    print("Initial stack:", ss2)

    try:
        for i in range(3):
            ss2.push(i)
            print("Current stack:", ss2)
    except Exception as e:
        print("Got exception:", e)


if __name__ == "__main__":
    main()
