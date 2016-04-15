def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    outputList = []
    
    def flatElem(bList):
        if type(bList) is list:
            if len(bList) == 1:
                flatElem(bList[0])
            elif len(bList) > 1:
                flatElem(bList[0:len(bList)/2])
                flatElem(bList[len(bList)/2:])
        else:
            outputList.append(bList)
            
    flatElem(aList)
    return outputList