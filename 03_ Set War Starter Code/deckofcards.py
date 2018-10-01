#Homework 03
#Justin Gallicchio
#CSE 2050
import doublylinked

class DeckOfCards:
    def __init__(self, cards):
        self.deck = doublylinked.createlink(cards)

    def dealTop():
        return self.deck.removeFirst()

    def dealBottom():
        return self.deck.removeLast()

    def addBottom(card):
        self.deck.addLast(card)

    def addTop(cards):
        self.deck.addFirst(card)

    def addPileTop(pile):
        self.deck.addDeck(pile, 'top')

    def addPileBottom(pile):
        self.deck.addDeck(pile, 'bottom')

    def deal(nplayers, ncards=None):
        players = {}
        cardind = ncards
        for people in range(nplayers):
            players{people: doublylinked.createlink(None)}
        if ncards is None:
            while self.deck._length > 0:
                for play in range(nplayers):
                    players[play].addFirst(self.removeFirst())
        else:
            while cardind > 0:
                for play in range(nplayers):
                    players[play].addFirst(self.removeFirst())
                cardind -= 1

    def __len__():
        return self.deck._length
