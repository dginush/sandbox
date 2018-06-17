# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem


# def solve(arr, money):
#     for i in range(len(arr)):
#         ai = arr[i]
#         if ai >= money:
#             # print('i={}, arr[i]={}, money={}'.format(i, arr[i], money))
#             continue
#         target_aj = money - ai
#         for j in range(i + 1, len(arr)):
#             aj = arr[j]
#             if aj >= money:
#                 continue
#             if target_aj == aj:
#                 print("{} {}".format(i + 1, j + 1))
#                 return
def solve(a, money):
    b = {a[i]: i + 1 for i in range(0, len(a))}
    for i in range(len(a)):
        if money - a[i] in b:
            print("{} {}".format(i + 1, b[money - a[i]]))
            break


'''
2
4
5
1 4 5 3 2
4
4
2 2 4 3


'''

if __name__ == '__main__':
    t = int(input())  # number of trips

    for t_itr in range(t):
        money = int(input())  # money for the specific trip

        n = int(input())  # number of flavours

        arr = list(map(int, input().rstrip().split()))  # flavours prices array

        solve(arr, money)
