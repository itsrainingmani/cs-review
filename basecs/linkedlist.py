class SinglyLL:
    def __init__(self, init_node=None):
        self.head = init_node
        self.tail = init_node

    def __str__(self):
        n = self.head
        s = str(n.value) + " -> "
        while n.next:
            s += str(n.next.value) + " -> "
            n = n.next
        return s

    # Add a node to the tail of the list
    def insert(self, node):
        n = node.value
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    # Search a linked list for a value
    def search(self, value):
        n = self.head
        while n and n.value != value:
            n = n.next
        return n != None

    def delete(self, value):
        if self.head == None:
            return False

        n = self.head
        if n.value == value:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
            return True
        while n.next != None and n.next.value != value:
            n = n.next
        if n.next != None:
            if n.next == self.tail:
                self.tail = n
            n.next = n.next.next
            return True
        return False

    # Removes the tail and returns the value - HARDish
    # def pop(self):
    #     if self.head == None:
    #         return None
    #     elif self.head != None and self.head.next

    def traverse(self):
        n = self.head
        while n != None:
            print(n.value)
            n = n.next


class DoublyLL:
    def __init__(self, init_node=None):
        self.head = init_node
        self.tail = init_node

    def __str__(self):
        n = self.head
        s = str(n.value) + " <-> "
        while n.next:
            s += str(n.next.value) + " <-> "
            n = n.next
        return s


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

    def __str__(self):
        return str(self.value)


if __name__ == "__main__":
    ll = SinglyLL(Node(1))
    ll.insert(Node(45))
    ll.insert(Node(60))
    ll.insert(Node(12))
    print(ll.head, ll.tail)
    print(ll)

    # print(ll.search(11))
    # print(ll.delete(45))

    ll.traverse()
    # print(ll)
