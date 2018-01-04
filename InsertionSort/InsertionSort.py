def insertion_sort(lists):
    length = len(lists)

    for i in range(1, length):
        for j in range(i, 0, -1):
            if lists[j] < lists[j - 1]:
                lists[j], lists[j - 1] = lists[j - 1], lists[j]
            else:
                break
    return lists


if __name__ == '__main__':
    lists = [1, 3, 5, 7, 9, 8, 2, 4, 6, 100]
    print(insertion_sort(lists))
