# Create a program that allows user to Enter his/her name and Age
# Calculate the year in which user was born
# Print the answer to the Terminal

import datetime


name = input("Enter your name: ")
age = input("Enter your age: ")
age = int(age)
today = datetime.date.today()
year = today.year
year_of_birth = (year - age)

greeting = f"Hello, {name} , you were born {year_of_birth}"

print(greeting)

