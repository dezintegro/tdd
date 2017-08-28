import unittest
from main import Dollar


class TestCurrencyMethods(unittest.TestCase):

    def test_multiply(self):
        five = Dollar(5)
        product = five.times(2)
        self.assertEquals(10, product.amount)
        product = five.times(3)
        self.assertEquals(15, product.amount)

    def test_equality(self):
        self.assertTrue(Dollar(5) == Dollar(5))
        self.assertTrue(Dollar(5) != Dollar(6))

if __name__ == '__main__':
    unittest.main()