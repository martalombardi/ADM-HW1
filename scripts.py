# --------------------------------------- PROBLEM 1 ---------------------------------------

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
# Function to swap case of each character in the input string
def swap_case(s):
    swapped = []  # List to store swapped characters
    
    # Iterate through each character in the string
    for char in s:
        if char.isupper():
            swapped.append(char.lower())  # Convert uppercase to lowercase
        else:
            swapped.append(char.upper())  # Convert lowercase to uppercase
    
    return ''.join(swapped)  # Join the swapped characters into a string

if __name__ == '__main__':
    s = input()  # Get input string
    result = swap_case(s)  # Call the function to swap case
    print(result)  # Print the result

# String Split and Join
# Function to split a string by spaces and join with hyphens
def split_and_join(line):
    return '-'.join(line.split())  # Split by spaces and join with '-'

if __name__ == '__main__':
    line = input()  # Get input string
    result = split_and_join(line)  # Call the function to split and join
    print(result)  # Print the result

# What's Your Name?
# Function to print a greeting with full name
def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")  # Print formatted greeting

if __name__ == '__main__':
    first_name = input()  # Input first name
    last_name = input()  # Input last name
    print_full_name(first_name, last_name)  # Call the function

# Mutations
# Function to mutate a string at a given position
def mutate_string(string, position, character):
    string_list = list(string)  # Convert string to list
    string_list[position] = character  # Replace character at position
    return ''.join(string_list)  # Return mutated string

if __name__ == '__main__':
    s = input()  # Get input string
    i, c = input().split()  # Get position and character
    s_new = mutate_string(s, int(i), c)  # Call the function to mutate string
    print(s_new)  # Print the mutated string

# Find a string
# Function to count occurrences of a substring in a string
def count_substring(string, sub_string):
    count = 0  # Initialize count
    len_sub_string = len(sub_string)  # Length of the substring
    
    # Iterate through the string to check for substring matches
    for i in range(len(string) - len_sub_string + 1):
        if string[i:i+len_sub_string] == sub_string:
            count += 1  # Increment count if substring matches
    
    return count  # Return the count

if __name__ == '__main__':
    string = input().strip()  # Get input string
    sub_string = input().strip()  # Get substring to search
    count = count_substring(string, sub_string)  # Call the function to count occurrences
    print(count)  # Print the count

# String Validators
# Check if the string contains various types of characters
if __name__ == '__main__':
    s = input()  # Get input string
    
    # Check if any alphanumeric, alphabetic, digits, lowercase, or uppercase characters exist
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))

# Text Alignment
# This function prints an 'H' pattern based on input thickness
thickness = int(input())  # Get thickness input
c = 'H'  # Character to use for the pattern

# Top cone of the pattern
for i in range(thickness):
    print((c * (2 * i + 1)).center(thickness * 2))

# Upper pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Middle belt
for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))

# Lower pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Bottom cone
for i in range(thickness):
    print((c * (2 * (thickness - i) - 1)).center(thickness * 2).rjust(thickness * 6))

# Text Wrap
# Function to wrap text at a specified width
import textwrap

def wrap(string, max_width):
    len_string = len(string)  # Length of the string
    s = ""
    upper = max_width
    i = 0
    
    # Split the string into chunks of max_width
    while i < len_string:
        if i + max_width > len_string:
            upper = len_string - i
        s = s + string[i:i+upper] + "\n"
        i += upper
    
    return s  # Return the wrapped string

if __name__ == '__main__':
    string, max_width = input(), int(input())  # Get input string and max width
    result = wrap(string, max_width)  # Call the wrap function
    print(result)  # Print the wrapped string

# Designer Door Mat
# Function to print a designer door mat pattern
def designer(n, m):
    rows_above = n // 2  # Number of rows above the 'WELCOME' line

    # Print top half of the mat
    for i in range(rows_above):
        pattern = ('.|.' * (2 * i + 1)).center(m, '-')  # Generate pattern with center alignment
        print(pattern)
    
    # Print the middle 'WELCOME' line
    print('WELCOME'.center(m, '-'))

    # Print bottom half of the mat
    for i in range(rows_above - 1, -1, -1):
        pattern = ('.|.' * (2 * i + 1)).center(m, '-')  # Mirror the pattern from top half
        print(pattern)

if __name__ == '__main__':
    n, m = map(int, input().split())  # Get dimensions of the mat
    designer(n, m)  # Call the function to print the mat

# String Formatting
# Function to print formatted numbers in decimal, octal, hexadecimal, and binary
def print_formatted(number):
    formatted = []
    width = len(bin(number)) - 2  # Calculate width for formatting
    
    # Generate formatted strings for each number
    for i in range(1, number + 1):
        sub = [
            str(i).rjust(width),
            oct(i).replace('0o', '').rjust(width),
            str(hex(i).replace('0x', '').upper()).rjust(width),
            bin(i).replace('0b', '').rjust(width)
        ]
        formatted.append(sub)
    
    # Print the formatted numbers
    for sublist in formatted:
        print(' '.join(sublist))

if __name__ == '__main__':
    n = int(input())  # Get the input number
    print_formatted(n)  # Call the function to print formatted numbers

# Alphabet Rangoli
# Function to print a Rangoli pattern of letters
import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase  # Get lowercase alphabet
    pattern_lines = []  # List to store pattern lines
    
    # Generate top half of the pattern
    for i in range(size - 1, -1, -1):
        letters = '-'.join(alphabet[size - 1:i:-1] + alphabet[i:size])
        line = letters.center(4 * size - 3, '-')
        pattern_lines.append(line)
    
    # Generate bottom half (mirrored from top)
    for i in range(1, size):
        letters = '-'.join(alphabet[size - 1:i:-1] + alphabet[i:size])
        line = letters.center(4 * size - 3, '-')
        pattern_lines.append(line)
    
    print('\n'.join(pattern_lines))  # Print the entire pattern

if __name__ == '__main__':
    n = int(input())  # Get the input size
    print_rangoli(n)  # Call the function to print the rangoli

# Capitalize!
# Function to capitalize the first letter of each word in a string
def solve(s):
    return ' '.join([word.capitalize() for word in s.split()])  # Capitalize each word

if __name__ == '__main__':
    s = input()  # Get input string
    result = solve(s)  # Call the function to capitalize words
    print(result)  # Print the result
    
# The Minion Game
# This function determines the winner between Kevin and Stuart in the Minion Game.
def minion_game(string):
    
    scores = {'Kevin': 0, 'Stuart': 0}  # Initialize scores for both players
    string_len = len(string)  # Length of the input string

    # Loop through each character in the string
    for i in range(string_len):
        if string[i] in 'AEIOU':  # Check if the character is a vowel
            scores['Kevin'] = scores['Kevin'] + string_len - i  # Kevin scores for vowels
        else:
            scores['Stuart'] = scores['Stuart'] + string_len - i  # Stuart scores for consonants

    # Determine and print the winner or draw
    if scores['Kevin'] > scores['Stuart']:
        print("Kevin " + str(scores['Kevin']))  # Kevin wins
    elif scores['Stuart'] > scores['Kevin']:
        print("Stuart " + str(scores['Stuart']))  # Stuart wins
    else:
        print("Draw")  # It's a draw

if __name__ == '__main__':
    s = input()  # Input string
    minion_game(s)  # Call the function to play the game

# Merge the Tools!
# This function splits a string into k-sized chunks and removes duplicate characters from each chunk.
def merge_the_tools(string, k):
    # Iterate through the string in chunks of size k
    for i in range(0, len(string), k):
        unique = []  # List to store unique characters in each segment
        # Iterate through each character in the current segment
        for c in string[i:i+k]:
            if c not in unique:
                unique.append(c)  # Add character to unique list if not already present
        print(''.join(unique))  # Print the unique characters as a string

if __name__ == '__main__':
    string, k = input(), int(input())  # Input string and integer k
    merge_the_tools(string, k)  # Call the function to merge tools

# SETS
    
# Introduction to Sets
# This function calculates the average of unique elements from an array.
def average(array):
    unique = set(array)  # Convert array to a set to remove duplicates
    avg = round(sum(unique)/len(unique), 3)  # Calculate the average, rounded to 3 decimal places
    return avg

