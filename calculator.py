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
        if problem_pieces[1]:
            num1 = int(problem_pieces[1])
        if problem_pieces[2]:
            num2 = int(problem_pieces[2])
    except ValueError:
        print "These are not valid inputs."
    else:
        if operator == "+":
            print add(num1, num2)
        # elif operator == "-":

        # elif operator == "*":

        # elif operator == "/":

        # elif operator == "square":

        # elif operator == "cube":

        # elif operator == "pow":

        # elif operator == "mod":
