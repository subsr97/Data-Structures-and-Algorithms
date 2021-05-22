class Node:
    """
    Basic node implementation with a single link.
    """

    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)


class SinglyListList:
    """
    Singly Linked List implementation.
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_first(self, val):
        """
        Insert an element in the front.
        """
        new_node = Node(val)

        if self.head == None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.size += 1

    def add_last(self, val):
        """
        Insert an element in the end.
        """
        new_node = Node(val)

        if self.head == None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def add_at(self, ind, val):
        """
        Insert an element at an index.
        """

        if ind < 0 or ind > self.size:
            raise Exception("Invalid index.")
        elif ind == 0:
            self.add_first(val)
        elif ind == self.size:
            self.add_last(val)
        else:

            new_node = Node(val)
            curr_node = self.head

            for _ in range(ind - 1):
                curr_node = curr_node.next

            new_node.next = curr_node.next
            curr_node.next = new_node
            self.size += 1

    def remove_first(self):
        if self.size == 0:
            raise Exception("Empty linked list.")

        curr_head = self.head
        self.head = self.head.next

        self.size -= 1

        if self.size == 0:
            self.head = self.tail = None

        return curr_head

    def remove_last(self):
        if self.size == 0:
            raise Exception("Empty linked list.")
        elif self.size == 1:
            return self.remove_first()

        curr_node = self.head

        while curr_node.next != self.tail:
            curr_node = curr_node.next

        curr_tail = self.tail
        curr_node.next = None
        self.tail = curr_node

        self.size -= 1

        return curr_tail

    def remove_at(self, ind):
        if ind < 0 or ind > self.size - 1:
            raise Exception("Invalid index.")
        elif ind == 0:
            return self.remove_first()
        elif ind == self.size - 1:
            return self.remove_last()
        else:
            curr_node = self.head

            for _ in range(ind - 1):
                curr_node = curr_node.next

            node_to_be_removed = curr_node.next
            curr_node.next = curr_node.next.next
            self.size -= 1

            return node_to_be_removed

    def __str__(self):
        string_rep = ""

        current_node = self.head
        while current_node != None:
            string_rep += str(current_node.val) + " -> "
            current_node = current_node.next

        string_rep += (
            f"[ Size: {str(self.size)} Head: {str(self.head)} Tail: {str(self.tail)} ]"
        )

        return string_rep


def main():
    sll = SinglyListList()
    sll.add_first(1)
    sll.add_first(0)
    sll.add_last(3)
    sll.add_at(2, 2)
    sll.add_at(0, -1)
    sll.add_at(5, 4)

    print(sll)

    print(sll.remove_first())
    print(sll)

    print(sll.remove_last())
    print(sll)

    print(sll.remove_at(0))
    print(sll)

    print(sll.remove_at(1))
    print(sll)

    print(sll.remove_at(1))
    print(sll)

    try:
        print(sll.remove_at(1))
    except Exception as e:
        print("Exception:", e)

    print(sll.remove_last())
    print(sll)

    try:
        print(sll.remove_first())
    except Exception as e:
        print("Exception:", e)


if __name__ == "__main__":
    main()
