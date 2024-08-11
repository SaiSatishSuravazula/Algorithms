def SelectionSort(arr):
    i = 0
    while i != len(arr)-1:
        min = arr[i]
        pos = i     ## Initialize pos to the current index i
        j = i + 1
        while (j != len(arr)):
            if (arr[j] < min):
                min = arr[j]
                pos = j
            j += 1
        arr[i],arr[pos] = arr[pos],arr[i]
        i += 1

# Asking the user for the number of elements
num_elements = int(input("Enter the number of elements: "))

# Initialize an empty list to store the elements
elements = []

# Loop to take each element as input
for _ in range(num_elements):
    element = int(input("Enter an element: "))
    elements.append(element)

print("List of elements:", elements)

SelectionSort(elements)

print("Sorted array: ", elements)