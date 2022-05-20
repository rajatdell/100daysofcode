# Day 2

# Exercise 2 - Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):


weight = input("Enter your weight in kg: ")
height = input("Enter the height in m: ")


#print(f"your entered weight: {weight}kg and height: {height}m" )

bmi = int(weight)/int(height**2)
print(int(bmi))
