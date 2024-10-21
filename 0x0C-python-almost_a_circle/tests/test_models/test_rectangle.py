import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    # Test initialization
    def test_initialization(self):
        rect = Rectangle(10, 20, 5, 5)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 5)

    # Test type and value errors on width
    def test_width_validation(self):
        with self.assertRaises(TypeError):
            Rectangle("10", 20)
        with self.assertRaises(ValueError):
            Rectangle(-10, 20)

    # Test type and value errors on height
    def test_height_validation(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "20")
        with self.assertRaises(ValueError):
            Rectangle(10, -20)

    # Test type and value errors on x
    def test_x_validation(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 20, "5")
        with self.assertRaises(ValueError):
            Rectangle(10, 20, -1)

    # Test type and value errors on y
    def test_y_validation(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 20, 5, "5")
        with self.assertRaises(ValueError):
            Rectangle(10, 20, 5, -1)

    # Test area calculation
    def test_area(self):
        rect = Rectangle(10, 2)
        self.assertEqual(rect.area(), 20)

    # Test the display method by capturing stdout
    def test_display(self):
        import io
        import sys
        rect = Rectangle(2, 3, 2, 2)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        rect.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    # Test the __str__ method
    def test_str(self):
        rect = Rectangle(4, 6, 2, 2, 1)
        self.assertEqual(str(rect), "[Rectangle] (1) 2/2 - 4/6")

    # Test the update method
    def test_update(self):
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(1, 2, 3, 4, 5)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 5)
        rect.update(height=7, y=8)
        self.assertEqual(rect.height, 7)
        self.assertEqual(rect.y, 8)

    # Test dictionary representation
    def test_to_dictionary(self):
        rect = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(rect.to_dictionary(), {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9})
