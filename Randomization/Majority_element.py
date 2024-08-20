"""
Given a list of numbers, using random selection of choice of two elements per iteration, determine the Majority element. 
A Majority element is that which repeats more than half the times in the list. 
You have to provide an O(n) algorithm. 
"""


def majorityElement(arr):
        """
        The function gives the majority element in the array assuming there is majority element in the array
        """
        counter = 1
        size = len(arr)
        i=1
        candidate = arr[0]
        while(i<size):
            if(counter == 0):
                candidate = arr[i]
                counter = 1
                i+=1 
                continue
            if(arr[i] != candidate):
                counter-=1
            else:
                counter+=1
            i+=1
        
        return candidate

arr = [2,1,1,1,2]
print(majorityElement(arr))
    