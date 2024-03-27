import unittest
from unittest.mock import patch
from luhn_verify_credit_card import *

class TestLuhnsFunctions(unittest.TestCase):

    @patch('builtins.input', side_effect=['1234-5678-9012-3456'])
    def test_get_credit_number_valid(self, mock_input):
        self.assertEqual(get_credit_number(), '1234567890123456')

    def test_verify_card_number_valid(self):
        self.assertTrue(verify_card_number('79927398713'))

    def test_verify_card_number_invalid(self):
        self.assertFalse(verify_card_number('79927398710'))

if __name__ == '__main__':
    unittest.main()

