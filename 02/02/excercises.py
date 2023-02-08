# 1. Create a list of different types of python objects, and print all the types. The one who gets the the most unique types wins respect points:

# my_list = ["Labas", 1, 1.2, [1, 2], (1,3)]

# for x in my_list:
#     print(type(x))


# 2. print all the items separated with "|"

# my_list = ["Labas", 1, 1.2, [1, 2], (1,3)]

# print(*my_list, sep = "|")



# 3. create a list of floats with 3 decimal points, create another list with all the values rounded to 2 decimals.

# float_list = [1.333, 44.331, 31.313, 55.123]

# round_number = [round(num,2) for num in float_list]

# print(round_number)

# 4. Create a list with student names and sort them, print the result to the terminal.

# my_list = ["Tomas", "Tadas", "Marius", "Linas", "Paulius"]

# print(sorted(my_list, reverse = False))

# 5. write a program that allows user to write in any float number and then round it.

# float_number = float(input("write in any float number: "))
# round_number = int(input("write decimal point to round: "))

# float_number, round_number = (input("float number and decimal point: ").split (" "))

# print(round(float(float_number), int(round_number)))


# Create a program which would take 5 separate sentences containing 5 words.
# Make those sentences in separate lists and sort them out (reverse=False)
# Create 5 five new lists what would contain first, second  indexed elements from those lists. (first list containing
# all first elements of those five, second list second elements and so on).
# print the length of all list items and print the longest lenght list and shortest.


sentences = []
new_list_one = []
new_list_two = []
new_list_three = []
new_list_four = []
new_list_five = []
new_sentences = [new_list_one, new_list_two, new_list_three, new_list_four, new_list_five]



for item in range(5):
    sentence = (input("Enter sentence: ").split())
    sentences.append(sentence)


for sentence in sentences:
    print(sorted(sentence, reverse=False))

for x in range(5):
    new_list_one.append(sentence[0])
    new_list_two.append(sentence[1])
    new_list_three.append(sentence[2])
    new_list_four.append(sentence[3])
    new_list_five.append(sentence[4])

for y in new_sentences:
    print(sorted(new_list_one, reverse=False))
  

print(new_sentences)

