import unittest

class TestFactorial:

    def test_factorial(self):
        res = factorial(5)
        self.assertEqual(res,121)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


if __name__ == "__main__":
    unittest.main()