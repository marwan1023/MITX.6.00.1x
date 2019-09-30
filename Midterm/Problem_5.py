Problem 5
 Bookmark this page
Problem 5
20.0/20.0 points (graded)
Write a Python function that returns a list of keys in aDict that map to integer values that are unique (i.e. values appear exactly once in aDict). The list of keys you return should be sorted in increasing order. (If aDict does not contain any unique values, you should return an empty list.)

This function takes in a dictionary and returns a list.

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    tmp = {}
    result = []
    for value in aDict.values():
        if(value in tmp.keys()): tmp[value] += 1
        else: tmp[value] = 1
    for key in aDict.keys():
        if(tmp[aDict[key]] == 1): result.append(key)
    return sorted(result)