if __name__ == '__main__':
    n = int(input())  # Input the number of elements
    arr = list(map(int, input().split()))  # Input the array of elements
    result = average(arr)  # Call the average function
    print(result)  # Print the result

# No Idea!
# This function calculates happiness based on two sets A and B.
def happiness(arr, A, B):
    A = set(A)  # Convert A to a set
    B = set(B)  # Convert B to a set
    # Add 1 if element is in A, subtract 1 if in B, else add 0
    return sum((1 if e in A else -1 if e in B else 0) for e in arr)

if __name__ == '__main__':
    size = list(map(int, input().rstrip().split()))  # Input the sizes of arrays
    arr = list(map(int, input().rstrip().split()))  # Input the main array
    A = list(map(int, input().rstrip().split()))  # Input set A
    B = list(map(int, input().rstrip().split()))  # Input set B
    print(happiness(arr, A, B))  # Print the happiness score

# Symmetric Difference
# This function calculates and prints the symmetric difference of two sets.
def symmetricDifference(a, b):
    symDiff = []  # List to store symmetric difference elements
    set_a = set(a)  # Convert a to a set
    set_b = set(b)  # Convert b to a set
    # Loop through set_a and add elements not in set_b
    for e in set_a:
        if e not in set_b:
            symDiff.append(e)
        else:
            set_b.remove(e)  # Remove common elements from set_b
    symDiff = sorted(symDiff + list(set_b))  # Sort the final symmetric difference list
    print('\n'.join(list(map(str, symDiff))))  # Print each element on a new line

if __name__ == '__main__':
    M = int(input())  # Input size of set a
    a = list(map(int, input().rstrip().split()))  # Input elements of set a
    N = int(input())  # Input size of set b
    b = list(map(int, input().rstrip().split()))  # Input elements of set b
    symmetricDifference(a, b)  # Call the function to print the symmetric difference

# Set.add()
# This function counts the number of distinct countries.
def distinctCountry(N, country_stamps):
    distinct = set()  # Create an empty set to store distinct countries
    for country in country_stamps:
        if country not in distinct:
            distinct.add(country)  # Add country to the set if not already present
    return len(distinct)  # Return the number of distinct countries

if __name__ == '__main__':
    N = int(input())  # Input number of stamps
    country_stamps = [input().strip() for _ in range(N)]  # Input the list of country names
    print(distinctCountry(N, country_stamps))  # Print the number of distinct countries

# Set .discard(), .remove() & .pop()
# This function performs commands on a set and returns the sum of elements.
def commandSum(s, commands):
    for command in commands:
        command_list = list(command.split())  # Split command into list
        match command_list[0]:
            case "discard":
                s.discard(int(command_list[1]))  # Discard the element from the set
            case "pop":
                s.pop()  # Pop an element from the set
            case "remove":
                s.remove(int(command_list[1]))  # Remove the element from the set
    return sum(s)  # Return the sum of elements in the set

if __name__ == '__main__':
    n = int(input())  # Input number of elements in set
    s = set(map(int, input().split()))  # Input elements of set
    N = int(input())  # Input number of commands
    commands = [input().strip() for _ in range(N)]  # Input commands
    print(commandSum(s, commands))  # Print the sum of elements after commands

# Set .union() Operation
# This function returns the size of the union of two sets.
def union(arr1, arr2):
    return len(arr1.union(arr2))  # Return the size of the union

if __name__ == '__main__':
    n1 = int(input())  # Input size of set 1
    arr1 = set(map(int, input().strip().split()))  # Input elements of set 1
    n2 = int(input())  # Input size of set 2
    arr2 = set(map(int, input().strip().split()))  # Input elements of set 2
    print(union(arr1, arr2))  # Print the size of the union

# Set .intersection() Operation
# This function returns the size of the intersection of two sets.
def intersection(arr1, arr2):
    return len(arr1.intersection(arr2))  # Return the size of the intersection

if __name__ == '__main__':
    n1 = int(input())  # Input size of set 1
    arr1 = set(map(int, input().strip().split()))  # Input elements of set 1
    n2 = int(input())  # Input size of set 2
    arr2 = set(map(int, input().strip().split()))  # Input elements of set 2
    print(intersection(arr1, arr2))  # Print the size of the intersection

# Set .difference() Operation
# This function returns the size of the difference between two sets.
def difference(arr1, arr2):
    return len(arr1.difference(arr2))  # Return the size of the difference

if __name__ == '__main__':
    n1 = int(input())  # Input size of set 1
    arr1 = set(map(int, input().strip().split()))  # Input elements of set 1
    n2 = int(input())  # Input size of set 2
    arr2 = set(map(int, input().strip().split()))  # Input elements of set 2
    print(difference(arr1, arr2))  # Print the size of the difference

# Set .symmetric_difference() Operation
# This function returns the size of the symmetric difference between two sets.
def sym_difference(arr1, arr2):
    return len(arr1.symmetric_difference(arr2))  # Return the size of the symmetric difference

if __name__ == '__main__':
    n1 = int(input())  # Input size of set 1
    arr1 = set(map(int, input().strip().split()))  # Input elements of set 1
    n2 = int(input())  # Input size of set 2
    arr2 = set(map(int, input().strip().split()))  # Input elements of set 2
    print(sym_difference(arr1, arr2))  # Print the size of the symmetric difference

# Set Mutations
# This function performs various mutations on a set and returns the sum of elements.
def manipulation(A, commands):
    for i in range(0, len(commands), 2):
        command = commands[i].split()  # Parse command
        command_list = [command[0], command[1], set(map(int, commands[i+1].strip().split()))]
        match command_list[0]:
            case "difference_update":
                A.difference_update(command_list[2])  # Perform difference update
            case "intersection_update":
                A.intersection_update(command_list[2])  # Perform intersection update
            case "symmetric_difference_update":
                A.symmetric_difference_update(command_list[2])  # Perform symmetric difference update
            case "update":
                A.update(command_list[2])  # Perform update
    return sum(A)  # Return the sum of elements in the set

if __name__ == '__main__':
    nA = int(input())  # Input size of set A
    A = set(map(int, input().strip().split()))  # Input elements of set A
    N = int(input())  # Input number of commands
    commands = [input().strip() for _ in range(2 * N)]  # Input commands
    print(manipulation(A, commands))  # Print the sum of elements after mutations

# The Captain's Room
# Function to find the captain's room number.
def findCaptainRoom(K, room_list):
    # Sum of unique room numbers multiplied by K minus total sum of room_list divided by K-1 gives the captain's room.
    unique_sum = sum(set(room_list))
    total_sum = sum(room_list)
    captain_room = (unique_sum * K - total_sum) // (K - 1)
    return captain_room  

if __name__ == '__main__':
    K = int(input())  # Input the size of family groups (excluding the captain).
    rep_rooms = list(map(int, input().strip().split()))  # Input the room numbers of all family members and the captain.
    print(findCaptainRoom(K, rep_rooms))  # Output the captain's room number.

# Check Subset
# Function to check if set A is a subset of set B for multiple test cases.
def subSet(T, setA, setB):
    result = []
    for i in range(T):
        # Check if set A is a subset of set B.
        if(setA[i].difference(setB[i]) == set()):
            result.append("True")
        else:
            result.append("False")
    return '\n'.join(result)

if __name__ == '__main__':
    T = int(input())  # Input the number of test cases.
    setA = []
    setB = []
    for _ in range(T):
        nA = int(input())  # Input the size of set A.
        setA.append(set(map(int, input().strip().split())))  # Input the elements of set A.
        nB = int(input())  # Input the size of set B.
        setB.append(set(map(int, input().strip().split())))  # Input the elements of set B.
    print(subSet(T, setA, setB))  # Output "True" if set A is a subset of set B, otherwise "False".

# Check Strict Superset
# Function to check if set A is a strict superset of all sets in a list.
def superSet(A, sets):
    # Loop through each set B and check if A is a strict superset of B.
    for B in sets:
        if not(A > B):
            return "False"
    return "True"

if __name__ == '__main__':
    A = set(map(int, input().strip().split()))  # Input the elements of the superset A.
    N = int(input())  # Input the number of sets to compare with A.
    sets = []
    for _ in range(N):
        sets.append(set(map(int, input().strip().split())))  # Input the elements of each set B.
    print(superSet(A, sets))  # Output "True" if A is a strict superset of all sets, otherwise "False".

# COLLECTIONS

