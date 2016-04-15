import math

def polysum (n, s):
    ''' Returns the sum of the area and the square of the perimeter 
    of a regular polygon, rounded to 4 decimal places. 
    n is number of sides, and s is length of every side '''    
    
    if n == 0:
        print "Invalid number of sides"
        return -1
    else:
        area = (0.25 * n * s**2) / math.tan(math.pi / n)
        boundary = n*s
        result = area + boundary**2
        return round(result, 4)