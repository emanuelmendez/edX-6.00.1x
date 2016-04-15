def dict_interdiff(d1, d2):
    '''
    You are also given a function f, that takes in two integers, 
    performs an unknown operation on them, and returns a value.
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    inter_dict = {}
    diff_dict = {}
    
    for key in d1.keys():
        if d2.has_key(key):
            inter_dict[key] = f(d1[key], d2[key])
        else:
            diff_dict[key] = d1[key]
    
    for key in d2.keys():
        if not d1.has_key(key):
            diff_dict[key] = d2[key]
    
    return (inter_dict, diff_dict)