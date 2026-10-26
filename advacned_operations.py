def multiply(a, b):
    """Return the product of two numbers."""
    return a * b
 
 
def divide(a, b):
    """Divide the first number by the second number."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
 
    return a / b