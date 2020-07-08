class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def changeNext(self, node):
        self.next = node

    def removeNext(self):
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addBegin(self, data):
        temp = Node(data)
        temp.changeNext(self.head)
        self.head = temp

    def isEmpty(self):
        return self.head == None

    def getNodeDataList(self):
        rv = []
        current = self.head
        while current != None:
            rv.append(current.data)
            current = current.next
        return rv

    def removeEnd(self):
        if self.isEmpty():
            print("Can\'t list empty")
            return 

        if self.head.next == None:
            self.head = None
            return
        
        last = None
        current = self.head
        while current.next != None:
            last = current
            current = current.next
        last.next = None
        return

    def getHeadData(self):
        if not self.isEmpty():
            return self.head.data
