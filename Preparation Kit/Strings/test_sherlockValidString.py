#!/usr/bin/python3
# content of test_expectation.py
import unittest
from unittest.mock import patch
import sherlockValidString
import os


def get_input():
    stack = []
    with open('tests/input01.txt') as raw_input:
        for line in raw_input:
            stack.append(line)
    return stack

def get_output():
    stack = []
    with open('tests/output01.txt') as raw_output:
        for line in raw_output:
            new_line=line.rstrip().split(' ')
            input = ""
            for elem in new_line:
                input = input + elem
            stack.append(input)
    print ("Desired Output", stack)
    return stack[0]


class SherlockValidString(unittest.TestCase):
    def test_main(self):
        with patch('builtins.input', side_effect=get_input()):
            stacks = sherlockValidString.main()
        print ("Actual Output", stacks)
        self.assertEqual(stacks, get_output())

if __name__ == '__main__':
    unittest.main()
