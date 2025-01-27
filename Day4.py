#!/usr/bin/env python
# coding: utf-8

# In[2]:


def sum_even_numbers(n):
    total = 0
    for i in range(2, n+1, 2):
        total += i
    return total

# Example usage
n = int(input("Enter a positive integer: "))
result = sum_even_numbers(n)
print(f"The sum of all even numbers between 1 and {n} is: {result}")

