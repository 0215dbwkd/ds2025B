import random

class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.link:
            current = current.link
        current.link = Node(data)

    def remove(self, target):
        if self.head.data == target:
            self.head = self.head.link
            return
        current = self.head
        previous = None
        while current:
            if current.data == target:
                previous.link = current.link #삭제 역할
            previous = current
            current = current.link

    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return f"{target}을(를) 찾았습니다"
            else:
                current = current.link
        return f"{target}은(는) 링크드리스트 안에 존재하지 않습니다"

    def reverse_list(self):
        current = self.head
        previous = None
        while current:
            next_node = current.link
            current.link = previous
            previous = current
            current = next_node
        self.head = previous

    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while True:
            try:
                slow = slow.link
                fast = fast.link.link
                if slow is fast:
                    return True
            except:
                return False

    def __str__(self):
        node = self.head
        out_texts = ""
        while node is not None:
            out_texts = out_texts + f"{node.data} -> "
            node = node.link
        return out_texts + "end"


ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)
print(ll)

print(ll.search(100))
print(ll.search(10))

print(ll.detect_cycle())
# ll.head.link.link.link = ll.head  # 3번 노드가 1번 노드를 가리킨다
# print(ll.detect_cycle())
ll.remove(90)
ll.remove(10)
print(ll)

ll.reverse_list()
print(ll)
