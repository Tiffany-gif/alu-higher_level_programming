#!/usr/bin/python3
import unittest
from 1-my_list import MyList  # Import our class

class TestMyList(unittest.TestCase):
    """Tests for the MyList class"""

    def test_sorted_output(self):
        """Check if print_sorted correctly prints a sorted list"""
        my_list = MyList()
        my_list.extend([3, 1, 4, 2, 5])  # Add elements

        expected_output = "[1, 2, 3, 4, 5]\n"

        # Capture print output
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output  # Redirect stdout
        my_list.print_sorted()
        sys.stdout = sys.__stdout__  # Reset stdout

        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()

