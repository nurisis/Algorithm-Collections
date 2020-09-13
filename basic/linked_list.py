class Node:
    def __init__(self, data=None) -> None:
        super().__init__()
        if data:
            self.data = data
        else:
            self.data = None
        self.next = None

    def set_data(self, data):
        self.data = data

    def set_next(self, node):
        self.next = node


class linked_list(object):
    def __init__(self) -> None:
        super().__init__()
        self.head = None

    def add(self, data):
        node = Node(data)
        if self.head:
            temp_node = self.head
            # 마지막 노드를 찾는다
            while True:
                if temp_node.next:
                    temp_node = temp_node.next
                else:
                    break
            temp_node.next = node
        else:
            self.head = node

    def remove(self, data):
        temp = self.head
        # head 노드를 바꿀 경우
        if temp.data == data:
            self.head = temp.next
            return

        while True:
            if not temp:
                break
            if temp.next and temp.next.data == data:
                c_node = temp.next
                temp.next = c_node.next
                break
            temp = temp.next

    def to_string(self):
        temp = self.head
        while temp:
            print(f"{temp.data} ->", end=' ')
            temp = temp.next
