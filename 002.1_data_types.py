# Day 3

# Exercise 1 - Write a program that adds the digits in a 2 digit number.
# e.g. if the input was 35, then the output should be 3 + 5 = 8

# # 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# # 🚨 Don't change the code above 👆

# ####################################
# #Write your code below this line 👇
# print(str(int(two_digit_number)))

# len_eq = len(two_digit_number)


# for x in len_eq:
#     total_sum += two_digit_number[x]


# Solution

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# Solution 1
# Convert the number to list and then add items in the list
len_eq = [int(x) for x in str(two_digit_number)]

print(sum(len_eq))

# Solution 2
a = int(two_digit_number[0])
b = int(two_digit_number[1])
print(a+b)
