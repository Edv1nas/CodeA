# allow user to enter two numbers, print out which one is higher than the other, or are they equal?

# number_one = int(input("Please enter first number: "))
# number_second = int(input("Please enter second number: "))

# if number_one > number_second:
#     print("First entered number is higher.")

# elif number_one < number_second:
#     print("Second entered number is higher.")

# else:
#     print("Numbers are equal.")


number_one, number_two = input("Please enter two number separated by space: ").split()

if number_one > number_two:
    print("First entered number is higher.")

elif number_one < number_two:
    print("Second entered number is higher.")

else:
    print("Numbers are equal.")