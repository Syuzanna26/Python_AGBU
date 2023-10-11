# 1. Write a Python program that print list elements count.

text1 = ["car", "bus", "airplane", "train"]
numb1 = len(text1)
print(f"This list contains elements: {numb1}")


# 2. Write a Python list use add, remove, elements use insert, append, pop, remove and extend methods.

colors1 = ["red", "white", "black", "blue"]
# colors1.insert(1,"yellow")
# print(f"List elements after inserting a new element are: {colors1}")
# colors1.append("brown")
# print(f"List elements after appending a new element are: {colors1}")
# colors1.pop(2)
# print(f"List elements after deleting are: {colors1}")
# colors1.remove("blue")
# print(f"List elements after removing are: {colors1}")


colors1 = ["red", "white", "black", "blue"]
colors2 = ["orange", "yellow", "green"]
colors1.extend(colors2)
print(f"List elements after extending are: {colors1}")


# 3. Write a Python program to check if a list is empty or not

# text1 = [1,2]
# if len(text1) == 0:
#     print("This list is empty.")
# else:
#     print("This list is not empty.")


# 4. Write a Python program to create a tuple with different data types.

text1 = ("red", 2, True, "abc", 2.3)
print(text1)
print(type(text1))


# 5. Write a Python program to create a tuple of numbers and print one item.

text1 = (1, 8, 12, 6, 5)
print(text1[2])


# 6. Write a Python program to get the 4th element from the last element of a tuple.
colors1 = ("red", "black", "white", "blue", "yellow", "green")
print(f"The 4th element from the last of a tuple is: {colors1[-4]}")

myset1 = [1,2,3]
myset2 = [4,5]
myset3 = myset1+myset2
print(myset3)

