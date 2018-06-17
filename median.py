def merge_halves(a, l, r):
    l_index, r_index, a_index = 0, 0, 0

    while l_index < len(l) and r_index < len(r):
        if l[l_index] < r[r_index]:
            a[a_index] = l[l_index]
            l_index += 1
        else:
            a[a_index] = r[r_index]
            r_index += 1
        a_index += 1
    a[a_index:len(a)] = l[l_index:] + r[r_index:]
    return a


def merge_sort(a):
    l2 = int(len(a) / 2)
    left = a[:l2]
    right = a[l2:]

    if (len(left)) is 1 and len(right) is 1:
        a[0], a[1] = (left[0], right[0]) if left[0] < right[0] else (right[0], left[0])
        return a

    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)

    merged = merge_halves([None] * (len(left) + len(right)), left, right)

    return merged


def return_median(array):
    l2 = int(len(array) / 2)

    return (array[l2 - 1] + array[l2]) / 2.0 if len(array) % 2 == 0 else array[l2]
    pass


if __name__ == '__main__':
    n = int(input())

    a = []

    for _ in range(n):
        a_item = int(input())
        a.append(a_item)
        print("{:.1f}".format(return_median(merge_sort(a))))
