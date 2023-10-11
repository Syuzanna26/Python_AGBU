# # 1. Write a Python program to get the largest number from a list.
#
# mylist = [5, 56, 965, 32, 854, 23, 8, 457, 222, 1, 1035]
# mylist.sort()
# print(f"The largest number from a list is: {mylist[-1]}")
#
#
# # 2. Write a Python program to check a list is empty or not.
#
# mylist = ["winter", "summer", 25, 63.5, "spring"]
# if len(mylist) == 0:
#     print("This list is empty.")
# else:
#     print("This list is not empty.")
#
#
# # 3. Write a Python program to remove all elements from a given set.
#
# colors1 = {"white", "black", "blue", "yellow"}
# print(f"The original set elements are: {colors1}")
# colors1.clear()
# print(f"After removing all elements from a set: {colors1}")
#
#
# # 4. Write a Python program to check if a given value is present in a set or not.
#
# colors1 = {"white", "black", "blue", "yellow", "pink"}
# print("This element exist in this set:")
# print("red" in colors1)
#
#
# # 5. Write a Python program to convert a list to a tuple.
#
# text1 = ["white", "black", "blue", "yellow", "pink"]
# print(f"The original type of this text is: {type(text1)}")
# text2 = tuple(text1)
# print(f"After converting the text it becomes: {type(text2)}")
#
#
#
# # 6. Write a Python program to remove an item from a tuple.
#
# colors1 = ("white", "black", "blue", "yellow", "pink")
# print(f"The type of colors1 is: {type(colors1)}")
# print(f"Its original elements are: {colors1}")
# colors2 = list(colors1)
# colors2.remove("blue")
# colors1 = tuple(colors2)
# print(f"After removing one element it becomes: {colors1}")
# print(f"The type of colors1 is: {type(colors1)}")
#
#
#
# # 7. Write a Python script to check whether a given key already exists in a dictionary or not.
#
# dict1 = {"seasons": ["Winter", "Spring", "Summer", "Autumn"],
#          "weather": ["cool", "hot", "cold"],
#          "holidays": ["New Year", "Halloween", "Thanksgiving"]}
# print(dict1.keys())
# if "seasons" in dict1:
#     print(f"This word is one of the keys already existing in dict1.")
#
#
# # 8. Write a Python script to merge two Python dictionaries.
# dict1 = {"seasons": ["Winter", "Spring", "Summer", "Autumn"]}
# dict2 = {"weather": ["cool", "hot", "cold"]}
# dict1.update(dict2)
# print(dict1)
#
#
#
# 9.
# color1 = ["pink", "brown", "black"]
# input1 = input("Please enter the first word here: ")
# color1.insert(0, input1)
# print(f"After adding the first element it becomes: {color1}")
# input2 = input("Please enter the second word here: ")
# color1.append(input2)
# print(f"After adding the second element it becomes: {color1}")
#
#
# # 10.
# color1 = ("red", "white", "blue", "yellow")
# print(color1.count("red"))
#
#
# # 11.
# season1 = {"winter", "summer", "spring"}
# if "winter" in season1:
#     print("winter".upper())
#
#
# 12.
# dict1 = {"winter": ["snow", "snowman", "christmas"]}
# dict2 = {"summer": ["sea", "holiday", "beach"]}
# dict1.update(dict2)
# print(dict1)