# collections.Counter()
# Function to calculate profit based on available sizes and desired sizes.
from collections import Counter

def counter(sizes, desired_sizes):
    occ_size = Counter(sizes)  # Count occurrences of each size.
    profit = 0
    for size in desired_sizes:
        if occ_size[size[0]] > 0:  # If the desired size is available.
            profit += size[1]  # Add the profit for this size.
            occ_size[size[0]] -= 1  # Decrease the count of the available size.
    return profit  # Return the total profit.

if __name__ == '__main__':
    X = int(input())  # Input the total number of sizes available.
    sizes = list(map(int, input().strip().split()))  # Input the available sizes.
    N = int(input())  # Input the number of desired sizes.
    desired_sizes = [list(map(int, input().strip().split())) for _ in range(N)]  # Input desired sizes with profits.
    print(counter(sizes, desired_sizes))  # Output the total profit.

# DefaultDict Tutorial
# Function to index words and return their positions based on given lists.
from collections import defaultdict

def index(A, B):
    d = defaultdict(list)  # Create a default dictionary with lists.
    result = ""
    for i in range(len(A)):
        d[A[i]].append(i + 1)  # Store positions (1-indexed) of each word in A.
    for word in B:
        # Get the positions of each word in B, return -1 if not found.
        result = result + ' '.join(map(str, d.get(word, [-1]))) + "\n"
    return result  # Return the formatted result.

if __name__ == '__main__':
    size = list(map(int, input().strip().split()))  # Input sizes for A and B.
    A = [input() for _ in range(size[0])]  # Input words for list A.
    B = [input() for _ in range(size[1])]  # Input words for list B.
    print(index(A, B))  # Output the indexed positions.

# Collections.namedtuple()
# Function to calculate the average marks of students using namedtuple.
from collections import namedtuple

def avg(N, students):
    # Calculate the average marks from the list of students.
    return sum([int(student.MARKS) for student in students]) / N

if __name__ == '__main__':
    N = int(input())  # Input the number of students.
    names = list(input().strip().split())  # Input the names of the attributes.
    Student = namedtuple('Student', ', '.join(names[:4]))  # Define a namedtuple for student attributes.
    # Unpacking operator * to create student instances from input.
    students = [Student(*input().strip().split()) for _ in range(N)]
    print(avg(N, students))  # Output the average marks.

# Collections.OrderedDict()
# Function to accumulate item quantities using OrderedDict.
from collections import OrderedDict

def ordered(N, items_list):
    items = OrderedDict()  # Create an OrderedDict to maintain the order of items.

    for item in items_list:
        key, value = ' '.join(item[:-1]), int(item[-1])  # Combine all but the last item as key, last item as value.
        items[key] = items.get(key, 0) + value  # Accumulate values for each key.

    return '\n'.join(f"{key} {value}" for key, value in items.items())  # Return formatted result.

if __name__ == '__main__':
    N = int(input())  # Input the number of items.
    items_list = [list(map(str, input().strip().split())) for _ in range(N)]  # Input item details.
    print(ordered(N, items_list))  # Output accumulated items.

# Word Order
# Function to count unique words and their occurrences in order.
from collections import OrderedDict

def occ(words_list):
    words = OrderedDict()  # Use an OrderedDict to maintain insertion order.

    for word in words_list:
        words[word] = words.get(word, 0) + 1  # Count occurrences of each word.
    
    return str(len(words)) + '\n' + ' '.join(f"{value}" for value in words.values())  # Format output.

if __name__ == '__main__':
    n = int(input())  # Input the number of words.
    words_list = [input() for _ in range(n)]  # Input words.
    print(occ(words_list))  # Output the word count and occurrences.

# Collections.deque()
# Function to perform operations on a deque based on given commands.
from collections import deque

def operate(commands):
    d = deque()  # Initialize a deque.
    
    for command in commands:
        match command[0]:
            case "append":
                d.append(command[1])  # Append to the right.
            case "pop":
                d.pop()  # Remove from the right.
            case "popleft":
                d.popleft()  # Remove from the left.
            case "appendleft":
                d.appendleft(command[1])  # Append to the left.
    
    return ' '.join(map(str, d))  # Return the elements in the deque as a string.

if __name__ == '__main__':
    N = int(input())  # Input the number of commands.
    commands = [input().strip().split() for _ in range(N)]  # Input the commands.
    print(operate(commands))  # Output the final state of the deque.

# Company Logo
# Function to generate a logo based on character occurrences.
from collections import Counter, OrderedDict

def logo(s):
    occ = Counter(s)  # Count occurrences of each character.
    recurrent_ch = OrderedDict()  # Maintain order of characters.
    len_logo = 3  # Limit the logo to 3 characters.
    
    while len_logo > 0:
        max_occ = max(occ.values())  # Find the maximum occurrence.
        max_ch = sorted([c for c in occ.keys() if occ[c] == max_occ])  # Sort characters by max occurrence.
        len_max_ch = len(max_ch)  # Number of characters with max occurrence.
        
        if len_max_ch > len_logo:  # If more than 3 characters have the same max occurrence, take the first 3.
            max_ch = max_ch[:len_logo]
        
        for c in max_ch:
            recurrent_ch[c] = max_occ  # Add to result and remove from count.
            del occ[c]
        
        len_logo -= len_max_ch  # Decrease the remaining length to fill.
    
    formatted_result = '\n'.join(f"{key} {value}" for key, value in recurrent_ch.items())  # Format the output.
    return formatted_result  

if __name__ == '__main__':
    s = input()  # Input the string for the logo.
    print(logo(s))  # Output the logo representation.

# Piling Up!
# Function to determine if blocks can be stacked based on specified rules.
def stack(blocks):
    result = []
    
    for block in blocks:
        left_idx, right_idx = 0, len(block) - 1  # Initialize left and right indices.
        prev_height = float('inf')  # Previous height set to infinity.
        can_stack = True  # Assume stacking is possible.
        
        while left_idx <= right_idx:
            if block[left_idx] >= block[right_idx]:  # Choose the larger block.
                current_height = block[left_idx]
                left_idx += 1
            else:
                current_height = block[right_idx]
                right_idx -= 1

            if current_height > prev_height:  # Check if the current height exceeds the previous height.
                can_stack = False  # Stacking is not possible.
                break
            
            prev_height = current_height  # Update previous height for next iteration.
        
        result.append("Yes" if can_stack else "No")  # Append result for the current block.

    return "\n".join(result)  # Return all results.

if __name__ == '__main__':
    T = int(input())  # Input the number of test cases.
    blocks = []
    for _ in range(T):
        n = int(input())  # Input the number of blocks.
        block = list(map(int, input().strip().split()))  # Input the block heights.
        blocks.append(block)  # Add to the list of blocks.
    print(stack(blocks))  # Output the stacking results.

# DATE AND TIME

# Calendar Module
# Function to determine the capitalized name of the day of the week for a given date.
import calendar

def capitalDay(date):
    month = int(date[0])  # Extract the month from the date.
    day = int(date[1])    # Extract the day from the date.
    year = int(date[2])   # Extract the year from the date.
    return calendar.day_name[calendar.weekday(year, month, day)].upper()  # Return the day name in uppercase.

if __name__ == '__main__':
    date = list(input().strip().split())  # Input the date as a list of strings.
    print(capitalDay(date))  # Output the capitalized day name.

# Time Delta
# Function to calculate the absolute time difference in seconds between two datetime strings.
#!/bin/python3

import os
from datetime import datetime

def time_delta(t1, t2):
    format = "%a %d %b %Y %H:%M:%S %z"  # Define the format for the datetime strings.
    
    dt1 = datetime.strptime(t1, format)  # Parse the first datetime string.
    dt2 = datetime.strptime(t2, format)  # Parse the second datetime string.
    
    abs_diff = abs((dt1 - dt2).total_seconds())  # Calculate the absolute difference in seconds.
    
    return str(int(abs_diff))  # Return the difference as a string.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # Open output file.
    t = int(input())  # Input the number of test cases.
    for t_itr in range(t):
        t1 = input()  # Input the first datetime string.
        t2 = input()  # Input the second datetime string.
        delta = time_delta(t1, t2)  # Calculate the time difference.
        fptr.write(delta + '\n')  # Write the result to the output file.
    fptr.close()  # Close the output file.

