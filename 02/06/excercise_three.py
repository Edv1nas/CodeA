# We have 3 dictionaries :  dic_one={1:10, 2:20} dic_two={3:30, 4:40} dic_three={5:50,6:60}
# Create one final dictionary from all those 3.

dic_one={1:10, 2:20}
dic_two={3:30, 4:40}
dic_three={5:50,6:60}
new_dict = {}

new_dict.update(dic_one)
new_dict.update(dic_two)
new_dict.update(dic_three)
print(new_dict)