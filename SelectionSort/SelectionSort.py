
def selection_sort(lists):
    length = len(lists)

    for i in range(0, length):
        min_index = i
        for j in range(i + 1, length):
            if lists[min_index] > lists[j]:
                min_index = j
        lists[i], lists[min_index] = lists[min_index], lists[i]

    return lists


if __name__ == '__main__':
    lists = [5, 4, 3, 2, 6, 8, 9, 10]
    print(selection_sort(lists))