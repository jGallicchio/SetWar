import unittest
from deckofcards import DeckOfCards

class TestDeck(unittest.TestCase):
    def testemptydeck(self):
        c = DeckOfCards()
        self.assertEqual(len(c), 0)

    def testdeckoften(self):
        c = DeckOfCards(['1020', '1020', '1020', '1020', '1020', '1020', '1020', '1020', '1020', '1020'])
        self.assertEqual(len(c), 10)

    def testdeckremovetop(self):
        c = DeckOfCards(['1020', '1020', '1020', '1020', '1020', '1020', '1020', '1020', '1020', '1020'])
        c.dealTop()
        self.assertEqual(len(c), 9)

    def testdeckremovebottom(self):
        c = DeckOfCards(['1020', '1020', '1020', '1020', '1020', '1020', '1020', '1020', '1020', '1020'])
        c.dealTop()
        self.assertEqual(len(c), 9)


unittest.main()
