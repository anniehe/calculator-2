def add(num_list):
    """Returns the sum of the input integers."""

    result = 0
    for num in num_list:
        result += num
    return result


def subtract(num_list):
    """Takes first number, subtracts second, subtracts next until end of list, returns result."""

    result = num_list[0]
    for num in range(1, len(num_list)):
        result -= num_list[num]
    return result


def multiply(num_list):
    """Multiplies the inputs together."""

    result = 1
    for num in num_list:
        result *= num
    return result


def divide(num_list):
    """Takes first number, divides by second, divides by next until end of list, returns a floating point result."""

    result = float(num_list[0])
    for num in range(1, len(num_list)):
        result /= num_list[num]
    return result


def square(num_list):
    """Returns a list of the squares of the input."""

    result = []
    for num in num_list:
        result.append(num**2)
    return result


def cube(num_list):
    """Returns a list of the cubes of the inputs."""

    result = []
    for num in num_list:
        result.append(num**3)
    return result


def power(num1, num2):
    """Raises the first integer to the power of the second integer and returns the value."""

    return num1 ** num2


def mod(num1, num2):
    """Returns the remainder when the first integer is divided by the second integer."""

    return num1 % num2