# EXCEPTIONS

#Exceptions
# Function to perform integer division and handle exceptions.
def division(operands):
    result = []  # Initialize an empty list to store results.
    for couple in operands:  # Iterate over each pair of operands.
        try:
            # Attempt integer division and append the result.
            result.append(int(couple[0]) // int(couple[1]))
        except ZeroDivisionError as e:
            # Handle division by zero and append the error message.
            result.append(f"Error Code: {e}")
        except ValueError as e:
            # Handle value errors (e.g., invalid input) and append the error message.
            result.append(f"Error Code: {e}")
    return '\n'.join(map(str, result))  # Return the results as a newline-separated string.

if __name__ == '__main__':
    T = int(input())  # Input the number of test cases.
    operands = [input().strip().split() for _ in range(T)]  # Input each pair of operands.
    print(division(operands))  # Output the results of the division.

# BUILT-INS

# Zipped!
# Function to calculate the average marks of students.
def avg(N, X, marks):
    # Create a list of student indices from 0 to N-1.
    students = [i for i in range(0, N)]
    
    # Create a list of tuples that pair each student with their corresponding marks.
    marks_tuples = [tup for sub in marks for tup in zip(students, sub)]
    
    # Initialize a result list to hold the total marks for each student.
    result = [0] * N
    
    # Sum up the marks for each student based on the tuples created.
    for mark in marks_tuples:
        result[mark[0]] += mark[1]
    
    # Calculate the average marks for each student by dividing total marks by X.
    result = [avg / X for avg in result]
    
    # Return the averages as a newline-separated string.
    return "\n".join(map(str, result))

if __name__ == '__main__':
    # Read the first line of input, which contains N (number of students) and X (number of subjects).
    NX = list(map(int, input().strip().split()))
    
    # Read the subsequent lines of input, which contain the marks for each subject.
    marks = [list(map(float, input().strip().split())) for _ in range(NX[1])]
    
    # Print the average marks for each student.
    print(avg(NX[0], NX[1], marks))

# Athlete Sort
#!/bin/python3
import math
import os
import random
import re
import sys

# Function to sort a list of lists based on the k-th element of each sublist.
def sortK(arr, k):
    # Sort the array using the k-th element of each sublist as the key.
    k_sorted = sorted(arr, key=lambda x: x[k])
    
    # Join each sublist into a string and return all sublists as newline-separated strings.
    return "\n".join(map(str, [' '.join(map(str, sublist)) for sublist in k_sorted]))

if __name__ == '__main__':
    # Read the first line of input, which contains n (number of rows) and m (number of columns).
    nm = input().split()

    n = int(nm[0])  # Convert n to an integer.

    m = int(nm[1])  # Convert m to an integer.

    arr = []  # Initialize an empty list to hold the rows.

    # Read each row of input and append it to arr.
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())  # Read the index of the column to sort by.
    
    # Print the sorted array based on the k-th column.
    print(sortK(arr, k))

# ginortS
def sortAlfa(s):
    # Sort the string s using a custom sorting key.
    return ''.join(sorted(s, key=lambda x: (
        x.isdigit() and int(x) % 2 == 0,  # Sort by whether the character is an even digit first.
        x.isdigit(),                    # Then, sort by whether the character is a digit.
        x.isupper(),                    # Next, sort by whether the character is uppercase.
        x                               # Finally, sort alphabetically.
    )))

if __name__ == '__main__':
    s = input()  # Read input from the user.
    print(sortAlfa(s))  # Print the sorted result.

# PYTHON FUNCTIONALS

# Map and Lambda Function
# Define a lambda function to calculate the cube of a number.
cube = lambda x: x ** 3 

def fibonacci(n):
    # Initialize an empty list to store Fibonacci numbers.
    fibonacci_list = []
    # Continue generating Fibonacci numbers until we have n numbers.
    while len(fibonacci_list) < n:
        # Append the first Fibonacci number.
        if len(fibonacci_list) == 0:
            fibonacci_list.append(0)
        # Append the second Fibonacci number.
        elif len(fibonacci_list) == 1:
            fibonacci_list.append(1)
        # Calculate and append the next Fibonacci number.
        else:
            fibonacci_list.append(fibonacci_list[-2] + fibonacci_list[-1])
    return fibonacci_list  # Return the list of Fibonacci numbers.

if __name__ == '__main__':
    n = int(input())  # Read an integer input n from the user.
    # Generate a list of Fibonacci numbers and map the cube function to each number.
    print(list(map(cube, fibonacci(n))))  # Print the cubed Fibonacci numbers.

# REGEX AND PARSING CHALLENGES

# Detect Floating Point Number
def isFloat(N):
    # Initialize an empty list to store the results.
    result = []
    # Iterate over each element n in the input list N.
    for n in N:
        # Check if n is a valid floating-point number according to specified criteria.
        if (((n[0].isdigit() or n[0] == ".")  # The first character should be a digit or a decimal point.
             or (len(n) > 1 and (n[0] in ["+", "-"] and (n[1].isdigit() or n[1] == "."))))  # Allow for + or - followed by a digit or a decimal point.
             and not any(c.isalpha() for c in n)  # Ensure there are no alphabetic characters in n.
             and not n[-1] == "."  # The last character should not be a decimal point.
             and n.count(".") == 1  # There should be exactly one decimal point in n.
             and "+" not in n[1:]  # The '+' character should not appear after the first position.
             and "-" not in n[1:]):  # The '-' character should not appear after the first position.
            result.append("True")  # If n is valid, append "True" to the result list.
        else:
            result.append("False")  # If n is not valid, append "False" to the result list.
    return "\n".join(result)  # Return the result list joined by new lines.

if __name__ == '__main__':
    T = int(input())  # Read an integer input T (number of test cases).
    N = [input() for _ in range(T)]  # Read T strings as input for testing.
    print(isFloat(N))  # Call isFloat function and print the result.

# Re.split()
# Define a regular expression pattern to split numbers using commas or periods.
# This pattern matches a comma or period that is preceded by a digit and followed by a digit.
regex_pattern = r"(?<=\d)[,.](?=\d)"

import re  # Import the regular expression module.
# Read a line of input, split it using the defined regex pattern, and print the resulting parts.
# Each part is printed on a new line.
print("\n".join(re.split(regex_pattern, input())))

# Group(), Groups() & Groupdict()
import re  # Import the regular expression module.

def firstRep(s):
    # Use a regex to search for the first repeated character in the string.
    # The pattern r'([a-zA-Z0-9])\1' looks for any alphanumeric character that is repeated immediately after itself.
    rep = re.search(r'([a-zA-Z0-9])\1', s)
    
    # If a repeated character is found, return it; otherwise, return -1.
    return(rep.group(1) if rep else -1)

if __name__ == '__main__':
    s = input()  # Read a string from input.
    print(firstRep(s))  # Print the first repeated character or -1 if none is found.

# Re.findall() & Re.finditer()
import re  # Import the regular expression module.

def match(s):
    # Use re.findall to search for sequences of two or more vowels (a, e, i, o, u) 
    # that are surrounded by consonants.
    # The regex pattern:
    # - (?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM]): Positive lookbehind assertion to ensure
    #   that the matched vowels are preceded by a consonant (case insensitive).
    # - ([aeiouAEIOU]{2,}): Capture group to match two or more vowels.
    # - (?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM]): Positive lookahead assertion to ensure
    #   that the matched vowels are followed by a consonant (case insensitive).
    matches = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])([aeiouAEIOU]{2,})(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])', s)
    
    # If matches are found, join them with newline characters and return the result.
    # If no matches are found, return -1.
    return("\n".join(matches) if matches else -1)

if __name__ == '__main__':
    s = input()  # Read a string from input.
    print(match(s))  # Print the matched vowel sequences or -1 if none are found.

# Re.start() & Re.end()
def indices(S, k):
    indices = []  # Initialize an empty list to store the indices of occurrences.
    start = 0  # Set the starting position for searching.

    # Use a while loop to find all occurrences of the substring k in S.
    while (start := S.find(k, start)) != -1:
        # If k is found, append a tuple with the start and end indices to the list.
        indices.append((start, start + len(k) - 1))
        start += 1  # Move to the next position for the next search.

    # Return the indices as a formatted string or (-1, -1) if no occurrences are found.
    return "\n".join(map(str, indices)) if indices else "(-1, -1)"

