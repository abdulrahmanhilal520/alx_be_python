def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den
        return result
    
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
      
    except ValueError:
        print("Error: Please enter numeric values only.")
        return None
