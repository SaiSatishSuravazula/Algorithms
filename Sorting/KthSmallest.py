def partition(arr, low, high):
    pivot = arr[low]
    i, j = low + 1, high
    while i <= j:
        if arr[i] <= pivot:
            i += 1
        elif arr[j] > pivot:
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i, j = i + 1, j - 1
    arr[i - 1], arr[low] = arr[low], arr[i - 1]
    return i - 1

def k_sort(arr, low, high, k):
    if low <= high:
        pi = partition(arr, low, high)
        if pi == k:
            return arr[pi]
        elif pi > k:
            return k_sort(arr, low, pi - 1, k)
        else:
            return k_sort(arr, pi + 1, high, k - pi - 1)
    return None

# Asking the user for the number of elements
num_elements = int(input("Enter the number of elements: "))

# Initialize an empty list to store the elements
elements = []

# Loop to take each element as input
for _ in range(num_elements):
    element = int(input("Enter an element: "))
    elements.append(element)

# Asking the user for the Kth smallest
k = int(input("Enter the kth element: ")) - 1  # Adjust k to be zero-based

print("List of elements:", elements)

result = k_sort(elements, 0, num_elements - 1, k)
if result is not None:
    print("Kth smallest element is:", result)
else:
    print("Invalid input.")
