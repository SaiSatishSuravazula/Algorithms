# Given a permuted list A containing n numbers in the range [0,n-1],find how many numbers coincide with their index ON AVERAGE. 

import random

# Count the number of elements that coincide with their index in the permutation. 


def count(perm):
    sum = 0
    for i in range(len(perm)):
       if perm[i] == i:
           sum += 1
    return sum


# Calculate the average number of fixed points over a number of random permutations.

def average_fixed_points(n, trials):
    total_fixed_points = 0

    for _ in range(trials):
        perm = list(range(n))
        random.shuffle(perm)
        
        total_fixed_points += count(perm)
    
    return total_fixed_points / trials


n = 10  # Size of the permutation
trials = 10000  # Number of trials to estimate the average

avg_fixed_points = average_fixed_points(n, trials)
print(f"Average number of fixed points in a permutation of size {n}: {avg_fixed_points}")
