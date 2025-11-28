
def safe_divide(numerator,denominator):
    

    try:
        n=float(numerator)
        d=float(denominator)
        x=n/d
        return f'The result of the division is {x}'
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
    


