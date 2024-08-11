def CountingSort(arr):
    count = [0] * 10
    for num in arr:
        if 0 <= num < 10:  
            count[num] += 1

    m = 0
    for j in range(len(count)):
        while count[j] > 0:
            arr[m] = j
            count[j] -= 1
            m += 1

input_list = input("Enter numbers(0-9) separated by spaces: ").strip().split()
arr = list(map(int, input_list))
CountingSort(arr)
print(arr)