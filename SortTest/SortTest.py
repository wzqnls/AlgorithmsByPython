import random
from datetime import datetime


class SortTest(object):

    @staticmethod
    def generate_random_list(n , l, r):
        lists = [int(random.random() * (r + 1 - l)) for i in range(n)]
        return lists

    @staticmethod
    def generate_near_ordered_list(n, swap_times):
        lists = [i for i in range(n)]
        for i in range(swap_times):
            num1 = int(random.random() * len(lists))
            num2 = int(random.random() * len(lists))
            num1, num2 = num2, num1
        return lists

    @staticmethod
    def print_list(lists):
        for i in lists:
            print(i + " ")
        print('\n')

    @staticmethod
    def is_sorted(lists):

        for i in range(len(lists) - 1):
            if lists[i] > lists[i + 1]:
                return False
        return True

    @classmethod
    def test_sort(cls, class_name, lists):
        start_time = datetime.now()
        class_name.sort(lists)
        # lists.sort()
        end_time = datetime.now()
        spend_time = end_time - start_time
        if cls.is_sorted(lists):
            print(class_name.__name__ + ": " + str(spend_time.total_seconds()) + '\n')
