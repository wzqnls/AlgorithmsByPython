import copy


class MergeSort(object):

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
            print(lists)

    def sort(self, lists, *args):
        if len(args):
            l = args[0]
            r = args[1]
            if l >= r:
                return

            mid = int((l + r) / 2)
            self.sort(lists, l, mid)
            self.sort(lists, mid + 1, r)
            self.merge(lists, l, mid, r)
        else:
            self.sort(lists, 0, len(lists) - 1)


if __name__ == '__main__':
    lists = [7, 3, 5, 1,4]
    merge_sort = MergeSort()
    merge_sort.sort(lists)
    print(lists)
