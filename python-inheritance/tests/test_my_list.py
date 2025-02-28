import unittest
from 1-my_list import MyList

class TestMyList(unittest.TestCase):
    def test_print_sorted(self):
        my_list = MyList([3, 1, 2])
        # Capture the printed output
        with self.assertLogs() as captured:
            my_list.print_sorted()
        self.assertEqual(captured.output, ['[1, 2, 3]'])

if __name__ == "__main__":
    unittest.main()

