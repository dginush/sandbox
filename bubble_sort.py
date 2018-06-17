def swap():
    swaps = 0
    for i in range(0, len(a)):
        for j in range(1, len(a) - i):
            if a[j - 1] > a[j]:
                tmp = a[j]
                a[j] = a[j - 1]
                a[j - 1] = tmp
                swaps += 1
    return swaps


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    print("Array is sorted in {} swaps.".format(swap()))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))
