#!/usr/bin/python3
# content of test_expectation.py
import unittest
from unittest.mock import patch
import maxArraySum_dynamic
import os


def get_input(i):
    stack = []
    name = 'input/input' + str(i)+'.txt'
    if os.path.exists(name) == False:
        return None
    with open(name) as raw_input:
        for line in raw_input:
            stack.append(line)
    return stack

def get_output(i):
    stack = []
    name = 'output/output' + str(i)+'.txt'
    #print ("Testing output", name)
    with open(name) as raw_output:
        for line in raw_output:
            new_line=line.rstrip().split(' ')
            input = ""
            for elem in new_line:
                input = input + elem
            stack.append(int(input))
    print ("Desired Output", input)
    return stack[0]


class MaxArraySum_dynamic(unittest.TestCase):
    def test_main(self):
        finish = False
        tests_numbers = [30,31,32,33,4,10]
        #print ("Testing input number: ", str(i))
        for i in tests_numbers:
            print ("Testing input ", str(i) )
            if get_input(i) is not None :
                with patch('builtins.input', side_effect=get_input(i)):
                    output = maxArraySum_dynamic.main()
                #print ("Actual Output", output)
                self.assertEqual(output, get_output(i))
            else: finish = True

if __name__ == '__main__':
    unittest.main()
