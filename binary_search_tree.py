# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem


class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def checkBST(root, from_left, form_right):
    print("current root: {}, lefts: {}, rights: {}".format(root.data, from_left, form_right))
    if root.left is not None:
        if root.data > root.left.data and checkBST(root.left, True, False):
            pass
        else:
            return False
    if root.right is not None:
        if root.data < root.right.data and checkBST(root.right, False, True):
            pass
        else:
            return False
    return True


def main():
    root = node(5)

    root.left = node(4)
    root.right = node(7)

    root.left.left = node(3)
    root.left.right = node(8)

    print(checkBST(root, False, False))


if __name__ == '__main__':
    main()
    print('j')
