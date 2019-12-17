#!/usr/bin/python3
# content of test_expectation.py
import unittest
from unittest.mock import patch
import hashTables
#import sys
#import io
#import subprocess
#import os


class TesthashTables(unittest.TestCase):
    def test_main(self):
        #saved_stdout = sys.stdout
        #try:
            #path = os.path.dirname(os.path.abspath(__file__))
            #input_file = os.path.join(path, 'tests/input15.txt')
            #out_file = os.path.join(path, 'tests/output15.txt')
            #print(input_file)
            #input = open('/home/andres/Programs/python/tests/input15.txt', 'rb', buffering=0)
            #expected = open("/home/andres/Programs/python/tests/output15.txt", "r", encoding="utf-8")


        user_input = [
            '1',
            '4',
            '5',
            '1 4 5 3 2'
        ]

        expected_stacks = [
            (1, 4)
        ]

        #hashTables.main()
            # with open("/home/andres/Programs/python/tests/output15.txt") as f:
            #     for line in f:
            #     #sys.stdout = out
            #         print("current line:", line)
            #         sys.stdin = line
            #
        with patch('builtins.input', side_effect=user_input):
            stacks = hashTables.main()
        self.assertEqual(stacks, expected_stacks)

        #     output = sys.stdout.getvalue()
        #     self.assertEqual(output, expected)
        #     input.close
        #     output.close
        #
        # finally:
        #      sys.stdout = saved_stdout

if __name__ == '__main__':
    unittest.main()
