import unittest
from unittest import TestCase
from Quadf import Quadratic_function as Quadf


class Test_quad_function(unittest.TestCase):
    def test_delta_negative(self):
        self.assertEqual(None, Quadf.delta(5.0, 10.0, 15.0))

    def test_delta_value_negative(self):
        self.assertEqual(None, Quadf.delta(5.0, -10.0, 15.0))
        self.assertEqual(160, Quadf.delta(-1.0, -10.0, 15.0))

    def test_delta_positive(self):
        self.assertEqual(4, Quadf.delta(1, 6, 8))

    def test_delta_zero(self):
        self.assertEqual(0, Quadf.delta(2, 4, 2))
        self.assertEqual(0, Quadf.delta(2, -4, 2))

    def test_delta_string(self):
        self.assertEqual(None, Quadf.delta(2, 2, "fas"))
        self.assertEqual(None, Quadf.delta(2, "fas", 2))
        self.assertEqual(None, Quadf.delta("fas", 4, 2))

    def test_delta_None(self):
        self.assertEqual(None, Quadf.delta(2, 4, None))
        self.assertEqual(None, Quadf.delta(2, None, 2))
        self.assertEqual(None, Quadf.delta(None, 4, 2))


    def test_zero_place_correct_data(self):
        self.assertEqual((-4, -2), Quadf.zero_place(1, 6, 8))
        self.assertEqual((2, 4), Quadf.zero_place(1, -6, 8))

    def test_zero_place_delta_zero(self):
        self.assertEqual(1, Quadf.zero_place(2, -4, 2))
        self.assertEqual(-1, Quadf.zero_place(2, 4, 2))

    def test_zero_place_is_None(self):
        '''
        delta is None:
            delta <0
            a,b,c = string
            a,b,c = None
        '''
        self.assertEqual(None, Quadf.zero_place(5.0, -10.0, 15.0))
        self.assertEqual(None, Quadf.zero_place(5.0, None, 15.0))
        self.assertEqual(None, Quadf.zero_place("aad", 4, 1.0))

    def test_zero_place_is_zero(self):
        self.assertEqual(None, Quadf.zero_place(0, -4, 2))


if __name__ == '__main__':
    unittest.main()



