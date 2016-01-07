"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
print "Welcome to the prefix calculator!"
problem_pieces = [""]

while problem_pieces[0] != "q":
    problem = raw_input("> ")
    problem_pieces = problem.split(" ")

    operator = problem_pieces[0]
    try:
        if len(problem_pieces) > 1:
            num1 = int(problem_pieces[1])
        if len(problem_pieces) > 2:
            num2 = int(problem_pieces[2])
    except ValueError:
        print "These are not valid inputs."
    else:
        if operator == "+":
            print add(num1, num2)
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
        elif operator == "pow":
            print power(num1, num2)
        elif operator == "mod":
            print mod(num1, num2)
        else:
            print "That's not a valid operator."
