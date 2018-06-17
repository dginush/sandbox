# https://www.hackerrank.com/challenges/ctci-merge-sort/problem
import os


def countInversions(arr):
    count = 0
    for i in range(0, len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j] < arr[j - 1]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                count += 1
    return count


arr = [2, 1, 3, 1, 2]
print(countInversions(arr))

#
# if __name__ == '__main__':
#     t = int(input())
#     for t_itr in range(t):
#         n = int(input())
#         arr = list(map(int, input().rstrip().split()))
#         result = countInversions(arr)
#         print(result)
