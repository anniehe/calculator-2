"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from multi_arithmetic import *


# Your code goes here
print "Welcome to the prefix calculator!"

while True:
    problem = raw_input("> ")
    problem_pieces = problem.split(" ")
    operator = problem_pieces[0]
    
    if operator == "pow":
        try:
            if len(problem_pieces) > 1:
                num1 = float(problem_pieces[1])
            if len(problem_pieces) > 2:
                num2 = float(problem_pieces[2])
        except ValueError:
            print "These are not valid inputs."
        print power(num1, num2)
    else:
        try:
            num_list = []
            for num in range(0, len(problem_pieces)-2):
                num_list[num] = int(problem_pieces[num+1])
        except ValueError:
            print "These are not valid inputs."
        else:
            if operator == "+":
                print add(num_list)
            elif operator == "-":
                print subtract(num1, num2)
            elif operator == "*":
                print multiply(num1, num2)
            elif operator == "/":
                print divide(num1, num2)
            elif operator == "square":
                print square(num1)
            elif operator == "cube":
                print cube(num1)
            elif operator == "mod":
                print mod(num1, num2)
            elif operator == "q":
                break
            else:
                print "That's not a valid operator."
