#!/usr/bin/python3
# content of test_expectation.py
import unittest
from unittest.mock import patch
import iceCreamParlor_HashMap
import os


def get_input():
    stack = []
    with open('tests/input00.txt') as raw_input:
        for line in raw_input:
            #input = line.split('\n')
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


class IceCreamParlor_HashMap(unittest.TestCase):
    def test_main(self):
        # try:
        # saved_stdout = saved_stdout
        with patch('builtins.input', side_effect=get_input()):
            stacks = iceCreamParlor_HashMap.main()
        print ("Actual Output", stacks)
        self.assertEqual(stacks, get_ouput())

        # finally:
        #      sys.stdout = saved_stdout

if __name__ == '__main__':
    unittest.main()
