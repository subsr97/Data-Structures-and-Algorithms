class Node:
    def __init__(self):
        self.word_dict = dict()
        self.word_end_count = 0


class Trie:
    def __init__(self):
        self.root = Node()
        self.root.word_end_count = 1

    def add_word(self, word):

        print("Add:", word)

        curr_node = self.root

        for letter in word:
            if letter in curr_node.word_dict:
                curr_node = curr_node.word_dict[letter]
                continue
            else:
                new_node = Node()
                curr_node.word_dict[letter] = new_node
                curr_node = new_node

        curr_node.word_end_count += 1

    def search(self, word):

        print("Search:", word)

        curr_node = self.root

        for letter in word:
            if letter in curr_node.word_dict:
                curr_node = curr_node.word_dict[letter]
            else:
                return False

        return curr_node.word_end_count > 0

    def has_prefix(self, word):

        print("Has Prefix:", word)

        curr_node = self.root

        for letter in word:
            if letter in curr_node.word_dict:
                curr_node = curr_node.word_dict[letter]
            else:
                return False

        return True

    def delete(self, word):

        print("Delete:", word)

        curr_node = self.root

        for letter in word:
            if letter in curr_node.word_dict:
                curr_node = curr_node.word_dict[letter]
            else:
                raise Exception("Word not found")

        if curr_node.word_end_count == 0:
            raise Exception("Word not found")
        else:
            curr_node.word_end_count -= 1


def main():
    trie = Trie()

    trie.add_word("shopping")
    trie.add_word("shopper")
    trie.add_word("for")
    trie.add_word("formal")
    trie.add_word("zebra")

    print(trie.search("shop"))
    print(trie.has_prefix("shop"))

    print(trie.search("for"))
    print(trie.search("formal"))
    print(trie.has_prefix("formality"))

    print(trie.search("z"))
    print(trie.search("xerox"))
    print(trie.search("zebra"))

    trie.delete("zebra")
    print(trie.search("zebra"))

    try:
        trie.delete("shop")
    except Exception as e:
        print("Exception:", e)

    trie.delete("formal")
    print(trie.search("formal"))


if __name__ == "__main__":
    main()
