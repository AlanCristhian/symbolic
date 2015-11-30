import unittest

import symbolic


class SystemSuite(unittest.TestCase):
    def test_instance(self):
        obtained = symbolic.solve([
            middle == (left + right) / 2,
            right == left + 10,
            right <= 100,
            left >= 0,
            ] for left, middle, right in symbolic.Variables)
        self.assertEqual(obtained[0].value, 90.0)
        self.assertEqual(obtained[1].value, 95.0)
        self.assertEqual(obtained[2].value, 100.0)


if __name__ == '__main__':
    unittest.main()
