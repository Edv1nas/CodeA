# Write a python program that asks user to enter 3 integers and find the highest value entered.

number1 =  input("Please enter first number: ")
number2 =  input("Please enter second number: ")
number3 =  input("Please enter third number: ")

my_list = []

my_list.append(number1)
my_list.append(number2)
my_list.append(number3)

print(max(my_list))