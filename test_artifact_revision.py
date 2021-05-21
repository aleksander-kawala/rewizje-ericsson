from artifact_revision import ArtifactRevision
import unittest

class ArtifactRevisionTest(unittest.TestCase):

    def test_next_subrevision_0_to_1(self):
        rev = ArtifactRevision("A")
        next_rev = rev.next_subrevision()
        self.assertEqual(str(next_rev), "A1")

    def test_next_subrevision_9_to_10(self):
        rev = ArtifactRevision("A9")
        next_rev = rev.next_subrevision()
        self.assertEqual(str(next_rev), "A10")

    def test_next_sharp_A_to_B(self):
        rev = ArtifactRevision("A2")
        next_rev = rev.next_sharp()
        self.assertEqual(str(next_rev), "B")

    def test_next_sharp_Z_to_AA(self):
        rev = ArtifactRevision("Z66")
        next_rev = rev.next_sharp()
        self.assertEqual(str(next_rev), "AA")

    def test_compare_B_greater_then_A(self):
        rev_a = ArtifactRevision("AZ1")
        rev_b = ArtifactRevision("ABC123")
        self.assertTrue(rev_b > rev_a)

    def test_compare_A_less_then_B(self):
        rev_a = ArtifactRevision("A63")
        rev_b = ArtifactRevision("A124")
        self.assertTrue(rev_a < rev_b)

    def test_compare_A_not_equal_B(self):
        rev_a = ArtifactRevision("ZB102")
        rev_b = ArtifactRevision("ZB201")
        self.assertTrue(rev_a != rev_b)

if __name__ == '__main__':
    unittest.main(verbosity=2)