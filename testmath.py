#Python Example (unittest):
import unittest

def subtract(a, b):
    return a - b

class TestMath(unittest.TestCase):
    def test_subtract_positive_numbers(self):
        # Arrange
        a = 10
        b = 5
        # Act
        result = subtract(a, b)
        # Assert
        self.assertEqual(result, 5)

    def test_subtract_negative_result(self):
        self.assertEqual(subtract(5, 10), -5)

if __name__ == "__main__":
    unittest.main()

