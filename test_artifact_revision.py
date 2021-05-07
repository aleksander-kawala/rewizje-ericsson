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

    def test_next_letter_Z_to_AA(self):
        rev = ArtifactRevision("Z66")
        next_rev = rev.next_sharp()
        self.assertEqual(str(next_rev), "AA")

if __name__ == '__main__':
    unittest.main(verbosity=2)