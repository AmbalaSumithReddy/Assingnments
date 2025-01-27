#!/usr/bin/env python
# coding: utf-8

# In[1]:


def calculate_grade(marks):
    average = sum(marks) / len(marks)
    if average >= 90:
        return "Grade: A"
    elif 80 <= average < 90:
        return "Grade: B"
    elif 70 <= average < 80:
        return "Grade: C"
    else:
        return "Grade: Fail"

# Example usage
marks = []
for i in range(1, 4):
    mark = float(input(f"Enter the marks for subject {i}: "))
    marks.append(mark)

grade = calculate_grade(marks)
print(grade)

