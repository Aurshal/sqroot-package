import math
def sqroot(num:float)->float:
    """
    Given a number 'num', this functio returns
    the square root of the number
    """
    try:
        return math.sqrt(num)
    except ValueError:
        return "Input must be positive real number"


