from .constants import MONEY_UNITS


def divide_money_into_units(amount):
    """
    Takes amount argument as an int value and returns dictionary of (int, int) pair.
    Returned dictionary key values represent unit of money and corresponding count
    shows how many exists in the withdrawal amount. This function tries to divide 
    the given amount into most minimal amount of paper money.
    """
    result = {}

    for unit in MONEY_UNITS:
        count = amount // unit
        if count > 0:
            result[unit] = count
    
        amount -= count * unit
        
    return result