if __name__ == '__main__':
    S = input().strip()  # Read the input string S and remove leading/trailing whitespace.
    k = input().strip()  # Read the substring k to find in S.
    print(indices(S, k))  # Print the result of the indices function.

# Regex Substitution
import re

def converter(text):
    # Replace "&&" with "and" and "||" with "or" in the given text.
    # The regex ensures that these replacements happen only when
    # they are surrounded by spaces, indicating they are standalone operators.
    return re.sub(r"(?<= )&&(?= )", "and", re.sub(r"(?<= )\|\|(?= )", "or", text))

if __name__ == '__main__':
    N = int(input())  # Read the number of lines of input.
    # Read N lines of input and join them into a single string with newlines.
    text = "\n".join(input() for _ in range(N))
    print(converter(text))  # Print the converted text.

# Validating Roman Numerals
import re
# Define the regex pattern for validating Roman numerals
# The pattern breakdown:
# ^          : Asserts the start of the string
# M{0,3}    : Matches 0 to 3 'M's (1000-3000)
# (CM|CD|D?C{0,3}) : Matches 'CM' (900), 'CD' (400), or 0-3 'C's with an optional 'D' (500) (100-800)
# (XC|XL|L?X{0,3}) : Matches 'XC' (90), 'XL' (40), or 0-3 'X's with an optional 'L' (50) (10-80)
# (IX|IV|V?I{0,3}) : Matches 'IX' (9), 'IV' (4), or 0-3 'I's with an optional 'V' (5) (1-8)
# $          : Asserts the end of the string

regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

# Read input, match against the regex pattern, and print True or False
print(str(bool(re.match(regex_pattern, input()))))

# Validating phone numbers
import re

def validator(numbers):
    # Define the regex pattern for validating Indian mobile numbers
    # The pattern breakdown:
    # ^          : Asserts the start of the string
    # [789]      : The first digit must be 7, 8, or 9
    # \d{9}      : Followed by exactly 9 digits (0-9)
    # $          : Asserts the end of the string
    regex_pattern = r"^[789]\d{9}$"
    
    # Use a list comprehension to check each number against the regex pattern
    return "\n".join(["YES" if re.match(regex_pattern, number) else "NO" for number in numbers])

if __name__ == "__main__":
    N = int(input())  # Read the number of phone numbers
    # Read N phone numbers and strip any leading/trailing whitespace
    numbers = [input().strip() for _ in range(N)]
    
    # Validate the numbers and print the results
    print(validator(numbers))

# Validating and Parsing Email Addresses
import re
import email.utils

def validator(couples):
    # Define the regex pattern for validating email addresses
    # The pattern breakdown:
    # ^                : Asserts the start of the string
    # [a-zA-Z]        : The first character must be a letter (uppercase or lowercase)
    # [\w.-]+         : Followed by one or more word characters (letters, digits, underscores),
    #                   dots, or hyphens
    # @                : There must be an '@' symbol
    # [a-zA-Z]+       : The domain name must consist of one or more letters
    # \.               : Followed by a dot
    # [a-zA-Z]{1,3}   : The domain extension must consist of 1 to 3 letters
    # $                : Asserts the end of the string
    regex_pattern = r"^[a-zA-Z][\w.-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$"
    
    # Use a list comprehension to filter and format valid email addresses
    return "\n".join([f"{name} <{address}>" for name, address in couples if re.match(regex_pattern, address)])

if __name__ == "__main__":
    n = int(input())  # Read the number of email address/name pairs
    # Parse n email address/name pairs using email.utils.parseaddr
    couples = [email.utils.parseaddr(input().strip()) for _ in range(n)]
    
    # Validate the couples and print the formatted valid email addresses
    print(validator(couples))

# Hex Color Code
import re

def colorCodes(CSS):
    # Define the regex pattern for matching hexadecimal color codes
    # Breakdown of the regex pattern:
    # (?<!^)           : Negative lookbehind to ensure that the match does not start at the beginning of the string
    # #                : Matches the '#' character that starts a hex color code
    # (?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3}) : Non-capturing group that matches either:
    #   - [0-9a-fA-F]{6} : Exactly 6 hexadecimal digits (0-9, a-f, A-F)
    #   - [0-9a-fA-F]{3} : Exactly 3 hexadecimal digits (0-9, a-f, A-F)
    regex_pattern = r'(?<!^)(#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3}))'
    
    hex_codes = []  # Initialize a list to store found hex color codes
    for code in CSS:  # Iterate over each line of CSS input
        # Use re.findall to find all occurrences of the hex color pattern in the current line
        hex_codes.extend(re.findall(regex_pattern, code))
    
    # Join the found hex codes with new line characters and return the result
    return "\n".join(hex_codes)

if __name__ == "__main__":
    N = int(input())  # Read the number of CSS lines
    # Read N lines of CSS input, stripping any leading or trailing whitespace
    CSS = [input().strip() for _ in range(N)]
    
    # Print the extracted hexadecimal color codes
    print(colorCodes(CSS))

# HTML Parser - Part 1
from html.parser import HTMLParser

# Define a custom HTML parser class that inherits from HTMLParser
class MyHTMLParser(HTMLParser):
    # Handle start tags
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")  # Print the start tag
        for attr in attrs:  # Iterate over the attributes of the tag
            # Print the attribute name and its value, or 'None' if the value is missing
            print(f"-> {attr[0]} > {attr[1] if attr[1] else 'None'}")
        
    # Handle end tags
    def handle_endtag(self, tag):
        print(f"End   : {tag}")  # Print the end tag
        
    # Handle self-closing tags (start-end tags)
    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")  # Print the self-closing tag
        for attr in attrs:  # Iterate over the attributes of the tag
            # Print the attribute name and its value, or 'None' if the value is missing
            print(f"-> {attr[0]} > {attr[1] if attr[1] else 'None'}")

# Main block to execute the parser
if __name__ == "__main__":
    parser = MyHTMLParser()  # Create an instance of the custom parser
    for _ in range(int(input())):  # Read the number of lines to parse
        parser.feed(input().strip())  # Feed each line of input to the parser

# HTML Parser - Part 2
from html.parser import HTMLParser

# Define a custom HTML parser class that inherits from HTMLParser
class MyHTMLParser(HTMLParser):
    # Handle comments in the HTML
    def handle_comment(self, data):
        # Check if the comment is multi-line or single-line
        print(">>> Multi-line Comment" if '\n' in data else ">>> Single-line Comment")
        print(data)  # Print the comment data

    # Handle text data in the HTML
    def handle_data(self, data):
        # Print the data only if it is not just whitespace
        if data.strip():
            print(">>> Data\n" + data)  # Print the data with a preceding label

# Main block to execute the parser
if __name__ == "__main__":
    html = ""  # Initialize an empty string to store HTML input
    # Read multiple lines of HTML input
    for i in range(int(input())):
        html += input().rstrip()  # Append each line to the html string
        html += '\n'  # Add a newline character to separate lines
        
    parser = MyHTMLParser()  # Create an instance of the custom parser
    parser.feed(html)  # Feed the HTML string to the parser
    parser.close()  # Close the parser

# Detect HTML Tags, Attributes and Attribute Values
from html.parser import HTMLParser

# Define a custom HTML parser class that inherits from HTMLParser
class MyHTMLParser(HTMLParser):
    # Handle start tags (e.g., <tag>)
    def handle_starttag(self, tag, attrs):
        print(tag)  # Print the name of the tag
        # Iterate through the attributes of the tag
        for attr in attrs:
            # Print the attribute name and its corresponding value
            print(f'-> {attr[0]} > {attr[1]}')

# Main block to execute the parser
if __name__ == "__main__":
    n = int(input())  # Read the number of lines of HTML input
    parser = MyHTMLParser()  # Create an instance of the custom parser
    for _ in range(n):
        # Feed each line of HTML input to the parser
        parser.feed(input().rstrip())  # Remove trailing spaces before feeding

# Validating UID
import re

