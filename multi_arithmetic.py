def add(num_list):
    """Returns the sum of the input integers."""

    total = 0
    for num in num_list:
        total += num
    return total


def subtract(num_list):
    """Returns the second number subtracted from the first."""

    result = num_list[0]
    for num in range(1, len(num_list)):
        result -= num_list[num]
    return result


def multiply(num1, num2):
    """Multiplies the two inputs together."""

    return num1 * num2


def divide(num1, num2):
    """Divides the first input by the second, returning a floating point."""

    return float(num1) / num2


def square(num1):
    """Returns the square of the input."""

    return num1 ** 2


def cube(num1):
    """Returns the cube of the input."""

    return num1 ** 3


def power(num1, num2):
    """Raises the first integer to the power of the second integer and returns the value."""

    return num1 ** num2


def mod(num1, num2):
    """Returns the remainder when the first integer is divided by the second integer."""

    return num1 % num2
