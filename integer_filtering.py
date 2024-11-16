#Create a Python function named "get_integers" that accepts a list of mixed non-negative integers and strings. The function should filter and return only the integers in the same order as they appear in the original list.

def get_integers(list): 
    new_list = []
    for i in list:
        if isinstance(i, int):
            new_list.append(i)
    return new_list

list_of_crap = ["spicy", 1531, "meme", 36168, "sleepy", 0, 2, 1, 34]
print(get_integers(list_of_crap))

