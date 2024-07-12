# Math Interpreter README

## Overview
The Math Interpreter is a Python program that takes a mathematical expression as input from the user, validates it, and evaluates the expression. The program supports basic arithmetic operations, exponentiation, and handles parentheses. It also includes a debug mode to help trace the execution flow and identify potential issues in the input expression.

## Features
- Supports addition, subtraction, multiplication, division, and exponentiation.
- Handles parentheses for grouping operations.
- Includes a debug mode for detailed tracing.
- Accepts physical constants like 'e'.
- Provides input validation to ensure correct syntax.
- Allows for continuous operation until the user decides to quit.

## Requirements
- Python 3.x

## How to Use

### Running the Program
To start the Math Interpreter, run the script using a Python interpreter. The program will prompt you to enter a mathematical expression.

### Input Format
- The program accepts standard mathematical expressions using the operators `+`, `-`, `*`, `/`, `^`.
- You can use parentheses `(` and `)` for grouping.
- The constant `e` can be used to represent the mathematical constant Euler's number.
- Enter `quit` to exit the program.

### Debug Mode
To activate debug mode, append `,debug` to your expression. This will provide detailed information about the evaluation process.

### Example Inputs
- `3 + 5`
- `2 * (3 + 4)`
- `5^2`
- `2 * e`
- `3 + 5,debug`

## Functions

### Main Functions
- **math_interpreter()**: The main function that runs the program, prints welcome message, and handles continuous input.
- **parse_expression()**: Handles input fetching, debug mode activation, and calls the main evaluation function.
- **operate(string, debug)**: Recursively evaluates the mathematical expression and handles different operators.

### Helper Functions
- **get_input()**: Gets and validates user input.
- **loop()**: Prompts the user to enter another expression or exit.
- **debug(string)**: Determines if the input is in debug mode.
- **add(str_1, str_2)**: Adds two numbers.
- **subtract(str_1, str_2)**: Subtracts the second number from the first.
- **multiply(str_1, str_2)**: Multiplies two numbers.
- **divide(str_1, str_2)**: Divides the first number by the second.
- **power(str_1, str_2)**: Raises the first number to the power of the second.
- **remove_space(inpt)**: Removes spaces from the input string.
- **get_numbers(inpt, i_operator)**: Splits the input string into two numbers at the operator.
- **match_operator(x, y, curr_operator)**: Matches the operator to the corresponding function.
- **chain_operate(i_char, i_operators, string, op, debug)**: Handles expressions with multiple operators.

## Example Usage

```bash
$ python math_interpreter.py
```
```
Welcome to the Math Interpreter.
Input an expression below or type quit to exit the program
Input an expression: 
2 + 2
4.0
Would you like to enter another expression? (y/n)
n
Goodbye
```
In debug mode:
```bash
$ python math_interpreter.py
```
```
Welcome to the Math Interpreter.
Input an expression below or type quit to exit the program
Input an expression: 
2 + 3 * 4,debug
Entering in debug mode
---------Working---------
Removing spaces
Evaluating: 2+3*4
Looking for operators
Operators:  ['+', '*']
More than 1 operators or has grouping
Looking for parenthesis
Looking for exponents
Current operator: + ->Skipping
Current operator: * ->Skipping
Looking for multiplication or division
Current operator: + ->Skipping
Current operator: *
Last operator
---------------
Evaluating: 2+12.0
Looking for operators
Operators:  ['+']
Only 1 operator
Current operator:  +
Returning:  14.0
Returning:  14.0
---------Done---------
Elapsed Time: 3.3740997314453125ms
14.0
Would you like to enter another expression? (y/n)
n
Goodbye
```
