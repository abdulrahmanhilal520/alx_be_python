def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den
        return result
    
    except ZeroDivisionError:
        print("Division On Zero Not Allowed")
        return None
      
    except ValueError:
        print("Invalid Input, pleas Enter Numbers Only ")
        return None
