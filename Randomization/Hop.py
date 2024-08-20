import random

n = int(input("Enter a number: "))

i=n 
count = 0
while i != 1:
    i = random.randint(1,i)
    count += 1
    
print(count)