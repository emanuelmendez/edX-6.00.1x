def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    if d == {}:
        return d
    
    tuples = d.items()
    inv_dict = {}
    
    for item in tuples:
        if item[1] not in inv_dict.keys():
            value_list = []
            value_list.append(item[0])
            inv_dict[item[1]] = value_list
        else:
            value_list = []
            value_list = inv_dict[item[1]] + [item[0]]
            value_list.sort()
            inv_dict[item[1]] = value_list
      
    return inv_dict