from document_revision import DocRevision
import unittest

class DocRevisionTest(unittest.TestCase):

    def test_next_preliminary_1_to_2(self):
        rev = DocRevision("PA1")
        next_rev = rev.next_preliminary()
        self.assertEqual(str(next_rev), "PA2")

    def test_next_preliminary_99_to_100(self):
        rev = DocRevision("PAA99")
        next_rev = rev.next_preliminary()
        self.assertEqual(str(next_rev), "PAA100")

    def test_next_sharp_PA_to_A(self):
        rev = DocRevision("PA2")
        next_rev = rev.next_sharp()
        self.assertEqual(str(next_rev), "A")

    def test_next_sharp_ZZ_to_PAAA1(self):
        rev = DocRevision("ZZ")
        next_rev = rev.next_sharp()
        self.assertEqual(str(next_rev), "PAAA1")

    def test_compare_B_greater_then_A(self):
        rev_a = DocRevision("PB3")
        rev_b = DocRevision("B")
        self.assertTrue(rev_b > rev_a)

    def test_compare_A_less_then_B(self):
        rev_a = DocRevision("C")
        rev_b = DocRevision("PD124")
        self.assertTrue(rev_a < rev_b)

    def test_compare_A_not_equal_B(self):
        rev_a = DocRevision("PH1")
        rev_b = DocRevision("PH2")
        self.assertTrue(rev_a != rev_b)

if __name__ == '__main__':
    unittest.main(verbosity=2)