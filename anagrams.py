# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

def check(string_a, string_b):
    to_be_deleted = 0
    for letter in string_a:
        if letter not in merge.keys():
            merge[letter] = [0, 0]
        merge[letter][0] += 1
    for letter in string_b:
        if letter not in merge.keys():
            merge[letter] = [0, 0]
        merge[letter][1] += 1
    for value in merge.values():
        to_be_deleted += abs(value[0] - value[1])
    return to_be_deleted


merge = {}

if __name__ == '__main__':
    a = input()
    b = input()
    print(check(a, b))
