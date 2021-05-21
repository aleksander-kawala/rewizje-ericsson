from rstate import RState, RStateException
import unittest

class RStateTest(unittest.TestCase):

        def test_next_build_001_to_002(self):
            rstate = RState("R1A001")
            next_rstate = rstate.next_build()
            self.assertEqual(str(next_rstate), "R1A002")

        def test_next_build_099_to_100(self):
            rstate = RState("R1A099")
            next_rstate = rstate.next_build()
            self.assertEqual(str(next_rstate), "R1A100")

        def test_next_letter_N_to_S(self):
            rstate = RState("R1N002")
            next_rstate = rstate.next_letter()
            self.assertEqual(str(next_rstate), "R1S001")

        def test_next_letter_Z_to_AA(self):
            rstate = RState("R1Z002")
            next_rstate = rstate.next_letter()
            self.assertEqual(str(next_rstate), "R1AA001")

        def test_next_number_1_to_2(self):
            rstate = RState("R1A002")
            next_rstate = rstate.next_number()
            self.assertEqual(str(next_rstate), "R2A001")

        def test_next_number_9_to_10(self):
            rstate = RState("R9ZAV538")
            next_rstate = rstate.next_number()
            self.assertEqual(str(next_rstate), "R10A001")

        def test_compare_A_less_then_B(self):
            rstate_a = RState("R1A002")
            rstate_b = RState("R1B001")
            self.assertTrue(rstate_a < rstate_b)

        def test_compare_A_not_equal_B(self):
            rstate_a = RState("R1A002")
            rstate_b = RState("R1B001")
            self.assertTrue(rstate_a != rstate_b)

        def test_compare_B_greater_then_A(self):
            rstate_a = RState("R1A002")
            rstate_b = RState("R1B001")
            self.assertTrue(rstate_b > rstate_a)

if __name__ == '__main__':
    unittest.main(verbosity=2)