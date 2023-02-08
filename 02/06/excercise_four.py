# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x):
# You can use input to receive the number. Example:
# n= 5 , output:  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

my_dict = {}

x = int(input("please input number from on to five:"))

for x in range(0, x +1):
    y = x*x

    my_dict[x] = y

print(my_dict)

