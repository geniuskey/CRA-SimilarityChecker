from unittest import TestCase

from game import Game


class TestGame(TestCase):
    def setUp(self):
        super().setUp()
        self.game = Game()

    def test_run(self):
        self.fail()

    def test_check_alpha(self):
        test_cases = [
            ("ASD", "DSA", 40),
            ("A", "BB", 0),
            ("AAABB", "BAA", 40),
            ("AA", "AAE", 20),
        ]
        for a, b, ans in test_cases:
            with self.subTest(f"{a}, {b}, {ans}"):
                ret = self.game.check_alpha(a, b)
                self.assertEqual(ret, ans)
