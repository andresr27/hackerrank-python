#!/usr/bin/python3
# content of test_expectation.py
import unittest
from unittest.mock import patch
import iceCreamParlor_binarySearch
import os


def get_input():
    stack = []
    with open('tests/input00.txt') as raw_input:
        for line in raw_input:
            stack.append(line)
    return stack

def get_ouput():
    stack = []
    with open('tests/output00.txt') as raw_output:
        for line in raw_output:
            new_line=line.rstrip().split(' ')
            input = ()
            for elem in new_line:
                input = input + (int(elem),)
            stack.append(input)
    print ("Desired Output", stack)
    return stack


class IceCreamParlor_binarySearch(unittest.TestCase):
    def test_main(self):
        with patch('builtins.input', side_effect=get_input()):
            stacks = iceCreamParlor_binarySearch.main()
        print ("Actual Output", stacks)
        self.assertEqual(stacks, get_ouput())

if __name__ == '__main__':
    unittest.main()
