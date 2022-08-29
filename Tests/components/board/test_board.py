import unittest

import numpy as np
import pandas as pd
from components import hand
from components import board
from components import card


class MyBoardTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.board = board.Board()
        self.board2 = board.Board(("As", "Ad", "Tc", "Td", card.Card("Ah")))
        self.board3 = board.Board(("Qd", "Ad", "Jc", "Td", card.Card("Ah")))
        self.board4 = board.Board(("Qd", "5d", "Td", "Tc", card.Card("Ah")))
        self.board5 = board.Board(("As", "Ad", "Ah"))
        self.board6 = board.Board(("Ks", "Qs", "Js"))

    def test_new_board(self):
        new_board = board.Board()
        self.assertIsInstance(new_board, board.Board)
        self.assertIsInstance(new_board, pd.Series)
        new_board = board.Board(["As", "Ad", "Tc"])
        self.assertIsInstance(new_board, board.Board)
        self.assertRaises(ValueError, lambda: board.Board(["As", "As", "Tc"]))
        self.assertRaises(ValueError, lambda: board.Board(["As", "Ad", "Tc", "Td", card.Card("Ah"), "Js"]))
        new_board = board.Board(("As", "Ad", "Tc", "Td", card.Card("Ah")))
        self.assertEqual(new_board["flop_1"], "As")
        self.assertEqual(new_board["flop_2"], "Ad")
        self.assertEqual(new_board["flop_3"], "Tc")
        self.assertEqual(new_board["turn"], "Td")
        self.assertEqual(new_board["river"], "Ah")

    def test_len(self):
        self.assertIsInstance(len(self.board), int)
        self.assertEqual(len(self.board), 0)
        self.board["flop_2"] = "As"
        self.board["flop_1"] = "Ad"
        self.assertEqual(len(self.board), 2)

    def test_add(self):
        self.assertRaises(ValueError, lambda: self.board.add("AA"))
        self.board.add("As")
        self.assertEqual(self.board["flop_1"], "As")
        self.board.add("Qs")
        self.assertNotEqual(self.board["flop_2"], "As")
        self.assertEqual(self.board["flop_2"], "Qs")
        self.assertRaises(ValueError, lambda: self.board.add("Qs"))

    def test_indexing(self):
        self.assertEqual(len(self.board2), 5)
        self.assertEqual(len(self.board2[:3]), 3)

    def test_flop_combination(self):
        self.assertEqual(len(self.board2.flop_combinations), 3)
        self.assertIsInstance(self.board2.flop_combinations[0], hand.Combo)
        combos = np.array([hand.Combo("AsAd"), hand.Combo("AsTc"), hand.Combo("AdTc")])
        for i in range(3):
            self.assertEqual(self.board2.flop_combinations[i], combos[i])

    def test_is_rainbow(self):
        self.assertTrue(self.board2.is_rainbow)
        self.assertFalse(self.board3.is_rainbow)
        self.assertFalse(self.board4.is_rainbow)
        self.assertTrue(self.board5.is_rainbow)
        self.assertFalse(self.board6.is_rainbow)

    def test_is_monotone(self):
        self.assertFalse(self.board2.is_monotone)
        self.assertFalse(self.board3.is_monotone)
        self.assertTrue(self.board4.is_monotone)
        self.assertFalse(self.board5.is_monotone)
        self.assertTrue(self.board6.is_monotone)

    def test_is_triplet(self):
        self.assertFalse(self.board2.is_triplet)
        self.assertFalse(self.board3.is_triplet)
        self.assertFalse(self.board4.is_triplet)
        self.assertTrue(self.board5.is_triplet)
        self.assertFalse(self.board6.is_triplet)

    def test_has_pair(self):
        self.assertTrue(self.board2.has_pair)
        self.assertFalse(self.board3.has_pair)
        self.assertFalse(self.board4.has_pair)
        self.assertTrue(self.board5.has_pair)
        self.assertFalse(self.board6.has_pair)

    def test_has_straightdraw(self):
        self.assertFalse(self.board2.has_straightdraw)
        self.assertTrue(self.board3.has_straightdraw)
        self.assertTrue(self.board4.has_straightdraw)
        self.assertFalse(self.board5.has_straightdraw)
        self.assertTrue(self.board6.has_straightdraw)

    def test_has_gutshot(self):
        self.assertTrue(self.board2.has_gutshot)
        self.assertTrue(self.board3.has_gutshot)
        self.assertTrue(self.board4.has_gutshot)
        self.assertFalse(self.board5.has_gutshot)
        self.assertTrue(self.board6.has_gutshot)

    def test_has_flushdraw(self):
        self.assertFalse(self.board2.has_flushdraw)
        self.assertTrue(self.board3.has_flushdraw)
        self.assertTrue(self.board4.has_flushdraw)
        self.assertFalse(self.board5.has_flushdraw)
        self.assertTrue(self.board6.has_flushdraw)

    def test_get_differences(self):
        self.assertEqual(self.board2._get_differences(), (0, 4, 4))
        self.assertEqual(self.board3._get_differences(), (2, 1, 3))
        self.assertEqual(self.board4._get_differences(), (7, 2, 5))
        self.assertEqual(self.board5._get_differences(), (0, 0, 0))
        self.assertEqual(self.board6._get_differences(), (1, 2, 1))


if __name__ == '__main__':
    unittest.main()
