from main8_2 import *
from unittest import TestCase, main


class FunctionTest(TestCase):
    def test_isDivision(self):
        self.assertEqual(division(18, 3), 6)

    def test_isDigitNominator(self):
        self.assertEqual(division('18', 3), TypeError)

main()
