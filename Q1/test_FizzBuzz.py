import unittest
import FizzBuzz

class TestFizzBuzz(unittest.TestCase):
    def test_FizzBuzz_3(self):
        self.assertEqual(FizzBuzz.FizzBuzz(3),'Fizz')

if __name__ == '__main__':
    unittest.main()