import random

from SortTest.SortTest import SortTest


class QuickSort(object):
    """
    随机化快速排序算法
    对于近乎有序的数组排序又很大性能提升
    """

    @classmethod
    def sort(cls, lists, *args):
        if len(args):
            l = args[0]
            r = args[1]
            if l >= r:
                return

            # 第一次递归返回标定点位置
            p = cls.partition(lists, l, r)
            cls.sort(lists, l, p - 1)
            cls.sort(lists, p + 1, r)

        else:
            cls.sort(lists, 0, len(lists) - 1)

    @staticmethod
    def partition(lists, l, r):

        # 随机化标定点
        random_index = int(random.random() * (r - l + 1) + l)
        lists[l], lists[random_index] = lists[random_index], lists[l]
        # v代表标定点的值
        v = lists[l]

        # arr[l + 1...j] < v; arr[j + 1...i] < v
        j = l
        for i in range(l+1, r+1):
            if lists[i] < v:
                j += 1
                lists[i], lists[j] = lists[j], lists[i]
        lists[l], lists[j] = lists[j], lists[l]
        return j


if __name__ == '__main__':
    # test_lists = SortTest.generate_random_list(1000, 0, 1000)
    test_lists = SortTest.generate_near_ordered_list(1000000, 1000)
    SortTest.test_sort(QuickSort, test_lists)
