# https://www.hackerrank.com/challenges/ctci-ransom-note/problem

if __name__ == '__main__':
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])

    magazine = input().rstrip().split()
    ransom = input().rstrip().split()

    dic = {}

    for word in magazine:
        if word not in dic.keys():
            dic[word] = [1, 0]
        else:
            dic[word][0] += 1
    for word in ransom:
        if word not in dic.keys():
            dic[word] = [0, 1]
        else:
            dic[word][1] += 1
    answer = 'Yes'
    for value in dic.values():
        if value[1] > value[0]:
            answer = 'No'
            break

    print(answer)
