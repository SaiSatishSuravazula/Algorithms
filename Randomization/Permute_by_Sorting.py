"""
Permute a list of numbers using the following method:
Permute-by-Sorting 
"""
import random

def Permute_by_Sorting(arr):
    n = len(arr)
    new_list = [0 for i in range(n)]
    for i in range(n):
        new_list[i] = random.randint(0, n**3)

    arr = Sort_Permute(arr, new_list)
    return arr

def Sort_Permute(arr, new_list):

    index_mapping = {}
    
    sorted_new_list = sorted(new_list)
    
    index = 0
    for value in sorted_new_list:
        index_mapping[value] = index
        index += 1
    
    permuted_arr = [0] * len(arr)
    
    for i in range(len(new_list)):
        original_value = arr[i]
        position = index_mapping[new_list[i]]
        permuted_arr[position] = original_value
    
    return permuted_arr



# Asking the user for the number of elements
num_elements = int(input("Enter the number of elements: "))

# Initialize an empty list to store the elements
elements = []

# Loop to take each element as input
for _ in range(num_elements):
    element = int(input("Enter an element: "))
    elements.append(element)

print("List of elements:", elements)

elements = Permute_by_Sorting(elements)

print("List of elements after permuting: ", elements)