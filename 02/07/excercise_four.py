# Write a small calculator application, that allows user to enter two numbers and a symbol, given and then do the operation and print an answer.

# First version

number_one, operation, number_two = int(input("Enter first number: ")), input("Please enter math operation, for example: +.-,*...: "), int(input("Enter second number: "))

if operation == "+":
    print(number_one+number_two)
elif operation == "*":
    print(number_one*number_two)
elif operation == "-":
    print(number_one-number_two)
elif operation == "/":
    print(number_one/number_two)
else:
    pass

# Second version

# number_one, operation, number_two = input("Enter condition: ").split()

# number_one = int(number_one)
# number_two = int(number_two)

# operation_list = ["+", "-", "*", "/"]

# if operation in operation_list:

#     if operation == "+":
#         answer = number_one + number_one
#     elif operation == "-":
#         answer = number_one - number_two
#     elif operation == "*":
#         answer = number_one * number_two
#     elif operation == "/":
#         answer = number_one / number_two

#     print(answer)

# else:

#     print("Pypyp")