class Node:
    """
    Basic node implementation with a single link.
    """

    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)


class Queue:

    """
    Queue implementation using Linked List.
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        """
        Insert an element into the queue.
        """
        new_node = Node(value)

        if self.tail == None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        """
        Dequeue an element from the queue.
        """
        if self.head == None:
            raise Exception("Empty queue!")

        front = self.head
        self.head = front.next

        return front

    def __str__(self):

        string_rep = ""

        current_node = self.head
        while current_node != None:
            string_rep += str(current_node.val) + " -> "
            current_node = current_node.next

        return string_rep


def main():
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q)

    for _ in range(3):
        print("Dequeued:", q.dequeue())
        print("Current queue:", q)

    try:
        q.dequeue()
    except Exception as e:
        print("Exception:", e)


if __name__ == "__main__":
    main()
