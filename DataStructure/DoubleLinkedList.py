#  Node
class Node:
    """
    _prev
    data
    _next
    """

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self._prev = prev
        self._next = next
        if prev is None:
            self._prev = None
        if next is None:
            self._next = None

        def __print__():
            return str(self.data)


# DLL
class DoubleLinkedList:
    """
    head
    tail
    node
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def create(self, node):
        self.__init__()
        self.head = node
        self.tail = node
        node._prev = node._next = None
        self.length += 1

    def insert(self, index, dataNode):
        if isinstance(dataNode, Node):
            item = dataNode
        else:
            item = Node(dataNode)
        if index < 0 or index > self.length:
            print("Insert index outsize !")
            return
        # insert at head
        if index == 0:
            if self.head is None:  # no node in list
                # self.head = self.tail = item
                # item._prev = item._next = None
                # self.length += 1
                self.create(node=item)
            else:
                tmp = self.head
                self.head = item
                # item._prev = None
                item._next = tmp
                tmp._prev = item
                self.length += 1

        # insert at tail
        elif index == self.length:
            # print("add at tail")
            tmp = self.tail
            tmp._next = item
            item._prev = tmp
            item._next = None
            self.tail = item
            self.length += 1

        else:
            i = 0
            tmp = self.head
            while i < self.length:
                prev = tmp
                if None != tmp._next:
                    tmp = tmp._next
                    i += 1
                else:
                    print("error query index " + str(index) + "i = " + str(i))
                    break
                if i == index:
                    item._next = tmp
                    tmp._prev = item
                    item._prev = prev
                    prev._next = item
                    self.length += 1
                    break

    def traverse(self):
        print("traverse: (index,value)")
        tmp = self.head
        for i in range(0, self.length):
            print("(" + str(i) + "," + str(tmp.data) + ")")
            tmp = tmp._next

    def reverseTravers(self):
        print("reverseTravers: (index,value)")
        tmp = self.tail
        for i in range(0, self.length):
            print("(" + str(self.length - i) + "," + str(tmp.data) + ")")
            tmp = tmp._prev

    def searchNode(self, node):  # currenly just return the first node index matched
        if isinstance(node, Node):
            item = node
        else:
            item = Node(node)
        tmp = self.head
        for i in range(0, self.length):
            # print("(" + str(i) + "," + str(tmp.data) + ")")
            if tmp.data == item.data:
                return i
            tmp = tmp._next
        return "not found!"

    def deleteNode(self, index):
        if index < 0 or index >= self.length:
            print("Insert index outsize !")
            return False
        # delete first node
        if index == 0:
            self.head = self.head._next
            self.head._prev = None
            self.length -= 1
            # tmp = self.head._next
            # tmp._prev = None
            # self.head = tmp
            return True

        if index == self.length - 1:  # last node delete
            self.tail = self.tail._prev
            self.tail._next = None
            self.length -= 1
            return True

        if 0 < index < self.length:
            tmp = self.head
            for i in range(0, index):
                tmp = tmp._next
            prev = tmp._prev
            next = tmp._next
            prev._next = next
            next._prev = prev
            self.length -= 1
            return True

    def __str__(self):
        Head = self.head
        List = "|"
        node = self.head
        for i in range(0, self.length):
            List = List + '->' + str(node.data)
            node = node._next
        List = "HEAD:" + str(Head.data) + "\nLIST:" + str(List) + "\n tail:" + str(
            self.tail.data) + "\n Length: " + str(self.length)
        return List


dll = DoubleLinkedList()
# dll.create(node)
dll.insert(0, 0)
dll.insert(1, 1)
dll.insert(2, 2)
dll.insert(3, 3)
# print(dll)
dll.insert(1, 1)
dll.insert(0, 0)
# print(dll.searchNode(1))
print(dll)
dll.deleteNode(4)
dll.insert(4, 4)
print(dll)
# dll.traverse()
# dll.reverseTravers()
