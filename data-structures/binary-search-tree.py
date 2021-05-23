class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


class BST:
    def __init__(self):
        self.root = None

    def add(self, val):
        new_node = Node(val)

        if self.root == None:
            self.root = new_node
            return

        curr_node = self.root

        while True:
            if val == curr_node.val:
                return
            elif val < curr_node.val:
                if curr_node.left == None:
                    curr_node.left = new_node
                    break
                else:
                    curr_node = curr_node.left
            else:
                if curr_node.right == None:
                    curr_node.right = new_node
                    break
                else:
                    curr_node = curr_node.right

    def search(self, val):
        curr_node = self.root

        while curr_node != None:
            if val == curr_node.val:
                return True
            elif val < curr_node.val:
                if curr_node.left != None:
                    curr_node = curr_node.left
                else:
                    return False
            else:
                if curr_node.right != None:
                    curr_node = curr_node.right
                else:
                    return False

        return False

    def inorder_traversal(self):
        self.inorder_traversal_helper(self.root)

    def inorder_traversal_helper(self, node: Node):
        if node == None:
            return

        self.inorder_traversal_helper(node.left)
        print(node.val, end="\t")
        self.inorder_traversal_helper(node.right)

        if node == self.root:
            print()

    def preorder_traversal(self):
        self.preorder_traversal_helper(self.root)

    def preorder_traversal_helper(self, node: Node):
        if node == None:

            return

        print(node.val, end="\t")
        self.preorder_traversal_helper(node.left)
        self.preorder_traversal_helper(node.right)

        if node == self.root:
            print()

    def postorder_traversal(self):
        self.postorder_traversal_helper(self.root)

    def postorder_traversal_helper(self, node: Node):
        if node == None:
            return

        self.postorder_traversal_helper(node.left)
        self.postorder_traversal_helper(node.right)
        print(node.val, end="\t")

        if node == self.root:
            print()

    def find_max(self, node):
        if node == None:
            return None

        curr_node = node

        while curr_node.right != None:
            curr_node = curr_node.right

        return curr_node

    def find_min(self, node):
        if node == None:
            return None

        curr_node = node

        while curr_node.left != None:
            curr_node = curr_node.left

        return curr_node

    def delete_helper(self, node: Node, val: int):
        if node == None:
            return

        if val < node.val:
            node.left = self.delete_helper(node.left, val)
        elif val > node.val:
            node.right = self.delete_helper(node.right, val)
        else:

            if node.left == None:
                temp = node.right
                node = None
                return temp
            elif node.right == None:
                temp = node.left
                node = None
                return temp
            else:
                temp = self.find_min(node.right)
                node.val = temp.val
                node.right = self.delete_helper(node.right, temp.val)

        return node

    def delete(self, val):
        self.root = self.delete_helper(self.root, val)


def main():
    bst = BST()

    bst.add(1)
    bst.add(3)
    bst.add(2)
    bst.add(4)
    bst.add(5)
    bst.add(10)
    bst.add(7)
    bst.add(8)
    bst.add(6)
    bst.add(10)

    for i in range(7):
        print(f"{i} : {bst.search(i)}")

    bst.inorder_traversal()
    bst.preorder_traversal()
    bst.postorder_traversal()

    bst.delete(4)
    bst.inorder_traversal()

    bst.delete(3)
    bst.inorder_traversal()

    bst.delete(10)
    bst.inorder_traversal()

    bst.delete(7)
    bst.inorder_traversal()

    bst.delete(9)
    bst.inorder_traversal()

    bst.delete(1)
    bst.inorder_traversal()


if __name__ == "__main__":
    main()
