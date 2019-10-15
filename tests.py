import unittest
from pocal import Pocal


class TestPowerCalculator(unittest.TestCase):

    def test_days_of_power(self):
        loan0 = Pocal(r1=1000, d1=3, r2=500, d2=10, r3=1500, d3=7, k=21000)
        loan1 = Pocal(r1=3000, d1=3, r2=500, d2=10, r3=1500, d3=7, k=700000)
        loan2 = Pocal(r1=500, d1=3, r2=500, d2=10, r3=500, d3=7, k=21000)
        loan3 = Pocal(r1=1300, d1=0, r2=500, d2=0, r3=1500, d3=7, k=10000)
        loan4 = Pocal(r1=10000, d1=3, r2=500, d2=10, r3=1500, d3=7, k=11000)

        self.assertEqual(loan0.get_days_of_power(), 10)
        self.assertEqual(loan1.get_days_of_power(), 141)
        self.assertEqual(loan2.get_days_of_power(), 17)
        self.assertEqual(loan3.get_days_of_power(), 5)
        self.assertEqual(loan4.get_days_of_power(), 1)


if __name__ == '__main__':
    unittest.main()
