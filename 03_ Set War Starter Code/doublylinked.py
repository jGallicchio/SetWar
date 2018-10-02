def createlink(L):
    deck = DubLinkedList()
    if L is not None:
        for item in L:
            #add items using linked list class
            deck.addLast(item)
    return deck

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
        self._tail = None
        self._length = 0

    def _add(self, item, before, after):
        if item is not None:
            node = ListNode(item, before, after)
            if self._head is None:
                self._head = node
                self._tail = node
            if after == self._head:
                self._head.prev = node
                self._head = node
            elif before == self._tail:
                self._tail.link = node
                self._tail = node
            self._length += 1

    def addFirst(self, item):
        self._add(item, None, self._head)

    def addLast(self, item):
        self._add(item, self._tail, None)

    def _remove(self, node):
        if node is not None:
            before = node.prev
            after = node.link
            if node is self._head:
                self._head = after
            else:
                before.link = after
            if node is self._tail:
                self._tail = before
            else:
                after.prev = before
            self._length -= 1
            return node.data

    def removeFirst(self):
        return self._remove(self._head)

    def removeLast(self):
        return self._remove(self._tail)

    def addDeck(self, Deck2, AddLocation):
        if self is None: return Deck2
        if Deck2 is None: return self
        if AddLocation == 'bottom':
            if self._head is None:
                self._head = Deck2.deck._head
            else:
                self._tail.link = Deck2.deck._head
                Deck2.deck._head.prev = self._tail
            self._tail = Deck2.deck._tail
            self._length += Deck2.deck._length
            Deck2.deck.__init__()
            return self
        elif AddLocation == 'top':
            if self._head is None:
                self._head = Deck2.deck._head
            else:
                Deck2.deck._tail.link = self._head
                self._head.prev = Deck2.deck._tail
            self._head = Deck2.deck._head
            self._length += Deck2.deck._length
            Deck2.deck.__init__()
            return self

    def CreateList(self):
        cur = self._head
        Lst = []
        while cur is not None:
            Lst.append(cur.data)
            cur = cur.link
        return Lst
        
    def __len__(self):
        return self._length
