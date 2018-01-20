import random

from SortTest.SortTest import SortTest


class MaxHeap(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.data = [-1] * (capacity + 1)

    def size(self):
        return self.count

    def insert(self, item):
        assert self.count + 1 <= self.capacity
        self.data[self.count + 1] = item
        self.count += 1
        self.shift_up(self.count)

    def shift_up(self, k):

        while k > 1 and self.data[k // 2] < self.data[k]:
            self.data[k // 2], self.data[k] = self.data[k], self.data[k // 2]
            k //= 2

    def shift_down(self, k):
        while 2 * k <= self.count:
            # j代表左儿子, j+1代表右儿子
            j = 2 * k

            # 如果右儿子存在且比左二子大，则k与右儿子比较交换
            if j + 1 <= self.count and self.data[j] < self.data[j + 1]:
                j += 1

            if self.data[k] < self.data[j]:
                self.data[k], self.data[j] = self.data[j], self.data[k]
                k = j
            else:
                break

    def extract_max(self):
        assert self.count > 0
        ret = self.data[1]
        self.data[1] = self.data[self.count]
        self.count -= 1
        self.shift_down(1)

        return ret

    def get_max(self):
        assert self.count > 0
        return self.data[1]


if __name__ == '__main__':

    max_heap = MaxHeap(100)
    for i in range(50):
        max_heap.insert(int(random.random() * 10000000))

    print(max_heap.size())

    res = [""] * max_heap.size()
    for i in range(max_heap.size()):
        res[i] = max_heap.extract_max()
    print(res)

    # test_lists = SortTest.generate_random_list(100000, 0, 1000000)
    # SortTest.test_sort()
