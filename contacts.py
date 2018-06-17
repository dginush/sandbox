# https://www.hackerrank.com/challenges/ctci-contacts/problem

class node:
    def __init__(self):
        self.counter = 0
        self.nexts = {}


def write_tree(name, length, root):
    if length == 0:
        return
    if name[0] not in root.keys():
        root[name[0]] = node()
    root[name[0]].counter += 1
    write_tree(name[1:], length - 1, root[name[0]].nexts)
    return


def count(name, length, root):
    if length == 1:
        if name[0] in root.keys():
            return root[name[0]].counter
        else:
            return 0
    else:
        if name[0] in root.keys():
            return count(name[1:], length - 1, root[name[0]].nexts)
        else:
            return 0


tree = {}

if __name__ == '__main__':
    n = int(input())

    for n_itr in range(n):
        opContact = input().split()

        op = opContact[0]

        contact = opContact[1]

        if op == 'add':
            # names.append(contact)
            write_tree(contact, len(contact), tree)

        elif op == 'find':
            counter = count(contact, len(contact), tree)
            print(counter)