def validator(UIDs):
    results = []  # Initialize a list to store the validation results for each UID
    for UID in UIDs:
        # Check the following conditions for a valid UID:
        valid = (
            len(UID) == 10 and  # UID must be exactly 10 characters long
            re.match(r'^[A-Za-z0-9]+$', UID) and  # UID must contain only alphanumeric characters
            len(set(UID)) == len(UID) and  # All characters in the UID must be unique
            sum(c.isupper() for c in UID) >= 2 and  # At least 2 uppercase letters
            sum(c.isdigit() for c in UID) >= 3  # At least 3 digits
        )
        # Append "Valid" if all conditions are met, otherwise append "Invalid"
        results.append("Valid" if valid else "Invalid")
    
    # Join the results into a single string separated by newlines
    return '\n'.join(results)

if __name__ == "__main__":
    N = int(input())  # Read the number of UIDs to validate
    UIDs = [input().strip() for _ in range(N)]  # Read each UID and remove any surrounding whitespace
    print(validator(UIDs))  # Validate the UIDs and print the results

# Validating Credit Card Numbers
import re

def validator(card_numbers):
    results = []  # Initialize a list to store validation results for each card number
    for card in card_numbers:
        # Define the regex pattern to validate the card number
        pattern = r'^(?!.*(\d)(?:-?\1){3})[4-6]\d{3}-?\d{4}-?\d{4}-?\d{4}$'
        
        # Check if the card matches the pattern and the count of hyphens is either 0 or 3
        if re.match(pattern, card) and card.count('-') in {0, 3}:
            if '-' in card:  # If the card contains hyphens
                groups = card.split('-')  # Split the card number into groups
                # Check if each group has exactly 4 digits
                if all(len(group) == 4 for group in groups):
                    results.append("Valid")  # Valid card number
                    continue
                else:
                    results.append("Invalid")  # Invalid group length
                    continue
            results.append("Valid")  # Valid card number without hyphens
        else:
            results.append("Invalid")  # Invalid card number
    return '\n'.join(results)  # Return all results as a single string separated by newlines

if __name__ == "__main__":
    N = int(input())  # Read the number of card numbers to validate
    card_numbers = [input().strip() for _ in range(N)]  # Read each card number and strip whitespace
    print(validator(card_numbers))  # Validate the card numbers and print results

# Validating Postal Codes
import re

# Regular expression to match integers in the range of 000000 to 999999
# Allows numbers from 1 to 999999 (without leading zeros) or exactly 000000.
regex_integer_in_range = r"^(?:[1-9]\d{5}|0{6})$"  # Do not delete 'r'.

# Regular expression to find alternating repetitive digit pairs.
# Uses a lookahead to check for two consecutive identical digits (e.g., 11, 22, etc.).
regex_alternating_repetitive_digit_pair = r"(?=(\d)(?=\d\1))"  # Do not delete 'r'.

# Read the input string
P = input()

# Check if the input matches the integer range pattern and if there are less than two alternating repetitive digit pairs
is_valid = (
    bool(re.match(regex_integer_in_range, P)) and 
    len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2
)

# Print the result: True if both conditions are satisfied, otherwise False
print(is_valid)

# Matrix Script
#!/bin/python3
import re
# Read the dimensions of the matrix
size = list(map(int, input().split()))

# Initialize the matrix
matrix = [input() for _ in range(size[0])]

# Decode the script by reading column-wise
dec_matrix = ''.join(matrix[n][m] for m in range(size[1]) for n in range(size[0]))

# Print the final output
print(re.sub(r'(?<=\w)([^\w]+)(?=\w)', ' ', dec_matrix))

# XML

# XML 1 - Find the Score
import sys
import xml.etree.ElementTree as etree
from collections import deque

def get_attr_number(node):
    # Initialize the score to count attributes
    score = 0
    # Use a queue to facilitate level-order traversal of the XML tree
    queue = deque([node])
    
    while queue:
        # Remove the first element from the queue
        tag = queue.popleft()
        # Count the number of attributes of the current node and add to score
        score += len(tag.attrib)
        # Enqueue all child nodes for further processing
        for subtag in tag:
            queue.append(subtag)
    
    return score

if __name__ == '__main__':
    # Read the first line (not used but can be necessary for structured input)
    sys.stdin.readline()
    # Read the entire XML input from standard input
    xml = sys.stdin.read()
    # Parse the XML string into an ElementTree object
    tree = etree.ElementTree(etree.fromstring(xml))
    # Get the root element of the XML tree
    root = tree.getroot()
    # Call the function to get the total number of attributes and print the result
    print(get_attr_number(root))

# XML2 - Find the Maximum Depth
import xml.etree.ElementTree as etree
from collections import deque

# Initialize a global variable to keep track of maximum depth
maxdepth = 0

# Function to compute the total number of attributes in the XML node
def get_attr_number(node):
    score = 0
    # Use a deque for level-order traversal of the XML tree
    queue = deque([node])
    
    while queue:
        tag = queue.popleft()  # Remove the first element from the queue
        score += len(tag.attrib)  # Count the attributes of the current node
        for subtag in tag:
            queue.append(subtag)  # Enqueue all child nodes for further processing
    return score

# Recursive function to determine the maximum depth of the XML tree
def depth(elem, level):
    global maxdepth
    level += 1  # Increment the depth level
    maxdepth = max(maxdepth, level)  # Update maxdepth if the current level is greater
    attr_count = get_attr_number(elem)  # Get the total number of attributes in the current element
    
    for child in elem:
        depth(child, level)  # Recur for each child node to find its depth

if __name__ == '__main__':
    n = int(input())  # Read the number of lines of XML input
    xml = ""
    for i in range(n):
        xml += input() + "\n"  # Read each line and construct the XML string
    
    # Parse the XML string into an ElementTree object
    tree = etree.ElementTree(etree.fromstring(xml))
    # Call the depth function starting from the root node with initial level -1
    depth(tree.getroot(), -1)
    # Print the maximum depth found in the XML tree
    print(maxdepth)

# CLOSURES AND DECORATIONS

# Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        formatted = []
        for number in l:
            number = number[1:] if number.startswith("0") else number  # Remove leading '0'
            number = "91" + number if len(number) < 10 else number  # Add '91' prefix if needed
            formatted.append(f"+91 {number[-10:-5]} {number[-5:]}")  # Format number
        return f(formatted)  # Pass the formatted list to the original function
    return fun  # Return the inner function

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')  # Sort and print the formatted numbers

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]  # Read input numbers
    sort_phone(l)  # Call the decorated function

# Decorators 2 - Name Directory
import operator

# Decorator to sort by age and format names
def person_lister(f):
    def inner(people):
        # Sort people by age (3rd element) while maintaining the input order for same ages
        sorted_people = sorted(people, key=lambda x: int(x[2]))  # Sort by age
        return [f(person) for person in sorted_people]  # Format the names
    return inner

# Function to format names based on sex
@person_lister
def name_format(person):
    # Determine the title based on the sex
    title = "Mr. " if person[3] == "M" else "Ms. "
    # Return the formatted name
    return title + person[0] + " " + person[1]

if __name__ == '__main__':
    n = int(input())  # Read the number of people
    people = [input().split() for _ in range(n)]  # Read people's details
    print(*name_format(people), sep='\n')  # Print formatted names

# NUMPY

# Arrays
import numpy

def arrays(arr):
    # Convert the input list 'arr' from strings to floats, 
    # create a NumPy array, and then flip it (reverse the order)
    return(numpy.flip(numpy.array(list(map(float, arr)))))

# Read a line of input, strip any extra whitespace, and split it into a list of strings
arr = input().strip().split(' ')

# Call the 'arrays' function with the input list and store the result
result = arrays(arr)

# Print the resulting flipped NumPy array
print(result)

# Shape and Reshape
import numpy

def npMatrix(arr):
    # Create a NumPy array from the input list 'arr' and reshape it into a 3x3 matrix
    return(numpy.reshape(numpy.array(arr), (3, 3)))

if __name__ == '__main__':
    # Read a line of input, strip any extra whitespace, split it into a list of strings,
    # and convert each string to an integer to create a list of integers
    arr = list(map(int, input().strip().split()))
    
    # Call the 'npMatrix' function with the input list and print the resulting 3x3 matrix
    print(npMatrix(arr))

# Transpose and Flatten
import numpy

def transposeFlatten(arr):
    # Convert the input list 'arr' into a NumPy array
    np_array = numpy.array(arr)
    
    # Transpose the NumPy array (swap rows and columns)
    tr = numpy.transpose(np_array)
    
    # Flatten the NumPy array into a one-dimensional array
    fl = np_array.flatten()
    
    # Return the transposed array and the flattened array as a tuple
    return (tr, fl)

