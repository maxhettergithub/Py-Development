'''
Create a function that accepts strings. The function thus created should be able to return a string where each character is doubled in the original string. 
For instance, if the parameter of the function is “now”, then it should return “nnooww”. 
'''
def double_string(string):
    characters = list(string)
    new_string = ''
    for i in characters:
        new_string = new_string + i + i
    return new_string


print(double_string("meme"))