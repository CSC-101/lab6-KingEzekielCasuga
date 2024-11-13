import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp

# Part 1

# replicates the index smallest from function, but with the input as
# a list of books instead

def index_smallest_char_from(values:list[data.Book], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None
    mindex = start
    for idx in range(start + 1, len(values)):
        n = 0
        while values[idx].title[n] == values[mindex].title[n]:
            n = n + 1
        if values[idx].title[n] < values[mindex].title[n]:
            mindex = idx
    return mindex

# uses the selection sorting algorithm on an input list of books

def selection_sort_books(books:list[data.Book]) -> None:
    for idx in range(len(books) - 1):
        mindex = index_smallest_char_from(books, idx)
        tmp = books[mindex]
        books[mindex] = books[idx]
        books[idx] = tmp

# Part 2

def swap_case(string:str) -> str:
    swapped = []
    for char in string:
        if (char.isupper()) or (not char.isalpha()):
            swapped.append(char.lower())
        if char.islower():
            swapped.append(char.upper())
    return ''.join(swapped)

# Part 3

def str_translate(string:str, char:str, char_new:str) -> str:
    string_new = []
    for i in range(len(string)):
        if string[i] != char:
            string_new.append(string[i])
        else:
            string_new.append(char_new)
    return ''.join(string_new)

# Part 4

def histogram(paragraph:str) -> dict:
    histogram = {}
    paragraph.split(' ')
    for letter in paragraph:
        if letter in histogram:
            histogram[letter] += 1
        else:
            histogram[letter] = 1
    return histogram