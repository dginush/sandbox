# https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem


def check(phrase):
    unclosed = []
    for i in range(len(phrase)):
        if phrase[i] in matches.keys():
            unclosed.append(matches[phrase[i]])
        elif len(unclosed) == 0:
            return 'NO'
        elif phrase[i] == unclosed[-1]:
            del unclosed[-1]
        else:
            return 'NO'
    return 'YES' if len(unclosed) == 0 else 'NO'


matches = {'{': '}', '[': ']', '(': ')'}

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        expression = input()
        print(check(expression))
