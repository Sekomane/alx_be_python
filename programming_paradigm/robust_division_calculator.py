# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divide two values, handling errors such as:
    - Non-numeric inputs
    - Division by zero
    """

    try:
        # Convert inputs to float
        num = float(numerator)
        den = float(denominator)

        try:
            result = num / den
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
