#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Ask the user to enter a positive integer n
n = int(input("Enter a positive integer: "))

# Use a for loop to print all numbers from 1 to n on separate lines
print("Numbers from 1 to", n)
for i in range(1, n + 1):
    print(i)

# Use a while loop to calculate the sum of all numbers from 1 to n and print the result
sum_numbers = 0
i = 1
while i <= n:
    sum_numbers += i
    i += 1

print("The sum of all numbers from 1 to", n, "is:", sum_numbers)


# In[8]:



def calculate_square(n):
    return n * n

n = int(input("Enter a positive integer: "))

result = calculate_square(n)
print(f"The square of {n} is: {result}")

