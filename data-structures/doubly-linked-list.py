class Node:
    """
    Node implementation with next and previous links.
    """

    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.val)


class DoublyLinkedList:
    """
    Doubly linked list implementation.
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.lookup_table = dict()

    def add_first(self, val):
        new_node = Node(val)
        self.lookup_table[val] = new_node

        if self.head == None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    def add_last(self, val):
        new_node = Node(val)
        self.lookup_table[val] = new_node

        if self.head == None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.size += 1

    def add_at(self, ind, val):

        if ind < 0 or ind > self.size:
            raise Exception("Invalid index.")
        elif ind == 0:
            self.add_first(val)
        elif ind == self.size:
            self.add_last(val)
        else:
            new_node = Node(val)
            self.lookup_table[val] = new_node

            curr_node = self.head
            for _ in range(ind - 1):
                curr_node = curr_node.next

            new_node.next = curr_node.next
            new_node.prev = curr_node

            curr_node.next.prev = new_node
            curr_node.next = new_node

            self.size += 1

    def remove_first(self):
        if self.head == None:
            raise Exception("Empty linked list.")

        curr_head = self.head
        self.head = self.head.next

        self.size -= 1

        if self.size == 0:
            self.head = self.tail = None

        if curr_head.val in self.lookup_table:
            del self.lookup_table[curr_head.val]

        return curr_head

    def remove_last(self):
        if self.head == None:
            raise Exception("Empty linked list.")
        elif self.size == 1:
            return self.remove_first()

        curr_tail = self.tail
        self.tail = self.tail.prev
        self.tail.next = None

        self.size -= 1

        if curr_tail.val in self.lookup_table:
            del self.lookup_table[curr_tail.val]

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

            for _ in range(ind):
                curr_node = curr_node.next

            print("Node to be deleted:", curr_node)

            curr_node.prev.next = curr_node.next
            curr_node.next.prev = curr_node.prev

            self.size -= 1

            if curr_node.val in self.lookup_table:
                del self.lookup_table[curr_node.val]

            return curr_node

    def remove_value(self, val):
        if val not in self.lookup_table:
            raise Exception("Invalid value.")

        node_to_be_removed = self.lookup_table[val]

        if node_to_be_removed == self.head:
            return self.remove_first()
        elif node_to_be_removed == self.tail:
            return self.remove_last()
        else:
            node_to_be_removed.prev.next = node_to_be_removed.next
            node_to_be_removed.next.prev = node_to_be_removed.prev

            self.size -= 1

            del self.lookup_table[node_to_be_removed.val]

            return node_to_be_removed

    def __str__(self):
        string_rep = ""

        current_node = self.head
        while current_node != None:
            string_rep += str(current_node.val) + " <-> "
            current_node = current_node.next

        string_rep += (
            f"[ Size: {str(self.size)} Head: {str(self.head)} Tail: {str(self.tail)} ]"
        )

        return string_rep


def main():
    dll = DoublyLinkedList()

    dll.add_first(1)
    print(dll)

    dll.add_last(3)
    print(dll)

    dll.add_at(1, 2)
    print(dll)

    dll.add_last(4)
    print(dll)

    dll.add_at(4, 5)
    print(dll)

    print(dll.remove_first())
    print(dll)

    print(dll.remove_at(1))
    print(dll)

    print(dll.remove_at(0))
    print(dll)

    print(dll.remove_last())
    print(dll)

    print(dll.remove_value(4))
    print(dll)


if __name__ == "__main__":
    main()
