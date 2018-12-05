from app.simple import Letters
import unittest


class TestSimpleClassLetterMethods(unittest.TestCase):
    def setUp(self):
        self.av = Letters()

    def test_a_returns_string_a(self):
        tv = self.av.A()
        self.assertEqual(tv, "A")

    def test_b_returns_string_b(self):
        tv = self.av.B()
        self.assertEqual(tv, "B")

    def test_c_returns_string_c(self):
        tv = self.av.C()
        self.assertEqual(tv, "C")


if __name__ == "__main__":
    unittest.main()
