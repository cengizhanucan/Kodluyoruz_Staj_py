# Function that flattens a list:
def flatten(l):
    empty = []
    for i in range (len(l)):
        if isinstance(l[i], list):
            empty += flatten(l[i])
        else:
            empty.append(l[i])
    return empty
    
# Function that reverses the list, reverses the list inside of the list, if that exists.
def reverse_list(l):
    for i in range (len(l)):
        if isinstance(l[i], list):
            l[i] = l[i][::-1]
    return l[::-1]
    
    
    
