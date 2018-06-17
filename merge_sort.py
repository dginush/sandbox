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


if __name__ == '__main__':
    arr = [1, 5, 23, 77, 34, 12, 88, 553, 234, 612, 551, 226, 78]
    # arr = [5, 3, 1]
    print(merge_sort(arr))
