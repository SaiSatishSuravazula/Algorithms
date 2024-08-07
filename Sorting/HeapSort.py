# Perform Heapify operation on a given array following a)Top-Down Approach

def Max_Heapify(arr, i, size):
    l = 2*i + 1
    r = 2*i + 2
    if l<size and arr[l] > arr[i]:
        largest = l
    else: largest = i
    if r<size and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        Max_Heapify(arr, largest, size)

def Build_Max_Heap(arr):
    size = len(arr)
    for index in range(size//2-1, -1, -1):
        Max_Heapify(arr, index, size)

def Heap_Sort(arr):
    Build_Max_Heap(arr)
    size = len(arr)
    for index in range(size-1, 0, -1):
        arr[0], arr[index] = arr[index], arr[0]
        size -= 1
        Max_Heapify(arr, 0, size)

# Asking the user for the number of elements
num_elements = int(input("Enter the number of elements: "))

# Initialize an empty list to store the elements
elements = []

# Loop to take each element as input
for _ in range(num_elements):
    element = int(input("Enter an element: "))
    elements.append(element)

print("List of elements:", elements)

Heap_Sort(elements)

print("Sorted array: ", elements)
