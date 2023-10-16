import random
import string
import matplotlib.pyplot as plt

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _fnv1a_hash(self, key):
        FNV_OFFSET_BASIS = 0x811c9dc5
        FNV_PRIME = 0x01000193

        hash_value = FNV_OFFSET_BASIS
        for char in key:
            hash_value ^= ord(char)
            hash_value *= FNV_PRIME
            hash_value &= 0xFFFFFFFF

        return hash_value

    def _get_bucket_index(self, key):
        hash_value = self._fnv1a_hash(key)
        return hash_value % self.size

    def insert(self, key, value):
        bucket_index = self._get_bucket_index(key)
        bucket = self.table[bucket_index]

        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)

        bucket.append((key, value))

    def search(self, key):
        bucket_index = self._get_bucket_index(key)
        bucket = self.table[bucket_index]
        comparisons = 0

        for existing_key, existing_value in bucket:
            comparisons += 1
            if existing_key == key:
                return existing_value, comparisons

        return None, comparisons

def test_if_search_is_correct():
    size = 100
    hash_table = HashTable(size)
    hash_table.insert("key1", "value1")

    keys = ["key1", "key2"]

    for key in keys:
        res = hash_table.search(key)
        if res is not None:
            print(f"{key}: {res[0]}")
        else:
            print(f"{key} wasn't found")

def generate_data(size):
    data = []
    for _ in range(size):
        key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(1, 20)))
        value = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(1, 200)))
        data.append((key, value))
    return data

def insert_data_into_table(hash_table, data):
    for i in data:
        hash_table.insert(i[0], i[1])

def search_data_in_table(hash_table, data):
    comparisons = 0
    for i in data:
        comparisons += hash_table.search(i[0])[1]
    return comparisons

def get_plots_data():
    hash_table = HashTable(5000)
    sizes = [100, 1000, 5000, 10000, 20000]
    comparisons_data = []

    for size in sizes:
        print("\n")
        print("TABLE SIZE AND ELEMENTS NUMBER: ", size)
        data = generate_data(size)

        insert_data_into_table(hash_table, data)
        comparisons = search_data_in_table(hash_table, data)
        comparisons_data.append([size, comparisons])

        print("Comparisons:", comparisons)
    return comparisons_data

def build_plots(comparisons_data):
    plt.ylabel("Data sizes")
    plt.title("Search perfomance")
    plt.grid()

    for i in comparisons_data:
        y = (5000*i[1])/i[0]
        plt.plot([0, 5000], [0, y], label=f"{i[0]}")

    plt.xticks([])

    plt.legend()
    plt.show()

def main():
    test_if_search_is_correct()
    """ comparisons_data = get_plots_data()
    build_plots(comparisons_data) """
         

if __name__ == '__main__':
    main()
