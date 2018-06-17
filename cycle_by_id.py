went_trough = []


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def has_cycle(head):
    id_head = id(head)
    if head is None:
        went_trough.clear()
        del went_trough[:]
        return False
    elif id_head not in went_trough:
        went_trough.append(id_head)
        return has_cycle(head.next)
    else:
        went_trough.clear()
        del went_trough[:]
        return True

head = Node
head.next = Node(data=2)
head.next.next = Node(data=3)
head.next.next.next = Node(data=4)
head.next.next.next.next = head.next.next


print(has_cycle(head))
print(went_trough)

head = Node
head.next = Node(data=2)
head.next.next = Node(data=3)
head.next.next.next = Node(data=4)
head.next.next.next.next = head.next.next

print(has_cycle(head))
print(went_trough)

