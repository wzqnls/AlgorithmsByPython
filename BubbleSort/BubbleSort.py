
def bubble_sort(lists):
    length = len(lists)
    for i in range(0, length):
        for j in range(0, length - 1 - i):
            if lists[j] > lists[j + 1]:
                lists[j + 1], lists[j] = lists[j], lists[j + 1]
    return lists


if __name__ == '__main__':
    lists = [1, 2, 3, 6, 8, 22, 11, 77, 66]
    print(bubble_sort(lists))
