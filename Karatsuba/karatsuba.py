"""Multiplication of two integers using Karatsuba algorithm"""

from math import ceil
import unittest

def multiply(a, b):
    if a < 10 or b < 10:
        return a * b
    a_str = str(a)
    b_str = str(b)
    a_len = len(a_str)
    b_len = len(b_str)
    m = ceil(max(len(a_str), len(b_str)) / 2)
    low_a = a_str[-m:]
    if not low_a:
        low_a = '0'
    high_a = a_str[:a_len-m]
    if not high_a:
        high_a = '0'
    low_b = b_str[-m:]
    if not low_b:
        low_b = '0'
    high_b = b_str[:b_len-m]
    if not high_b:
        high_b = '0'
    z0 = multiply(int(low_a), int(low_b))
    z1 = multiply(int(low_a) + int(high_a), int(low_b) + int(high_b))
    z2 = multiply(int(high_a), int(high_b))
    return z2 * 10**(m*2) + (z1 - z2 - z0) * 10**m + z0
    

class TestMultiplicationOfTwoNumbers(unittest.TestCase):
    def test_products_of_two_numbers(self):
        self.assertEqual(multiply(0, 10), 0)
        self.assertEqual(multiply(2, 1), 2)
        self.assertEqual(multiply(23, 200), 4600)
        self.assertEqual(multiply(12345, 6789), 83810205)
        self.assertEqual(multiply(-12345, -6789), 83810205)
        self.assertEqual(multiply(12345, -6789), -83810205)
        self.assertEqual(multiply(3141592653589793238462643383279502884197169399375105820974944592,
                                  2718281828459045235360287471352662497757247093699959574966967627),
                                  8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184)
        self.assertEqual(multiply(88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888,
                                  99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999),
                                  8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888711111111111111111111111111111111111111111111111111111111111111111111111111111111111111112)


if __name__ == '__main__':
    print(multiply(0, 10))
    print(multiply(2, 1))
    print(multiply(23, 200))
    print(multiply(12345, 6789))
    print(multiply(-12345, -6789))
    print(multiply(12345, -6789))
    print(multiply(3141592653589793238462643383279502884197169399375105820974944592,
                   2718281828459045235360287471352662497757247093699959574966967627))
    print(multiply(88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888,
                   99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999))
    print(multiply(88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888,
                   78779078363576474357645493898985134563527843309600099650780112330405507708994574587853675446576895789454534655676765593123234235453453459999991112346998766642354356554764099111135678657809814126787559789774339911298884659000988896783253278504488888992547745798058678673256786877979749))
    unittest.main()