import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_initialization(self):
        square = Square(5, 3, 4, 1)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)
        self.assertEqual(square.id, 1)

    def test_size_property(self):
        square = Square(10)
        self.assertEqual(square.size, 10)

    def test_size_setter(self):
        square = Square(10)
        square.size = 20
        self.assertEqual(square.size, 20)
        self.assertEqual(square.width, 20)
        self.assertEqual(square.height, 20)

    def test_update_with_args(self):
        square = Square(10, 10, 10, 10)
        square.update(1, 15, 20, 25)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 15)
        self.assertEqual(square.x, 20)
        self.assertEqual(square.y, 25)

    def test_update_with_kwargs(self):
        square = Square(10, 10, 10, 10)
        square.update(size=30, x=40, y=50)
        self.assertEqual(square.size, 30)
        self.assertEqual(square.x, 40)
        self.assertEqual(square.y, 50)

    def test_str(self):
        square = Square(5, 1, 2, 3)
        self.assertEqual(str(square), "[Square] (3) 1/2 - 5")

    def test_to_dictionary(self):
        square = Square(5, 1, 2, 3)
        expected_dict = {
            "id": 3,
            "size": 5,
            "x": 1,
            "y": 2
        }
        self.assertEqual(square.to_dictionary(), expected_dict)
