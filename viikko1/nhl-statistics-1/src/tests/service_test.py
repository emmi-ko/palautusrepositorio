import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_name_true(self):
        self.assertEqual(self.stats.search("Semenko").__str__(), "Semenko EDM 4 + 12 = 16")
        
    def test_search_name_false(self):
        self.assertEqual(self.stats.search("Testi Nimi"), None)

    def test_team_true(self):
        self.assertEqual(len(self.stats.team("EDM")), 3)
   
    def test_top_default(self):
        self.assertEqual(self.stats.top(2)[0].__str__(), "Gretzky EDM 35 + 89 = 124")
        self.assertEqual(self.stats.top(2)[1].__str__(), "Lemieux PIT 45 + 54 = 99")

    def test_top_assists(self):
        self.assertEqual(self.stats.top(3, SortBy.ASSISTS)[1].__str__(), "Yzerman DET 42 + 56 = 98")

    def test_top_goals(self):
        self.assertEqual(self.stats.top(1, SortBy.GOALS)[0].__str__(), "Lemieux PIT 45 + 54 = 99")

