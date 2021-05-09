from rstate import RState, RStateException
import unittest

class RStateTest(unittest.TestCase):

    def test_new_rstate_build_000_exception(self):
        with self.assertRaises(RStateException) as context:
            rstate = RState("R1A000")

    def test_next_build_001_to_002(self):
        rstate = RState("R1A001")
        next_rstate = rstate.next_build()
        self.assertEqual(str(next_rstate), "R1A002")

    def test_compare_A_less_then_B(self):
        rstate_a = RState("R1A002")
        rstate_b = RState("R1B001")
        self.assertTrue(rstate_a < rstate_b)

    def c(self):
        rstate_a = RState("R1A002")
        rstate_b = RState("R1B001")
        comparsion = comparsion(rstate_a, rstate_b)
        self.assertTrue(rstate_b > rstate_a)

    def test_compare_A_not_equal_B(self):
        rstate_a = RState("R1A002")
        rstate_b = RState("R1B001")
        self.assertTrue(rstate_a != rstate_b)

    def test_next_letter_N_to_S(self):
        rstate = RState("R1N002")
        next_rstate = rstate.next_letter()
        self.assertEqual(str(next_rstate), "R1S001")

    def comprasion(self):


if __name__ == '__main__':
    unittest.main(verbosity=2)