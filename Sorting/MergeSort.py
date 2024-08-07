# Implement Merge Sort using recursion and Divide and Conquer Strategy.

def merge(arr, left, middle, right, temp):
    i, j, k = left, middle + 1, left

    # Merge the two halves into the temporary array
    while i <= middle and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    # Copy the remaining elements of the left half, if any
    while i <= middle:
        temp[k] = arr[i]
        i += 1
        k += 1

    # Copy the remaining elements of the right half, if any
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    # Copy the sorted subarray into the original array
    for i in range(left, right + 1):
        arr[i] = temp[i]

# Example usage
def merge_sort(arr, left, right, temp):
    if left < right:
        middle = (left + right) // 2
        merge_sort(arr, left, middle, temp)
        merge_sort(arr, middle + 1, right, temp)
        merge(arr, left, middle, right, temp)

# Asking the user for the number of elements
num_elements = int(input("Enter the number of elements: "))

# Initialize an empty list to store the elements
elements = []

# Loop to take each element as input
for _ in range(num_elements):
    element = int(input("Enter an element: "))
    elements.append(element)

# Create a temporary array for merge process
temp = [0] * num_elements

# Perform merge sort
merge_sort(elements, 0, num_elements - 1, temp)

print("Sorted elements:", elements)



	   