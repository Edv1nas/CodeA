list_one = [str(a) for a in input("Please enter somethink: ").split()]
reversed_list_one = sorted(list_one, reverse=False)
list_two = [str(a) for a in input("Please enter somethink: ").split()]
reversed_list_two = sorted(list_one, reverse=False)
list_three = [str(a) for a in input("Please enter somethink: ").split()]
reversed_list_three = sorted(list_one, reverse=False)
list_four = [str(a) for a in input("Please enter somethink: ").split()]
reversed_list_four = sorted(list_one, reverse=False)
list_five = [str(a) for a in input("Please enter somethink: ").split()]
reversed_list_five = sorted(list_one, reverse=False)


# print(reversed_list_one)
# print(reversed_list_two)
# print(reversed_list_three)
# print(reversed_list_four)
# print(reversed_list_five)

first_item_list = []
first_item_list.append(reversed_list_one[0])
first_item_list.append(reversed_list_two[0])
first_item_list.append(reversed_list_three[0])
first_item_list.append(reversed_list_four[0])
first_item_list.append(reversed_list_five[0])

second_item_list = []
second_item_list.append(reversed_list_one[1])
second_item_list.append(reversed_list_two[1])
second_item_list.append(reversed_list_three[1])
second_item_list.append(reversed_list_four[1])
second_item_list.append(reversed_list_five[1])

third_item_list = []
third_item_list.append(reversed_list_one[2])
third_item_list.append(reversed_list_two[2])
third_item_list.append(reversed_list_three[2])
third_item_list.append(reversed_list_four[2])
third_item_list.append(reversed_list_five[2])

fourth_item_list = []
fourth_item_list.append(reversed_list_one[3])
fourth_item_list.append(reversed_list_two[3])
fourth_item_list.append(reversed_list_three[3])
fourth_item_list.append(reversed_list_four[3])
fourth_item_list.append(reversed_list_five[3])

fifth_item_list = []
fifth_item_list.append(reversed_list_one[4])
fifth_item_list.append(reversed_list_two[4])
fifth_item_list.append(reversed_list_three[4])
fifth_item_list.append(reversed_list_four[4])
fifth_item_list.append(reversed_list_five[4])

print(first_item_list)
print(second_item_list)
print(third_item_list)
print(fourth_item_list)
print(fifth_item_list)


# joined_list1 =("".join(first_item_list))
# print(first_item_list)



first_list_len = int(len("".join(first_item_list)))
second_list_len = int(len("".join(second_item_list)))
third_list_len = int(len("".join(third_item_list)))
fourth_list_len = int(len("".join(fourth_item_list)))
fifth_list_len = int(len("".join(fifth_item_list)))

# all_list_len =

print(first_list_len)
print(second_list_len)
print(third_list_len)
print(fourth_list_len)
print(fifth_list_len)


print("Longest items lenght is: " + str(max(first_list_len, second_list_len, third_list_len, fourth_list_len, first_list_len)))
print("Shortest items lenght is: " + str(min(first_list_len, second_list_len, third_list_len, fourth_list_len, first_list_len)))


first_item_list.append(first_list_len)
second_item_list.append(second_list_len)
third_item_list.append(third_list_len)
fourth_item_list.append(fourth_list_len)
fifth_item_list.append(fifth_list_len)


max_list = max(first_item_list, second_item_list, third_item_list, fourth_item_list, first_item_list)

max_list.remove(max_list[-1])
print(max_list)

min_list = min(first_item_list, second_item_list, third_item_list, fourth_item_list, first_item_list)

min_list.remove(min_list[-1])
print(min_list)
