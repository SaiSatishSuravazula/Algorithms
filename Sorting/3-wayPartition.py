def ThreeWayPartition(elements, low, high):
    x = elements[low]
    i,j,k = low+1, high, low
    while(i<=j):
        if elements[i] < x:
            elements[i], elements[k] = elements[k], elements[i]
            i += 1
        elif elements[i] > x:
            elements[i], elements[j] = elements[j], elements[i]
            j -= 1
        else:
            i += 1
    elements[i-1], elements[low] = elements[low], elements[i-1]
    return i-1


# Asking the user for the number of elements
n = int(input("Enter the number of elements: "))

# Initialize an empty list to store the elements
elements = []

# Loop to take each element as input
for _ in range(n):
    element = int(input("Enter an element: "))
    elements.append(element)

low = 0
high = n-1
print(f"Index of first element after doing 3-way partition: {ThreeWayPartition(elements,low, high)}")