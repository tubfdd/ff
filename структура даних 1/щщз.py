class Node:
    def init(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def str(self):
        return f"{self.data} -> {self.next}"


class DoubleLinkedList:

    def init(self):
        self.head = None
        self.tail = None

    def str(self):
        return str(self.head)

    def push_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def push_start(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def pop_end(self):
        if not self.tail:
            return None

        data = self.tail.data

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return data

    def pop_start(self):

        if not self.head:
            return None

        data = self.head.data

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return data


class Shop:
    def init(self):

        self.queue1 = DoubleLinkedList()
        self.queue2 = DoubleLinkedList()
        self.queue3 = DoubleLinkedList()

    def add_buyer(self, name, idx):

        if idx == 1:
            self.queue1.push_end(name)
        elif idx == 2:
            self.queue2.push_end(name)
        elif idx == 3:
            self.queue3.push_end(name)
        else:
            print("Невірний номер каси!")

    def serve_buyer(self, idx):

        if idx == 1:
            buyer = self.queue1.pop_start()
            queue = self.queue1
        elif idx == 2:
            buyer = self.queue2.pop_start()
            queue = self.queue2
        elif idx == 3:
            buyer = self.queue3.pop_start()
            queue = self.queue3
        else:
            print("Невірний номер каси!")
            return

        if buyer:
            print(f"Покупець {buyer} був обслугований на касі {idx}.")
        else:
            print(f"Черга {idx} вже порожня.")


        if queue.head is None:
            self._reorder(idx)

    def _reorder(self, idx):

        last_buyer = None

        if self.queue3.tail:
            last_buyer = self.queue3.pop_end()
        elif self.queue2.tail:
            last_buyer = self.queue2.pop_end()
        elif self.queue1.tail:
            last_buyer = self.queue1.pop_end()

        if last_buyer:
            if idx == 1:
                self.queue1.push_end(last_buyer)
            elif idx == 2:
                self.queue2.push_end(last_buyer)
            elif idx == 3:
                self.queue3.push_end(last_buyer)
            print(f"Покупець {last_buyer} переміщений у чергу {idx}.")
        else:
            print("Немає покупців для переміщення.")

    def display_info(self):

        print("Черга 1:", self._queue_to_list(self.queue1))
        print("Черга 2:", self._queue_to_list(self.queue2))
        print("Черга 3:", self._queue_to_list(self.queue3))