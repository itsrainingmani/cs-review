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

    def reverseTraverse(self):
        # First check if the tail exists
        if self.tail != None:
            # now set the current node to be the tail
            curr = self.tail
            # we forward traverse the list until we reach the node before the current node

            # Since we move the current node back one link in each step, we check to see that it's not
            # the head node yet
            while curr != self.head:
                prev = self.head
                while prev.next != curr:
                    prev = prev.next
                print(prev.next.value)
                curr = prev
            print(curr.value)


class DoublyLL:
    def __init__(self, init_node=None):
        if init_node:
            # If we give an init node we check if it is an instance of the DoubleNode class
            # If it is not, we raise a TypeError that can be handled by the calling code
            if not isinstance(init_node, DoubleNode):
                raise TypeError("Init node must be of type DoubleNode")
        self.head = init_node
        self.tail = init_node

    def __str__(self):
        if not self.head:
            return ""
        n = self.head
        s = str(n.value) + " <-> "
        while n.next:
            s += str(n.next.value) + " <-> "
            n = n.next
        return s

    def insert(self, node):
        if not isinstance(node, DoubleNode):
            raise TypeError("Node must be of type DoubleNode")
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def delete(self, value):
        if self.head == None:
            return False
        if value == self.head.value:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return True
        else:
            n = self.head.next
            while n != None and n.value != value:
                n = n.next
            if n == self.tail:
                self.tail = self.tail.prev
                self.tail.next = None
                return True
            elif n != None:
                n.prev.next = n.next
                n.next.prev = n.prev
                return True
            return False

    def reverseTraverse(self):
        n = self.tail
        while n != None:
            print(n.value)
            n = n.prev

    # Same as LL
    def traverse(self):
        n = self.head
        while n != None:
            print(n.value)
            n = n.next

    # Same as LL
    def search(self, value):
        n = self.head
        while n and n.value != value:
            n = n.next
        return n != None


class DoubleNode:
    def __init__(self, val):
        self.value = val
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.value)


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

    def __str__(self):
        return str(self.value)


if __name__ == "__main__":
    try:
        dll = DoublyLL(Node(3))
    except TypeError:
        dll = DoublyLL(DoubleNode(3))
    # print(dll)

    dll.insert(DoubleNode(4))
    dll.insert(DoubleNode(30))
    dll.insert(DoubleNode(300))
    # dll.reverseTraverse()
    print(dll.delete(300))
    print(dll)
    # ll = SinglyLL(Node(1))
    # ll.insert(Node(45))
    # ll.insert(Node(60))
    # ll.insert(Node(12))
    # # print(ll.head, ll.tail)
    # print(ll)

    # # print(ll.search(11))
    # print(ll.delete(45))

    # # ll.traverse()
    # ll.reverseTraverse()
    # print(ll)
