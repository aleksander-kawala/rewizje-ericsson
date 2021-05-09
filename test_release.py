from release import Release
import unittest

class ReleaseTest(unittest.TestCase):

    def test_next_quarter_1_to_2(self):
        rev = Release("G19Q1")
        next_rev = rev.next_quarter()
        self.assertEqual(str(next_rev), "G19Q2")

    def test_next_year_19_to_20(self):
        rev = Release("G19Q4")
        next_rev = rev.next_quarter()
        self.assertEqual(str(next_rev), "G20Q1")

    def test_next_version_0_to_1(self):
        rev = Release("G20Q2")
        next_rev = rev.next_version()
        self.assertEqual(str(next_rev), "G20Q2.1")

    def test_next_version_9_to_10(self):
        rev = Release("G21Q3.9")
        next_rev = rev.next_version()
        self.assertEqual(str(next_rev), "G21Q3.10")

    def test_compare_B_greater_then_A(self):
        rev_a = Release("G21Q2.3")
        rev_b = Release("G21Q2.23")
        rev_a = rev_a.grater()
        rev_b = rev_b.grater()
        self.assertTrue(rev_b > rev_a)

    def test_compare_A_less_then_B(self):
        rev_a = Release("G20Q3.2")
        rev_b = Release("G20Q4")
        rev_a = rev_a.grater()
        rev_b = rev_b.grater()
        self.assertTrue(rev_a < rev_b)

    def test_compare_A_not_equal_B(self):
        rev_a = Release("G19Q4.12")
        rev_b = Release("G19Q4.1")
        rev_a = rev_a.grater()
        rev_b = rev_b.grater()
        self.assertTrue(rev_a != rev_b)

if __name__ == '__main__':
    unittest.main(verbosity=2)