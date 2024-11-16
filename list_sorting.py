'''
Write a Python function that takes two parameters: a list of numbers and a second parameter that can have one of three values:
If the second parameter is "asc", the function should return the list of numbers in ascending order. If it is "desc", the function should return the list of numbers in descending order. If the second parameter is "none", the function should return the unaltered list.
'''
import random as rand
def sort_list(unsorted_list, order = None):
    sorted_list = []
    counter = 0
    if order == None:
        return unsorted_list
    elif order == "asc":
        while len(unsorted_list) > 0:
            for i in unsorted_list:
                if i == min(unsorted_list):
                    sorted_list.append(i)
                    unsorted_list.remove(i)        
    elif order == "desc":
        while len(unsorted_list) > 0:
            for i in unsorted_list:
                if i == max(unsorted_list):
                    sorted_list.append(i)
                    unsorted_list.remove(i)     
    return sorted_list 
      
def main():
    print(f"Unsorted List: {num_list}")
    print(f"Sorted List: {sort_list(num_list, "desc")}")

num_list = [rand.randint(1,100) for i in range(10)]
main()