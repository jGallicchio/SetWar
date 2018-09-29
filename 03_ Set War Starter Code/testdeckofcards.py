import unittest
from deckofcards import DeckOfCards
# from ListDeckOfCards import DeckOfCards

class TestDeckOfCards(unittest.TestCase):

    def test_create_empty_deck(self):
        d = DeckOfCards()
        assert(len(d) == 0)

    def test_create_deck_from_list(self):
        s = "a b c d"
        d = DeckOfCards(s.split())
        self.assertNotEqual(len(d), 0)
        self.assertEqual(d.dealTop(), 'a')
        self.assertEqual(d.dealTop(), 'b')
        self.assertEqual(d.dealTop(), 'c')
        self.assertEqual(d.dealTop(), 'd')
        self.assertEqual(len(d), 0)

    def test_dealTop_and_dealBottom(self):
        s = "111 222 333 444 555 666 777 888 999"
        d = DeckOfCards(s.split())
        self.assertNotEqual(len(d), 0)
        assert(d.dealTop() == '111')
        assert(d.dealBottom() == '999')
        assert(d.dealTop() == '222')
        assert(d.dealBottom() == '888')
        assert(d.dealTop() == '333')
        assert(d.dealBottom() == '777')
        assert(d.dealBottom() == '666')
        assert(d.dealBottom() == '555')
        assert(d.dealTop() == '444')
        self.assertEqual(len(d), 0)

    def test_addTop(self):
        d = DeckOfCards([3, 4, 5, 6, 7, 8])
        d.addTop(2)
        d.addTop(1)
        assert(d.dealTop() == 1)
        assert(d.dealTop() == 2)
        assert(d.dealTop() == 3)

    def test_addBottom(self):
        d = DeckOfCards([1,2,3])
        d.addBottom(4)
        d.addBottom(5)
        assert(d.dealBottom() == 5)
        assert(d.dealBottom() == 4)
        assert(d.dealBottom() == 3)

    def test_addPileTop(self):
        p = DeckOfCards([1,2])
        d = DeckOfCards([3,4])
        d.addPileTop(p)
        self.assertEqual(len(p), 0)
        assert(d.dealTop() == 1)
        assert(d.dealTop() == 2)
        assert(d.dealTop() == 3)
        assert(d.dealTop() == 4)
        self.assertEqual(len(d), 0)

    def test_addPileBottom(self):
        p = DeckOfCards([3,4])
        d = DeckOfCards([1,2])
        d.addPileBottom(p)
        self.assertEqual(len(p), 0)
        assert(d.dealTop() == 1)
        assert(d.dealTop() == 2)
        assert(d.dealTop() == 3)
        assert(d.dealTop() == 4)
        self.assertEqual(len(d), 0)

    def test_isEmpty(self):
        d = DeckOfCards([1,2])
        self.assertNotEqual(len(d), 0)
        d = DeckOfCards()
        self.assertEqual(len(d), 0)
        d = DeckOfCards([])
        self.assertEqual(len(d), 0)

    def test_deal_all_2ways(self):
        d = DeckOfCards([0,1,2,3,4,5,6,7])
        p = d.deal(2)
        self.assertEqual(len(d), 0)
        assert([p[0].dealTop() for i in range(4)] == [6,4,2,0])
        assert([p[1].dealTop() for i in range(4)] == [7,5,3,1])
        self.assertEqual(len(p[0]), 0)
        self.assertEqual(len(p[1]), 0)

    def test_deal_all_unequal_hands(self):
        d = DeckOfCards([0,1,2,3,4,5,6])
        p = d.deal(2)
        self.assertEqual(len(d), 0)
        assert([p[0].dealTop() for i in range(4)] == [6,4,2,0])
        assert([p[1].dealTop() for i in range(3)] == [5,3,1])
        self.assertEqual(len(p[0]), 0)
        self.assertEqual(len(p[1]), 0)

    def test_deal_all_3ways(self):
        d = DeckOfCards([0,1,2,3,4,5,6,7,8])
        p = d.deal(3)
        self.assertEqual(len(d), 0)
        assert([p[0].dealTop() for i in range(3)] == [6,3,0])
        assert([p[1].dealTop() for i in range(3)] == [7,4,1])
        assert([p[2].dealTop() for i in range(3)] == [8,5,2])
        self.assertEqual(len(p[0]), 0)
        self.assertEqual(len(p[1]), 0)
        self.assertEqual(len(p[2]), 0)


if __name__ == '__main__':
    unittest.main()
