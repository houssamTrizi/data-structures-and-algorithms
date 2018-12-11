class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class DoubleNode(Node):
    def __init__(self, value, next_node=None, prev_node=None):
        super().__init__(value, next_node)
        self.prev_node = prev_node


class LinkedList:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add(self, value):
        """O(1)"""
        pass

    def remove(self, value):
        """O(n)"""
        pass

    def contains(self, value):
        """O(n)"""
        pass


class SinglyLinkedList(LinkedList):

    def add(self, value):

        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node

    def remove(self, value):
        """
        we should consider these cases:

        1- the list is empty.
        2- the node to remove is the only one in the list.
        3- the node to remove is the head.
        4- the node to remove is the tail.
        5- the value to remove is somewhere in between.
        6- the node to remove doesn't exist.

        :param value: value to remove
        :return: True if the value is removed False otherwise
        """

        if not self.head:
            # Case 1
            return False

        node = self.head

        if node.value == value:
            if node == self.tail:
                # Case 2
                self.head = None
                self.tail = None
            else:
                # Case 3
                self.head = node.next_node
            return True

        while node.next_node and node.next_node.value != value:

            node = node.next_node

        if node.next_node:
            if node.next_node == self.tail:
                # Case 4
                self.tail = node
            # Case 5 if condition in line 73 is false
            node.next_node = node.next_node.next_node
            return True
        # Case 6
        return False

    def contains(self, value):
        """

        :param value: the value to search for
        :return: True if the value is found False otherwise
        """
        current = self.head

        while current and current.value != value:
            current = current.next_node

        if current:
            return True
        return False

    def traverse(self):
        current = self.head
        while current:
            yield current.value
            current = current.next_node

    def reverse_traverse(self):
        if self.tail:
            current = self.tail
            while current != self.head:
                previous = self.head
                while previous.next_node != current:
                    previous = previous.next_node
                yield current.value
                current = previous

    def __repr__(self):

        str_out = "*"
        current = self.head

        while current:
            str_out += f" --> {current.value}"

            current = current.next_node

        str_out += ""
        return str_out


class DoublyLinkedList(LinkedList):

    def add(self, value):
        node = DoubleNode(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next_node = self.head
            self.head.prev_node = node
            self.head = node

    def remove(self, value):
        if not self.head:
            # Case 1
            return False
        current = self.head

        if current.value == value:
            if current == self.tail:
                # Case 2
                self.head = None
                self.tail = None
            else:
                # Case 3
                self.head = self.head.next_node
                self.head.prev_node = None
            return True
        while current and current.value != value:
            current = current.next_node
        if current == self.tail:
            # Case 4
            self.tail = self.tail.prev_node
            self.tail.next_node = None
            return True
        elif current:
            # Case 5
            current.prev_node.next_node = current.next_node
            current.next_node.prev_node = current.prev_node
            return True
        # Case 6
        return False

    def traverse(self):
        current = self.head
        while current:
            yield current.value
            current = current.next_node

    def reverse_traverse(self):
        current = self.tail
        while current:
            yield current.value
            current = current.prev_node

    def __repr__(self):
        str_out = "*"
        current = self.head
        while current:
            str_out += f"<-- {current.value} -->"
            current = current.next_node
        str_out += "*"
        return str_out


if __name__ == '__main__':
    ls = DoublyLinkedList()

    for elt in range(20):
        ls.add(elt)
    print("*" * 10 + " Traverse ")
    [print(elt) for elt in ls.traverse()]
    [print(elt) for elt in ls.reverse_traverse()]

