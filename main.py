import math
import time

operators = ['+', '-', '*', '/', '^']


def get_input():
    """Gets the input for math_interpreter() and does input validation"""

    valid = False
    # List of allowed characters
    allowed_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/', '^', ' ']
    inpt = ""
    while not valid:
        inpt = input("Input an expression: \n")

        if inpt is None:
            continue

        # exit condition for program
        if inpt == "quit":
            return inpt

        # input validation
        i_char = 0
        while i_char < len(inpt):
            char = inpt[i_char]
            if (char not in allowed_nums) and (char not in operators):
                # checks for debug mode
                if (inpt[i_char:] == ",debug") and (inpt != ",debug"):
                    return inpt[0:i_char] + "!"

                # checks for physical constants
                if inpt[i_char] == "e":
                    before = inpt[0:i_char]
                    after = inpt[i_char + 1:]
                    inpt = before + str(math.e) + after
                    i_char += 1
                    continue

                # checks for grouping
                if inpt[i_char] == "(":
                    if (")" in inpt[i_char+1:]) and ("(" not in inpt[i_char+1:]):
                        i_char += 1
                        continue
                elif inpt[i_char] == ")":
                    if ("(" in inpt[0:i_char]) and (")" not in inpt[0:i_char]):
                        i_char += 1
                        continue

                # checks for decimal places
                if (inpt[i_char] == '.') and (inpt[i_char - 1] in allowed_nums):
                    i_char += 1
                    continue

                # the input is not valid
                valid = False
                break
            valid = True
            i_char += 1

    return inpt


def loop():
    """A function that prompts the user for repetition of the program"""
    while True:
        inpt = input("Would you like to enter another expression? (y/n)\n")
        if (inpt == 'y') or (inpt == 'n'):
            break
    return inpt


def debug(string):
    """A function that puts the code in debug mode"""

    return 1 if string[-1] == "!" else 0


def add(str_1, str_2):
    """Takes in 2 strings and casts as floats for addition"""

    return float(str_1) + float(str_2)


def subtract(str_1, str_2):
    """Takes in 2 strings and casts as floats for subtraction"""

    return float(str_1) - float(str_2)


def multiply(str_1, str_2):
    """Takes in 2 strings and casts as floats for multiplication"""

    return float(str_1) * float(str_2)


def divide(str_1, str_2):
    """Takes in 2 strings and casts as floats for division"""

    return float(str_1) / float(str_2)


def power(str_1, str_2):
    """Takes in 2 strings and casts as floats for exponentiation"""

    return pow(float(str_1), float(str_2))


def remove_space(inpt):
    """Removes all the spaces in an input string"""

    new_inpt = ""
    for c in inpt:
        if c != " ":
            new_inpt += c
    return new_inpt


def get_numbers(inpt, i_operator):
    """Splits an input string at the operator into
    two numbers stored as strings"""

    num_1 = inpt[0:i_operator]
    num_2 = inpt[i_operator + 1:len(inpt)]
    return num_1, num_2


def match_operator(x, y, curr_operator):
    """Switch-like statement to match a string operator to
    numerical operator and perform the given operation"""

    if curr_operator == "+":
        return add(x, y)
    elif curr_operator == "-":
        return subtract(x, y)
    elif curr_operator == "*":
        return multiply(x, y)
    elif curr_operator == "/":
        return divide(x, y)
    elif curr_operator == "^":
        return power(x, y)


def chain_operate(i_char, i_operators, string, op, debug):
    """Works recursively with operate() to handle
    multi-operator expressions"""

    if i_operators[i_char] == i_operators[0]:
        if debug == 1:
            print("First operator")
        current_string = string[0:i_operators[i_char + 1]]
        after_string = string[i_operators[i_char + 1]:]
        x, y = get_numbers(current_string, i_operators[i_char])
        if debug == 1:
            print("---------------")
        ret = operate(str(match_operator(x, y, op)) +
                      after_string, debug)
        if debug == 1:
            print("Returning: ", ret)
        return ret
    elif i_operators[i_char] == i_operators[-1]:
        if debug == 1:
            print("Last operator")
        before_string = string[0:i_operators[i_char - 1] + 1]
        current_string = string[i_operators[i_char - 1] + 1:]
        x, y = get_numbers(current_string, i_operators[i_char] - len(before_string))
        if debug == 1:
            print("---------------")
        ret = operate(before_string + str(match_operator(x, y, op)),
                      debug)
        if debug == 1:
            print("Returning: ", ret)
        return ret
    else:
        if debug == 1:
            print("Inbetween operator")
        before_string = string[0:i_operators[i_char - 1] + 1]
        current_string = string[i_operators[i_char - 1] + 1:
                                i_operators[i_char + 1]]
        after_string = string[i_operators[i_char + 1]:]
        x, y = get_numbers(current_string, i_operators[i_char] - len(before_string))
        if debug == 1:
            print("---------------")
        ret = operate(before_string + str(match_operator(x, y, op)) +
                      after_string, debug)
        if debug == 1:
            print("Returning: ", ret)
        return ret


