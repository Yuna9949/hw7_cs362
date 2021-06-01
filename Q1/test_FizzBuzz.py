import unittest
import FizzBuzz

class TestFizzBuzz(unittest.TestCase):
    def test_FizzBuzz_3(self):
        self.assertEqual(FizzBuzz.FizzBuzz(3),'Fizz')

    def test_FizzBuzz_5(self):
        self.assertEqual(FizzBuzz.FizzBuzz(5),'Buzz')

    def test_FizzBuzz_15(self):
        self.assertEqual(FizzBuzz.FizzBuzz(15),'FizzBuzz')

    def test_FizzBuzz_else(self):
        self.assertEqual(FizzBuzz.FizzBuzz(2), 2)

if __name__ == '__main__':
    unittest.main()