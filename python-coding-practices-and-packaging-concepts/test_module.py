import unittest
from mymodule import square, double, add, increment

class TestSquare(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(2), 4)
        self.assertEqual(square(3), 9)
    
class TestDouble(unittest.TestCase):
    def test_double(self):
        self.assertEqual(double(2), 4)
        self.assertEqual(double(3), 6)

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 2), 4)
        self.assertEqual(add(3, 3), 6)

class TestIncrement(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(increment(2), 3)
        self.assertEqual(increment(3), 4)

unittest.main()