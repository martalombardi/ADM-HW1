# INTRODUCTION

# Say "Hello, World!" With Python
# This line prints "Hello, World!" to the console
print("Hello, World!")

# Python If-Else
import math
import os
import random
import re
import sys

# Main block of code to execute if the script is run directly
if __name__ == '__main__':
    # Read an integer input and remove leading/trailing spaces
    n = int(input().strip())
    
    # Check if the number is odd
    if n % 2 != 0:
        print("Weird")
    else:
        # If number is even and in the range 2-5 (inclusive)
        if n in range(2, 6):
            print("Not Weird")
        # If number is even and in the range 6-20 (inclusive)
        elif n in range(6, 21):
            print("Weird")
        # If number is even and greater than 20
        elif n > 20:
            print("Not Weird")

# Arithmetic Operators
if __name__ == '__main__':
    # Read two integers from input
    a = int(input())
    b = int(input())
    
    # Print the sum of a and b
    print(a + b)
    # Print the difference of a and b
    print(a - b)
    # Print the product of a and b
    print(a * b)

# Python: Division
if __name__ == '__main__':
    # Read two integers from input
    a = int(input())
    b = int(input())
    
    # Perform integer division (quotient without remainder)
    print(a // b)
    # Perform floating point division
    print(a / b)

# Loops
if __name__ == '__main__':
    # Read an integer input
    n = int(input())
    
    # Check if the number is within the valid range [1, 20]
    if 1 <= n <= 20:
        # Loop through numbers from 0 to n-1
        for i in range(n):
            # Print the square of each number
            print(i * i)
    else:
        # Print an error message if the input is out of range
        print("The number must be in the interval [1,20]")

# Write a function
def is_leap(year):
    # By default, the year is not a leap year
    leap = False
    
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # Check if the year is divisible by 100
        if year % 100 == 0:
            # Check if the year is divisible by 400
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    
    # Return whether the year is a leap year or not
    return leap

# Read a year input and check if it's a leap year
year = int(input())
print(is_leap(year))

# Print Function
def printFunction(n):
    # Loop through numbers from 1 to n
    for i in range(1, n + 1):
        # Print all numbers without spaces, using 'end' to avoid newlines
        print(i, end='')

# Main block to execute the printFunction
if __name__ == '__main__':
    # Read an integer input
    n = int(input())
    # Call the print function to display the numbers from 1 to n
    printFunction(n)

# DATA TYPES

# List Comprehensions
# This function generates a list of coordinates based on the conditions given
def coordinates(x, y, z, n):
    # Using list comprehension to generate coordinates [i, j, k]
    # where i + j + k is not equal to n
    coord = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]
    return coord

if __name__ == '__main__':
    # Read inputs for x, y, z, and n
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # Print the result of the coordinates function
    print(coordinates(x, y, z, n))

# Find the Runner-Up Score!
# This function finds the second highest score from a list of scores
def runnerUpScore(arr):
    # Initialize two variables to track the highest and second highest scores
    # Setting them to negative infinity ensures any real score will be higher
    first_score = -float("inf")
    second_score = -float("inf")
    
    # Iterate through each score in the input list
    for score in arr:
        # If the current score is higher than the highest recorded score
        if score > first_score:
            # The current highest score becomes the second highest
            second_score = first_score
            # Update the highest score with the current score
            first_score = score
        # If the current score is between the highest and second highest scores
        elif score > second_score and score != first_score:
            # Update the second highest score with the current score
            second_score = score
    
    # Return the second highest score
    return second_score

if __name__ == '__main__':
    # Read the number of elements and the list of scores
    n = int(input())
    arr = map(int, input().split())
    # Print the result of the runnerUpScore function
    print(runnerUpScore(arr))

