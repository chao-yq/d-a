class Node:
    """
    data
    _next
    """

    def __init__(self, data, pnext=None):
        self.data = data
        self._next = pnext
        if pnext is None:
            self._next = None

        def __print__(self):
            return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        # self.head._next = None

    def isEmpty(self):
        return self.length == 0

    def insert(self, index, dataNode):
        if isinstance(dataNode, Node):
            item = dataNode
        else:
            item = Node(dataNode)
        if index < 0 or index > self.length:
            print("Insert index outsize !")
            return

        if index == 0:
            item._next = self.head
            self.head = item
            self.length += 1
            return
        i = 0
        tmpNode = self.head
        prev = self.head
        while i < self.length:
            prev = tmpNode
            if None != tmpNode._next:
                tmpNode = tmpNode._next
            i += 1
            if i == index:
                item.__next = tmpNode
                prev._next = item
                self.length += 1

    def append(self, dataNode):
        if isinstance(dataNode, Node):
            item = dataNode
        else:
            item = Node(dataNode)
        if self.head is None:
            self.head = item
            self.head._next = None
            self.length += 1
        else:
            node = self.head
            while None != node._next:
                node = node._next
            node._next = item
            self.length += 1

    def delete(self, index):
        if self.isEmpty():
            print("already empty! ")
            return
        if index < 0 or index > self.length:
            print("index outsize !")
            return
        node = self.head
        (prev) = self.head
        if index == 0:
            self.head = self.head._next
            self.length -= 1
        i = 1
        while i < index and node._next:
            if i == index:
                prev._next = node._next
                self.length -= 1
                return
            prev = node
            node = node.next
            i += 1

    def query(self, nodeData):
        node = self.head
        i = 0
        while i < self.length:
            if nodeData == node.data:
                return i
            i += 1
            node = node._next

        return "not in list"

    def clear(self):
        self.head = None
        self.length = 0

    def __str__(self):
        Head = self.head.data
        List = "|"
        node = self.head
        for i in range(0, self.length):
            List = List + '->' + str(node.data)
            node = node._next
        List = "HEAD:" + str(Head) + "\nLIST:" + str(List)
        return List


list = LinkedList()
list.append(1)
list.append(2)
list.append(3)
print(list)
list.insert(0, 0)
print(list)
list.insert(4, 4)
print(list)
# print(list.isEmpty())
# list.appen(Node(2))
# print(list.head.data)
# list.appen(Node(3))
# print(list.head._next.data)
# print(list)
# list.delete(0)
# print(list.query(2))
# print(list)
