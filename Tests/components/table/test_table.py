import unittest
import numpy as np
import components.table as table
import components.tournament as tournament
import components.table_player as player
from components.constants import Street


class MyTableTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.level = tournament.Level(4, 400)
        self.level2 = tournament.Level(5, 600)
        self.tour = tournament.Tournament(level=self.level)
        self.p1 = player.TablePlayer(name="Toto", seat=1, stack=2000)
        self.p2 = player.TablePlayer(name="Tata", seat=2, stack=2500)
        self.p3 = player.TablePlayer(name="Titi", seat=6, stack=25000)
        self.p4 = player.TablePlayer(name="Tété", seat=4, stack=120327)
        self.p5 = player.TablePlayer(name="Tutu", seat=5, stack=267)
        self.pl_list = [self.p1, self.p2, self.p3, self.p4]

    def test_new_table(self):
        tab = table.Table()
        self.assertIsInstance(tab, table.Table)
        self.assertIsInstance(tab.deck, table.Deck)
        self.assertIsInstance(tab.board, table.Board)
        self.assertIsInstance(tab._pots, list)
        self.assertIsInstance(tab.players, table.Players)
        self.assertIsInstance(tab.current_pot, table.Pot)
        self.assertIsInstance(tab.street, Street)
        self.assertEqual(tab.street, Street.PREFLOP)
        self.assertEqual(tab.pot, 0)
        self.assertEqual(tab.deck.len, 52)
        self.assertEqual(tab.board.len, 0)
        self.assertEqual(len(tab._pots), 1)
        with self.assertRaises(ValueError):
            tab.max_players = 11
        tab.max_players = 9
        self.assertEqual(tab.max_players, 9)
        tab.level = self.level2
        self.assertEqual(tab.level.sb, 300)
        tab.add_tournament(self.tour)
        self.assertEqual(tab.level.sb, 200)
        self.assertIsInstance(tab.tournament, tournament.Tournament)
        self.assertIsInstance(tab._tournament, tournament.Tournament)
        self.assertEqual(self.level.bb, 400)

    def test_playing_order(self):
        tab = table.Table()
        for pl in self.pl_list:
            pl.sit(tab)
        self.p1.distribute("AcKc")
        self.assertEqual(tab.playing_order, [2, 4, 6, 1])
        self.assertIsInstance(tab.players_waiting, list)
        self.assertEqual(tab.players_waiting, [self.p2, self.p4, self.p3, self.p1])
        tab._street = Street.FLOP
        self.assertEqual(tab.playing_order, [6, 1, 2, 4])
        self.assertEqual(tab.players_waiting, [self.p3, self.p1, self.p2, self.p4])
        self.assertEqual(self.p1.stack, 2000)
        self.p2.bet(4000)
        self.assertEqual(self.p2.stack, 0)
        self.assertTrue(self.p2.is_all_in)
        self.assertFalse(self.p2.can_play)
        self.assertEqual(tab.players_waiting, [self.p3, self.p1, self.p4])
        self.assertEqual(self.p1.to_call, 2000)
        self.p1.call()
        self.assertEqual(tab.players_waiting, [self.p3, self.p4])
        tab.draw_flop("As", "Ad", "Ah")
        self.assertEqual(self.p1.hand_score, 11)
        self.assertEqual(self.p1.rank_class, 2)
        self.assertEqual(self.p1.class_str, "Four of a Kind")

    def test_draws(self):
        tab = table.Table()
        tab.draw_flop("As", "Ad", "Ah")
        self.assertEqual(tab.board.len, 3)
        self.assertTrue((tab.board.values[:3] == np.array(["As", "Ad", "Ah"])).all())
        self.assertRaises(ValueError, lambda: tab.draw_flop())
        self.assertRaises(ValueError, lambda: tab.draw_turn("As"))
        self.assertRaises(ValueError, lambda: tab.draw_river("Jd"))
        tab.draw_turn("Ac")
        self.assertEqual(tab.board.len, 4)
        self.assertEqual(tab.board["turn"], "Ac")
        self.assertTrue((tab.board.values[:4] == np.array(["As", "Ad", "Ah", "Ac"])).all())
        self.assertRaises(ValueError, lambda: tab.draw_flop())
        self.assertRaises(ValueError, lambda: tab.draw_turn("Jd"))
        tab.draw_river("Jd")
        self.assertEqual(tab.board.len, 5)
        self.assertEqual(tab.board["river"], "Jd")
        self.assertTrue((tab.board.values == np.array(["As", "Ad", "Ah", "Ac", "Jd"])).all())

    def test_pregame_betting_and_odds(self):
        tab = table.Table()
        tab.max_players = 6
        tab.add_tournament(self.tour)
        for pl in self.pl_list:
            pl.sit(tab)
        tab.bb = 2
        tab.players.distribute_positions()
        tab.post_pregame()
        self.assertEqual(tab.current_pot.value, 800)
        self.assertEqual(tab.current_pot.highest_bet, tab.level.bb)
        self.assertEqual(tab.players[1].to_call, 0)
        self.assertEqual(tab.players[1].pot_odds, float("inf"))
        self.assertEqual(tab.players[1].req_equity, 0)
        self.assertEqual(tab.players[1].current_bet, 400)
        self.assertEqual(tab.players[2].to_call, 400)
        self.assertEqual(tab.players[2].pot_odds, 2)
        self.assertEqual(tab.players[2].current_bet, 0)
        self.assertEqual(tab.players[2].req_equity, 1/3)
        self.assertEqual(tab.players[4].to_call, 400)
        self.assertEqual(tab.players[6].to_call, 200)
        self.assertEqual(tab.players[6].pot_odds, 4)
        self.assertEqual(tab.players[6].req_equity, 1/5)
        self.assertEqual(tab.players[6].current_bet, 200)


if __name__ == '__main__':
    unittest.main()
