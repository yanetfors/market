import unittest
from main import calculate_market_auction


class Test_Calculate_Values(unittest.TestCase):
    def test_calculate_values(self):
        result = {
            'market_value': 216384.71025600002,
            'auction_value': 126089.52642
        }
        self.assertEqual(calculate_market_auction(67352, 2007), result)

    def test_id_not_exist(self):
        self.assertEqual(calculate_market_auction(87964, 2011), {})


if __name__ == '__main__':
    unittest.main()
