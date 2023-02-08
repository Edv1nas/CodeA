# print("hello world")

# print("Hello world", "blablabla", sep=":")

# a = "Ali"
# print(type(a))

# if type(a) == str:
#     print("qwert")

# my_name = "Ali"

sentence = input("Please input a sentece of at least 10 word: ")

x = sentence.split()
sorted_x =(sorted(sentence, reverse=True))

print(x)
print(sorted_x)