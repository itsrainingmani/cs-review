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
        while i > 0 and self.heap[i] < self.heap[self.get_parent_index(i)]:
            self.swap(i, self.get_parent_index(i))
            i = self.get_parent_index(i)

    def filter_down(self, index):
        min_index = 0
        left, right = self.get_children_indices(index)
        if right >= len(self.heap):
            if left >= len(self.heap):
                return
            else:
                min_index = left
        else:
            if self.heap[left] <= self.heap[right]:
                min_index = left
            else:
                min_index = right
        if self.heap[index] > self.heap[min_index]:
            self.swap(min_index, index)
            self.filter_down(min_index)

    def swap(self, i1, i2):
        temp = self.heap[i1]
        self.heap[i1] = self.heap[i2]
        self.heap[i2] = temp

    # Broken
    def remove(self, value):
        try:
            index = self.heap.index(value)
        except ValueError:
            print("The value does not exist in the heap")
            return False

        self.heap[index] = self.heap[self.count - 1]
        self.heap.pop()
        self.count -= 1
        self.filter_down(index)

        return True

    def contains(self, value):
        start = 0
        nodes = 1

    def get_parent_index(self, cur_index):
        return (cur_index - 1) // 2

    def get_children_indices(self, cur_index):
        return 2 * cur_index + 1, 2 * cur_index + 2


if __name__ == "__main__":
    mh = MinHeap()

    for i in [3, 9, 12, 13, 1]:
        mh.add(i)
        print(mh)

    mh.remove(1)
    print(mh)
