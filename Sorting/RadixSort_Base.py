import queue

def get_ind(num, ind, base):
    return (num // (base ** ind)) % base

def radix_sort(arr, base):
    max_num = max(arr) 
    num_inds = 0

    while base ** num_inds <= max_num:
        num_inds += 1

    for ind in range(num_inds):

        queues = [queue.Queue() for _ in range(base)]

        for num in arr:
            ind_value = get_ind(num, ind, base)
            queues[ind_value].put(num) 

        arr.clear() 
        for q in queues:
            while not q.empty():  
                arr.append(q.get())  

base = int(input("Enter the base: "))
arr = list(map(int, input("Enter a list: ").split()))

radix_sort(arr, base)

print("Sorted list:", arr)