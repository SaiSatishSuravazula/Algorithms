"""
Permute a list of numbers using the following method:
Randomize-in-Place
"""

import random

def Randomize_in_place(arr):

    n = len(arr)
    for i in range(n):
        j = random.randint(i, n-1)
        arr[i], arr[j] = arr[j], arr[i]

# Asking the user for the number of elements
num_elements = int(input("Enter the number of elements: "))

# Initialize an empty list to store the elements
elements = []

# Loop to take each element as input
for _ in range(num_elements):
    element = int(input("Enter an element: "))
    elements.append(element)

print("List of elements:", elements)

Randomize_in_place(elements)

print("List of elements after permuting: ", elements)