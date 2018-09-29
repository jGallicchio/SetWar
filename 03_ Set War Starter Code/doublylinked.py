def createlink(L):
    for item in L:
        #add items using linked list class
        pass

class ListNode:
    def __init__(self, data, prev = None, link = None):
		self.data = data
		self.prev =	prev
		self.link =	link
		if prev is not None:
			self.prev.link = self
		if link is not None:
			self.link.prev = self

#ate Linked List class

class DubLinkedList:
    def __init__(self):
        self._head = None
        self._length = 0
        self._tail = None

    def addFirst(self, item):
        if len(self) == 0:
            self._tail = self._head = ListNode(item, None, None)
        else:
            newnode = ListNode(item, None, self._head)
            self._head.prev = newnode
            self._head = newnode
        self._length += 1

    def addLast(self, item):
        if len(self) == 0:
            return addFirst(item)
        else:
            newnode = ListNode(item, self._tail, None)
            self._tail.link = newnode
            self._tail = newnode
        self._length += 1

    def removeFirst(self):
        self._length -= 1
        item = self._head.item
        self._head = self._head.link
        return item

    def removeLast(self):
        if len(self) == 1:
            return self.removeFirst
        self._length -= 1
        currentnode = self._head
        while currentnode.link.link is not None:
            currentnode = currentnode.link
        item = currentnode.link.item
        currentnode.link = None
        return item

    def __len__(self):
        return self._length
