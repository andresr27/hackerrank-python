#!/usr/bin/python3
# content of test_expectation.py
import unittest
from unittest.mock import patch
import code


def get_input():
    stack = []
    with open('tests/input00.txt') as raw_input:
        for line in raw_input:
            stack.append(line)
    print("Input Stack", stack)
    return stack

def get_output():
    stack = []
    with open('tests/output00.txt') as raw_output:
        for line in raw_output:
            new_line=line.rstrip()
            input_std = ""
            for elem in new_line:
                input_std = input_std + elem
            stack.append(input_std)
    print ("Expect Output", stack)
    return stack


class UnitTestClass(unittest.TestCase):
    def test_main(self):
        with patch('builtins.input', side_effect=get_input()):
            stacks = code.main()
        print ("Actual Output", stacks)
        self.assertEqual(get_output(), stacks)

if __name__ == '__main__':
    unittest.main()