# Nested Lists
# This function finds students with the second lowest grade and prints their names alphabetically
def secondLowestGrade(scores):
    # Initialize the lowest and second lowest score variables to infinity
    lowest_score = float("inf")
    second_lowest_score = float("inf")
    # Lists to hold student names who have the lowest and second lowest scores
    first_names = []
    second_names = []

    # Iterate through each student and their score in the dictionary
    for name in scores.keys():
        score = scores.get(name)
        # If the current score is lower than the recorded lowest score
        if score < lowest_score:
            # Update the second lowest score and move the first names to second
            second_lowest_score = lowest_score
            second_names = first_names
            # Update the lowest score and record the name as the lowest scorer
            lowest_score = score
            first_names = [name]
        # If the current score is equal to the lowest score, add the name to the first names list
        elif score == lowest_score:
            first_names.append(name)
        # If the score is equal to the second lowest, add the name to the second names list
        elif score == second_lowest_score:
            second_names.append(name)
        # If the score falls between the lowest and second lowest, update the second lowest score
        elif lowest_score < score < second_lowest_score:
            second_lowest_score = score
            second_names = [name]
    
    # Sort the names of students with the second lowest score in alphabetical order
    second_names.sort()
    
    # Print each name from the second lowest names list
    for i in range(len(second_names)):
        print(second_names[i])

if __name__ == '__main__':
    # Read input for the number of students and their scores
    scores = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores[name] = score
    # Call the function to find and print students with the second lowest grade
    secondLowestGrade(scores)

# Finding the percentage
# This function calculates the average score of a queried student
def avgQuery(student_marks, query_name):
    # Get the list of scores for the queried student
    query_name_scores = student_marks.get(query_name)
    # Calculate the average score
    average = sum(query_name_scores) / len(query_name_scores)
    # Return the average formatted to 2 decimal places
    return "{:.2f}".format(average)

if __name__ == '__main__':
    # Read the number of students and their marks
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    # Read the student name to query
    query_name = input()
    # Print the average score of the queried student
    print(avgQuery(student_marks, query_name))

# Lists
# This function performs various operations on a list based on user input
def performCommands(operations):
    arr = []
    # Iterate over the operations and execute them
    for operation in operations:
        command, *number = operation.split()
        value = list(map(int, number))
        match command:
            case "insert":
                # Insert value[1] at index value[0]
                arr.insert(value[0], value[1])
            case "print":
                # Print the current list
                print(arr)
            case "remove":
                # Remove the first occurrence of value[0]
                arr.remove(value[0])
            case "append":
                # Append value[0] to the list
                arr.append(value[0])
            case "sort":
                # Sort the list
                arr.sort()
            case "pop":
                # Remove the last element from the list
                arr.pop()
            case "reverse":
                # Reverse the list
                arr.reverse()

if __name__ == '__main__':
    # Read the number of operations
    N = int(input())
    operations = []
    # Read each operation and store it in the list
    for i in range(N):
        command = input()
        operations.append(command)
    # Execute the operations
    performCommands(operations)

# Tuples
# This block creates a tuple from input integers and prints its hash value
if __name__ == '__main__':
    # Read the number of elements in the tuple
    n = int(input())
    # Create a tuple from the input integers
    t = tuple(map(int, input().split()))
    # Print the hash of the tuple
    print(hash(t))

# STRINGS

# sWAP cASE
def swap_case(s):
    swapped = []
    
    for char in s:
        if char.isupper():
            swapped.append(char.lower())
        else:
            swapped.append(char.upper())
    return(''.join(swapped))

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# String Split and Join
def split_and_join(line):
    return '-'.join(line.split())

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# What's Your Name?
def print_full_name(first, last):
    print("Hello " + first + " " + last + "! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

# Mutations
def mutate_string(string, position, character):
    string_list = list(string)
    string_list[position] = character
    return ''.join(string_list)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# Find a string
def count_substring(string, sub_string):
    
    count = 0
    len_sub_string = len(sub_string)
    
    for i in range(len(string) - len_sub_string + 1):
        if string[i:i+len_sub_string] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

# String Validators
if __name__ == '__main__':
    s = input()
    
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s)) 
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))

# Text Alignment
thickness = int(input())  
c = 'H'

for i in range(thickness):
    print((c * (2 * i + 1)).center(thickness * 2))

for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))

for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

for i in range(thickness):
    print((c * (2 * (thickness - i) - 1)).center(thickness * 2).rjust(thickness * 6))

# Text Wrap
import textwrap

def wrap(string, max_width):
    len_string = len(string)
    s = ""
    upper = max_width
    i = 0
    
    while i < len_string:
        if i + max_width > len_string:
            upper = len_string - i
        s = s + string[i:i+upper] + "\n"
        i = i + upper
    return(s)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# Designer Door Mat
