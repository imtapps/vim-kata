import unittest


def calculate_number(numeral):
    return None


class MyTests(unittest.TestCase):

    def test_roman_numeral_i_produces_1(self):
        roman_numeral = calculate_number('i')
        self.assertEqual(1, roman_numeral)


if __name__ == '__main__':
    unittest.main()
