import unittest
import LeapYear
class TestLeapYear(unittest.TestCase):
    def test_LeapYear_4(self):
        self.assertEqual(LeapYear.LeapYear(2012), True)

if __name__=='__main__':
    unittest.main