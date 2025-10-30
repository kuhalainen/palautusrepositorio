import unittest
from statistics_service import StatisticsService
from player_reader import PlayerReader

from urllib import request
from player import Player
import random

class PlayerReaderStub:
    def __init__(self):
        self.players = []

    def get_players(self):
        return self.players

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.reader = PlayerReaderStub()

        self.top = Player("TopPlayer", "T1", 6, 4)    # 10 points
        self.second = Player("Second", "T1", 5, 2)    # 7 points
        self.third = Player("Third", "T2", 4, 3)      # 7 points
        self.solo = Player("Solo", "T3", 1, 0)        # 1 point

        self.reader.players.extend([self.top, self.second, self.third, self.solo])
        self.stats = StatisticsService(self.reader)

    #def test_hello_world(self):
    #    self.assertEqual("Hello world", "Hello world")

    def test_search_nonexistent_player(self):
        self.assertAlmostEqual(None, self.stats.search("KJFLFSLKJFSALKJFSALKJFSALKJFSA"))

    def test_search_partial_name_matches(self):
        result = self.stats.search("Top")
        self.assertIsNotNone(result)
        self.assertEqual(result.name, "TopPlayer")

    def test_team_returns_all_members(self):
        team_players = self.stats.team("T1")
        names = sorted([p.name for p in team_players])
        self.assertEqual(len(team_players), 2)
        self.assertEqual(names, ["Second", "TopPlayer"])

    def test_team_returns_empty_list_for_unknown_team(self):
        self.assertEqual(self.stats.team("NO_SUCH_TEAM"), [])

    def test_top_returns_players_sorted_by_points_and_off_by_one_behavior(self):
        top_list = self.stats.top(1)
        self.assertTrue(len(top_list) >= 1)
        self.assertEqual(top_list[0].name, "TopPlayer")
        self.assertEqual(len(top_list), 1 + 1)

    def test_top_with_zero_returns_single_top(self):
        res = self.stats.top(0)
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0].name, "TopPlayer")

    def test_top_raises_index_error_if_too_large(self):
        with self.assertRaises(IndexError):
            self.stats.top(len(self.reader.players))

if __name__ == "__main__":
    unittest.main()
