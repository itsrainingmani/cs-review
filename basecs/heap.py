class MinHeap:
    def __init__(self):
        self.heap = []
        self.count = 0

    def __str__(self):
        return str(self.heap)

    def add(self, value):
        self.heap.append(value)
        self.count += 1
        self.min_heapify()

    def min_heapify(self):
        i = self.count - 1
        while i > 0 and self.heap[i] < self.heap[(i - 1) // 2]:
            self.swap(i, (i - 1) // 2)
            i = (i - 1) // 2

    def swap(self, i1, i2):
        temp = self.heap[i1]
        self.heap[i1] = self.heap[i2]
        self.heap[i2] = temp

    # Broken
    def remove(self, value):
        try:
            index = self.heap.index(value)
            left, right = self.get_children_indices(index)
        except ValueError:
            print("The value does not exist in the heap")
            return False
        self.count -= 1
        self.heap[index] = self.heap[self.count]

        while (
            left < self.count
            and self.heap[index] > self.heap[left]
            or self.heap[index] > self.heap[right]
        ):
            if self.heap[left] < self.heap[right]:
                self.swap(left, index)
                index = left
            else:
                self.swap(right, index)
                index = right
        return True

    def contains(self, value):
        start = 0
        nodes = 1

        

    def get_parent_index(self, cur_index):
        return (index - 1) / 2

    def get_children_indices(self, cur_index):
        return 2 * cur_index + 1, 2 * cur_index + 2


if __name__ == "__main__":
    mh = MinHeap()

    for i in [3, 9, 12, 7, 1]:
        mh.add(i)
        print(mh)

    # mh.remove(9)
    print(mh)
