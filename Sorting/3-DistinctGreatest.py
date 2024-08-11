#  Determine the 1st,2nd and 3rd largest DISTINCT elements in a list using a O(n) algorithm. (Hint : Use Heap)

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
    return size

def GreatestThree(arr):
    heap_size = Build_Max_Heap(arr)
    top3 = set()                       #Use set for 3 distinct elements
    while len(top3) < 3 and heap_size > 0:
        top3.add(arr[0])
        heap_size -= 1
        arr[0], arr[heap_size] = arr[heap_size], arr[0]
        Max_Heapify(arr, 0, heap_size)
    return list(top3)

input_list = input("Enter numbers separated by spaces: ").strip().split()
arr = list(map(int, input_list))
final = GreatestThree(arr)
print("The three greatest distinct elements are: ", final)