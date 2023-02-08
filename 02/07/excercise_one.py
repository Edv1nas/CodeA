# Let user enter name, surname and age. Print if user is allowed to enter an online casino or not. 21 is the age cap.

name = (input("Please enter your name: "))
surname = (input("Please enter your name: "))
age = (input("Please enter your age: "))

if age >= 21:
    print(f'{name} {surname} you can enter to casino.')
else:
    print(f'{name} {surname} you can\'t enter to casino.')
