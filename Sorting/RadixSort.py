# Use QUEUE data structure to implement Radix Sort,taking the base and the list of positive integers as input from the user.
import queue

def Radix_Sort(arr):

    # Determine the length of the largest element
    max_length = len(str(max(arr)))      #max element will have more digits

    # Pad all elements with leading zeros to match the length of the largest element
    arr = [str(element).zfill(max_length) for element in arr]

    buckets = [queue.Queue() for _ in range(10)] # Create a list of empty queues
    for j in range(-1, -max_length - 1, -1):
        for i in range(len(arr)):
            digit = int (arr[i][j])
            buckets[digit].put(arr[i])

        index = 0
        # Collect elements from buckets and put them back into arr
        for b in range(10):
            while not buckets[b].empty():
                arr[index] = buckets[b].get()
                index += 1

    # Convert back to integers after sorting
    arr = [int(element) for element in arr]
    return arr

        
# Asking the user for the number of elements
num_elements = int(input("Enter the number of elements: "))

# Initialize an empty list to store the elements
elements = []

# Loop to take each element as input
for _ in range(num_elements):
    element = int(input("Enter an element: "))
    elements.append(element)


print("elements:", elements)

elements = Radix_Sort(elements)

print("Sorted elements: ", elements)