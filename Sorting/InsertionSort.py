def Insertion_Sort(arr):
    for index in range(1, len(arr)):

        current_value = arr[index]
        #Insert the current value into the left sorted sub-array
        position = index-1

        while position >= 0 and arr[position] > current_value:
            arr[position+1] = arr[position]
            position = position - 1
        arr[position+1] = current_value

# Asking the user for the number of elements
num_elements = int(input("Enter the number of elements: "))

# Initialize an empty list to store the elements
elements = []

# Loop to take each element as input
for _ in range(num_elements):
    element = int(input("Enter an element: "))
    elements.append(element)

print("List of elements:", elements)

Insertion_Sort(elements)

print("Sorted array: ", elements)