class HashMap:
    """
    Hash map implementation with Separate Chaining.
    """

    def __init__(self, capacity=10, threshold=0.5):

        if capacity <= 0:
            raise Exception("Invalid capacity.")
        elif threshold <= 0:
            raise Exception("Invalid threshold.")

        self.capacity = capacity
        self.threshold = threshold
        self.hash_map = [None] * capacity
        self.size = 0
        self.threshold_limit = capacity * threshold

    def calculate_hash(self, key, capacity):
        return abs(hash(key)) % capacity

    def add(self, key, value):
        hash_value = self.calculate_hash(key, self.capacity)

        if self.hash_map[hash_value] == None:
            self.hash_map[hash_value] = [(key, value)]
            self.size += 1
        else:
            does_key_exist = False
            for ind, (k, v) in enumerate(self.hash_map[hash_value]):
                if key == k:
                    self.hash_map[hash_value][ind] = (key, value)
                    does_key_exist = True

            if not does_key_exist:
                self.hash_map[hash_value].append((key, value))
                self.size += 1

        if self.size > self.threshold_limit:
            self.resize_table()

    def remove(self, key):
        hash_value = self.calculate_hash(key, self.capacity)

        if self.hash_map[hash_value] == None:
            raise Exception("Invalid key.")
        else:
            for ind, (k, v) in enumerate(self.hash_map[hash_value]):
                if key == k:
                    self.hash_map[hash_value].remove((k, v))
                self.size -= 1
                return v

    def resize_table(self):
        new_capacity = self.capacity * 2
        new_hash_map = [None] * new_capacity
        new_threshold_limit = new_capacity * self.threshold

        for hash_value_ind in range(0, self.capacity):
            if self.hash_map[hash_value_ind] == None:
                continue

            for (k, v) in self.hash_map[hash_value_ind]:
                hash_value = self.calculate_hash(k, new_capacity)

                if new_hash_map[hash_value] == None:
                    new_hash_map[hash_value] = [(k, v)]
                else:
                    new_hash_map[hash_value].append((k, v))

        self.capacity = new_capacity
        self.hash_map = new_hash_map
        self.threshold_limit = new_threshold_limit

    def get(self, key):
        hash_value = self.calculate_hash(key, self.capacity)

        if self.hash_map[hash_value] == None:
            raise Exception("Invalid key.")

        for (k, v) in self.hash_map[hash_value]:
            if k == key:
                return v

        raise Exception("Invalid key.")

    def __str__(self):
        string_representation = f"\n[ Capacity:{self.capacity}  Size:{self.size} Threshold:{self.threshold} Threshold Limit:{self.threshold_limit} ]\n"

        string_representation += "# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n"

        for (ind, l) in enumerate(self.hash_map):
            string_representation += f"{ind} : "
            if l == None:
                string_representation += "None"
            else:
                for (key, val) in self.hash_map[ind]:
                    string_representation += str((key, val, abs(hash(key)))) + " -> "
            string_representation += "\n"

        string_representation += "# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n"

        return string_representation


def main():
    hash_map = HashMap(10, 0.5)

    hash_map.add("zero", 0)
    hash_map.add("one", 1)
    hash_map.add("two", 2)
    hash_map.add("three", 3)
    hash_map.add("four", 4)
    print(hash_map)

    print(hash_map.remove("zero"))
    print(hash_map)

    hash_map.add("five", 5)
    print(hash_map)

    hash_map.remove

    hash_map.add("six", 6)
    print(hash_map)

    hash_map.add("seven", 7)
    hash_map.add("eight", 8)
    hash_map.add("nine", 9)
    hash_map.add("ten", 10)

    print(hash_map)

    hash_map.add("two", "TWO")
    hash_map.add("three", "THREE")
    hash_map.add("five", "FIVE")
    hash_map.add("seven", "SEVEN")

    print(hash_map)

    print(hash_map.get("one"))
    print(hash_map.get("two"))
    print(hash_map.get("three"))

    try:
        print(hash_map.get("twenty"))
    except Exception as e:
        print("Exception:", e)


if __name__ == "__main__":
    main()
