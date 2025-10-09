"""
equation_generator.py

This module generates random math equations for the Nerdle game.
It creates valid equations in the format: number operator number = result
For example: 12+34=46 or 8*7=56
"""
import random

def generate_numbers_for_addition():
    """
    Generate two numbers that when added create an 8-character equation.
    Returns a tuple of (num1, num2, result)
    Format: NN+NN=NN
    Example: (12, 34, 46) creates "12+34=46"
    """
    while True:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        result = num1 + num2
        equation = f"{num1}+{num2}={result}"
        if len(equation) == 8 and result <= 99:
            return (num1, num2, result)

def generate_numbers_for_subtraction():
    """
    Generate two numbers that when subtracted create an 8-character equation.
    Returns a tuple of (num1, num2, result)
    Format: NN-NN=NN
    Example: (56, 23, 33) creates "56-23=33"
    """
    while True:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        if num1 >= num2:
            result = num1 - num2
            equation = f"{num1}-{num2}={result}"
            if len(equation) == 8 and result >= 10:
                return (num1, num2, result)

def generate_numbers_for_multiplication():
    """
    Generate two numbers that when multiplied create an 8-character equation.
    Returns a tuple of (num1, num2, result)
    Format: N*NN=NNN
    Example: (3, 34, 102) creates "3*34=102"
    """
    while True:
        num1 = random.randint(1, 9)
        num2 = random.randint(10, 99)
        result = num1 * num2
        equation = f"{num1}*{num2}={result}"
        if len(equation) == 8 and 100 <= result <= 999:
            return (num1, num2, result)

def generate_numbers_for_division():
    """
    Generate two numbers that when divided create an 8-character equation.
    Returns a tuple of (dividend, divisor, result)
    Format: NNN/NN=N
    Example: (252, 36, 7) creates "252/36=7"
    """
    while True:
        result = random.randint(2, 9)
        divisor = random.randint(10, 99)
        dividend = result * divisor
        equation = f"{dividend}/{divisor}={result}"
        if len(equation) == 8:
            return (dividend, divisor, result)

################################################################################
#  DO NOT EDIT BELOW THIS LINE, THESE FUNCTIONS ARE ALREADY COMPLETED FOR YOU  #
################################################################################

def generate_equation():
    """
    Generate a random math equation for the Nerdle game.
    """
    operations = ['+', '-', '*', '/']
    operation = random.choice(operations)
    
    if operation == '+':
        num1, num2, result = generate_numbers_for_addition()
        equation = f"{num1}+{num2}={result}"
    elif operation == '-':
        num1, num2, result = generate_numbers_for_subtraction()
        equation = f"{num1}-{num2}={result}"
    elif operation == '*':
        num1, num2, result = generate_numbers_for_multiplication()
        equation = f"{num1}*{num2}={result}"
    else:  # operation == '/'
        num1, num2, result = generate_numbers_for_division()
        equation = f"{num1}/{num2}={result}"
    
    if len(equation) != 8:
        return generate_equation()
    
    return equation

def validate_equation(equation):
    """
    Check if a given equation string is mathematically correct.
    """
    if not isinstance(equation, str):
        return False
    if len(equation) != 8:
        return False
    if '=' not in equation:
        return False
    
    try:
        left_side, right_side = equation.split('=')
        expected_result = int(right_side)
        
        if '+' in left_side:
            parts = left_side.split('+')
            actual_result = int(parts[0]) + int(parts[1])
        elif '-' in left_side:
            parts = left_side.split('-')
            actual_result = int(parts[0]) - int(parts[1])
        elif '*' in left_side:
            parts = left_side.split('*')
            actual_result = int(parts[0]) * int(parts[1])
        elif '/' in left_side:
            parts = left_side.split('/')
            if int(parts[1]) == 0 or int(parts[0]) % int(parts[1]) != 0:
                return False
            actual_result = int(parts[0]) // int(parts[1])
        else:
            return False

        return actual_result == expected_result
        
    except Exception:
        return False
