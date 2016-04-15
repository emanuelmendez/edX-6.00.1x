def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    After you define your function, make a function call to run_satisfiesF(L, satisfiesF). 
    Do not define f or run_satisfiesF.
    """
    
    length = len(L)
    index = 0
    
    for count in range(length):
        if index >= len(L):
            break
        if not f(L[index]):
            L.remove(L[index])
        else:
            index += 1
            
    return len(L)
    
run_satisfiesF(L, satisfiesF)