import re

'''
signs = ['+', '-', '*', '/']


class Calculator(object):
    def evaluate(self, string):
        return 0


Calculator().evaluate("2 / 2 + 3 * 4 - 6")  # => 7
'''

'''
21 / 2 + 523 * 4 - 6
10     + 523 * 4 - 6
10     + 2092    - 6


'''
th = "241 / 2 * 43 - 53 + 3 + 523 * 4 / 2 - 6"
st1 = re.findall(r'\d+', th)
st2 = re.findall(r'[/+*/-]', th)

st1 = [int(x) for x in st1]
print(st1, len(st1))
print(st2, len(st2))

result = 0
i = 0
initial_length = len(st2)
while i < initial_length:
    if st2[i] == '*':
        st1[i] *= st1[i + 1]
        del st1[i + 1]
        del st2[i]
        initial_length -= 1
        continue
    if st2[i] == '/':
        st1[i] = int(st1[i] / st1[i + 1])
        del st1[i + 1]
        del st2[i]
        initial_length -= 1
        continue
    i += 1
print('h')

i = 0
while len(st2) > 0:
    if st2[i] == '+':
        st1[i] += st1[i + 1]
        del st1[i + 1]
        del st2[i]
    elif st2[i] == '-':
        st1[i] -= st1[i + 1]
        del st1[i + 1]
        del st2[i]

print('st1 is: ', st1)