if __name__ == '__main__':
    # Read two integers N and M from input, which represent the number of rows and columns, respectively
    N, M = map(int, input().strip().split())
    
    # Read N lines of input, each containing M integers, and create a list of lists (2D array)
    arr = [list(map(int, input().strip().split())) for _ in range(N)]
    
    # Call the 'transposeFlatten' function with the input array and store the result
    result = transposeFlatten(arr)
    
    # Print the transposed array
    print(result[0])
    
    # Print the flattened array
    print(result[1])

# Concatenate
import numpy

def concatenate(arrN, arrM):
    # Convert the input lists 'arrN' and 'arrM' into NumPy arrays
    array_N = numpy.array(arrN)
    array_M = numpy.array(arrM)
    
    # Concatenate the two arrays along the specified axis (0 for vertical stacking)
    return numpy.concatenate((array_N, array_M), axis=0)

if __name__ == '__main__':
    # Read the dimensions of the arrays from input, where dim[0] is the number of rows for arrN,
    # and dim[1] is the number of rows for arrM
    dim = list(map(int, input().strip().split()))
    
    arrN = []  # Initialize an empty list to store the first array
    # Loop to read 'dim[0]' rows of input for the first array
    for _ in range(dim[0]):
        row = list(map(int, input().strip().split()))  # Read a row and convert it to a list of integers
        arrN.append(row)  # Append the row to arrN
    
    arrM = []  # Initialize an empty list to store the second array
    # Loop to read 'dim[1]' rows of input for the second array
    for _ in range(dim[1]):
        row = list(map(int, input().strip().split()))  # Read a row and convert it to a list of integers
        arrM.append(row)  # Append the row to arrM
    
    # Print the result of concatenating arrN and arrM
    print(concatenate(arrN, arrM))

# Zeros and Ones
import numpy

def zerosOnes(shape):
    # Create a NumPy array filled with zeros of the specified shape and with int64 data type
    zeros = numpy.zeros(shape, dtype=numpy.int64)
    # Create a NumPy array filled with ones of the specified shape and with int64 data type
    ones = numpy.ones(shape, dtype=numpy.int64)
    # Return a formatted string containing both arrays, separated by a newline
    return f"{zeros}\n{ones}"

if __name__ == '__main__':
    # Read the shape of the arrays from input, splitting the input string and converting to integers
    shape = list(map(int, input().strip().split()))
    # Print the result of the zerosOnes function, which returns the arrays formatted as a string
    print(zerosOnes(shape))

# Eye and Identity
import numpy

# Set the print options for NumPy arrays to be compatible with legacy formatting from version 1.13
numpy.set_printoptions(legacy='1.13')

def diagonal(size):
    # Create a diagonal matrix (identity matrix) of specified dimensions (size)
    return numpy.eye(size[0], size[1], k=0)  # k=0 indicates the main diagonal

if __name__ == '__main__':
    # Read the size of the matrix from input, splitting the input string and converting to integers
    size = list(map(int, input().strip().split()))
    # Print the resulting diagonal matrix created by the diagonal function
    print(diagonal(size))

# Array Mathematics
import numpy

def operations(A, B):
    # Perform various operations on two NumPy arrays A and B
    add = numpy.add(A, B)  # Element-wise addition of A and B
    sub = numpy.subtract(A, B)  # Element-wise subtraction of B from A
    mul = numpy.multiply(A, B)  # Element-wise multiplication of A and B
    div = A // B  # Element-wise integer division of A by B (using floor division)
    mod = numpy.mod(A, B)  # Element-wise modulus operation (remainder of A divided by B)
    power = numpy.power(A, B)  # Element-wise exponentiation (A raised to the power of B)

    # Return the results of the operations formatted as a single string with newlines
    return (f"{add}\n{sub}\n{mul}\n{div}\n{mod}\n{power}")

if __name__ == '__main__':
    # Read the size of the arrays from input (expected to be two integers)
    size = list(map(int, input().strip().split()))

    # Create the first array A by reading 'size[0]' rows of input
    A = numpy.array([list(map(int, input().strip().split())) for _ in range(size[0])])

    # Create the second array B similarly to A
    B = numpy.array([list(map(int, input().strip().split())) for _ in range(size[0])])

    # Print the results of operations performed on arrays A and B
    print(operations(A, B))

# Floor, Ceil and Rint
import numpy
numpy.set_printoptions(legacy='1.13')  # Set the print options for NumPy arrays to legacy format (for compatibility)

def approximate(arr):
    # Calculate the floor, ceiling, and rounded values of the input array
    floor = numpy.floor(arr)  # Apply the floor function to each element of the array (greatest integer less than or equal to the element)
    ceil = numpy.ceil(arr)    # Apply the ceiling function to each element of the array (smallest integer greater than or equal to the element)
    rint = numpy.rint(arr)    # Apply the rounding function to each element of the array (round to the nearest integer)

    # Return the results formatted as a string with each result on a new line
    return(f"{floor}\n{ceil}\n{rint}")
    
if __name__ == '__main__':
    # Read a line of input, strip whitespace, split by spaces, and convert to a NumPy array of floats
    arr = numpy.array(list(map(float, input().strip().split())))

    # Print the results of the approximate function applied to the input array
    print(approximate(arr))

# Sum and Prod
import numpy

def sumProd(arr):
    # Calculate the sum along the specified axis and the product of those sums
    np_sum = numpy.sum(arr, axis=0)  # Compute the sum of the array along the columns (axis=0)
    np_prod = numpy.prod(np_sum)      # Compute the product of the summed values
    
    return np_prod  # Return the product of the sums

if __name__ == '__main__':
    # Read two integers, N and M, from input, which represent the number of rows and columns, respectively
    N, M = map(int, input().strip().split())
    
    # Create a 2D NumPy array by reading N lines of input, each containing M integers
    arr = numpy.array([list(map(int, input().strip().split())) for _ in range(N)])
    
    # Print the result of the sumProd function applied to the input array
    print(sumProd(arr))

# Min and Max
import numpy

def minMax(arr):
    # Calculate the maximum value among the minimum values of each row in the input array
    np_min = numpy.min(arr, axis=1)  # Compute the minimum value for each row (axis=1)
    np_max = numpy.max(np_min)        # Find the maximum value among the row minimums
    
    return np_max  # Return the maximum of the minimum values

if __name__ == '__main__':
    # Read two integers, N and M, from input, which represent the number of rows and columns, respectively
    N, M = map(int, input().strip().split())
    
    # Create a 2D NumPy array by reading N lines of input, each containing M integers
    arr = numpy.array([list(map(int, input().strip().split())) for _ in range(N)])
    
    # Print the result of the minMax function applied to the input array
    print(minMax(arr))

# Mean, Var and Std
import numpy

def stat(arr):
    # Calculate statistical metrics for the input array
    np_mean = numpy.mean(arr, axis=1)  # Compute the mean for each row (axis=1)
    np_var = numpy.var(arr, axis=0)     # Compute the variance for each column (axis=0)
    np_std = numpy.std(arr)              # Compute the standard deviation for the entire array
    
    # Format the standard deviation to 11 decimal places if it's greater than 0
    if np_std > 0:
        np_std = format(np_std, '.11f')
    
    # Return the mean, variance, and standard deviation as a formatted string
    return f"{np_mean}\n{np_var}\n{np_std}"

if __name__ == '__main__':
    # Read two integers, N and M, from input, which represent the number of rows and columns, respectively
    N, M = map(int, input().strip().split())
    
    # Create a 2D NumPy array by reading N lines of input, each containing M integers
    arr = numpy.array([list(map(int, input().strip().split())) for _ in range(N)])
    
    # Print the result of the stat function applied to the input array
    print(stat(arr))

# Dot and Cross
import numpy

def matMul(A, B):
    # Perform matrix multiplication using the dot product
    return numpy.dot(A, B)  # Return the result of multiplying matrix A by matrix B

if __name__ == '__main__':
    # Read the size of the square matrices from input
    N = int(input().strip())  # N represents the number of rows/columns in the square matrices

    # Create the first matrix A by reading N lines of input, each containing N integers
    A = numpy.array([list(map(int, input().strip().split())) for _ in range(N)])

    # Create the second matrix B similarly
    B = numpy.array([list(map(int, input().strip().split())) for _ in range(N)])

    # Print the result of the matrix multiplication of A and B
    print(matMul(A, B))

