import copy

from SortTest.SortTest import SortTest


# 自底向上归并排序算法
class MergeSortBU(object):

    @staticmethod
    def merge(lists, l, mid, r):
        temp = copy.deepcopy(lists[l:])

        i, j = l, mid + 1
        for k in range(l, r + 1):
            if i > mid:
                lists[k] = temp[j - l]
                j += 1
            elif j > r:
                lists[k] = temp[i - l]
                i += 1
            elif temp[i - l] > temp[j - l]:
                lists[k] = temp[j - l]
                j += 1
            else:
                lists[k] = temp[i - l]
                i += 1

    @classmethod
    def sort(cls, lists):
        length = len(lists)
        sz = 1
        while sz < length:
            i = 0
            while i < length - sz:
                cls.merge(lists, i, i + sz -1, min(i + sz * 2 -1, length - 1))
                # print(lists)
                i += sz * 2 -1
            sz *= 2
        return lists


if __name__ == '__main__':
    test_lists = SortTest.generate_random_list(10, 0, 10)
    SortTest.test_sort(MergeSortBU, test_lists)
