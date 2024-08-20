"""
Perform Random Binary Search and compare it with standard Binary Search. 
"""

import random
import time

def random_binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left != right:
        middle = random.randint(left, right-1)      #any integer between left and right-1 both inclusive.
        if arr[middle] < target:
            left = middle + 1
        else:
            right = middle

    if(arr[right] == target):
        return right
    else:
        return -1
        


def Binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left != right:
        middle = (left + right) // 2           #left<=middle<right
        if arr[middle] < target:
            left = middle + 1
        else:
            right = middle

    if(arr[right] == target):
        return right
    else:
        return -1
    
input_str = input("Enter the sorted numbers separated by spaces: ")

# Convert each element in the list to an integer
arr = list(map(int, input_str.split()))

target = int(input("Enter the element to be searched: "))

arr.sort()

print("Sorted arr: ", arr)

time_sum = 0
for i in range(100):
    start_time = time.time()
    pos = random_binary_search(arr, target)
    end_time = time.time()

    time_sum = end_time - start_time


print(f"Position: {pos}")
print(f"Average Execution time for Random binary search: {time_sum/100.0} seconds")

time_sum = 0
for i in range(100):
    start_time = time.time()
    pos = random_binary_search(arr, target)
    end_time = time.time()

    time_sum = end_time - start_time


print(f"Position: {pos}")
print(f"Average Execution time for normal binary search: {time_sum/100.0} seconds")



