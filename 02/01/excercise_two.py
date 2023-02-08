# Write a python program that multiplies all items in the list (all items are integers or floats in list, create a list yourself)

my_list = [1, 2, 3, 4, 30, 39]
multiply = []

a = 1

for b in my_list:
    a = a * b
    multiply.append(a)

print(my_list)
print(multiply)