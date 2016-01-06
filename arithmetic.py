def validate_num(num1):
    """Checks if the input was in integer form."""

    if isinstance(num1, int):
        return True
    else:
        print "Cannot compute! Your input was not in integer form."


def validate_nums(num1, num2):
    """Checks if the inputs were in integer form."""

    if isinstance(num1, int) and isinstance(num2, int):
        return True
    else:
        print "Cannot compute! Your input was not in integer form."


def add(num1, num2):
    """Returns the sum of the two input integers."""
    
    if validate_nums(num1, num2):
        return num1 + num2
    else:
        return 0


def subtract(num1, num2):
    """Returns the second number subtracted from the first."""

    if validate_nums(num1, num2):
        return num1 - num2
    else:
        return 0


def multiply(num1, num2):
    """Multiplies the two inputs together."""

    if validate_nums(num1, num2):
        return num1 * num2
    else:
        return 0


def divide(num1, num2):
    """Divides the first input by the second, returning a floating point."""

    if validate_nums(num1, num2):
        return float(num1) / num2
    else:
        return 0.0


def square(num1):
    """Returns the square of the input."""

    if validate_num(num1):
        return num1 ** 2
    else:
        return 0


def cube(num1):
    """Returns the cube of the input."""

    if validate_num(num1):
        return num1 ** 3
    else:
        return 0


def power(num1, num2):
    """Raises the first integer to the power of the second integer and returns the value."""
    
    if validate_nums(num1, num2):
        return num1 ** num2
    else:
        return 0


def mod(num1, num2):
    """Returns the remainder when the first integer is divided by the second integer."""

    if validate_nums(num1, num2):
        return num1 % num2
    else: 
        return 0


