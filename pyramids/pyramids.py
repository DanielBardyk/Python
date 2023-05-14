import os
import sys
from math import ceil

DIR_PATH = os.path.dirname(__file__)

class Hlow:
    def __init__(self, sizelimit):
        self._sizelimit = sizelimit
        self._heapsize = 0
        self._heap = [0] * (self._sizelimit + 1)
        self._heap[0] = sys.maxsize
        self._ROOT = 1
    
    def _parent(self, i):
        return i // 2
    
    def _left(self, i):
        return 2 * i

    def _right(self, i):
        return 2 * i + 1
    
    def _is_leaf(self, pos):  
        return pos * 2 > self._heapsize
    
    def _swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def _maxheapify(self, i):
        left = self._left(i)
        right = self._right(i)
        if not self._is_leaf(i):
            if (self._heap[i] < self._heap[left] or
            self._heap[i] < self._heap[right]):
                
                if self._heap[left] > self._heap[right]:
                    self._swap(i, left)
                    self._maxheapify(left)
                else:
                    self._swap(i, right)
                    self._maxheapify(right)

    def insert(self, element):
        if self._heapsize >= self._sizelimit:
            return
        self._heapsize += 1
        self._heap[self._heapsize] = element

        current = self._heapsize

        while (self._heap[current] > self._heap[self._parent(current)]):
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def extract_max(self):
        popped = self._heap[self._ROOT]
        self._heap[self._ROOT] = self._heap[self._heapsize]
        self._heapsize -= 1
        self._maxheapify(self._ROOT)
        return popped
    
    def get_heapsize(self):
        return self._heapsize
    
    def get_max(self):
        if not self._heapsize:
            return self._heap[0]
        return self._heap[self._ROOT]
        

class Hhigh:
    def __init__(self, sizelimit):
        self._sizelimit = sizelimit
        self._heapsize = 0
        self._heap = [0] * (self._sizelimit + 1)
        self._heap[0] = -1 * sys.maxsize
        self._ROOT = 1
    
    def _parent(self, i):
        return i // 2
    
    def _left(self, i):
        return 2 * i

    def _right(self, i):
        return 2 * i + 1
    
    def _is_leaf(self, pos):
        return pos * 2 > self._heapsize
    
    def _swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def _minheapify(self, i):
        left = self._left(i)
        right = self._right(i)
        if not self._is_leaf(i):
            if (self._heap[i] > self._heap[left] or
            self._heap[i] > self._heap[right]):
                
                if self._heap[left] < self._heap[right]:
                    self._swap(i, left)
                    self._minheapify(left)
                else:
                    self._swap(i, right)
                    self._minheapify(right)

    def insert(self, element):
        if self._heapsize >= self._sizelimit:
            return
        self._heapsize += 1
        self._heap[self._heapsize] = element

        current = self._heapsize

        while (self._heap[current] < self._heap[self._parent(current)]):
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def extract_min(self):
        popped = self._heap[self._ROOT]
        self._heap[self._ROOT] = self._heap[self._heapsize]
        self._heapsize -= 1
        self._minheapify(self._ROOT)
        return popped
    
    def get_heapsize(self):
        return self._heapsize
    
    def get_min(self):
        if not self._heapsize:
            return self._heap[0]
        return self._heap[self._ROOT]


def get_data(filename):
	arr = []

	with open(f'{DIR_PATH}/{filename}', 'r') as f:
		n = int(f.readline())
		for line in f:
			arr.append(int(line))
	f.close()

	return arr, n

def find_medians(array, size):
    max_pyramid_size = int(size / 2) + 1
    medians = []

    hlow = Hlow(max_pyramid_size)
    hhigh = Hhigh(max_pyramid_size)
    for element in array:
        if element < hlow.get_max():
            hlow.insert(element)
        else:
            hhigh.insert(element)

        if hlow.get_heapsize() - hhigh.get_heapsize() > 1:
            largest = hlow.extract_max()
            hhigh.insert(largest)
        elif hhigh.get_heapsize() - hlow.get_heapsize() > 1:
            smallest = hhigh.extract_min()
            hlow.insert(smallest)

        if hlow.get_heapsize() == hhigh.get_heapsize():
            median1 = hlow.get_max()
            median2 = hhigh.get_min()
            medians.append([median1, median2])
        else:
            if hlow.get_heapsize() > hhigh.get_heapsize():
                median = hlow.get_max()
            else:
                median = hhigh.get_min()
            medians.append([median])
    return medians

def write_medians(medians):
    with open(f'{DIR_PATH}/{os.path.basename(__file__).split(".")[0]}_output.txt', 'w') as f:
        for m in medians:
            f.write(" ".join(map(str, m)) + '\n')
    f.close()

def main():
    filename = input("Enter the filename: ")
    array, size = get_data(filename)
    medians = find_medians(array, size)
    write_medians(medians)
         

if __name__ == '__main__':
    main()