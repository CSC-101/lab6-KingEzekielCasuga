from unittest import expectedFailure

from data import Book
import lab6
import unittest

from lab6 import swap_case, str_translate, histogram


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1

    def test_selection_sort_books_1(self):
        input = [Book(['JK Rowling'], 'Harry Potter'),
                 Book(['Barack Obama'], 'My Life as President'),
                 Book(['Ezekiel Casuga'], 'A Talented Boy')]
        expected = [Book(['Ezekiel Casuga'], 'A Talented Boy'),
                    Book(['JK Rowling'], 'Harry Potter'),
                    Book(['Barack Obama'], 'My Life as President')]
        lab6.selection_sort_books(input)
        self.assertEqual(expected, input)

    def test_selection_sort_books_2(self):
        input = [Book(['JK Rowling'], 'Harry Potter'),
                 Book(['Barack Obama'], 'A Life as President'),
                 Book(['Ezekiel Casuga'], 'A Talented Boy')]
        expected = [Book(['Barack Obama'], 'A Life as President'),
                    Book(['Ezekiel Casuga'], 'A Talented Boy'),
                    Book(['JK Rowling'], 'Harry Potter'),]
        lab6.selection_sort_books(input)
        self.assertEqual(expected, input)

    def test_selection_sort_books_3(self):
        input = []
        expected = []
        lab6.selection_sort_books(input)
        self.assertEqual(expected, input)

    # Part 2

    def test_swap_case_1(self):
        input = 'HamBurger'
        result = swap_case(input)
        expected = 'hAMbURGER'
        self.assertEqual(result,expected)

    def test_swap_case_2(self):
        input = 'A Life NOT Lived'
        result = swap_case(input)
        expected = 'a lIFE not lIVED'
        self.assertEqual(result,expected)

    def test_swap_case_3(self):
        input = 'Ողջույն'
        result = swap_case(input)
        expected = 'ոՂՋՈՒՅՆ'
        self.assertEqual(result,expected)

    # Part 3

    def test_str_translate_1(self):
        input = 'Hamburger!'
        result = str_translate(input, 'r', 'O')
        expected = 'HambuOgeO!'
        self.assertEqual(result, expected)

    def test_str_translate_2(self):
        input = 'this is an assignment for CSC 101'
        result = str_translate(input, ' ', '_')
        expected = 'this_is_an_assignment_for_CSC_101'
        self.assertEqual(result, expected)

    # Part 4

    def test_histogram_1(self):
        input = "today is a beautiful day, isn't it?"
        result = histogram(input)
        expected = {' ': 6,"'": 1,',': 1,'?': 1,'a': 4,'b': 1,'d': 2,'e': 1,'f': 1,'i': 4,'l': 1,'n': 1,'o': 1,'s': 2,'t': 4,'u': 2,'y': 2}
        self.assertEqual(result, expected)

    def test_histogram_2(self):
        input = "my name is ezekiel and i am submitting this assignment"
        result = histogram(input)
        expected = {' ': 9,
 'a': 4,
 'b': 1,
 'd': 1,
 'e': 5,
 'g': 2,
 'h': 1,
 'i': 7,
 'k': 1,
 'l': 1,
 'm': 5,
 'n': 5,
 's': 5,
 't': 4,
 'u': 1,
 'y': 1,
 'z': 1}
        self.assertEqual(result, expected)





if __name__ == '__main__':
    unittest.main()