def operate(string, debug):
    """A recursive function that handles most of the
    logic for interpreting math expressions"""

    if debug == 1:
        print("Evaluating: " + string)

    contains_op = False
    for char in string:
        if char in operators:
            contains_op = True

    if not contains_op:
        if debug == 1:
            print("Pure Number")
            print("Returning: ", string)
        return float(string)

    if debug == 1:
        print("Looking for operators")
    i_operators = []
    str_ops = []
    for i_char in range(0, len(string)):
        if string[i_char] in operators:
            if (string[i_char] == "-") and ((i_char - 1 in i_operators)
                                            or (i_char == 0)):
                continue
            i_operators.append(i_char)
            str_ops.append(string[i_char])

    if debug == 1:
        print("Operators: ", str_ops)

    # case 1 (only 1 operator)
    if (len(i_operators) == 1) and ("(" not in string):
        curr_operator = string[i_operators[0]]
        if debug == 1:
            print("Only 1 operator")
            print("Current operator: ", curr_operator)
        x, y = get_numbers(string, i_operators[0])
        ret = match_operator(x, y, curr_operator)
        if debug == 1:
            print("Returning: ", ret)
        return ret

    # case 2 (more than 1 operator)
    if debug == 1:
        print("More than 1 operators or has grouping")

    # P
    if debug == 1:
        print("Looking for parenthesis")
    for i_char in range(0, len(string)):
        char = string[i_char]
        if char == "(":
            i_right = string.rindex(")")
            if debug == 1:
                print("Left parenthesis at index ", i_char)
                print("Right parenthesis at index ", i_right)
            before_string = string[0:i_char]
            current_string = string[i_char + 1:i_right]
            after_string = string[i_right + 1:]
            if debug == 1:
                print("---------------")
            expression = operate(current_string, debug)
            if debug == 1:
                print("---------------")
            ret = operate(before_string + str(expression) +
                          after_string, debug)
            if debug == 1:
                print("Returning: ", ret)
            return ret

    # E
    if debug == 1:
        print("Looking for exponents")
    for i_char in range(0, len(i_operators)):
        op = string[i_operators[i_char]]
        if debug == 1:
            skipping = " ->Skipping" if (op != "^") else ""
            print("Current operator: " + op + skipping)
        if op == "^":
            return chain_operate(i_char, i_operators, string, op, debug)

    # MD
    if debug == 1:
        print("Looking for multiplication or division")
    for i_char in range(0, len(i_operators)):
        op = string[i_operators[i_char]]
        if debug == 1:
            skipping = " ->Skipping" if (op == "+" or op == "-") else ""
            print("Current operator: " + op + skipping)
        if (op == "*") or (op == "/"):
            return chain_operate(i_char, i_operators, string, op, debug)

    # AS
    if debug == 1:
        print("Looking for addition or subtraction")
    for i_char in range(0, len(i_operators)):
        op = string[i_operators[i_char]]
        if debug == 1:
            print("Current operator: ", op)
        return chain_operate(i_char, i_operators, string, op, debug)


def parse_expression():
    """Starts the program by getting an input using get_input(),
    handles debug mode, and calls operate to evaluate the expression"""

    curr_inpt = get_input()
    if curr_inpt == "quit":
        print("Goodbye")
        exit(0)
    debug_mode = debug(curr_inpt)
    if debug_mode == 1:
        print("Entering in debug mode")
        time_begin = time.time()
        curr_inpt = curr_inpt[0:len(curr_inpt) - 1]
        print("---------Working---------")
        print("Removing spaces")

    curr_inpt = remove_space(curr_inpt)
    result = operate(curr_inpt, debug_mode)

    if debug_mode == 1:
        print("---------Done---------")
        time_end = time.time()
        print("Elapsed Time: " + str((time_end-time_begin)*1000) + "ms")
    return result


def math_interpreter():
    """A wrapper for parse_expression() that prints a welcome message
    and catches errors caused by early termination of the program"""

    print("Welcome to the Math Interpreter.")
    print("Input an expression below or type quit to exit the program")
    try:
        while True:
            print(parse_expression())
            loops = loop()
            if loops == 'n':
                print("Goodbye")
                break

    except KeyboardInterrupt:
        exit(0)


math_interpreter()
