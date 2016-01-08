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
            """ Adding each number from input to a list that will be used to do calculations.
                Try/except is used to make sure inputs can be converted to integers.
                """
            num_list = []
            for num in range(0, len(problem_pieces)-1):
                num_list.append(int(problem_pieces[num+1]))
        except ValueError:
            print "These are not valid inputs."
        else:
            if operator == "+":
                print add(num_list)
            elif operator == "-":
                print subtract(num_list)
            elif operator == "*":
                print multiply(num_list)
            elif operator == "/":
                print divide(num_list)
            elif operator == "square":
                print square(num_list)
            elif operator == "cube":
                print cube(num_list)
            elif operator == "mod":
                print mod(num1, num2)
            elif operator == "q":
                break
            else:
                print "That's not a valid operator."
