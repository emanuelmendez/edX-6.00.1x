def nfruits(dict, pattern):
    """
    Takes two arguments:
    - A non-empty dictionary containing type of fruit and its initial quantity
    - A string pattern of the fruits eaten
    Returns the maximum quantity out of the different types of fruits that 
    is available with Python when he has reached the campus.
    """
     
    # This counter will prevent buying 1 of all fruits at the last iteration
    counter = len(pattern)
    
    for letter in pattern:
        counter -=1
        # a fruit is eaten
        dict[letter] -= 1
        
        # buy 1 of all fruits except the one just eaten
        # (This will not happen in the last iteration)
        if counter > 0:
            for key in dict:
                if letter != key:
                    dict[key] += 1
                    
    return max(dict.values())