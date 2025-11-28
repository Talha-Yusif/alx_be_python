
def safe_divide(numerator,denominator):
    

    try:
        n=float(numerator)
        d=float(denominator)
        x=n/d
        return f'The result of the division is {x}'
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    


