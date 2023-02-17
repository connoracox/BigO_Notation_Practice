# 1
#Remove First and Last Character
# It's pretty straightforward. Your goal is to create a function that 
# removes the first and last characters of a string. You're given one 
# parameter, the original string. 
# You don't have to worry with strings with less than two characters.

# SOLUTION:
# I think it is O(N) because we are indexing into the string like it is a list.
# if not, it is O(1).

def remove_char(s):
    return s[1 : -1]

s = 'connor'
print(remove_char(s))

# 2
# String repeat
# Write a function that accepts an integer n and a string s as parameters, 
# and returns a string of s repeated exactly n times.

# SOLUTION:
# O(1) because it is a simple multiplication problem, it is constant.

def repeat_str(repeat, string):
    return string * repeat

print(repeat_str(6, "W"))

#3
# Sum of Digits / Digital Root
# Given n, take the sum of the digits of n. If that value has more than one digit, 
# continue reducing in this way until a single-digit number is produced. 
# The input will be a non-negative integer.

#SOLUTION:
# I think this is O(n^2) because there is a for loop nested inside of a while loop.

def digital_root(n):
    while n >= 9:
        sum_digits = 0
        for digit in str(n):
            sum_digits += int(digit)
        n = sum_digits
    return n

print(digital_root(348))

