def getSublists(L, n):
    """
    L not empty
    0 < n <= len(L)
    """
    
    if(n == len(L)):
        return [L]
    
    all_sublists = []
    
    for i in range(len(L)):
        if i + n <= len(L):
            sublist = []
            for j in range(n):
                sublist += [L[i+j]]
            all_sublists.append(sublist)
    
    return all_sublists
    
def longestRun(L):
    
    lr = [L[0]]
    
    for i in range(len(L)):
        temp = [L[i]]
        for j in range(i, len(L)):
            if j+1 < len(L):
                if L[j] <= L[j+1]:
                    temp += [L[j+1]]
                else:
                    break
        if len(temp) > len(lr):
            lr = temp
    return len(lr)