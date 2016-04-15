def ndigits (x):
    """
    Takes an integer x (either positive or negative) as an argument
    Returns number of digits in x
    """
    
    # error checking
    if type(x) is not int:
        print "Error, not an integer."
        return None
    
    # returns 1 if its a single digit
    if x in range(-9,10):
        return 1
        
    # if it has more than one digit,
    # it adds 1 and calls ndigit again, 
    # but throwing away the first digit (from the right)
    else:
        return 1 + ndigits(x/10)