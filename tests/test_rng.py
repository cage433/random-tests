import unittest

from random_tests.random_number_generator import RandomNumberGenerator


class RNGTests(unittest.TestCase):
    def test_reproducibility(self):
        terms = list(range(100))
        rng = RandomNumberGenerator(seed=1234)
        rng2 = RandomNumberGenerator(seed=1234)

        self.assertEqual(
            rng.shuffle(terms),
            rng2.shuffle(terms),
        )

        self.assertNotEqual(
            rng.shuffle(terms),
            rng.shuffle(terms),
        )


