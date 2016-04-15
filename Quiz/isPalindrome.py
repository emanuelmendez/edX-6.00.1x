def isPalindrome(aString):
    '''
    aString: a string
    '''
    length = len(aString)
    
    for index in range (0, length):
        if (aString[index] != aString[length-index-1] ):
            return False

    return True