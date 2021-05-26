class UnionFind:
    def __init__(self, size):
        if size < 0:
            raise Exception("Invalid size.")

        self.component_size = [0] * size
        self.parent = [-1] * size
        self.component_count = size
        self.size = size

        for ind in range(size):
            self.parent[ind] = -1
            self.component_size[ind] = 1

    def find(self, element):

        if element < 0 or element >= self.size:
            raise Exception("Invalid element.")

        root = element
        while self.parent[element] != -1 and element != -1:
            root = self.parent[element]
            element = root

        it = element
        while it != root:
            next_element = self.parent[it]
            self.parent[it] = root

            self.component_size[next_element] -= 1
            self.component_size[root] += 1

            it = next_element

        return root

    def unify(self, element1, element2, return_if_cyclic=False):
        if (
            element1 < 0
            or element1 >= self.size
            or element2 < 0
            or element2 >= self.size
        ):
            raise Exception("Invalid element.")

        root1 = self.find(element1)
        root2 = self.find(element2)

        if root1 != root2:
            if self.component_size[root1] >= self.component_size[root2]:
                self.parent[root2] = root1
                self.component_size[root1] += self.component_size[root2]
            else:
                self.parent[root1] = root2
                self.component_size[root2] += self.component_size[root1]

            self.component_count -= 1
        elif return_if_cyclic:
            return True

        return False

    def connected(self, element1, element2):
        return self.find(element1) == self.find(element2)

    def component_size(self, element):
        return self.component_size[self.find(element)]

    def is_cyclic(self, edges):
        parent = [-1] * self.size

        for edge in edges:
            if self.unify(edge[0], edge[1], True):
                return True

        return False


def main():
    union_find = UnionFind(3)

    graph = [(0, 1), (1, 2), (2, 0)]

    if union_find.is_cyclic(graph):
        print("Cyclic graph.")
    else:
        print("Acyclic graph,")


if __name__ == "__main__":
    main()
