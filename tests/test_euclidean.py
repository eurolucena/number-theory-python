import unittest

from src.euclidean import gcd, extended_gcd


class TestEuclideanAlgorithms(unittest.TestCase):

    def test_gcd_basic(self):
        self.assertEqual(gcd(252, 198), 18)
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(17, 13), 1)

    def test_gcd_with_zero(self):
        self.assertEqual(gcd(10, 0), 10)
        self.assertEqual(gcd(0, 10), 10)
        self.assertEqual(gcd(0, 0), 0)

    def test_gcd_negative_inputs(self):
        self.assertEqual(gcd(-252, 198), 18)
        self.assertEqual(gcd(252, -198), 18)
        self.assertEqual(gcd(-252, -198), 18)

    def test_extended_gcd(self):
        test_cases = [
            (252, 198),
            (17, 13),
            (48, 18),
            (-252, 198),
            (252, -198),
        ]

        for a, b in test_cases:
            g, x, y = extended_gcd(a, b)

            self.assertEqual(g, gcd(a, b))
            self.assertEqual(a * x + b * y, g)


if __name__ == "__main__":
    unittest.main()
