#Homework 03
#Justin Gallicchio
#CSE 2050
import doublylinked

class DeckOfCards:
    def __init__(self, cards=None):
        self.deck = doublylinked.createlink(cards)

    def dealTop(self):
        return self.deck.removeFirst()

    def dealBottom(self):
        return self.deck.removeLast()

    def addBottom(self, card):
        self.deck.addLast(card)

    def addTop(self, card):
        self.deck.addFirst(card)

    def addPileTop(self, pile):
        self.deck.addDeck(pile, 'top')

    def addPileBottom(self, pile):
        self.deck.addDeck(pile, 'bottom')

    def deal(self, nplayers, ncards=None):
        players = []
        cardind = ncards
        for people in range(nplayers):
            players.append(DeckOfCards())
        if ncards is None:
            while self.deck._length > 0:
                for play in range(nplayers):
                    players[play].addTop(self.deck.removeFirst())
        else:
            while cardind > 0:
                for play in range(nplayers):
                    players[play].addTop(self.deck.removeFirst())
                cardind -= 1
        return players

    def view(self):
        return self.deck.CreateList

    def __len__(self):
        return self.deck._length
