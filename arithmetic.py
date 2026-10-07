"""
Basic Arithmetic Operations Module

A clean implementation of fundamental arithmetic operations with error handling.
"""


class ArithmeticError(Exception):
    """Custom exception for arithmetic operations."""
    pass


def add(x: float, y: float) -> float:
    """
    Add two numbers.
    
    Args:
        x: First number
        y: Second number
        
    Returns:
        Sum of x and y
    """
    return x + y


def subtract(x: float, y: float) -> float:
    """
    Subtract two numbers.
    
    Args:
        x: First number
        y: Second number
        
    Returns:
        Difference of x and y
    """
    return x - y


def multiply(x: float, y: float) -> float:
    """
    Multiply two numbers.
    
    Args:
        x: First number
        y: Second number
        
    Returns:
        Product of x and y
    """
    return x * y


def divide(x: float, y: float) -> float:
    """
    Divide two numbers with zero-division handling.
    
    Args:
        x: Numerator
        y: Denominator
        
    Returns:
        Quotient of x and y
        
    Raises:
        ArithmeticError: If y is zero
    """
    if y == 0:
        raise ArithmeticError("Cannot divide by zero")
    return x / y


def modulus(x: float, y: float) -> float:
    """
    Calculate modulus (remainder) of two numbers.
    
    Args:
        x: Dividend
        y: Divisor
        
    Returns:
        Remainder of x divided by y
        
    Raises:
        ArithmeticError: If y is zero
    """
    if y == 0:
        raise ArithmeticError("Cannot calculate modulus with zero")
    return x % y


def power(x: float, y: float) -> float:
    """
    Raise x to the power of y.
    
    Args:
        x: Base number
        y: Exponent
        
    Returns:
        x raised to the power of y
    """
    return x ** y


def main():
    """Main function to demonstrate arithmetic operations."""
    try:
        print("=" * 40)
        print("Basic Arithmetic Calculator")
        print("=" * 40)
        
        a = float(input("\nEnter first number: "))
        b = float(input("Enter second number: "))
        
        print("\n" + "-" * 40)
        print(f"Results:")
        print("-" * 40)
        print(f"Add:      {a} + {b} = {add(a, b)}")
        print(f"Subtract: {a} - {b} = {subtract(a, b)}")
        print(f"Multiply: {a} × {b} = {multiply(a, b)}")
        print(f"Divide:   {a} ÷ {b} = {divide(a, b):.4f}")
        print(f"Modulus:  {a} % {b} = {modulus(a, b)}")
        print(f"Power:    {a} ^ {b} = {power(a, b)}")
        print("-" * 40)
        
    except ValueError:
        print("Error: Please enter valid numbers")
    except ArithmeticError as e:
        print(f"Arithmetic Error: {e}")


if __name__ == "__main__":
    main()
