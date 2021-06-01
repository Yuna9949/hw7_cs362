import unittest
import LeapYear
class TestLeapYear(unittest.TestCase):
    def test_LeapYear_4(self):
        self.assertEqual(LeapYear.LeapYear(2012), True)

    def test_LeapYear_100(self):
        self.assertEqual(LeapYear.LeapYear(2100), False)

if __name__=='__main__':
    unittest.main