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