# Inner and Outer
import numpy

def innerOut(A, B):
    # Calculate the inner and outer products of vectors A and B
    
    inner = numpy.inner(A, B)  # Compute the inner product (dot product) of vectors A and B
    outer = numpy.outer(A, B)  # Compute the outer product of vectors A and B
    
    # Return the results of inner and outer products as formatted strings
    return f"{inner}\n{outer}"

if __name__ == '__main__':
    # Read vector A from input, convert the input string to a list of integers, and create a NumPy array
    A = numpy.array(list(map(int, input().strip().split())))

    # Read vector B in the same way
    B = numpy.array(list(map(int, input().strip().split())))

    # Print the results of the inner and outer products of vectors A and B
    print(innerOut(A, B))

# Polynomials 
import numpy  # Import the NumPy library for numerical operations

def polyX(P, x):
    # Evaluate the polynomial P at the point x
    return numpy.polyval(P, x)  # Use NumPy's polyval function to compute the polynomial value

if __name__ == '__main__':
    # Read the coefficients of the polynomial from input, convert the input string to a list of floats, and create a NumPy array
    P = numpy.array(list(map(float, input().strip().split())))

    # Read the value of x at which to evaluate the polynomial
    x = int(input())

    # Print the result of evaluating the polynomial at x
    print(polyX(P, x))

# Linear Algebra
import numpy

def det(A):
    # Calculate the determinant of the matrix A using NumPy's linear algebra module
    det = numpy.linalg.det(A)

    # Check if the determinant is an integer value
    if det == int(det):
        # If it's an integer, format it to one decimal place
        return f"{det:.1f}"
    else:
        # If it's not an integer, format it to two decimal places
        return f"{det:.2f}"

if __name__ == '__main__':
    # Read the size of the matrix from input
    N = int(input())

    # Read the matrix A from input, converting each row into a list of floats
    A = numpy.array([list(map(float, input().strip().split())) for _ in range(N)])

    # Print the determinant of the matrix A by calling the det function
    print(det(A))

# --------------------------------------- PROBLEM 2 ---------------------------------------

# Birthday Cake Candles
#!/bin/python3 

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Find the maximum height of the candles
    max_height = max(candles)
    # Count how many candles have the maximum height and return that count
    return candles.count(max_height)

if __name__ == '__main__':
    # Open the output file specified in the environment variable 'OUTPUT_PATH'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of candles from input
    candles_count = int(input().strip())

    # Read the heights of the candles from input, split by space, and convert to integers
    candles = list(map(int, input().rstrip().split()))

    # Call the function to count the tallest candles
    result = birthdayCakeCandles(candles)

    # Write the result to the output file
    fptr.write(str(result) + '\n')

    # Close the output file
    fptr.close()

# Number Line Jumps
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts the following parameters:
#  1. INTEGER x1 - starting position of the first kangaroo
#  2. INTEGER v1 - jump distance of the first kangaroo
#  3. INTEGER x2 - starting position of the second kangaroo
#  4. INTEGER v2 - jump distance of the second kangaroo
#

def kangaroo(x1, v1, x2, v2):
    # Check if the kangaroos have the same jump distance
    if v1 == v2:
        # If they start at the same position, they will always be together
        if x1 == x2:
            return "YES"
        else:
            # If they start at different positions, they will never meet
            return "NO"
    
    # Check if the kangaroo starting behind can catch up with the other kangaroo
    if (x2 - x1) / (v1 - v2) > 0 and (x2 - x1) % (v1 - v2) == 0:
        return "YES"  # They will meet
    else:
        return "NO"   # They will not meet

if __name__ == '__main__':
    # Open the output file specified in the environment variable 'OUTPUT_PATH'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the input values as a single line, split by spaces, and store in a list
    first_multiple_input = input().rstrip().split()

    # Convert the input values to integers
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])

    # Call the kangaroo function to determine if they meet
    result = kangaroo(x1, v1, x2, v2)

    # Write the result to the output file
    fptr.write(result + '\n')

    # Close the output file
    fptr.close()

# Viral Advertising
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as a parameter, representing the number of days.
#

def viralAdvertising(n):
    # Initialize variables to keep track of total recipients and total likes
    recipients = 0
    likes = 0
    
    # Loop through each day from 1 to n
    for i in range(1, n + 1):
        if i == 1:
            # On the first day, 5 people receive the advertisement
            recipients = 5
            # Half of the recipients (5 // 2 = 2) like the advertisement
            likes = 5 // 2
        else:
            # For subsequent days, the number of recipients is 3 times the likes from the previous day
            recipients = recipients // 2 * 3
            # Add the number of likes from the current day to the total likes
            likes += recipients // 2
    
    # Return the total number of likes received after n days
    return likes

if __name__ == '__main__':
    # Open the output file specified in the environment variable 'OUTPUT_PATH'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of days as input
    n = int(input().strip())

    # Call the viralAdvertising function to calculate the total likes
    result = viralAdvertising(n)

    # Write the result to the output file
    fptr.write(str(result) + '\n')

    # Close the output file
    fptr.close()

# Recursive Digit Sum
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts the following parameters:
#  1. STRING n - a string representation of the number
#  2. INTEGER k - the number of times to concatenate n
#

def superDigit(n, k):
    # Calculate the initial digit sum by converting each character in n to an integer,
    # summing them up, and then multiplying by k (the number of times n is repeated)
    digit = sum(list(map(int, n))) * k
    
    # Reduce digit to a single digit by summing the digits until it is less than 10
    while digit >= 10:
        digit = sum(list(map(int, list(str(digit)))))
    
    # Return the final single-digit result
    return digit

if __name__ == '__main__':
    # Open the output file specified in the environment variable 'OUTPUT_PATH'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the input, which consists of a number in string format and an integer k
    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]  # The number as a string
    k = int(first_multiple_input[1])  # The integer k

    # Call the superDigit function to compute the super digit
    result = superDigit(n, k)

    # Write the result to the output file
    fptr.write(str(result) + '\n')

    # Close the output file
    fptr.close()

# Insertion Sort - Part 1
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts the following parameters:
#  1. INTEGER n - the number of elements in the array
#  2. INTEGER_ARRAY arr - the array to be sorted using insertion sort
#

def insertionSort1(n, arr):
    # Store the last element of the array, which will be inserted in its correct position
    e = arr[-1]
    
    # Initialize i to the second last index (n - 2)
    i = n - 2
    
    # Shift elements of arr[0..i] that are greater than e to one position ahead
    while i >= 0 and arr[i] > e:
        arr[i + 1] = arr[i]  # Move element one position to the right
        print(' '.join(map(str, arr)))  # Print the current state of the array
        i -= 1  # Decrement i to check the next element
    
    # Place the last element e in its correct position
    arr[i + 1] = e
    
    # Print the final state of the array after insertion
    print(' '.join(map(str, arr)))

if __name__ == '__main__':
    # Read the number of elements in the array
    n = int(input().strip())

    # Read the array elements from input
    arr = list(map(int, input().rstrip().split()))

    # Call the insertionSort1 function to perform insertion sort
    insertionSort1(n, arr)

# Insertion Sort - Part 2
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts the following parameters:
#  1. INTEGER n - the number of elements in the array
#  2. INTEGER_ARRAY arr - the array to be sorted using insertion sort
#

def insertionSort2(n, arr):
    # Iterate through the array starting from the second element
    for i in range(1, n):
        e = arr[i]  # Store the current element to be inserted
        j = i - 1  # Initialize j to the index of the last sorted element

        # Shift elements of arr[0..i-1] that are greater than e to the right
        while j >= 0 and e < arr[j]:
            arr[j + 1] = arr[j]  # Move the larger element one position ahead
            j -= 1  # Move to the previous element

        # Place the current element e in its correct position
        arr[j + 1] = e
        
        # Print the current state of the array after each insertion
        print(' '.join(map(str, arr)))

if __name__ == '__main__':
    # Read the number of elements in the array
    n = int(input().strip())

    # Read the array elements from input
    arr = list(map(int, input().rstrip().split()))

    # Call the insertionSort2 function to perform insertion sort
    insertionSort2(n, arr)
